#coding:utf-8
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
#去除readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
#清空文本
driver.find_element_by_id("train_date").clear()
#输入值
driver.find_element_by_id("train_date").send_keys("2018-04-24")
time.sleep(3)
driver.quit()