import time
from selenium import webdriver  # 导入webdriver包
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from selenium.common.exceptions import NoSuchElementException
from src.common.base import Base
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
URL_68_FORWORD = "http://211.145.72.68:8080/forecom/login.shtml"


class LoginPage(Base):
    def __init__(self, driver1):
        print("LoginPage init")
        self.driver = driver1

    def login(self, url):
        self.driver.get(url)
        self.setUserName("qweqwe123")
        self.setPasswd("qweqwe123")
        self.loginButton()
        time.sleep(3)
        current_url = self.driver.current_url
        print(current_url)

    def setUserName(self, username):
        try:
            self.driver.find_element_by_id("username").send_keys(username)
        except NoSuchElementException:
            print("没有找到用户名")

    def setPasswd(self, passwd):
        self.driver.find_element_by_id("password").send_keys(passwd)

    def setCheckCode(self, checkcode):
        self.driver.find_element_by_id("login_code").send_keys(checkcode)

    def loginButton(self):
        self.driver.find_element_by_id("login_bt").click()

    def remember(self):
        self.driver.find_element_by_id("ru").click()



if __name__ == "__main__":
    log1 = LoginPage()
