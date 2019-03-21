import time
from selenium import webdriver  # 导入webdriver包
from selenium.webdriver.support.wait import WebDriverWait
from src.common.base import Base
from src.pages.login_page import LoginPage

locat1 = ("xpath",
          "//div[@class='row list-area override-row']/div[@class='row all-area override-row']/div[@class='col-md-11 words-area']/a[4]")
locat2 = ("xpath",
           "//div[@class='row list-area override-row']/div[@class='row all-area override-row']/div[@class='col-md-11 words-area']/a[2]")


class SupplierInformation(Base):
    def __init__(self, driver):
        self.driver = driver

    def address(self):
        self.driver.find_element_by_id("wh_addr_id").click()
        time.sleep(3)
        self.find_element(locat2).clic()


if __name__ == "__main__":
    #初始化driver和页面
    driver = webdriver.Firefox()
    log = LoginPage(driver)
    si = SupplierInformation(driver)

    #登录
    driver.maximize_window()
    log.login("http://211.145.72.68:8080/forecom/login.shtml")
    time.sleep(3)

    #进入供应商信息页面
    driver.get(
        "http://211.145.72.68:8080/foretrade/gxs/customer/supplierinformation.shtml?menu_no=510301011&is_nav=0&is_basic=0")
    time.sleep(3)
    si.address()
    time.sleep(3)
    si.find_element(locat1).click()
    print("yidingwei")


