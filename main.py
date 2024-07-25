import os
import sys
import datetime
import requests
from bs4 import BeautifulSoup

from PySide6.QtWidgets import *

APP_ICON = r'C:\source\seyeong_draft\menu_amkor\lunch-time.png'

class LUNCH:
    def __init__(self):
        self.day_list = ['월', '화', '수', '목', '금', '토', '일']
        self.day_list_en = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        self.menu_dict = {'월': {'한식': [], '일품식': []},
                          '화': {'한식': [], '일품식': []},
                          '수': {'한식': [], '일품식': []},
                          '목': {'한식': [], '일품식': []},
                          '금': {'한식': [], '일품식': []},
                          '토': {'한식': [], '일품식': []},
                          '일': {'한식': [], '일품식': []},
                          }
        self.week_day = ''

    def find_ww(self, add_week=0):
        today = datetime.datetime.today()
        print(today)
        self.week_day = self.day_list[today.weekday()]
        week_num = today.isocalendar()[1]
        site_url = f"https://intranet.amkor.co.kr/app/service/carte/view/detail?plant=S&year=2024&week={week_num+add_week}"
        return site_url

    @staticmethod
    def open_site(url):
        res = requests.get(url)
        res.raise_for_status()  # 정상 200
        if res.status_code != 200:
            print("[CONNECTION ERROR] Cannot connect menu site.")
        soup = BeautifulSoup(res.text, "lxml")
        lunch_menu = soup.find_all('tr', attrs={"class": f"tr-row-1"})
        err_page = soup.find('title').text
        if err_page == 'error page':
            print("[PAGE ERROR] No menu for this week. :(")
        return lunch_menu

    def find_menu(self, lunch_menu):
        category = ''
        for menu in lunch_menu:
            day = 0
            menu_items = menu.find_all('td')
            for detail in menu_items:
                if detail.text == '간편식' or detail.text == 'PLUS':
                    break
                elif detail.text == '중식': continue
                elif detail.text == '한식' or detail.text == '일품식':
                    category = detail.text
                    continue
                for idx, menu in enumerate(detail.contents):
                    if idx % 2 != 0: continue
                    self.menu_dict[self.day_list[day]][category].append(menu)
                day += 1

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

    def print_day_menu(self, week_day):
        print(f'*** {week_day} 요 일 ***')
        for cat in self.menu_dict[week_day].keys():
            print(f'<{cat}>')
            for me in self.menu_dict[week_day][cat]:
                print(me)
            print()

    def get_input(self):
        while (True):
            param = input(">> Type examples : 'exit', 'thisweek', 'tomorrow', 'yesterday', 'MON', 'TUE'... : ")
            if param == 'exit':
                break
            elif param.upper() in lu.day_list_en:
                idx = lu.day_list_en.index(param.upper())
                lu.print_day_menu(lu.day_list[idx])
            elif param in lu.day_list:
                idx = lu.day_list.index(param)
                lu.print_day_menu(lu.day_list[idx])
            elif param == 'thisweek':
                lu.print_week_menu()
            elif param == 'tomorrow':
                tom_idx = lu.day_list.index(lu.week_day) + 1
                if tom_idx >= 7:
                    print("[PAGE ERROR] No menu for next week. :(")
                else:
                    lu.print_day_menu(lu.day_list[tom_idx])
            elif param == 'yesterday':
                yes_idx = lu.day_list.index(lu.week_day) - 1
                if yes_idx == 0:
                    print("Yesterday was SUNDAY.")
                else:
                    lu.print_day_menu(lu.day_list[yes_idx])
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
    if menu == []:
        print("☺ : Let's go out!!!")
    else:
        lu.find_menu(lunch_menu=menu)
        lu.print_day_menu(lu.week_day)

    # lu.get_input()
    os.system("pause")


