import requests
import json
from datetime import datetime
from PyKakao import Message
from main import LUNCH
from send_function import Functions
API = Message(service_key="bfc4bd6ba10f9e4bdb90d5ba83501417")

class SendMsg:
    def __init__(self):
        self.fu = Functions()

    def access(self):
        auth_url = API.get_url_for_generating_code()
        print(auth_url)
        url = input('url : ')
        access_token = API.get_access_token_by_redirected_url(url)
        API.set_access_token(access_token)
        return access_token

    def set_api(self):
        self.fu.API = API

    def read_lunch_menu(self):
        lu = LUNCH()
        site_url = lu.find_ww(0)
        menu = lu.open_site(url=site_url)
        text = 'good'
        if menu == []:
            print("☺ : Let's go out!!!")
        else:
            lu.find_menu(lunch_menu=menu)
            text = lu.print_day_menu(lu.week_day)
        return text

    def test(self, token):
        # token = "발급받은 엑세스 키 값"
        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": 'Bearer ' + token}

        post = {
            "object_type": "text",
            "text": "Test " + str(datetime.now().strftime("%Y-%m-%d")),
            "link": {
                "web_url": "https://www.naver.com",
                "mobile_web_url": "https://www.naver.com"
            },
            "button_title": "확인"
        }
        data = {"template_object": json.dumps(post)}
        returnValue = requests.post(url, headers=header, data=data)

    def text_msg(self, text):
        # 메시지 유형 - 텍스트
        message_type = "text"

        # 파라미터
        # text = "텍스트 영역입니다. 최대 200자 표시 가능합니다."
        link = {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        }
        button_title = "바로 확인"

        API.send_message_to_me(
            message_type=message_type,
            text=text,
            link=link,
            button_title=button_title,
        )

if __name__ == "__main__":
    sm = SendMsg()
    fu = Functions()
    text = ''
    text = sm.read_lunch_menu()
    send = True
    if send is True:
        token = sm.access()
        sm.set_api()
        # sm.send_feed()
        # sm.list_msg()
        # sm.send_location()
        sm.text_msg(text)
    else:
        token = sm.access()
        sm.test(token)


# hr980320@nate.com
