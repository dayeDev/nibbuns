from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ShoppingBasket:
    URL = "https://www.nibbuns.co.kr/shop/basket.html"
    LOGIN_URL = "https://www.nibbuns.co.kr/shop/member.html?type=login"
    
    def __init__(self,driver: WebDriver):
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
    
    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_select")))        
    
    def increase_quantity(self): # + 버튼
        plus_button = self.driver.find_element(By.CLASS_NAME, "a_up")
        plus_button.click()
        
    def decrease_quantity(self): # - 버튼
        minus_button = self.driver.find_element(By.CLASS_NAME, "a_dw")
        minus_button.click()
        
    def apply_quantity_change(self): # 수량 적용 버튼
        apply_button = self.driver.find_element(By.CLASS_NAME, "btn_option")
        apply_button.click()
        
    def remove_item(self): # 삭제하기
        delete_button = self.driver.find_element(By.CLASS_NAME, "btn_select")
        delete_button.click()
        
        alert = Alert(self.driver) # 팝업
        alert.accept()
        
    def proceed_to_checkout(self): # 주문하기기
        order_button = self.driver.find_element(By.CLASS_NAME, "CSSbuttonBlack")
        order_button.click()       