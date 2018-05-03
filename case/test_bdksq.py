#coding:utf-8
from selenium import webdriver
import unittest
import time
from page.bdkpage import BdkPage
from page.loginpage import LoginPage
from comm.excelutil import ExcelUtil
import time
import ddt
import os

#测试数据
path=os.path.dirname(os.path.realpath(__file__))
filepath=os.path.join(path,"file\\bdkinfo.xlsx")

bdkdata=ExcelUtil(filepath,u"Sheet1").dict_data()
@ddt.ddt
class TestBdk(unittest.TestCase):
    '''测试不打卡申请
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.bdk=BdkPage(cls.driver)
        cls.loginpage=LoginPage(cls.driver)
        cls.username="yxiaowei@cqbornsoft.com"
        cls.password="111111"
        cls.url="https://officetest.nginx.cqbornsoft.com/login/toLogin.htm;SUPSESSIONID=95D01F7F9BE066F77E9979BCDFDF9827"
        cls.driver.get(cls.url)
        cls.loginpage.login(cls.username,cls.password)
    #def setUp(self):
    #     self.driver.get(self.url)
    #     time.sleep(2)
    @ddt.data(*bdkdata)
    def test_addbdk(self,bdkdata):
        #1.新增休假申请
        self.bdk.addbdk(bdkdata['reason'])
        #2.获取新增结果
        result=self.bdk.is_bdk_success()
        #3.断言
        self.assertIn(result,bdkdata['result'])
    def tearDown(self):
        #self.driver.refresh()
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()