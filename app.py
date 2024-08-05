import streamlit as st
import subprocess
import os

# GitHub Personal Access Token과 리포지토리 URL 설정
GITHUB_TOKEN = st.secrets["github_token"]
REPO_URL = "https://github.com/DECK6/gamechar.git"
REPO_DIR = "gamechar"

# Git 클론 명령어 실행
clone_cmd = f"git clone https://{GITHUB_TOKEN}@github.com/DECK6/gamechar.git {REPO_DIR}"
subprocess.run(clone_cmd, shell=True, check=True)

# 클론한 디렉토리로 이동
os.chdir(REPO_DIR)

# 스트림릿 애플리케이션 로드
exec(open("app.py").read())  # 실제 스트림릿 애플리케이션 파일 이름으로 변경
