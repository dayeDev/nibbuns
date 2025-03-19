import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from urllib import parse
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main_page import MainPage 
from search import Search

@pytest.mark.usefixtures("driver") 
class TestMainPage:
    # 메인 페이지 열기 및 검색 테스트
    def test_search(self, driver: WebDriver):
        try:
            ITEMS_XPATH = "//div[@class='item']"
            main_page = MainPage(driver)
            main_page.open()

            wait = ws(driver, 20)  # 대기 시간 증가
            wait.until(EC.url_contains("https://www.nibbuns.co.kr/"))
            assert "https://www.nibbuns.co.kr/" in driver.current_url
            time.sleep(2)

# 검색
            search.search_items('자켓')

# 4. 검색 결과 나타날 때까지 대기
            try: 
                ws(driver, 20).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))
            except TimeoutException:
                pass 

# 5. 검색 결과 가져오기
                items = driver.find_elements(By.XPATH, ITEMS_XPATH)
                item_name = parse.quote('자켓')

# 6. 검색 결과 확인
                assert len(items) > 0
                assert item_name in driver.current_url


# 검색 후 인기상품, 낮은가격, 높은가격 순 정렬
                for sort_type in ["인기상품", "낮은가격", "높은가격"]: 
                search.sort_items(sort_type)
                wait.until(EC.presence_of_all_elements_located((By.XPATH, ITEMS_XPATH)))

# 정렬 후 상품이 존재하는지 확인 
                sorted_items = driver.find_elements(By.XPATH, ITEMS_XPATH)
                assert len(sorted_items) > 0, f"{sort_type} 정렬 후 상품이 없습니다."

        except NoSuchElementException:
            driver.save_screenshot("search_test_no_element.png")
            pytest.fail("검색 또는 정렬 요소를 찾을 수 없습니다.")
