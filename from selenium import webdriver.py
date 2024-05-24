from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 로그인 정보 설정
url = "http://localhost:5470/login"  # 실제 로그인 페이지 URL로 변경
username = "admin"  # 실제 사용자명으로 변경
password = "1"  # 실제 비밀번호로 변경

# Selenium WebDriver 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 웹사이트 열기
    driver.get(url)
    time.sleep(2)  # 페이지 로드 대기

    # 사용자명 입력
    username_field = driver.find_element(By.ID, "email")  # username 필드의 ID로 변경
    username_field.clear()
    username_field.send_keys(username)

    # 비밀번호 입력
    password_field = driver.find_element(By.ID, "password")  # password 필드의 ID로 변경
    password_field.clear()
    password_field.send_keys(password)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.ID, "login-btn")  # 로그인 버튼의 ID로 변경
    login_button.click()

    # 로그인 후 페이지 대기
    time.sleep(5)

    # 로그인 성공 메시지 출력
    if "로그인 성공 시 리디렉션 될 URL" in driver.current_url:  # 실제 URL로 변경
        print(f"Logged in successfully as {username}")

    # 브라우저를 닫지 않고 유지하기 위해 무한 루프
    while True:
        time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")

# 의미없는 코드
