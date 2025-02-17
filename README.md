# 🍽 회사 식단표 API 및 웹/모바일 앱 개발

## 📌 프로젝트 개요
회사의 식단표를 자동으로 크롤링하고, 이를 웹과 모바일 앱에서 확인할 수 있도록 하는 프로젝트입니다.  
현재 **FastAPI를 이용한 백엔드 개발이 완료**되었으며, 앞으로 **React 및 React Native를 활용한 프론트엔드 개발을 진행할 예정**입니다.

---

## 🖥 개발 환경
- 운영 체제: **Windows**
- 프로그래밍 언어: **Python 3.11**
- 프레임워크 및 라이브러리:
  - **FastAPI** (백엔드 API 서버)
  - **BeautifulSoup** (웹 크롤링)
  - **React / React Native** (프론트엔드 예정)
  - **SQLite / PostgreSQL** (데이터베이스 예정)

---
## 🏗 개발 진행 과정

### 1️⃣ FastAPI를 활용한 백엔드 개발 (완료 ✅)
- FastAPI를 이용하여 **회사 식단 데이터를 제공하는 API 개발**
- `BeautifulSoup`을 활용한 **웹 크롤링 기능** 구현
- **로컬 서버**에서 테스트 완료

### 2️⃣ API 엔드포인트 (진행 중)
| 엔드포인트 | 설명 |
|-----------|------|
| `GET /` | API 상태 확인 |
| `GET /menu/week` | 이번 주 전체 메뉴 조회 |
| `GET /menu/day/{day}` | 특정 요일(월~금)의 메뉴 조회 |
---
## 🔥 다음 단계
### 3️⃣ 웹 프론트엔드 개발 (예정)
- React 또는 Next.js를 활용하여 웹페이지에서 메뉴 조회 기능 추가
- API 데이터를 가져와 화면에 표시
### 4️⃣ 모바일 앱 개발 (예정)
- React Native를 활용하여 모바일 앱 개발
- API 데이터를 활용하여 식단 정보를 앱에서 확인 가능하도록 구현
### 5️⃣ 서버 배포 (예정)
- FastAPI 서버를 **클라우드(AWS, Render 등)** 에 배포하여 어디서든 접근 가능하도록 설정
---


## 🖥 서버 실행 방법
### Windows 환경
1. **Python 가상환경 설정 (처음 한 번만 실행)**
    ```sh
    python -m venv venv
    venv\Scripts\activate
    pip install -r server/requirements.txt
    ```
2. **서버 실행**
    - `server_start.bat` 실행 → 자동으로 서버가 실행됨
    - 또는 수동 실행:
    ```sh
    cd server
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```
---
## 📂 프로젝트 폴더 구조
```commandline
📦 menu_amkor
├── 📂 server                 # FastAPI 기반 서버
│   ├── 📜 main.py            # FastAPI 서버 실행 코드
│   ├── 📜 menu_scraper.py    # 웹 크롤러 (BeautifulSoup 사용)
│   ├── 📜 models.py          # 데이터 모델 (추후 DB 적용 시 사용)
│   ├── 📜 config.py          # 설정 파일 (추후 환경변수 관리)
│   ├── 📜 requirements.txt   # 필요한 Python 패키지 목록
│   ├── 📂 tests              # 테스트 코드 모음
│   ├── 📂 static             # 정적 파일 (이미지 등)
│   └── 📜 SERVER_README.md   # 백엔드 설명 문서
│
├── 📂 web                    # React 기반 웹 프론트엔드
│   ├── 📜 package.json       # npm 패키지 정보
│   ├── 📜 index.js           # 웹 진입점
│   ├── 📂 src                # React 컴포넌트 및 페이지
│   ├── 📂 public             # 정적 파일 (favicon 등)
│   └── 📜 README.md          # 웹 설명 문서
│
├── 📂 app                    # React Native 기반 모바일 앱
│   ├── 📜 package.json       # npm 패키지 정보
│   ├── 📜 App.js             # 앱 진입점
│   ├── 📂 src                # React Native 컴포넌트 및 화면
│   ├── 📂 assets             # 앱에서 사용하는 이미지 등
│   └── 📜 README.md          # 모바일 앱 설명 문서
│
├── 📂 deploy                 # 배포 관련 파일
│   ├── 📜 Dockerfile         # 컨테이너화된 배포 설정
│   ├── 📜 docker-compose.yml # 여러 컨테이너를 구성하는 설정 파일
│   ├── 📜 nginx.conf         # Nginx 리버스 프록시 설정
│   ├── 📜 startup.sh         # 서버 실행 스크립트
│   └── 📜 README.md          # 배포 설명 문서
│
├── 📂 icons                  # 프로젝트 아이콘 및 로고
│   ├── 📜 lunch.ico          # 앱 아이콘
│
├── 📜 server_start.bat       # window에서 server 시작 배치 파일
├── 📜 .env                   # 환경변수 설정 파일
├── 📜 README.md              # 프로젝트 설명 문서
└── 📜 LICENSE                # 라이선스 정보
```
---
## 🛠 기술 스택
- Backend: FastAPI, Python, BeautifulSoup, Uvicorn
- Frontend (예정): React (Next.js), React Native
- Database (예정): SQLite or PostgreSQL
- Deployment (예정): Render, AWS, 또는 Vercel
---
## 💡 참고 및 개선할 점
- 프론트엔드 개발 후 API 최적화 진행 예정


