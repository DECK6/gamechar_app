import streamlit as st
import subprocess
import os

st.set_page_config(page_title="사진으로 게임 캐릭터 만들기", page_icon="🎮", layout="wide")

# GitHub Personal Access Token과 리포지토리 URL 설정
GITHUB_TOKEN = st.secrets["github_token"]
REPO_URL = "https://github.com/DECK6/gamechar.git"  # 각 리포지토리에 맞게 변경
REPO_DIR = "gamechar"  # 각 리포지토리에 맞게 변경

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
        import app  # 실제 스트림릿 애플리케이션 파일을 모듈로 가져오기
    except Exception as e:
        st.error(f"Failed to run the application: {e}")
