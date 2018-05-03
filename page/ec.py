#coding:utf-8
from  selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class find_element():
    def __init__(self,by,value):
        self.by=by
        self.value=value

    def __call__(self,driver):
        element=WebDriverWait(driver,30,0.5).until(lambda x:x.find_element(self.by,self.value))
        return element

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
ele1=find_element("id","kw")#实例化类，有call方法的类实例化后变成了一个函数
ele1(driver).send_keys("软件测试")

res1=WebDriverWait(driver,30,0.5).until(EC.title_is("软件测试_百度搜索"))#标题等于这个
print(res1)
res2=WebDriverWait(driver,30,0.5).until(EC.title_contains("软件测试"))#标题是否包含这个
#time.sleep(3)
#re=EC.title_is("软件测试_百度搜索")(driver)
print(res2)


#判断元素是否存在
loc1=("id","kw")
res3=WebDriverWait(driver,30,0.5).until(EC.presence_of_element_located(loc1))#如果元素存在就返回元素本身
print(res3)
#loc2=("id","kw33")
#res4=WebDriverWait(driver,30,0.5).until(EC.presence_of_element_located(loc2))#如果元素不存在就报超时
#print(res4)
#判断文字是否存在
loc3=("id","su")
text="百度"
res5=WebDriverWait(driver,30,0.5).until(EC.text_to_be_present_in_element(loc3,text))
print(res5)

driver.quit()




