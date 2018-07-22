#coding=utf-8
from email.header import Header
from email.mime.text import MIMEText
import smtplib
from HTMLTestRunner import HTMLTestRunner
import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'pc'
'''
手机自动化测试框架-驱动程序
思路:
1>获取框架中脚本的位置
2>获取需要运行的脚本
3>执行脚本--(从data中读取数据)-(截图)
4>邮件发送报告
'''
#创建测试套件--测试集
def createsuite():
    #1>获取框架中脚本的位置  test_dir
    test_dir="E:\\Lesson\\python\zxd\\appium_frameform_week1\\test_case"
    #2>获取需要运行的脚本--discover
    #参数1:脚本存放位置 test_dir
    #参数2:pattern 存放的格式   以test开头的py文件
    discov=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    #3>将获取的脚本加入至测试集
    #创建一个测试集
    suite=unittest.TestSuite()
    #循环遍历discov中的测试用例,并加入至suite测试集
    for test_case in discov:
        suite.addTest(test_case)
    #返回测试集
    return suite

#4>设计报告
#将HTMLTestRunner.py文件放入C:\Python27\Lib下
now=time.strftime('%Y-%m-%d %H-%M-%S')
#  .表示当前路径
reportname=".\\report\\"+now+"result.html"
#打开测试报告
file1=open(reportname,'wb')  #二进制写入方式
#stream报告文件     title:报告标题      description:报告描述
runner=HTMLTestRunner(stream=file1,title='test_youdaoyun_report',description='test_case')

#5>发送邮件设计
def sendReport(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    msg=MIMEText(mail_body,'html','utf-8')  #邮件格式设置
    msg['Subject']=Header('手机自动化测试报告','utf-8') #主题
    msg['From']='testing51test@163.com'  #发件人
    msg['To']='testing51test@163.com' #收件人,如果收件人为n个,收件人直接用分号隔开
    smtp=smtplib.SMTP('smtp.163.com') #邮件服务器设置
    smtp.login('testing51test@163.com','test51') #登录邮箱需要用户名,密码
    smtp.sendmail(msg['From'],msg['To'].split(';'),msg.as_string())
    smtp.quit()
    print '测试报告邮件发送成功'

#6>运行测试中的脚本
alltestnames=createsuite()
#利用runner运行
runner.run(alltestnames)
file1.close()
sendReport(reportname)