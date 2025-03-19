import time
import pytest 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from urllib import parse

from src.main_page import MainPage

@pytest.mark.usefixtures("driver") 
class TestMainPage:
# 2. 메인 페이지 접속
    def test_open_main_page(self, driver: WebDriver):
        try:
            ITEMS_XPATH = "//div[@class='item']"
            main_page = MainPage(driver)
            main_page.open()

            wait = ws(driver, 10)
            wait.until(EC.url_contains("https://www.nibbuns.co.kr/"))
            assert "https://www.nibbuns.co.kr/" in driver.current_url
            time.sleep(2)

# 3. "자켓" 검색
            main_page.search_items('자켓')

# 4. 검색 결과 나타날 때까지 대기
            ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))

# 5. 검색 결과 가져오기
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)
            item_name = parse.quote('자켓')

# 6. 검색 결과 확인
            assert len(items) > 0
            assert item_name in driver.current_url
         
        except NoSuchElementException as e:
              assert False
