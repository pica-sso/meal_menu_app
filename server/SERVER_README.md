# 🍽 회사 식단표 API (FastAPI)

## 📌 개요
이 서버는 **FastAPI**를 사용하여 회사 식단 정보를 제공하는 API입니다.  
BeautifulSoup을 활용해 웹에서 **식단 데이터를 크롤링**하고, JSON 형태로 제공합니다.

---

## 🏗 프로젝트 구조 (server 폴더)
```commandline
📦 server 
├── 📜 main.py # FastAPI 서버 실행 코드 
├── 📜 menu_scraper.py # 웹 크롤러 (BeautifulSoup 사용) 
├── 📜 models.py # 데이터 모델 (추후 DB 적용 시 사용) 
├── 📜 config.py # 설정 파일 (추후 환경변수 관리) 
├── 📜 requirements.txt # 필요한 Python 패키지 목록 
├── 📂 tests # 테스트 코드 모음 
├── 📂 static # 정적 파일 (이미지 등) 
└── 📜 server_readme.md # 백엔드 설명 문서
```
---

## 🚀 서버 실행 방법

### 1️⃣ 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```
### 2️⃣ 서버 실행
```commandline
uvicorn main:app --reload
```
- 기본적으로 http://127.0.0.1:8000에서 실행됩니다.
- --reload 옵션을 사용하면 코드 변경 시 자동으로 서버가 다시 시작됩니다.
### 3️⃣ API 문서 확인
- FastAPI는 자동으로 API 문서를 생성합니다.
- 아래 주소에서 API 테스트 및 확인이 가능합니다.

> Swagger UI: http://127.0.0.1:8000/docs
> 
> ReDoc: http://127.0.0.1:8000/redoc



### 📌 API 엔드포인트
| 메서드 | 엔드포인트            | 설명 |
|-----|------------------|------|
| GET | `/` | API 상태 확인         |
| GET | `/menu/week`     | 이번 주 전체 메뉴 조회     |
| GET | `/menu/day/{day}` | 특정 요일(월~금)의 메뉴 조회 |

🔹 **예제 요청 및 응답**  
`GET http://127.0.0.1:8000/menu/day/월`
```json
{
  "day": "월",
  "menu": {
    "한식": [
      "고기산적야채조림",
      "얼큰김치국",
      "들기름막국수",
      "아삭이고추양파무침",
      "깍두기/밥3종"
    ],
    "일품식": [
      "순살돈가스",
      "분모자떡볶이",
      "가쓰오장국",
      "열무김치/밥3종"
    ],
    "간편식": [
      "메뉴 중 1가지 선택",
      "1.수제샐러드",
      "2.떠먹는고구마케이크+견과류+음료1종",
      "3.치즈불고기버거+음료1종",
      "4.보틀선식set"
    ]
  }
}
```
---
### 🛠 사용된 기술 스택
- FastAPI: Python 기반의 고성능 API 프레임워크
- BeautifulSoup: HTML 파싱 및 웹 크롤링
- Uvicorn: FastAPI 서버 실행용 ASGI 서버
- SQLite (추후 적용 예정): 데이터베이스 저장
---
### 📝 TODO 리스트
- ✅ 크롤링 로직 수정하여 메뉴 밀리는 문제 해결
- ⏳ 데이터 캐싱 기능 추가 (속도 개선)
- ⏳ 크롤링 주기 자동화 (스케줄링)
- ⏳ SQLite/PostgreSQL 연동 (데이터 저장)
- ⏳ 배포용 Docker 컨테이너 구성
