import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DetailPage:
    # 요소
    URL = "https://www.nibbuns.co.kr/shop/shopdetail.html?branduid=70015"
    COMPARE_URL = "https://www.nibbuns.co.kr/shop/mypage.html?mypage_type=mywishlist"
    OPTION_LIST_EL = "basic_option"
    BUY_BUTTON_EL = "btn_buy"
    CART_BUTTON_EL = "cartBtn"
    WISH_LIST_BUTTON_EL = "#info > div.prd-btns > a:nth-child(4)"
    DETAIL_GOODS_EL = "#productDetail li.first > a"
    DETAIL_REVIEW_EL = "#productDetail li:nth-child(2) > a"
    DETAIL_QNA_EL = "#productDetail li:nth-child(3) > a"
    DETAIL_RELATION_EL = "#productDetail li:nth-child(4) > a"
    DETAIL_CHANGE_EL = "#productDetail li:nth-child(5) > a"
    FIXED_BUY_EL = "fixed_buy"
    WISH_LIST_PRODUCTS_EL = "#myWish"
    WISH_LIST_PRODUCT_TITLE_EL = "tb-left"
    WISH_LIST_PRODUCT_URL_EL = "tb-center"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(driver, 20)
    
    # 상품 페이지 열기
    def open(self):
        self.driver.get(self.URL)

    # 상품 옵션 선택
    def select_option(self, option):
        option_dropdown = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.OPTION_LIST_EL)))
        option_dropdown.click()
        select = Select(option_dropdown) # option 선택용 Select 모듈 사용
        select.select_by_visible_text(option)
    
    # 바로 구매 버튼 클릭
    def buy_click(self):
        buy_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.BUY_BUTTON_EL)))
        buy_button.click()

    # 장바구니 버튼 클릭
    def cart_click(self):
        cart_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.CART_BUTTON_EL)))
        cart_button.click()
    
    # 관심상품 버튼 클릭
    def wish_list_click(self):
        wish_list_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.WISH_LIST_BUTTON_EL)))
        wish_list_button.click()

    # 상품상세 탭 클릭
    def detail_goods_click(self):
        detail_goods_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_GOODS_EL)))
        self.driver.execute_script("arguments[0].click();", detail_goods_tab)

    # 상품후기 탭 클릭
    def detail_review_click(self):
        detail_review_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_REVIEW_EL)))
        self.driver.execute_script("arguments[0].click();", detail_review_tab)
    
    # 상품문의 탭 클릭
    def detail_qna_click(self):
        detail_qna_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_QNA_EL)))
        self.driver.execute_script("arguments[0].click();", detail_qna_tab)

    # 관련상품 탭 클릭
    def detail_relation_click(self):
        detail_relation_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_RELATION_EL)))
        self.driver.execute_script("arguments[0].click();", detail_relation_tab)

    # 배송 교환 반품 탭 클릭
    def detail_change_click(self):
        detail_change_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_CHANGE_EL)))
        self.driver.execute_script("arguments[0].click();", detail_change_tab)

    # 하단 스크롤 후 바로 구매 클릭
    def fixed_buy_click(self):
        # 현재 페이지의 전체 높이를 가져옵니다
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")
        # 전체 높이의 절반만큼 스크롤
        self.driver.execute_script(f"window.scrollTo(0, {scroll_height / 2});")
        # 버튼 클릭
        fixed_buy_button = self.wait.until(EC.presence_of_element_located((By.ID, self.FIXED_BUY_EL)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", fixed_buy_button)  # 버튼이 보이도록 스크롤
        fixed_buy_button.click()

    # 알럿 처리 함수
    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass

    # 임시 로그인 함수
    def login(self):
        self.driver.get("https://www.nibbuns.co.kr/shop/member.html?type=login")
        time.sleep(1)
        id_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "id")))
        id_input.send_keys("kim02jo")
        pw_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "passwd")))
        pw_input.send_keys("1q2w3e4r!@")
        login_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "CSSbuttonBlack")))
        login_button.click()
        time.sleep(1)

    # 확인용 관심상품 페이지 열기
    def open_wish_list(self):
        self.driver.get(self.COMPARE_URL)

    # 확인용 관심상품 정보 저장
    def save_compare_wish_list_product(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.WISH_LIST_PRODUCTS_EL)))
        wish_list_products = self.driver.find_elements(By.CSS_SELECTOR, self.WISH_LIST_PRODUCTS_EL)
        wish_list_product_list = []
        for product in wish_list_products:
            product_title = product.find_element(By.CLASS_NAME, self.WISH_LIST_PRODUCT_TITLE_EL).text
            product_url = product.find_element(By.CLASS_NAME, self.WISH_LIST_PRODUCT_URL_EL).get_attribute("href")
            product_code = product_url.split("branduid=")[1]
            wish_list_product_list.append({
                "product_title" : product_title,
                "product_code" : product_code
            })
        return wish_list_product_list
    


    


