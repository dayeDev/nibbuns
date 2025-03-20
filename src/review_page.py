# review_page.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as ws

class ReviewPage:
    def __init__(self, driver: webdriver):
        # 웹 드라이버 초기화
        self.driver = driver
        self.driver.implicitly_wait(10)  # 페이지 로딩 대기
        self.wait = ws(driver, 20)

    def open(self):
        # 리뷰 페이지 열기
        self.driver.get("https://www.nibbuns.co.kr/shop/reviewmore.html")
    
    def search_click(self, keyword):
        # 검색창 클릭
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "search_keyword")))
        search_input.click()

        # 검색어 입력
        search_input.send_keys(keyword)
        time.sleep(2)  # 입력 후 대기

        # 검색 버튼 클릭
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filter_area"]/div/div/div[6]/div[1]/div/div[2]')))
        search_button.click()
        time.sleep(2)  # 검색 결과 대기

    def get_search_results(self):
        # 검색결과 확인
        try:
            result_items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS, "sf_review_area")))
            return len(result_items) > 0  # 검색 결과 하나 이상이면 true 
        except:
            return False
        