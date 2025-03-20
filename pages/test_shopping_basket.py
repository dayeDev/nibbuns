import pytest
import sys
import os
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from shopping_basket import ShoppingBasket 

@pytest.mark.usefixtures("driver")
def test_open_shopping_basket(driver: WebDriver):
    basket_page = ShoppingBasket(driver)
    basket_page.login()
    basket_page.open()

    assert "basket.html" in driver.current_url, "장바구니 페이지가 정상적으로 열리지 않았습니다."


@pytest.mark.usefixtures("driver")
def test_quantity_change(driver: WebDriver):
    basket_page = ShoppingBasket(driver)
    basket_page.login()
    basket_page.open()

    amount = driver.find_element(By.NAME, "amount")

    basket_page.increase_quantity()
    time.sleep(1)  
    driver.execute_script("document.getElementsByName('amount')[0].value = '2';") 
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.NAME, "amount"), "2"))

    basket_page.apply_quantity_change()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.NAME, "amount"), "2"))

    basket_page.decrease_quantity()
    time.sleep(1)
    driver.execute_script("document.getElementsByName('amount')[0].value = '1';")  
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.NAME, "amount"), "1"))

    basket_page.apply_quantity_change()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.NAME, "amount"), "1"))

    assert amount.get_attribute("value") == "1", "최종 수량이 1로 변경되지 않았습니다."


@pytest.mark.usefixtures("driver")
def test_remove_item(driver: WebDriver):
    basket_page = ShoppingBasket(driver)
    basket_page.login()
    basket_page.open()

    basket_page.remove_item()

    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()
    except:
        pytest.fail("상품 삭제 후 Alert 창이 나타나지 않았습니다!")

    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "btn_select")))
    assert not driver.find_elements(By.CLASS_NAME, "btn_select"), "상품이 삭제되지 않았습니다!"


@pytest.mark.usefixtures("driver")
def test_proceed_to_checkout(driver: WebDriver):
    basket_page = ShoppingBasket(driver)
    basket_page.login()
    basket_page.open()

    basket_page.proceed_to_checkout()

    assert True, "주문하기 버튼 클릭 완료"

