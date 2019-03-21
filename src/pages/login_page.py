import time
from selenium import webdriver  # 导入webdriver包
from selenium.webdriver.support.wait import WebDriverWait
import unittest
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
        username = self.driver.find_element_by_id("username").send_keys("qweqwe123")
        password = self.driver.find_element_by_id("password").send_keys("qweqwe123")
        conmmit = self.driver.find_element_by_id("login_bt").click()
        time.sleep(3)
        current_url = self.driver.current_url
        print(current_url)

    def setUserName(self, username):
        self.driver.find_element_by_id("username").send_keys(username)

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
