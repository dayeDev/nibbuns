from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OrderAutomation:
    LOGIN_URL = "https://www.nibbuns.co.kr/shop/member.html?type=login"
    CART_URL = "https://www.nibbuns.co.kr/shop/basket.html"
    ORDER_URL = "https://www.nibbuns.co.kr/shop/order.html"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self):
        self.driver.get(self.LOGIN_URL)
        time.sleep(2)
        self.driver.find_element(By.NAME, "id").send_keys("kim02jo")
        self.driver.find_element(By.NAME, "passwd").send_keys("1q2w3e4r!@")
        self.driver.find_element(By.CLASS_NAME, "CSSbuttonBlack").click()
        time.sleep(2)

    def go_to_cart(self):
        self.driver.get(self.CART_URL)
        time.sleep(2)

    def place_order_from_cart(self):
        self.driver.find_element(By.CLASS_NAME, "CSSbuttonBlack").click()
        time.sleep(2)

    def fill_shipping_info(self):
        self.driver.get(self.ORDER_URL)
        time.sleep(2)
        checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, "same")))
        checkbox.click()
        time.sleep(2)

    def check_agreement(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "pay_agree"))).click()

    def submit_order(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "CSSbuttonBlack"))).click()
        time.sleep(3)
