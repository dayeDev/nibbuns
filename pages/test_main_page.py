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

        driver.quit()

# 버튼 클릭
    def test_click_buttons(self, driver: WebDriver):
        main_page = MainPage(driver)
        wait = ws(driver, 10)

        main_page.open()
        time.sleep(2)

        button_tests = [
            (main_page.click_news, "shopbrand.html?xcode=016"),
            (main_page.click_best, "bestseller.html?xcode=BEST"),
            (main_page.click_top, "shopbrand.html?xcode=023"),
            (main_page.click_blouse_shirt, "shopbrand.html?xcode=024"),
            (main_page.click_dress, "shopbrand.html?xcode=025"),
            (main_page.click_pants, "shopbrand.html?xcode=026"),
            (main_page.click_skirt, "shopbrand.html?xcode=027"),
            (main_page.click_outer, "shopbrand.html?xcode=028"),
            (main_page.click_bag_shoes, "shopbrand.html?xcode=029"),
            (main_page.click_acc, "shopbrand.html?xcode=030"),
            (main_page.click_inner_season, "shopbrand.html?xcode=031"),
            (main_page.click_sale, "shopbrand.html?xcode=009"),
        ]
# 클릭 후 url 변경 테스트 
        for click_function, expected_url in button_tests:
            click_function() 
            wait.until(EC.url_contains(expected_url)) 
            assert expected_url in driver.current_url, f"❌ {expected_url}로 이동하지 않음"
            time.sleep(2)
            driver.back() 
            time.sleep(1)