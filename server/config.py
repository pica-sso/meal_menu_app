import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 서버 설정
SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
DEBUG_MODE = os.getenv("DEBUG_MODE", "True") == "True"

# 로깅 설정
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "./logs/server.log")

