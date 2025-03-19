import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DetailPage:
    # 요소
    URL = "https://www.nibbuns.co.kr/shop/shopdetail.html?branduid=69560"
    OPTION_LIST_EL = "basic_option"
    BUY_BUTTON_EL = "btn_buy"
    CART_BUTTON_EL = "cartBtn"
    DETAIL_GOODS_EL = "#productDetail li.first > a"
    DETAIL_REVIEW_EL = "#productDetail li:nth-child(2) > a"
    DETAIL_QNA_EL = "#productDetail li:nth-child(3) > a"
    DETAIL_RELATION_EL = "#productDetail > div.page-body > div:nth-child(3) > ul > li:nth-child(4) > a"
    DETAIL_CHANGE_EL = "#productDetail li:nth-child(5) > a"
    FIXED_BUY_EL = "fixed_buy"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(driver, 10)
    
    # 상품 페이지 열기
    # [니쁜스강력추천]원터치 볼드 볼 이어링
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

    # 상품상세 탭 클릭
    def detail_goods_click(self):
        detail_goods_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_GOODS_EL)))
        detail_goods_tab.click()

    # 상품후기 탭 클릭
    def detail_review_click(self):
        detail_review_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_REVIEW_EL)))
        detail_review_tab.click()
    
    # 상품문의 탭 클릭
    def detail_qna_click(self):
        detail_qna_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_QNA_EL)))
        detail_qna_tab.click()

    # 관련상품 탭 클릭
    def detail_relation_click(self):
        detail_relation_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_RELATION_EL)))
        detail_relation_tab.click()

    # 배송 교환 반품 탭 클릭
    def detail_change_click(self):
        detail_change_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.DETAIL_CHANGE_EL)))
        detail_change_tab.click()

    # 하단 스크롤 후 바로 구매 클릭
    def fixed_buy_click(self):
        fixed_buy_button = self.wait.until(EC.presence_of_element_located((By.ID, self.FIXED_BUY_EL)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", fixed_buy_button)
        fixed_buy_button.click()

    # 알럿 처리 함수
    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert_text
            alert.accept()
            return alert_text
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
    


    


