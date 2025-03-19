from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class MainPage:
    URL = "https://www.nibbuns.co.kr/"
    SEARCH_INPUT_SELECTOR = 'input[name="search"]'  # 검색창 요소 반영

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.URL)

    # 검색 기능
    def search_items(self, item_name: str):
        search_input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.SEARCH_INPUT_SELECTOR))
        )
        search_input_box.clear()
        search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER)
