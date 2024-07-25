from PyKakao import Message
#from send_message import API
# API = Message(service_key="bfc4bd6ba10f9e4bdb90d5ba83501417")


class Functions:
    def __init__(self):
        self.API = None

    def send_feed(self):
        # 메시지 유형 - 피드
        message_type = "feed"

        # 파라미터
        content = {
            "title": "오늘의 디저트",
            "description": "아메리카노, 빵, 케익",
            "image_url": "https://mud-kage.kakao.com/dn/NTmhS/btqfEUdFAUf/FjKzkZsnoeE4o19klTOVI1/openlink_640x640s.jpg",
            "image_width": 640,
            "image_height": 640,
            "link": {
                "web_url": "http://www.daum.net",
                "mobile_web_url": "http://m.daum.net",
                "android_execution_params": "contentId=100",
                "ios_execution_params": "contentId=100"
            }
        }

        item_content = {
            "profile_text": "Kakao",
            "profile_image_url": "https://mud-kage.kakao.com/dn/Q2iNx/btqgeRgV54P/VLdBs9cvyn8BJXB3o7N8UK/kakaolink40_original.png",
            "title_image_url": "https://mud-kage.kakao.com/dn/Q2iNx/btqgeRgV54P/VLdBs9cvyn8BJXB3o7N8UK/kakaolink40_original.png",
            "title_image_text": "Cheese cake",
            "title_image_category": "Cake",
            "items": [
                {
                    "item": "Cake1",
                    "item_op": "1000원"
                },
                {
                    "item": "Cake2",
                    "item_op": "2000원"
                },
                {
                    "item": "Cake3",
                    "item_op": "3000원"
                },
                {
                    "item": "Cake4",
                    "item_op": "4000원"
                },
                {
                    "item": "Cake5",
                    "item_op": "5000원"
                }
            ],
            "sum": "Total",
            "sum_op": "15000원"
        }

        social = {
            "like_count": 100,
            "comment_count": 200,
            "shared_count": 300,
            "view_count": 400,
            "subscriber_count": 500
        }

        buttons = [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net"
                }
            },
            {
                "title": "앱으로 이동",
                "link": {
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            }
        ]

        self.API.send_message_to_me(
            message_type=message_type,
            content=content,
            item_content=item_content,
            social=social,
            buttons=buttons
        )

    def list_msg(self):
        # 메시지 유형 - 리스트
        message_type = "list"

        # 파라미터
        header_title = "WEEKELY MAGAZINE"
        header_link = {
            "web_url": "http://www.daum.net",
            "mobile_web_url": "http://m.daum.net",
            "android_execution_params": "main",
            "ios_execution_params": "main"
        }
        contents = [
            {
                "title": "자전거 라이더를 위한 공간",
                "description": "매거진",
                "image_url": "https://mud-kage.kakao.com/dn/QNvGY/btqfD0SKT9m/k4KUlb1m0dKPHxGV8WbIK1/openlink_640x640s.jpg",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://www.daum.net/contents/1",
                    "mobile_web_url": "http://m.daum.net/contents/1",
                    "android_execution_params": "/contents/1",
                    "ios_execution_params": "/contents/1"
                }
            },
            {
                "title": "비쥬얼이 끝내주는 오레오 카푸치노",
                "description": "매거진",
                "image_url": "https://mud-kage.kakao.com/dn/boVWEm/btqfFGlOpJB/mKsq9z6U2Xpms3NztZgiD1/openlink_640x640s.jpg",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://www.daum.net/contents/2",
                    "mobile_web_url": "http://m.daum.net/contents/2",
                    "android_execution_params": "/contents/2",
                    "ios_execution_params": "/contents/2"
                }
            },
            {
                "title": "감성이 가득한 분위기",
                "description": "매거진",
                "image_url": "https://mud-kage.kakao.com/dn/NTmhS/btqfEUdFAUf/FjKzkZsnoeE4o19klTOVI1/openlink_640x640s.jpg",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://www.daum.net/contents/3",
                    "mobile_web_url": "http://m.daum.net/contents/3",
                    "android_execution_params": "/contents/3",
                    "ios_execution_params": "/contents/3"
                }
            }
        ]
        buttons = [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net"
                }
            },
            {
                "title": "앱으로 이동",
                "link": {
                    "android_execution_params": "main",
                    "ios_execution_params": "main"
                }
            }
        ]

        self.API.send_message_to_me(
            message_type=message_type,
            header_title=header_title,
            header_link=header_link,
            contents=contents,
            buttons=buttons,
        )

    def send_location(self):
        # 메시지 유형 - 위치
        message_type = "location"

        # 파라미터
        address = "경기 성남시 분당구 판교역로 235 에이치스퀘어 N동 7층"
        address_title = "카카오 판교오피스"
        content = {
            "title": "카카오 판교오피스",
            "description": "카카오 판교오피스 위치입니다.",
            "image_url": "https://mud-kage.kakao.com/dn/drTdbB/bWYf06POFPf/owUHIt7K7NoGD0hrzFLeW0/kakaolink40_original.png",
            "image_width": 800,
            "image_height": 800,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com/mobile",
                "android_execution_params": "platform=android",
                "ios_execution_params": "platform=ios"
            }
        }
        buttons = [
            {
                "title": "웹으로 보기",
                "link": {
                    "web_url": "https://developers.kakao.com",
                    "mobile_web_url": "https://developers.kakao.com/mobile"
                }
            }
        ]

        self.API.send_message_to_me(
            message_type=message_type,
            address=address,
            address_title=address_title,
            content=content,
            buttons=buttons,
        )

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

        self.API.send_message_to_me(
            message_type=message_type,
            text=text,
            link=link,
            button_title=button_title,
        )
