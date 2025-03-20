from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Recent:
    URL = "https://www.nibbuns.co.kr/shop/todaygoods.html"
    COMPARE_URL = "https://www.nibbuns.co.kr/shop/shopdetail.html?branduid=70015"
    TODAY_PRODUCTS_EL = "tb-prd"
    PRODUCT_TITLE_EL = "dsc"
    PRODUCT_PRICE_EL = "price_1"
    PRODUCT_URL_EL = "td:nth-child(4) a"
    COMPARE_PRODUCT_TITLE_EL = "tit-prd"
    COMPARE_PRODUCT_PRICE_EL = "sell_price"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(driver, 20)

    # 오늘 본 상품 페이지 열기
    def open(self):
        self.driver.get(self.URL)
 
    # 오늘 본 상품 정보 저장
    def save_today_view_product(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.TODAY_PRODUCTS_EL)))
        today_products = self.driver.find_elements(By.CLASS_NAME, self.TODAY_PRODUCTS_EL)
        product_list = []
        for product in today_products:
            product_title = product.find_element(By.CLASS_NAME, self.PRODUCT_TITLE_EL).text
            product_price = product.find_element(By.CLASS_NAME, self.PRODUCT_PRICE_EL).text
            product_url = product.find_element(By.CSS_SELECTOR, self.PRODUCT_URL_EL).get_attribute("href")
            product_code = product_url.split("branduid=")[1].split("&")[0]
            product_list.append({
                "product_title" : product_title,
                "product_price" : product_price,
                "product_code" : product_code
            })
        return product_list
    
    # 비교용 상품 페이지 열기
    def open_compare_product(self):
        self.driver.get(self.COMPARE_URL)

    # 비교용 상품 정보 저장
    def save_compare_droduct(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.COMPARE_PRODUCT_TITLE_EL)))
        compare_product_list = []  
        product_title = self.driver.find_element(By.CLASS_NAME, self.COMPARE_PRODUCT_TITLE_EL).text
        product_price = self.driver.find_element(By.CLASS_NAME, self.COMPARE_PRODUCT_PRICE_EL).text
        product_url = self.driver.current_url
        product_code = product_url.split("branduid=")[1].split("&")[0]          
        compare_product_list.append({
            "product_title" : product_title,
            "product_price" : product_price,
            "product_code" : product_code
        })
        return compare_product_list
    
        