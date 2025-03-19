# login_page.py

# ID: kim02jo
# PW: 1q2w3e4r!@
# EMAIL: kim_02jo@naver.com
# HP: 010-1234-9999

"""
1. https://www.nibbuns.co.kr/ URL 진입
2. 로그인 버튼 선택 
3. 아이디 선택 후 kim02jo 입력
4. 비밀번호 선택 후 1q2w3e4r!@ 입력
5. 로그인 버튼 선택
6. https://www.nibbuns.co.kr/ 로그인 성공하면 메인홈 이동 확인
7. 로그아웃 버튼 선택
8. 로그인 버튼 노출된 거 확인 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        # 웹 드라이버 초기화
        self.driver = driver

    def open(self):
        # URL 이동 (페이지 로딩 타임아웃 예외 처리 추가)
        try:
            self.driver.get("https://www.nibbuns.co.kr/")
            print("페이지 로딩 완료")
            time.sleep(3)  # 추가 대기 (선택 사항)
        except Exception as e:
            print(f"페이지 로딩 실패: {e}")
            print("페이지 새로고침 시도...")
            try:
                self.driver.refresh()  # ✅ 페이지 새로고침
                time.sleep(5)  # 재시도 후 대기
                print("페이지 새로고침 완료")
            except Exception as e:
                raise AssertionError("페이지 로딩 타임아웃 발생")

    def click_login_button(self):
        # 로그인 버튼 클릭 (href 기반)
        wait = WebDriverWait(self.driver, 15)

        try:
             # 로그인 버튼이 존재하는지 먼저 확인
            wait.until(
                EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/shop/member.html?type=login")]')))
            print("로그인 버튼 찾는 중...")

            # 클릭 가능할 때까지 기다리기
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/shop/member.html?type=login")]'))
            )
            print("로그인 버튼 찾음!")

            # JavaScript 강제 클릭
            self.driver.execute_script("arguments[0].click();", login_button)
            print("로그인 버튼 클릭 완료!")

        except Exception as e:
            print(f"로그인 버튼 찾기 실패: {e}")
            raise AssertionError("로그인 버튼을 찾지 못했습니다.")
    

    def enter_credentials(self, username, password):
        # 아이디와 비밀번호 입력
        username_field = self.driver.find_element(By.NAME, "id")  # 아이디 입력 필드
        password_field = self.driver.find_element(By.NAME, "passwd")  # 비밀번호 입력 필드

        username_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(1)

    def submit_login(self):
        # 로그인 버튼 클릭
        submit_button = self.driver.find_element(By.XPATH, '//a[contains(@class, "CSSbuttonBlack fe")]')
        submit_button.click()
        time.sleep(3)  # 로그인 처리 대기

    def is_logged_in(self):
        # 로그인 성공 여부 확인 (메인 페이지 이동 체크)
        return "https://www.nibbuns.co.kr/" in self.driver.current_url

    def logout(self):
        # 로그아웃 버튼 클릭
        logout_button = self.driver.find_element(By.XPATH, '//a[contains(text(), "로그아웃")]')
        logout_button.click()
        time.sleep(2)

    def is_login_button_visible(self):
        # 로그인 버튼이 다시 나타났는지 확인 (로그아웃 성공 여부 체크)
        try:
            self.driver.find_element(By.XPATH, '//a[contains(text(), "로그인")]')
            return True
        except:
            return False
