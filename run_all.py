import unittest
from email.utils import formataddr
import time
from src.common import HTMLTestRunner
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import ddt


def sendMail1():
    # 第三方 SMTP 服务
    mail_host = "SMTP.qq.com"  # 设置服务器
    mail_user = "1447184083@qq.com"  # 用户名
    mail_pass = "zvcjvxvtoqkngebe"  # 口令

    sender = 'from@runoob.com'
    receivers = ['13241619609@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        msg = MIMEText("这是测试邮箱发送内容！", "plain", "utf-8")
        msg["From"] = formataddr(["FromSMTPQQ", mail_user])  # 括号中对应发件人邮箱昵称、发件人邮箱账号
        msg["To"] = formataddr(["RecSMTP", mail_pass])  # 括号中对应收件人邮箱昵称、收件人邮箱账号
        msg["Subject"] = "这是邮件的主题"  # 邮件的主题或标题

        server = smtplib.SMTP_SSL("SMTP.qq.com", 465)   # 括号中对应的是发件人邮箱中的SMTP服务器，端口
        server.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号和密码
        server.sendmail(mail_user, receivers, msg.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

def sendMail2():
    sender = 'from@runoob.com'
    receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
    message['To'] = Header("测试", 'utf-8')  # 接收者

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == "__main__":
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)

    casePath = "F:\\gitcode\\web_auto\\src\\testCase"
    report_path = "C:\\Users\\P007-13\\Desktop\\" + "report.html"
    rule = "test*.py"
    discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
    print(discover)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=" 测试报告 ", description="登录模块")

    runner.run(discover)

    time.sleep(5)
    sendMail1()