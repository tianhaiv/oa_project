#coding:utf-8
from selenium import webdriver
import  time
driver=webdriver.Firefox()

driver.get("http://www.cnblogs.com/yoyoketang/p/")
time.sleep(2)
js1="document.documentElement.scrollTop=10000"#只在火狐生效
js_chrome="document.body.scrollTop=10000"#在谷歌浏览器生效
js_all="window.scrollTo(0,5000)"#可在任何浏览器生效，0表示X轴，5000表示Y轴
#自动获取高度
js_heig="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js_heig)
#
target=driver.find_element_by_xpath("//h3[text()='最新评论']")
driver.execute_script("arguments[0].scrollIntoView();",target)
time.sleep(2)

driver.quit()