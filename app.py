import streamlit as st
import subprocess
import os
import importlib.util

st.set_page_config(page_title="로딩 중...", page_icon="⏳", layout="wide")

# GitHub Personal Access Token과 리포지토리 URL 설정
GITHUB_TOKEN = st.secrets["github_token"]
REPO_URL = "https://github.com/DECK6/gamechar.git"
REPO_DIR = "gamechar"

# 디버깅 메시지 추가
st.write("Starting the clone process...")

# Git 클론 명령어 실행
clone_cmd = f"git clone https://{GITHUB_TOKEN}@github.com/DECK6/gamechar.git {REPO_DIR}"
result = subprocess.run(clone_cmd, shell=True, check=False, capture_output=True, text=True)

# 디버깅 메시지 추가
st.write(f"Clone command output: {result.stdout}")
st.write(f"Clone command error (if any): {result.stderr}")

if result.returncode != 0:
    st.error("Failed to clone the repository.")
else:
    st.write("Repository cloned successfully.")
    # 클론한 디렉토리로 이동
    os.chdir(REPO_DIR)
    st.write("Changed directory to cloned repo.")
    
    # 스트림릿 애플리케이션 로드
    try:
        # app.py 파일 경로 설정
        app_path = os.path.join(REPO_DIR, 'app.py')

        # 모듈로서 app.py 파일 불러오기
        spec = importlib.util.spec_from_file_location("app", app_path)
        app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app)
    except Exception as e:
        st.error(f"Failed to run the application: {e}")
