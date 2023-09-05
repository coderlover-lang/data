from selenium import webdriver
# from selenium.common import 
from selenium.webdriver.common.by import By

from utils.get_cookies import KeepLogin
from utils.search import Search

from config.base import BaseConfig
from config.position import PositionConfig
from config.query import QueryConfig
from config.url import UrlConfig
import time 

base_conf = BaseConfig()
element_position_conf = PositionConfig()
query_conf = QueryConfig()
url_conf = UrlConfig()


driver = base_conf.get_driver() 

# driver.get("http://www.foooooot.com/trip/6878703/")


# Login 
# driver.get(url_conf.login_url)

login = KeepLogin(driver)
login.get_url(url_conf.login_url)
login.send_keys(
    element_xpath = [element_position_conf.password_xpath, element_position_conf.username_xpath], 
    element_value = [88888888, 18237106751], 
)
login.ensure_login(btn_xpath=element_position_conf.login_btn)

# Search 
driver.find_element(by = By.CLASS_NAME, value = 'sub-menu-link').click()

sh = Search(driver=driver)
sh.ensure_search(
    query_conf.query_keywords, 
    element_position_conf.search_xpath, 
    element_position_conf.search_btn 
)


eles = driver.find_elements(by= By.XPATH, value = "//html/body//ul[@class='tripsList']/li")

time.sleep(1000)

driver.quit()
# track json url:
# https://www.foooooot.com/v4/api/trip/6878703/





