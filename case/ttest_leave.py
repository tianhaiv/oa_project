#coding:utf-8
from selenium import webdriver
import unittest
import time
from page.leavepage import LeavePage
from page.loginpage import LoginPage
from comm.excelutil import ExcelUtil
import time
import ddt
import os

#测试数据
path=os.path.dirname(os.path.realpath(__file__))
filepath=os.path.join(path,"file\\leaveinfo.xlsx")

userdata=ExcelUtil(filepath,u"Sheet1").dict_data()
leavedata=ExcelUtil(filepath,u"Sheet2").dict_data()
@ddt.ddt
class TestLeave(unittest.TestCase):
    '''测试休假申请
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.leavepage=LeavePage(cls.driver)
        cls.loginpage=LoginPage(cls.driver)
        cls.username="yxiaowei@cqbornsoft.com"
        cls.password="111111"
        cls.url="https://officetest.nginx.cqbornsoft.com/login/toLogin.htm;SUPSESSIONID=95D01F7F9BE066F77E9979BCDFDF9827"
        cls.driver.get(cls.url)
        cls.loginpage.login(cls.username,cls.password)
    #def setUp(self):
    #     self.driver.get(self.url)
    #     time.sleep(2)
    @ddt.data(*leavedata)
    def test_addleave(self,leavedata):
        #1.新增休假申请
        self.leavepage.addleave(leavedata['typevalue'],leavedata['starttime'],leavedata['endtime'],leavedata['day'],leavedata['reason'],leavedata['file'])
        #2.获取新增结果
        result=self.leavepage.is_leave_success()
        #3.断言
        self.assertIn(result,leavedata['result'])
    def tearDown(self):
        #self.driver.refresh()
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()