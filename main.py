import os
import datetime
import requests
from bs4 import BeautifulSoup

APP_ICON = r'C:\source\seyeong_draft\menu_amkor\lunch-time.png'

class LUNCH:
    def __init__(self):
        self.day_list = ['월', '화', '수', '목', '금', '토', '일']
        self.day_list_en = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        self.menu_dict = {day: {'한식': [], '일품식': [], '간편식': []} for day in self.day_list}
        self.week_day = ''
        self.dates_days = []

    def find_ww(self, add_week=0):
        today = datetime.datetime.today()
        print(today)
        self.week_day = self.day_list[today.weekday()]
        week_num = today.isocalendar()[1]
        site_url = f"https://intranet.amkor.co.kr/app/service/carte/view/detail?plant=S&year={today.year}&week={week_num+add_week}"
        return site_url

    # @staticmethod
    def open_site(self, url):
        res = requests.get(url)
        res.raise_for_status()  # 정상 200
        if res.status_code != 200:
            print("[CONNECTION ERROR] Cannot connect menu site.")
            return []
        try:
            soup = BeautifulSoup(res.text, "html.parser")
            menu_table = soup.find('table')
            header_row = menu_table.find('tr')
            headers = header_row.find_all('td')
            self.dates_days = [header.text.strip() for header in headers[1:]]  # 첫 번째 헤더는 제외
            lunch_menu = soup.find_all('tr', attrs={"class": f"tr-row-1"})
            err_page = soup.find('title').text
            if err_page == 'error page':
                print("[PAGE ERROR] No menu for this week. :(")
        except Exception as e:
            print(e)
            return []
        return lunch_menu

    def make_menu_dict(self, menu_rows):
        menu_data = {'한식': [], '일품식': [], '간편식': []}
        categories = ['한식', '일품식', '간편식']
        for i, row in enumerate(menu_rows):
            if i >= len(categories):
                break  # Avoid IndexError
            columns = row.find_all('td')
            for j in range(1, min(len(columns), len(self.dates_days) + 1)):
                date_day = self.dates_days[j - 1]
                menu_items = columns[j].decode_contents().split('<br/>')
                category = categories[i]
                menu_data[category].append({
                    'date_day': date_day,
                    'menu': [item.strip() for item in menu_items if item.strip()]
                })
        return menu_data

    def find_menu(self, lunch_menu):
        category = ''
        for menu in lunch_menu:
            day = 0
            menu_items = menu.find_all('td')
            for detail in menu_items:
                if detail.text == 'PLUS':   # if detail.text == '간편식' or detail.text == 'PLUS':
                    break
                elif detail.text == '중식': continue
                elif detail.text == '한식' or detail.text == '일품식' or detail.text == '간편식':
                    category = detail.text
                    continue
                for idx, menu in enumerate(detail.contents):
                    if idx % 2 != 0: continue
                    self.menu_dict[self.day_list[day]][category].append(menu)
                day += 1

    def print_day_menu(self, week_day):
        text = f'*** {week_day} 요 일 ***\n'
        for cat in self.menu_dict[week_day].keys():
            text += f'<{cat}>\n'
            for me in self.menu_dict[week_day][cat]:
                text += me + '\n'
            text += '\n'
        print(text)
        return text

    def print_week_menu(self):
        for day in self.menu_dict.keys():
            if day == '토':
                return
            print(f'*** {day} 요 일 ***')
            for cat in self.menu_dict[day].keys():
                print(f'<{cat}>')
                for me in self.menu_dict[day][cat]:
                    print(me)
                print()
            print()

    def get_input(self):
        while (True):
            param = input(">> Type examples : 'exit', 'thisweek', 'tomorrow', 'yesterday', 'MON', 'TUE'... : ")
            if param == 'exit':
                break
            elif param.upper() in lu.day_list_en:
                idx = lu.day_list_en.index(param.upper())
                text = lu.print_day_menu(lu.day_list[idx])
            elif param in lu.day_list:
                idx = lu.day_list.index(param)
                text = lu.print_day_menu(lu.day_list[idx])
            elif param == 'thisweek':
                lu.print_week_menu()
            elif param == 'tomorrow':
                tom_idx = lu.day_list.index(lu.week_day) + 1
                if tom_idx >= 7:
                    print("[PAGE ERROR] No menu for next week. :(")
                else:
                    text = lu.print_day_menu(lu.day_list[tom_idx])
            elif param == 'yesterday':
                yes_idx = lu.day_list.index(lu.week_day) - 1
                if yes_idx == 0:
                    print("Yesterday was SUNDAY.")
                else:
                    text = lu.print_day_menu(lu.day_list[yes_idx])
            elif param == 'help':
                print('Enter what you want to know.')
                print("EX) 'thisweek', 'tomorrow', 'yesterday', 'MON', 'TUE'...")
            else:
                print(f'No {param}.')
        print('Exit the program. BYE!! :)')


if __name__ == '__main__':
    lu = LUNCH()
    site_url = lu.find_ww(0)
    menu = lu.open_site(url=site_url)
    menu_data = lu.make_menu_dict(menu)

    if menu == []:
        print("☺ : Let's go out!!!")
    else:
        lu.find_menu(lunch_menu=menu)
        text = lu.print_day_menu(lu.week_day)

    # lu.get_input()
    os.system("pause")


