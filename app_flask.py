from flask import Flask, jsonify
import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

class LUNCH:
    def __init__(self):
        self.day_list = ['월', '화', '수', '목', '금', '토', '일']
        self.menu_dict = {day: {'한식': [], '일품식': []} for day in self.day_list}
        self.week_day = ''
        self.dates_days = []

    def find_ww(self, add_week=0):
        today = datetime.datetime.today()
        self.week_day = self.day_list[today.weekday()]
        week_num = today.isocalendar()[1]
        site_url = f"https://intranet.amkor.co.kr/app/service/carte/view/detail?plant=S&year={today.year}&week={week_num+add_week}"
        return site_url

    def open_site(self, url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        menu_table = soup.find('table')
        header_row = menu_table.find('tr')
        headers = header_row.find_all('td')
        self.dates_days = [header.text.strip() for header in headers[1:]]
        lunch_menu = soup.find_all('tr', attrs={"class": f"tr-row-1"})
        return lunch_menu

    def make_menu_dict(self, menu_rows):
        menu_data = {'한식': [], '일품식': [], '간편식': []}
        for i, row in enumerate(menu_rows):
            columns = row.find_all('td')
            for j in range(1, min(len(columns), len(self.dates_days) + 1)):
                date_day = self.dates_days[j - 1]
                menu_items = columns[j].decode_contents().split('<br/>')
                if i == 0:
                    menu_data['한식'].append({'date_day': date_day, 'menu': [item.strip() for item in menu_items if item.strip()]})
                elif i == 1:
                    menu_data['일품식'].append({'date_day': date_day, 'menu': [item.strip() for item in menu_items if item.strip()]})
                elif i == 2:
                    menu_data['간편식'].append({'date_day': date_day, 'menu': [item.strip() for item in menu_items if item.strip()]})
        return menu_data

@app.route('/menu', methods=['GET'])
def get_menu():
    lu = LUNCH()
    site_url = lu.find_ww(0)
    menu = lu.open_site(url=site_url)
    menu_data = lu.make_menu_dict(menu)
    return jsonify(menu_data)

if __name__ == '__main__':
    app.run(debug=True)
