import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions') 
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-popup-blocking')

    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    
    yield driver
    
    driver.quit()
