import pytest
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from shopping_basket import ShoppingBasket  

@pytest.mark.usefixtures("driver")
class TestShoppingBasket:
    
    @classmethod
    def setup_class(cls):
        cls.driver = pytest.global_driver 
        cls.basket_page = ShoppingBasket(cls.driver)
        cls.basket_page.login()  
        cls.basket_page.open()  

    def test_open_shopping_basket(self):
        assert "basket.html" in self.driver.current_url, "장바구니 페이지가 정상적으로 열리지 않았습니다."

    def test_increase_quantity(self):
        self.basket_page.increase_quantity()
        WebDriverWait(self.driver, 5).until(
        lambda d: d.find_element(By.NAME, "amount").get_attribute("value") == "2"
        )
        assert self.driver.find_element(By.NAME, "amount").get_attribute("value") == "2", "수량이 증가되지 않았습니다."
    
    def test_decrease_quantity(self):
        self.basket_page.decrease_quantity()
        WebDriverWait(self.driver, 5).until(
        lambda d: d.find_element(By.NAME, "amount").get_attribute("value") == "1"
        )
    assert self.driver.find_element(By.NAME, "amount").get_attribute("value") == "1", "수량이 감소되지 않았습니다!"

    def test_apply_quantity_change(self):
        self.basket_page.apply_quantity_change()
        WebDriverWait(self.driver, 5).until(EC.staleness_of(self.driver.find_element(By.CLASS_NAME, "btn_option")))
        assert "basket.html" in self.driver.current_url, "수량 적용 후 페이지가 새로고침되지 않았습니다!"

    def test_remove_item(self):
        self.basket_page.remove_item()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())  
        alert = self.driver.switch_to.alert 
        alert.accept()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element((By.CLASS_NAME, "btn_select")))
        assert not self.driver.find_elements(By.CLASS_NAME, "btn_select"), "상품이 삭제되지 않았습니다!"

    def test_proceed_to_checkout(self):
        self.basket_page.proceed_to_checkout()
        
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()  
        except:
            pass  

        WebDriverWait(self.driver, 5).until(EC.url_contains("member.html"))
        assert "member.html" in self.driver.current_url, "주문하기 버튼 클릭 후 로그인 페이지로 이동하지 않았습니다!"
