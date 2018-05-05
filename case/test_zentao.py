from selenium import webdriver
from time import sleep
import unittest

class TestLogin(unittest.TestCase):
    '''登录'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://zentao.nginx.cqbornsoft.com/zentao/user-login-L3plbnRhby8=.html')
        sleep(1)

    def tearDown(self):
        sleep(1)
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_login_success(self):
        '''用户名密码正确'''
        self.driver.find_element_by_id('account').clear()
        self.driver.find_element_by_id('account').send_keys('chuhe')
        self.driver.find_element_by_name('password').send_keys('111111')
        self.driver.find_element_by_id('submit').click()
        user_text = self.driver.find_element_by_id('userMenu').text
        self.assertEqual('邓宇', user_text)

    def test_login_error(self):
        '''用户名错误，密码正确'''
        self.driver.find_element_by_id('account').clear()
        self.driver.find_element_by_id('account').send_keys('chuhe')
        self.driver.find_element_by_name('password').send_keys('11111')
        self.driver.find_element_by_id('submit').click()
        a = self.driver.switch_to.alert
        print(a.text)
        self.assertEqual('登录失败，请检查您的用户名或密码是否填写正确。22', a.text)
        a.accept()
        sleep(2)


if __name__ == "main":
    unittest.main()