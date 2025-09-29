from fastapi import FastAPI
from menu_scraper import LunchScraper
import uvicorn

app = FastAPI()
scraper = LunchScraper()

@app.get("/")
def read_root():
    print("[DEBUG] / 요청 받음")
    return {"message": "Welcome to the Lunch Menu API!"}

@app.get("/menu/week")
def get_week_menu():
    """이번 주 전체 메뉴 조회"""
    print("[DEBUG] /menu/week 요청 받음")  # 요청이 왔는지 확인
    site_url = scraper.find_ww(0)
    print(f"[DEBUG] Fetching weekly menu from: {site_url}")
    menu = scraper.open_site(site_url)
    week_menu = scraper.make_menu_dict(menu)
    print(f"[DEBUG] Weekly menu fetched: {week_menu}")
    return week_menu

@app.get("/menu/day/{day}")
def get_day_menu(day: str):
    """
    특정 요일의 메뉴 조회
    예: /menu/day/월, /menu/day/TUE
    """
    print(f"[DEBUG] /menu/day/{day} 요청 받음")  # 요청이 정상적으로 왔는지 확인
    site_url = scraper.find_ww(0)
    print(f"[DEBUG] Fetching daily menu from: {site_url}")
    menu = scraper.open_site(site_url)
    menu_dict = scraper.make_menu_dict(menu)
    print(f"[DEBUG] Daily menu dictionary: {menu_dict}")

    if day in scraper.day_list:
        result = {"day": day, "menu": scraper.menu_dict.get(day, {})}
        print(f"[DEBUG] Returning menu for {day}: {result}")
        return result
    elif day.upper() in scraper.day_list_en:
        index = scraper.day_list_en.index(day.upper())
        kor_day = scraper.day_list[index]
        result = {"day": kor_day, "menu": scraper.menu_dict.get(kor_day, {})}
        print(f"[DEBUG] Returning menu for {kor_day}: {result}")
        return result
    else:
        print(f"[DEBUG] Invalid day requested: {day}")
        return {"error": "Invalid day. Use '월' ~ '금' or 'MON' ~ 'FRI'."}


if __name__ == "__main__":
    print("[DEBUG] FastAPI 서버 실행")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    