#coding=utf-8
from selenium.webdriver.common.by import By

__author__ = 'pc'
import unittest
import time
from public import quit
from appium import webdriver
import xlrd
#unittest中的TestCase进行用例整合
class Anewnotes(unittest.TestCase):
    '''新建云笔记'''
    #HTMLTestRunner 解释
    def setUp(self):
        #开始,准备工作
        #1.手机信息
        desired_caps={
            'platformName':'Android',
            'platformVersion':'4.4.4',
            'deviceName':'192.168.56.101:5555',
            'appPackage':'com.youdao.note',
            'appActivity':'com.youdao.note.activity2.SplashActivity',
            'unicodeKeyboard':'True',
            'resetKeyboard':'True'
        }
        #2.启动Appium
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    #中间的函数为具体自定义的测试函数
    def test_newnotes(self):
        driver=self.driver
        wb=xlrd.open_workbook("E:\\Lesson\\python\\zxd\\appium_frameform_week1\\data\\data.xls")
        sh=wb.sheet_by_name('note')
        r_num=sh.nrows
        print r_num
        #循环遍历数据
        for i in range(1,r_num):
            id=sh.cell_value(i,0)
            title=sh.cell_value(i,1)
            print title
            content=sh.cell_value(i,2)
            result=sh.cell_value(i,3)
            time.sleep(5)
            #点击加号
            driver.find_element_by_id('com.youdao.note:id/add_note_floater_open').click()
            #点击新建笔记
            driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
            #智能等待
            driver.implicitly_wait(5)
            #   输入标题
            driver.find_element(By.ID,'com.youdao.note:id/note_title').send_keys(title)
            #输入正文 利用上次定位下层
            driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]').send_keys(content)
            #点击完成
            driver.find_element_by_name(u'完成').click()
            time.sleep(2)
            #验证:
            if result=='ok':
                #此元素是否存在?
                if driver.find_element_by_name(title) and driver.find_element_by_name(content):
                    print 'success'
                else:
                    print 'fail'
            elif title=='':
                r1=driver.find_element_by_id('com.youdao.note:id/title').text
                r2=driver.find_element_by_id('com.youdao.note:id/summary').text
                if r1==r2:
                    print 'success'
                else:
                    print 'fail'

    #后面可继续添加test函数
    def tearDown(self):
        #结束工作,调用公共函数
        quit.logout(self)

#程序的入口
if __name__=='__main__':
    unittest.main()
