import unittest
from src.pages.login_page import LoginPage
from selenium import webdriver
import time
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

URL_68_FORWORD = "http://211.145.72.68:8080/forecom/login.shtml"


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("类初始")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.l = LoginPage(cls.driver)

    def setUp(self):
        print("初始")

    def test_1(self):
        """正常登陆"""
        print("打开浏览器，输入网址")
        self.l.openBrowser(URL_68_FORWORD)
        self.l.setUserName("qweqwe123")
        self.l.setPasswd("qweqwe123")
        self.l.setCheckCode("1")
        self.l.loginButton()
        print("登录")
        time.sleep(3)
        cul = self.driver.current_url
        self.assertIn("ucenter.shtml", cul, "不在用户中心")

    def test_2(self):
        """记住密码登录"""
        print("打开浏览器，输入网址")
        self.l.openBrowser(URL_68_FORWORD)
        self.l.setUserName("qweqwe123")
        self.l.setPasswd("qweqwe123")
        self.l.setCheckCode("1")
        self.l.remember()
        self.l.loginButton()
        print("登录")
        time.sleep(3)
        cul = self.driver.current_url
        self.assertIn("1231242314", cul, "不在用户中心")

    def tearDown(self):
        print("结束")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("类结束")