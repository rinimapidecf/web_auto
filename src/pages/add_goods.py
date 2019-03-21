from src.common.base import Base
from src.pages.login_page import LoginPage
from src.pages.addgoods_select import AddGoodsSelect
from  selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time


class AddGoods(Base):
    def __init__(self, driver1):
        self.driver = driver1

    def mulu_select(self):
        self.driver.find_element_by_xpath("//a[@descrip_value='休闲食品']").click()
        time.sleep(3)
        print("已点击休闲食品")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//a[@descrip_value='二级02']").click()
        print("已点击二级")
        time.sleep(3)
        self.driver.find_element_by_id("next_one").click()
        time.sleep(3)


if __name__ == "__main__":
    driver2 = webdriver.Firefox()
    log = LoginPage(driver2)
    log.login("http://211.145.72.68:8080/forecom/login.shtml")
    time.sleep(3)
    driver2.get("http://211.145.72.68:8080/foretrade/seller/addgoods_select.shtml?menu_no=51010101")
    time.sleep(3)
    gs = AddGoodsSelect(driver2)
    gs.xian_huo()
    time.sleep(3)
    ad = AddGoods(driver2)
    ad.mulu_select()
