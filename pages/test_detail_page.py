import pytest
import sys
import os
import time
import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 상위 디렉토리로 이동 후 src를 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.detail_page import DetailPage
from src.recent import Recent


@pytest.mark.usefixtures("driver")
class TestDetailPage:
    BRAND_ID = "70015"
    OPTION = "아이보리"
    OPTION_NAME = "MK_p-name"
    title = "product_title"
    code = "product_code"

    # 로그 및 스크린샷 경로 설정
    LOG_DIR = "logs/test_detail_page"
    SCREENSHOT_DIR = f"{LOG_DIR}/fail_screenshot"

    # 폴더가 없다면 생성
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    # 로깅 설정
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(f"{LOG_DIR}/detail_page.log", encoding = "utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"))
    logger.addHandler(file_handler)

    # 스크린샷 설정
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = os.path.join(SCREENSHOT_DIR, f"error_{timestamp}.jpg")

    # 상품 상세페이지 진입 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_open_detail_page(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")
        
        except NoSuchElementException as e:
            self.logger.error(f"상품 상세페이지 진입 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"상품 상세페이지 진입 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"상품 상세페이지 진입 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

    
    # 상품 옵션 선택 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_select_option(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text
            self.logger.info("상품 옵션 선택 성공")

        except NoSuchElementException as e:
            self.logger.error(f"상품 옵션 선택 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"상품 옵션 선택 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"상품 옵션 선택 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False


    # 상품 바로 구매 버튼 클릭 테스트 (로그인 기준)
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_buy_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 로그인 진행
            detail_page.login()

            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text
            self.logger.info("상품 옵션 선택 성공")

            # 바로 구매 버튼 클릭
            detail_page.buy_click()

            # alert 발생 시 확인 클릭 (장바구니에 이미 상품이 있을 시 발생)
            detail_page.handle_alert()

            # 구매 페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains("order"))
            assert "order" in driver.current_url
            self.logger.info("상품 구매 버튼 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"상품 구매 버튼 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"상품 구매 버튼 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"상품 구매 버튼 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
    

    # 장바구니 버튼 클릭 테스트 (로그인 기준)
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_cart_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 로그인 진행
            detail_page.login()

            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text
            self.logger.info("상품 옵션 선택 성공")

            # 장바구니 버튼 클릭
            detail_page.cart_click()

            # 장바구니 담김 팝업 노출 확인
            cart_popup = wait.until(EC.visibility_of_element_located((By.ID, "cartPop")))
            assert cart_popup.is_displayed()
            self.logger.info("장바구니 버튼 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"장바구니 버튼 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"장바구니 버튼 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"장바구니 버튼 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

    
    # 관심상품 버튼 클릭 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_wish_list_click(self, driver:WebDriver):
        detail_page = DetailPage(driver)
        recent = Recent(driver)
        wait = ws(driver, 10)
        page_type = "mywishlist"

        try:
            # 로그인 진행
            detail_page.login()

            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 비교용 상품 정보 저장
            compare_products = recent.save_compare_droduct()

            # 비교용 상품 정보 저장 확인
            assert len(compare_products) > 0
            logging.info("상품 정보 저장 성공")
            logging.info(compare_products)

            # 관심상품 버튼 클릭
            detail_page.wish_list_click()

            # alert 발생 시 확인 클릭 (관심상품에 동일한 상품이 있을 시 발생)
            detail_page.handle_alert()

            # 확인용 관심상품 페이지 진입
            detail_page.open_wish_list()

            # 확인용 관심상품 페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(page_type))
            assert page_type in driver.current_url
            self.logger.info("관심상품 페이지 진입 성공")

            # 확인용 관심상품 페이지에 상품 정보 저장
            wish_list_droducts = detail_page.save_compare_wish_list_product()

            # 확인용 관심상품 페이지 상품 정보 저장 확인
            assert len(wish_list_droducts) > 0
            logging.info("확인용 상품 정보 저장 성공")
            logging.info(wish_list_droducts)

            # 비교 상품 존재 확인
            for wish_list_product in wish_list_droducts:
                assert any([
                    compare_products[0][self.title] in wish_list_product[self.title],
                ])
            self.logger.info("비교 상품 존재 확인 완료")
        
        except NoSuchElementException as e:
            self.logger.error(f"비교 상품 존재 확인 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"비교 상품 존재 확인 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"비교 상품 존재 확인 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False


    # 상품상세 탭 클릭 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_goods_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 상품상세 탭 클릭
            detail_page.detail_goods_click()

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_GOODS_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")
            self.logger.info("상품상세 탭 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"상품상세 탭 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"상품상세 탭 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"상품상세 탭 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False


    # 상품후기 탭 클릭 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_review_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 상품후기 탭 클릭
            detail_page.detail_review_click()

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_REVIEW_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")
            self.logger.info("상품후기 탭 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"상품후기 탭 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

        except TimeoutException as e:
            self.logger.error(f"상품후기 탭 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"상품후기 탭 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False


    # 상품문의 탭 클릭 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_qna_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 상품문의 탭 클릭
            detail_page.detail_qna_click()

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_QNA_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")
            self.logger.info("상품문의 탭 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"상품문의 탭 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

        except TimeoutException as e:
            self.logger.error(f"상품문의 탭 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"상품문의 탭 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

    
    # 관련상품 탭 클릭 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_relation_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 관련상품 탭 클릭
            detail_page.detail_relation_click()

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_RELATION_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")
            self.logger.info("관련상품 탭 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"관련상품 탭 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

        except TimeoutException as e:
            self.logger.error(f"관련상품 탭 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"관련상품 탭 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

    
    # 배송 교환 반품 탭 클릭 테스트
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_change_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 배송 교환 반품 탭 클릭
            detail_page.detail_change_click()

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_CHANGE_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")
            self.logger.info("배송 교환 반품 탭 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"배송 교환 반품 탭 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False

        except TimeoutException as e:
            self.logger.error(f"배송 교환 반품 탭 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"배송 교환 반품 탭 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False


    # 스크롤 후 바로 구매 버튼 클릭 테스트 (로그인 기준)
    #@pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_fixed_buy_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 10)

        try:
            # 로그인 진행
            detail_page.login()

            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
            self.logger.info("상품 상세페이지 진입 성공")

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text
            self.logger.info("상품 옵션 선택 성공")

            # 스크롤 후 바로 구매 버튼 클릭
            detail_page.fixed_buy_click()

            # 스크롤 후 바로 구매 버튼 클릭하였는지 확인
            info_fixed = wait.until(EC.presence_of_element_located((By.ID, "info")))
            assert info_fixed.is_displayed()
            self.logger.info("스크롤 후 바로 구매 버튼 클릭 성공")

            # 바로 구매 버튼 클릭
            detail_page.buy_click()

            # alert 발생 시 확인 클릭 (장바구니에 이미 상품이 있을 시 발생)
            detail_page.handle_alert()

            # 구매 페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains("order"))
            assert "order" in driver.current_url
            self.logger.info("상품 구매 버튼 클릭 성공")

        except NoSuchElementException as e:
            self.logger.error(f"스크롤 후 바로 구매 버튼 클릭 실패: 요소를 찾을 수 없음. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except TimeoutException as e:
            self.logger.error(f"스크롤 후 바로 구매 버튼 클릭 실패: 시간 초과. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False
        
        except Exception as e:
            self.logger.error(f"스크롤 후 바로 구매 버튼 클릭 실패: 알 수 없는 오류 발생. {e}")
            driver.save_screenshot(self.screenshot_name)
            assert False