#coding:utf-8
from selenium import webdriver
from page.qqemailpage import QqEmailPage
import unittest

class TestQqEmail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.qqemailpage=QqEmailPage(cls.driver)
        cls.url="https://mail.qq.com"
        cls.username='723459273@qq.com'
        cls.password='viviy870411'
        cls.title='测试邮件标题'
        cls.recever='viviy411@163.com'
        cls.text='测试邮件正文js处理'

    def setUp(self):
        self.driver.get(self.url)
    def test_writeemail(self):
        self.qqemailpage.login(self.username,self.password)
        self.qqemailpage.writeemail(self.recever,self.title,self.text)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()
