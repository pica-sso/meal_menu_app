import datetime
import requests
from bs4 import BeautifulSoup

class LunchScraper:
    def __init__(self):
        self.day_list = ['월', '화', '수', '목', '금', '토', '일']
        self.day_list_en = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        self.menu_dict = {day: {'한식': [], '일품식': [], '간편식': []} for day in self.day_list}
        self.week_day = ''
        self.dates_days = []

    def find_ww(self, add_week=0):
        today = datetime.datetime.today()
        self.week_day = self.day_list[today.weekday()]
        week_num = today.isocalendar()[1]
        site_url = f"https://intranet.amkor.co.kr/app/service/carte/view/detail?plant=S&year={today.year}&week={week_num+add_week}"
        print(f"site_url : {site_url}")
        return site_url

    def open_site(self, url):
        res = requests.get(url)
        res.raise_for_status()
        if res.status_code != 200:
            return []

        try:
            soup = BeautifulSoup(res.text, "html.parser")
            menu_table = soup.find('table')
            header_row = menu_table.find('tr')
            headers = header_row.find_all('td')
            self.dates_days = [header.text.strip() for header in headers[1:]]
            lunch_menu = soup.find_all('tr', attrs={"class": f"tr-row-1"})
            err_page = soup.find('title').text
            if err_page == 'error page':
                return []
        except Exception:
            return []

        return lunch_menu

    def make_menu_dict(self, menu_rows):
        menu_data = {day: {'한식': [], '일품식': [], '간편식': []} for day in self.dates_days}
        categories = ['한식', '일품식', '간편식']

        for i, row in enumerate(menu_rows):
            if i >= len(categories):
                break
            columns = row.find_all('td')

            for j in range(1, min(len(columns), len(self.dates_days) + 1)):
                date_day = self.dates_days[j - 1]
                menu_items = columns[j].decode_contents().split('<br/>')
                category = categories[i]

                menu_data[date_day][category] = [item.strip() for item in menu_items if item.strip()]

        return menu_data

    def get_week_menu(self, add_week=0):
        url = self.find_ww(add_week)
        menu_rows = self.open_site(url)
        if not menu_rows:
            return {"error": "No menu available for this week."}

        menu_data = self.make_menu_dict(menu_rows)
        return menu_data

    def get_day_menu(self, day):
        menu_data = self.get_week_menu()
        return menu_data.get(day, {"error": "Invalid day."})
