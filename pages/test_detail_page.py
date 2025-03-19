import pytest
import sys
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 상위 디렉토리로 이동 후 src를 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.detail_page import DetailPage


@pytest.mark.usefixtures("driver")
class TestDetailPage:
    BRAND_ID = "69560"

    # 상품 상세페이지 진입 테스트
    def test_open_detail_page(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            detail_page.open()
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
        
        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False
    


        