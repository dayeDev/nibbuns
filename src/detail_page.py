import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DetailPage:
    # 요소
    URL = "https://www.nibbuns.co.kr/shop/shopdetail.html?branduid=69560&xcode=030&mcode=003&scode=&type=Y&sort=manual&cur_code=030&search=&GfDT=amV7"
    OPTION_LIST_NAME = "optionlist[]"
    BUY_BUTTON_CLASS = "btn_buy fe"
    CART_BUTTON_ID = "cartBtn"
    DETAIL_GOODS_TEXT = "상품상세"
    DETAIL_REVIEW_TEXT = "상품후기"
    DETAIL_QNA_TEXT = "상품문의"
    DETAIL_RELATION_TEXT = "관련상품"
    DETAIL_CHANGE_TEXT = "배송"
    FIXED_BUY_ID = "fixed_buy"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(driver, 10)
    
    # 상품 페이지 열기
    # [니쁜스강력추천]원터치 볼드 볼 이어링
    def open(self):
        self.driver.get(self.URL)

    # 상품 옵션 선택
    def select_option(self, option):
        select = Select(self.wait.until(EC.presence_of_element_located((By.NAME, self.OPTION_LIST_NAME))))    # option 선택용 Select 모듈 사용
        select.select_by_value(option)
    
    # 바로 구매 버튼 클릭
    def buy_click(self):
        buy_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.BUY_BUTTON_CLASS)))
        buy_button.click()

    # 장바구니 버튼 클릭
    def cart_click(self):
        cart_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.CART_BUTTON_ID)))
        cart_button.click()

    # 상품상세 탭 클릭
    def detail_goods_click(self):
        detail_goods_tab = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.DETAIL_GOODS_TEXT)))
        detail_goods_tab.click()

    # 상품후기 탭 클릭
    def detail_review_click(self):
        detail_review_tab = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.DETAIL_REVIEW_TEXT)))
        detail_review_tab.click()
    
    # 상품문의 탭 클릭
    def detail_qna_click(self):
        detail_qna_tab = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.DETAIL_QNA_TEXT)))
        detail_qna_tab.click()

    # 관련상품 클릭
    def detail_relation_click(self):
        detail_relation_tab = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.DETAIL_RELATION_TEXT)))
        detail_relation_tab.click()

    # 배송 교환 반품 클릭
    def detail_change_click(self):
        detail_change_tab = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.DETAIL_CHANGE_TEXT)))
        detail_change_tab.click()

    # 하단 스크롤 후 바로 구매 클릭
    def fixed_buy_click(self):
        fixed_buy_button = self.wait.until(EC.presence_of_element_located((By.ID, self.FIXED_BUY_ID)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", fixed_buy_button)
        fixed_buy_button.click()

    # 임시 로그인 함수
    def login(self):
        self.driver.get("https://www.nibbuns.co.kr/shop/member.html?type=login")
        time.sleep(1)
        self.driver.find_element(By.NAME, "ID").send_keys("kim02jo")
        self.driver.find_element(By.NAME, "passwd").send_keys("1q2w3e4r!@")
        self.driver.find_element(By.CLASS_NAME, "CSSbuttonBlack fe").click()
        time.sleep(1)
    


    


