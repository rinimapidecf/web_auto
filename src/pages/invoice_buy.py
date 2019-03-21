import time
from selenium import webdriver  # 导入webdriver包
from src.common.base import Base
from src.pages.login_page import LoginPage
import sys
import os
from selenium.webdriver.support.select import Select

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
URL_68_FORWORD = "http://211.145.72.68:8080/forecom/login.shtml"


class InvoiceBuy(Base):
    def __init__(self, driver1):
        print("LoginPage init")
        self.driver = driver1

    def search(self):
        print(1)

    def kaiPiaoFang(self, name):
        self.driver.find_element_by_id("other_cust_name").send_keys(name)

    def kaiPiaoMoney(self, min, max):
        self.driver.find_element_by_id("invoice_fee_s").send_keys(min)
        self.driver.find_element_by_id("invoice_fee_e").send_keys(max)

    # 通过xpath来定位
    def bill_status1(self, option):
        self.driver.find_element_by_xpath(".//*[@id='bill_status']/option[%s]" % option).click()

    # 通过selecter来定位
    def bill_status2(self, text):
        billstatus2 = self.driver.find_element_by_id("bill_status")
        Select(billstatus2).select_by_visible_text(text)
        # time.sleep(3)
        # billstatus2.click()
        # print("click")

    # 通过xpath来定位
    def invoice_status1(self, option):
        self.driver.find_element_by_xpath(".//*[@id='bill_status']/option[%s]" % option).click()

    # 通过selecter来定位
    def invoice_status2(self, text):
        invoicestatus2 = self.driver.find_element_by_id("invoice_status")
        Select(invoicestatus2).select_by_visible_text(text)
        invoicestatus2.click()

    def query_button(self):
        self.driver.find_element_by_id("query").click()

    def reset_button(self):
        self.driver.find_element_by_id("resetButton").click()


if __name__ == "__main__":
    driver = webdriver.Firefox()
    log1 = LoginPage(driver)
    log1.login(URL_68_FORWORD)
    time.sleep(3)
    driver.get("http://211.145.72.68:8080/foretrade/gxs/trade/invoice/invoice_buy.shtml")
    time.sleep(3)
    yemian = InvoiceBuy(driver)
    yemian.bill_status2("已完成")
    time.sleep(3)
    yemian.kaiPiaoFang("四")
    time.sleep(3)
    yemian.kaiPiaoMoney(1, 6)
    time.sleep(3)
    yemian.invoice_status2("运费")
    time.sleep(3)
    yemian.query_button()
    time.sleep(3)
    yemian.reset_button()