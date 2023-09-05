from selenium import webdriver
from selenium.webdriver.common.by import By 

class KeepLogin():
    def __init__(self, driver : webdriver.Chrome ) -> None:
        self.driver = driver
        
    def get_url(self, url : str):
        self.driver.get(url)
        
    def send_keys(self, element_xpath, element_value):
        for i in range(len(element_value)):
            ele = self.driver.find_element(by=By.XPATH, value=element_xpath[i])
            ele.send_keys(element_value[i])
    