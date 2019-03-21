import unittest
from src.common import HTMLTestRunner
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

casePath = "C:\\Users\\P007-13\\Desktop\\study\\src\\testCase"
report_path = "C:\\Users\\P007-13\\Desktop\\study\\src\\reports\\" + "report.html"
rule = "test_login.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
print(discover)

fp = open(report_path, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=" 测试报告 ", description="登录模块")

runner.run(discover)

if __name__ == "__main__":
    unittest.main()

