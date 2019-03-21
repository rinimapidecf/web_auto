import time
from selenium import webdriver  # 导入webdriver包
from src.common.base import Base
from src.pages.login_page import LoginPage
import sys
import os
from selenium.webdriver.support.select import Select

from selenium.webdriver.support import expected_conditions

expected_conditions.title_is

class AddGoodsSelect(Base):
    def __init__(self, driver1):
        self.driver = driver1

    def xian_huo(self):
        self.driver.find_element_by_xpath(
            "//img[contains(@src,'/foretrade/skin/default/for-etrade/images/xian_add.png')]").click()

    def yu_shou(self):
        self.driver.find_element_by_xpath(
                    "//img[contains(@src,'/foretrade/skin/default/for-etrade/images/yu_add.png')]").click()

    def shuai_huo(self):
        self.driver.find_element_by_xpath(
                    "//img[contains(@src,'/foretrade/skin/default/for-etrade/images/shuai_add.png')]").click()
