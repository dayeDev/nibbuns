# test_login_page.py

import pytest
from src.login_page import LoginPage

def test_login(driver):
    # 1. LoginPage 객체 생성
    login_page = LoginPage(driver)

    # 2. 사이트 접속
    login_page.open()

    # 3. 로그인 버튼 클릭
    login_page.click_login_button()

    # 4. URL이 로그인 페이지로 이동했는지 확인
    # 로그인 페이지 URL
    expected_url = "https://www.nibbuns.co.kr/shop/member.html?type=login"  
    # 현재 URL 가져오기
    current_url = driver.current_url  

    assert expected_url in current_url, f"URL 이동 실패: {current_url} (기대값: {expected_url})"

    # 5. 아이디/비밀번호 입력
    login_page.enter_credentials("kim02jo", "1q2w3e4r!@")

    # 6. 로그인 버튼 클릭
    login_page.submit_login()

    # 7. 로그인 성공 확인
    assert login_page.is_logged_in(), "로그인 실패"

    # 8. 로그아웃 버튼 클릭
    login_page.logout()

    # 9. 로그인 버튼이 다시 나타나는지 확인
    assert login_page.is_login_button_visible(), "로그아웃 실패"