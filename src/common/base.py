from selenium import webdriver
import time

class Base:
    def __init__(self,driver):
        self.driver=driver

    def openBrowser(self,url):
        "打开浏览器"
        self.driver.maximize_window()
        self.driver.get(url)

    def closeBrowser(self):
        '关闭浏览器'
        self.driver.close()
        self.driver.quit()

    def find_element(self,locat):
        eles=self.driver.find_element(locat[0],locat[1])
        return eles


if __name__ == "__main__":
    driver=webdriver.Chrome()
    url="http://211.145.72.68:8080/forecom/member/member_mgr.shtml"
    base1=Base(driver)
    base1.openBrowser(url)
    time.sleep(5)
    base1.closeBrowser()
