from fastapi import FastAPI
from server.menu_scraper import LunchScraper

app = FastAPI()
scraper = LunchScraper()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Lunch Menu API!"}

@app.get("/menu/week")
def get_week_menu():
    """이번 주 전체 메뉴 조회"""
    return scraper.get_week_menu()

@app.get("/menu/day/{day}")
def get_day_menu(day: str):
    """
    특정 요일의 메뉴 조회
    예: /menu/day/월, /menu/day/TUE
    """
    if day in scraper.day_list:
        return scraper.get_day_menu(day)
    elif day.upper() in scraper.day_list_en:
        index = scraper.day_list_en.index(day.upper())
        return scraper.get_day_menu(scraper.day_list[index])
    else:
        return {"error": "Invalid day. Use '월' ~ '금' or 'MON' ~ 'FRI'."}
