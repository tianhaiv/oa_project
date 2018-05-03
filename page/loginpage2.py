#coding:utf-8
from selenium  import webdriver
driver=webdriver.Firefox()
import unittest
class LoginPage2():
    def __init__(self,driver):
        self.driver=driver

    def input_username(self,username):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        return username
    def input_psw(self,password):
        self.driver.find_element_by_id("passwords").clear()
        self.driver.find_element_by_id("passwords").send_keys(password)
        return password
    def button_click(self):
        self.driver.find_element_by_id("submit-a").click()

    def is_login_success(self,name):
        try:
            ss = self.driver.find_element_by_xpath("//*[@class='fn-left']/span[1]").text
            self.assertTrue(ss==name)
            return  True
        except:
            return False
