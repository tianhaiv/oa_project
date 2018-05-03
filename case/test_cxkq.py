#coding:utf-8
from selenium import webdriver
import unittest
import time
from page.cxkqpage import CxkqPage
from page.loginpage import LoginPage
from comm.excelutil import ExcelUtil
import time
import ddt
import os

#测试数据
path=os.path.dirname(os.path.realpath(__file__))
filepath=os.path.join(path,"file\\cxkqinfo.xlsx")

cxkqdata=ExcelUtil(filepath,u"Sheet1").dict_data()
@ddt.ddt
class TestBdk(unittest.TestCase):
    '''测试诚信考勤
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.cxkq=CxkqPage(cls.driver)
        cls.loginpage=LoginPage(cls.driver)
        cls.username="yxiaowei@cqbornsoft.com"
        cls.password="111111"
        cls.url="https://officetest.nginx.cqbornsoft.com/login/toLogin.htm;SUPSESSIONID=95D01F7F9BE066F77E9979BCDFDF9827"
        cls.driver.get(cls.url)
        cls.loginpage.login(cls.username,cls.password)
    #def setUp(self):
    #     self.driver.get(self.url)
    #     time.sleep(2)
    @ddt.data(*cxkqdata)
    def test_addcxkq(self,cxkqdata):
        #1.新增休假申请
        self.cxkq.addcxkq(cxkqdata['begindate'],cxkqdata['projectarea'],cxkqdata['remark'])
        #2.获取新增结果
        result=self.cxkq.is_cxkq_success()
        #3.断言
        self.assertIn(cxkqdata['result'],result)
    def tearDown(self):
        #self.driver.refresh()
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()