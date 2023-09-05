from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ChromeService
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

class BaseConfig():
    def __init__(self) -> None:
        driver_path = 'C:\\Users\\83725\\Desktop\\proj\\spider\\chromedriver_win32\\chromedriver.exe'
        
        
        options = ChromeOptions()
        service = ChromeService(executable_path=ChromeDriverManager().install())
        
        
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)
    
    def get_driver(self):
        return self.driver