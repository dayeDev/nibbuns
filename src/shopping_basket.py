from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ShoppingBasket:
    URL = "https://www.nibbuns.co.kr/shop/basket.html"
    LOGIN_URL = "https://www.nibbuns.co.kr/shop/member.html?type=login"
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self):
        self.driver.get(self.LOGIN_URL)
        time.sleep(1)  

        id_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "id")))
        id_input.send_keys("kim02jo")

        pw_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "passwd")))
        pw_input.send_keys("1q2w3e4r!@")

        login_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "CSSbuttonBlack")))
        login_button.click()

        time.sleep(1)  

    def open(self)
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn_select")))

    def increase_quantity(self):
        plus_button = self.driver.find_element(By.CLASS_NAME, "a_up")
        plus_button.click()

    def decrease_quantity(self):
        minus_button = self.driver.find_element(By.CLASS_NAME, "a_dw")
        minus_button.click()

    def apply_quantity_change(self):
        apply_button = self.driver.find_element(By.CLASS_NAME, "btn_option")
        apply_button.click()

    def remove_item(self):

        delete_button = self.driver.find_element(By.CLASS_NAME, "btn_select")
        delete_button.click()
        
        self.wait.until(EC.alert_is_present()) 
        alert = Alert(self.driver)
        alert.accept()

    def proceed_to_checkout(self):
        order_button = self.driver.find_element(By.CLASS_NAME, "CSSbuttonBlack")
        order_button.click()
