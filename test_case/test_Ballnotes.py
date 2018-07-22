#coding=utf-8
from appium import webdriver
import unittest
import time
import xlrd
from public import quit

class Ballnotes(unittest.TestCase):
    '''全部-最新页面切换'''
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.4.4'
        desired_caps['deviceName']='192.168.83.101:5555'
        desired_caps['appPackage']='com.youdao.note'
        desired_caps['appActivity']='com.youdao.note.activity2.SplashActivity'
        #模拟键盘输入
        desired_caps['unicodeKeyboard']='True'
        desired_caps['resetKeyboard']='True'
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def test_allnotes(self):
        driver=self.driver
        time.sleep(5)
        #截图1
        driver.get_screenshot_as_file("E:\\Lesson\\python\zxd\\appium_frameform_week1\\screen_png\\pic1.png")
         #点击全部
        driver.find_element_by_id('com.youdao.note:id/doc_all').click()
        time.sleep(2)
        driver.get_screenshot_as_file('E:\\Lesson\\python\zxd\\appium_frameform_week1\\screen_png\\pic2.png')
        #点击最新
        driver.find_element_by_id('com.youdao.note:id/doc_news').click()
        time.sleep(2)
        driver.get_screenshot_as_file('E:\\Lesson\\python\zxd\\appium_frameform_week1\\screen_png\\pic3.png')
    def tearDown(self):
        quit.logout(self)
if __name__=='__main__':
    unittest.main()