import time
import pytest 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from urllib import parse

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main_page import MainPage 

@pytest.mark.usefixtures("driver") 
class TestMainPage:
# 메인 페이지 접속
    def test_open_main_page(self, driver: WebDriver):
        ITEMS_XPATH = "//div[@class='item']"
        main_page = MainPage(driver)
        main_page.open()

        wait = ws(driver, 10)
        wait.until(EC.url_contains("https://www.nibbuns.co.kr/"))
        assert "https://www.nibbuns.co.kr/" in driver.current_url
        time.sleep(2)

# 버튼 클릭 후 url 변경 테스트
    def test_click_buttons(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            wait = ws(drover, 10)
            wait.until(EC.utl_contains("https://www.nibbuns.co.kr/"))

            button_tests = [
                (main_page.click_news, )
            ]