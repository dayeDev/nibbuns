import pytest
import sys
import os
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 상위 디렉토리로 이동 후 src를 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.detail_page import DetailPage


@pytest.mark.usefixtures("driver")
class TestDetailPage:
    BRAND_ID = "70015"
    OPTION = "아이보리"
    OPTION_NAME = "MK_p-name"

    # 상품 상세페이지 진입 테스트
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_open_detail_page(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url
        
        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False

    
    # 상품 옵션 선택 테스트
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_select_option(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False


    # 상품 바로 구매 버튼 클릭 테스트 (로그인 기준)
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_buy_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 로그인 진행
            detail_page.login()

            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text

            # 바로 구매 버튼 클릭
            detail_page.buy_click()

            # alert 발생 시 확인 클릭 (장바구니에 이미 상품이 있을 시 발생)
            detail_page.handle_alert()

            # 구매 페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains("order"))
            assert "order" in driver.current_url

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False
    

    # 장바구니 버튼 클릭 테스트 (로그인 기준)
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_cart_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 로그인 진행
            detail_page.login()

            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text

            # 장바구니 버튼 클릭
            detail_page.cart_click()

            # 장바구니 담김 팝업 노출 확인
            cart_popup = wait.until(EC.visibility_of_element_located((By.ID, "cartPop")))
            assert cart_popup.is_displayed()

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False


    # 상품상세 탭 클릭 테스트
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_goods_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 상품상세 탭 클릭
            detail_page.detail_goods_click()

            time.sleep(3)

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_GOODS_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False


    # 상품후기 탭 클릭 테스트
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_review_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 상품후기 탭 클릭
            detail_page.detail_review_click()

            time.sleep(3)

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_REVIEW_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False


    # 상품문의 탭 클릭 테스트
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_qna_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 상품문의 탭 클릭
            detail_page.detail_qna_click()

            time.sleep(3)

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_QNA_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False

    
    # 관련상품 탭 클릭 테스트
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_relation_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 관련상품 탭 클릭
            detail_page.detail_relation_click()

            time.sleep(3)

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_RELATION_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False

    
    # 배송 교환 반품 탭 클릭 테스트
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_detail_change_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 관련상품 탭 클릭
            detail_page.detail_change_click()

            time.sleep(3)

            # 눌렸는지 확인
            active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_page.DETAIL_CHANGE_EL + ".active")))
            assert "active" in active_tab.get_attribute("class")

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False


    
    # 상품 하단 스크롤 후 바로 구매 버튼 클릭 테스트 (로그인 기준)
    @pytest.mark.skip(reason="테스트 케이스 SKIP")
    def test_fixed_buy_click(self, driver: WebDriver):
        detail_page = DetailPage(driver)
        wait = ws(driver, 20)

        try:
            # 로그인 진행
            detail_page.login()

            # 상품 상세페이지 진입
            detail_page.open()

            # 상품 상세페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains(self.BRAND_ID))
            assert self.BRAND_ID in driver.current_url

            time.sleep(1)

            # 상품 옵션 선택
            detail_page.select_option(self.OPTION)

            # 상품 옵션 정상 선택되었는지 확인
            option_check = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.OPTION_NAME)))
            assert self.OPTION == option_check.text

            time.sleep(2)

            # 스크롤 후 바로 구매 버튼 클릭
            detail_page.fixed_buy_click()

            info_fixed = wait.until(EC.presence_of_element_located((By.ID, "info")))
            assert info_fixed.is_displayed()

            time.sleep(2)

            # 바로 구매 버튼 클릭
            detail_page.buy_click()

            # alert 발생 시 확인 클릭 (장바구니에 이미 상품이 있을 시 발생)
            detail_page.handle_alert()

            # 구매 페이지 정상 진입하였는지 확인
            wait.until(EC.url_contains("order"))
            assert "order" in driver.current_url

        except NoSuchElementException as e:
            assert False
        
        except TimeoutException as e:
            assert False
        
        except Exception as e:
            assert False