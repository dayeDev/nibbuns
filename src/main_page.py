
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

class MainPage:
    URL = "https://www.nibbuns.co.kr/"
    SEARCH_INPUT_SELECTOR = 'input[name="search"]'  

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.URL)

    # 페이지 로드 시간 측정
    def get_page_load_time(self):
        start_time = time.time()
        self.open()
        return time.time() - start_time

    # 버튼 클릭
    def click_button(self, xpath: str):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    def click_news(self):
        self.click_button("//a[@class='child pink' and contains(text(), 'NEW5%')]")
    
    def click_best(self):
        self.click_button("//a[@class='child purple' and contains(text(), 'BEST50')]")
   
    def click_top(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=023')]")
    
    def click_blouse_shirt(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=024')]")

    def click_dress(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=025')]")

    def click_pants(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=026')]")

    def click_skirt(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=027')]")

    def click_outer(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=028')]")
    
    def click_bag_shoes(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=029')]")
    
    def click_acc(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=030')]")
    
    def click_inner_season(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=031')]")

    def click_sale(self):
        self.click_button("//a[contains(@class, 'child') and contains(@href, 'xcode=009')]")
    
    #메인 로고 클릭 시 메인으로 이동
    def click_main_logo(self):
        logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@src='/design/piasom/img/logo.png']")))
        logo.click()

    #배너 클릭
    def banner_click(self, selector):
        banner = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        banner.click()

