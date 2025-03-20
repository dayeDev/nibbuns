import sys
import os
import pytest
from selenium import webdriver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from order import OrderAutomation

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def order(driver):
    return OrderAutomation(driver)

def test_full_order_process(order):
    order.login()
    order.go_to_cart()
    order.place_order_from_cart()
    order.fill_shipping_info()
    order.check_agreement()
    order.submit_order()
    assert "order_complete" in order.driver.current_url

