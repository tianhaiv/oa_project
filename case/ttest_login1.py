#coding:utf-8
import time
import unittest
from selenium import webdriver
from page.loginpage import LoginPage
class TestLogin(unittest.TestCase):
    '''测试登录
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
        cls.username="yxiaowei@cqbornsoft.com"
        cls.password="1234567y"
        cls.text="杨小薇"
        cls.url="http://192.169.2.247:28000"

    def setUp(self):
        self.driver.get(self.url)
        time.sleep(2)
    def test_loginsuccess(self):
        #1.登录
        self.loginpage.login(self.username,self.password)
        #2.获取登录结果
        result=self.loginpage.is_login_success()
        #3.断言结果
        self.assertTrue(result,self.text)

    def tearDown(self):
        #self.driver.refresh()
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()



