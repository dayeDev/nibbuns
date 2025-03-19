import pytest
import sys
import os
import time
import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 상위 디렉토리로 이동 후 src를 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.recent import Recent


@pytest.mark.usefixtures("driver")
class TestRecent:
    BRAND_ID = "70015"
    URL_NAME = "todaygoods"
    COMPARE_PRODUCT = {
        "product_title" : "(하이퀄리티)볼드하트 담수진주 네크리스",
        "product_price" : "29,000원",
        "product_code" : "70015"
    }
    title = "product_title"
    price = "product_price"
    code = "product_code"

    # 로그 및 스크린샷 경로 설정
    LOG_DIR = "fail_log/test_recent"
    SCREENSHOT_DIR = f"{LOG_DIR}/fail_screenshot"

    # 폴더가 없다면 생성
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    # 로깅 설정
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(f"{LOG_DIR}/recent_page.log", encoding = "utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"))
    logger.addHandler(file_handler)

    # 스크린샷 설정
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = os.path.join(SCREENSHOT_DIR, f"error_{timestamp}.jpg")

    # 오늘 본 상품 페이지 진입 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_open(self, driver: WebDriver):
        recent = Recent(driver)
        wait = ws(driver, 20)

        try:
            # 오늘 본 상품 페이지 진입
            recent.open()

            # 오늘 본 상품 페이지 진입 확인
            wait.until(EC.url_contains(self.URL_NAME))
            assert self.URL_NAME in driver.current_url
            self.logger.info("오늘 본 상품 페이지 진입 성공")
        
        except NoSuchElementException as e:
            self.logger.error(f"오늘 본 상품 페이지 진입 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"오늘 본 상품 페이지 진입 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"오늘 본 상품 페이지 진입 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
    
    
    # 오늘 본 상품 전체 저장 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_save_today_view_product(self, driver: WebDriver):
        recent = Recent(driver)
        wait = ws(driver, 20)

        try:
            # 비교용 상품 페이지 진입
            recent.open_compare_product()

            # 비교용 상품 페이지 진입 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("비교용 상품 페이지 진입 성공")

            # 오늘 본 상품 페이지 진입
            recent.open()

            # 오늘 본 상품 페이지 진입 확인
            wait.until(EC.url_contains(self.URL_NAME))
            assert self.URL_NAME in driver.current_url
            self.logger.info("오늘 본 상품 페이지 진입 성공")

            # 오늘 본 상품 전체 저장
            products = recent.save_today_view_product()

            # 오늘 본 상품 전체 저장 확인
            assert len(products) > 0
            logging.info("오늘 본 상품 전체 저장 성공")
            logging.info(products)

            # 비교 상품 존재 확인
            for product in products:
                assert self.COMPARE_PRODUCT[self.title] in product[self.title]
                assert self.COMPARE_PRODUCT[self.price] in product[self.price]
                assert self.COMPARE_PRODUCT[self.code] in product[self.code]
            self.logger.info("비교 상품 존재 확인 완료")
        
        except NoSuchElementException as e:
            self.logger.error(f"오늘 본 상품 전체 저장 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"오늘 본 상품 전체 저장 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"오늘 본 상품 전체 저장 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False



