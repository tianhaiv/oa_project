#coding:utf-8
import time
import unittest

import ddt
from selenium import  webdriver

from page.loginpage import LoginPage
from comm.excelutil import ExcelUtil
import os

#测试数据
path=os.path.dirname(os.path.realpath(__file__))
filepath=os.path.join(path,"file\\userinfo.xlsx")

testdata=ExcelUtil(filepath,u"Sheet1").dict_data()
@ddt.ddt
class Test_login2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.url="http://192.169.2.244:28000"
    def setUp(self):
        self.driver.get(self.url)
        time.sleep(2)
    @ddt.data(*testdata)
    def test_login(self,testdata):
        #1.登录
        self.loginpage.login(testdata['username'],testdata['password'])
        #2.获取登录结果
        result=self.loginpage.is_login_success()
        #3.断言
        self.assertEqual(result,testdata['text'])
    def tearDown(self):
        #self.driver.refresh()
        self.driver.delete_all_cookies()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if  __name__=="__main__":
    unittest.main()