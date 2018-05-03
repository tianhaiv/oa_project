#coding:utf-8
import time

def login(driver,username,password):
   driver.find_element_by_id("username").clear()
   driver.find_element_by_id("username").send_keys(username)
   driver.find_element_by_id("passwords").clear()
   driver.find_element_by_id("passwords").send_keys(password)
   driver.find_element_by_id("submit-a").click()
   time.sleep(2)