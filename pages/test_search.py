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
            main_page.search_items('자켓')

# 4. 검색 결과 나타날 때까지 대기
            ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))

# 5. 검색 결과 가져오기
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)
            item_name = parse.quote('자켓')

# 6. 검색 결과 확인
            assert len(items) > 0
            assert item_name in driver.current_url

        except TimeoutException:
            driver.save_screenshot("search_test_failed.png")
            pytest.fail("검색 결과 로딩이 너무 오래 걸립니다.")

        except NoSuchElementException:
            driver.save_screenshot("search_test_no_element.png")
            pytest.fail("검색 요소를 찾을 수 없습니다.")
         
        except NoSuchElementException as e:
              assert False
        finally:
              driver.quit() 
