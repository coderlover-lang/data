from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

class Search:
    def __init__(self, driver : webdriver.Chrome) -> None:
        self.driver = driver
    
    def ensure_search(self, keyword, search_xpath, btn_xpath):
        self.driver.find_element(by = By.XPATH, value=search_xpath).send_keys(keyword)
        time.sleep(2)
        self.driver.find_element(by = By.XPATH, value=btn_xpath).click()