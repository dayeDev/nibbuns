from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class Search:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        
    # 검색
    def search_items(self, item_name: str):
        search_input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.SEARCH_INPUT_SELECTOR))
        )
        search_input_box.clear()
        search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER)

    # 검색 후 정렬 버튼 클릭
    def sort_by_items(self, sort_type: str):
        sort_xpath = f"//a[span[text()='{sort_type}']]"
        sort_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, sort_xpath))
        )
        sort_button.click()