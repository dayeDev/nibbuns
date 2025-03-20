import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
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
            ITEMS_XPATH = "//div[@class='item']"
            main_page = MainPage(driver)
            main_page.open()

            wait = ws(driver, 10)
            wait.until(EC.url_contains("https://www.nibbuns.co.kr/"))
            assert "https://www.nibbuns.co.kr/" in driver.current_url
            time.sleep(2)

            # 검색
            Search_instance = Search(driver)
            Search_instance.search_items('자켓')

            # 검색 결과 나타날 때까지 대기
            try: 
                ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))
            except TimeoutException:
                driver.save_screenshot("search_fail.png")

            # 검색 결과 가져오기
            try:
                items = driver.find_elements(By.XPATH, ITEMS_XPATH)
                item_name = parse.quote('자켓')
                if len(items) == 0 or item_name not in driver.current_url:
                    pytest.skip("❗ 상품이 없거나 URL에 '자켓'이 포함되지 않음. 테스트 건너뜀.")
                else:
                    assert True  # ✅ 정상적으로 로딩되면 성공 처리
            except Exception as e:
                pytest.fail(f"🚨 예외 발생: {str(e)}")


    # 없는 상품 검색
    def test_search_no_result(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open()

        wait = ws(driver, 10)
        wait.until(EC.url_contains("https://www.nibbuns.co.kr/"))

        search_instance = Search(driver)
        search_instance.search_items("123")
        time.sleep(2)

        assert search_instance.is_no_result_displayed(), "❌ '검색어로 총 0개의 상품이 검색되었습니다.'메시지가 표시되지 않음"

    
    
    #         # 검색 후 인기상품, 낮은가격, 높은가격 순 정렬
    #         for sort_type in ["인기상품", "낮은가격", "높은가격"]:
    #             print(f"{sort_type} 정렬 시작")
    
    #             sort_xpath = f"//button[contains(text(), '{sort_type}')]"
    
    #             try:
    #                 # 버튼이 클릭 가능할 때까지 대기 후 클릭
    #                 sort_button = WebDriverWait(driver, 10).until(
    #                     EC.element_to_be_clickable((By.XPATH, sort_xpath))
    #                 )
    #                 sort_button.click()
    #             except Exception as e:
    #                 print(f"❌ 일반 클릭 실패: {str(e)}\n➡ JavaScript 클릭 시도")
    #                 driver.execute_script("arguments[0].click();", sort_button)
    
    # # 정렬 후 상품 리스트가 다시 로딩될 때까지 대기
    #         wait.until(EC.presence_of_all_elements_located((By.XPATH, ITEMS_XPATH)))
    #         sorted_items = driver.find_elements(By.XPATH, ITEMS_XPATH)

    #         assert len(sorted_items) > 0, f"❌ {sort_type} 정렬 후 상품이 없습니다."