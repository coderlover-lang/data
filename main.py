from selenium import webdriver
# from selenium.common import 
from selenium.webdriver.common.by import By

from utils.get_cookies import KeepLogin

from config.base import BaseConfig
from config.position import PositionConfig


base_conf = BaseConfig()
element_position_conf = PositionConfig()


driver = base_conf.get_driver() 

driver.get("http://www.foooooot.com/trip/6878703/")

# track json url:
# https://www.foooooot.com/v4/api/trip/6878703/





