import pytest 
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from shopping_basket import ShoppingBasket  

class TestShoppingBasket:
    
    @pytest.fixture(autouse=True)
    def setup_method(self, driver):
        self.driver = driver  
        self.driver.implicitly_wait(10)  
        self.basket_page = ShoppingBasket(self.driver)
        self.basket_page.login()
        self.basket_page.open()

    def test_open_shopping_basket(self):
        assert "basket.html" in self.driver.current_url, "장바구니 페이지가 정상적으로 열리지 않았습니다."

    def test_quantity_change(self):
        
        # Step 1: 초기 수량 확인
        initial_amount = self.driver.find_element(By.NAME, "amount").get_attribute("value")
        assert initial_amount == "1", "초기 수량이 1이 아닙니다!"

        # Step 2: 수량 증가 (+1)
        self.basket_page.increase_quantity()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.NAME, "amount"), "2")
            )
        except TimeoutException:
            pytest.fail("수량 증가 버튼 클릭 후 값이 '2'로 변경되지 않았습니다.")

        assert self.driver.find_element(By.NAME, "amount").get_attribute("value") == "2", "수량이 증가되지 않았습니다."

        # Step 3: 수량 감소 (-1)
        self.basket_page.decrease_quantity()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.NAME, "amount"), "1")
            )
        except TimeoutException:
            pytest.fail("수량 감소 버튼 클릭 후 값이 '1'로 변경되지 않았습니다.")

        assert self.driver.find_element(By.NAME, "amount").get_attribute("value") == "1", "수량이 감소되지 않았습니다!"

    def test_apply_quantity_change(self):
        self.basket_page.apply_quantity_change()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(self.driver.find_element(By.CLASS_NAME, "btn_option"))
            )
        except TimeoutException:
            pytest.fail("수량 적용 후 버튼이 사라지지 않았습니다.")

        assert "basket.html" in self.driver.current_url, "수량 적용 후 페이지가 새로고침되지 않았습니다!"

    def test_remove_item(self):
        self.basket_page.remove_item()
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())  
            alert = Alert(self.driver)
            alert.accept()
        except NoAlertPresentException:
            pytest.fail("상품 삭제 후 Alert 창이 나타나지 않았습니다.")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element((By.CLASS_NAME, "btn_select"))
            )
        except TimeoutException:
            pytest.fail("상품이 삭제된 후에도 장바구니에서 보이지 않습니다.")

        assert not self.driver.find_elements(By.CLASS_NAME, "btn_select"), "상품이 삭제되지 않았습니다!"

    def test_proceed_to_checkout(self):
        self.basket_page.proceed_to_checkout()
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("member.html"))
        except TimeoutException:
            pytest.fail("주문하기 버튼 클릭 후 로그인 페이지로 이동하지 않았습니다.")

        assert "member.html" in self.driver.current_url, "주문하기 버튼 클릭 후 로그인 페이지로 이동하지 않았습니다!"
