from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ChromeService
from selenium.webdriver.common.by import By 

class BaseConfig():
    def __init__(self) -> None:
        driver_path = '/opt/homebrew/Caskroom/chromedriver/116.0.5845.96/chromedriver-mac-arm64/chromedriver'
        
        
        options = ChromeOptions()
        service = ChromeService(executable_path=driver_path)
        
        
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def get_driver(self):
        return self.driver