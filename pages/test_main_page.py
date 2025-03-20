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

# 페이지 로딩 ㅅ속도
    def test_page_load_speed(self, driver: WebDriver):
        main_page = MainPage(driver)
        load_time = main_page.get_page_load_time()
        assert load_time < 5, f"❌ 페이지 로딩 속도가 너무 느림 ({load_time:.4f}초)"

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

# 메인 로고 클릭시 메인페이지로 이동 
        main_page.click_main_logo()
        wait.until(EC.url_contains("https://www.nibbuns.co.kr/")) 
        assert "https://www.nibbuns.co.kr/" in driver.current_url, "❌ 메인 페이지로 이동하지 않음"

# 배너 클릭
    def test_click_buttons(self, driver: WebDriver):
        main_page = MainPage(driver)
        wait = ws(driver, 10)

        main_page.open()
        time.sleep(2)

        banner = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-swiper-slide-index="3"] a')))
        banner.click()

        wait.until(EC.url_contains("https://www.nibbuns.co.kr/shop/shopdetail"))
        assert "https://www.nibbuns.co.kr/shop/shopdetail" in driver.current_url, "❌ 상세 페이지로 이동하지 않음"