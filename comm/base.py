#coding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import  time


class Base():
    def __init__(self,driver):
        self.driver=driver
        self.timeout=30
        self.poll=0.5
    def findElement(self,locator):
        '''locator传元祖，例如（“id”，“kw”）
        '''
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_element(*locator))
        return element

    def findElementNew(self,locator):
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(locator))
        return element

    def findElements(self,locator):
        elements=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_element(*locator))
        return elements

    def findElementsNew(self,locator):
        elements=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_all_elements_located(locator))
        return elements

    def sendKeys(self,locator,text):#封装send_keys
        ele=self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):#封装click
        self.findElement(locator).click()
    def clear(self,locator):#封装clear
        self.findElement(locator).clear()

    def textTrue(self,locator,text1):#判断文本是否相等
        ele=self.findElements(locator).text
        if ele==text1:
            return True
        else:
            return  False

    def select(self,locator1,value):#二次封装select
        ss=self.findElement(locator1)
        Select(ss).select_by_value(value)

    def upload(self,locator1,locator2,file,locator3):#二次封装图片上传
        self.click(locator1)
        self.sendKeys(locator2,file)
        self.click(locator3)
        time.sleep(5)

    def toiframe(self,frameid):
        self.driver.switch_to.frame(frameid)

    def element_isapeared(self,loactor):#判断元素是否消失
        element=WebDriverWait(self.driver,self.timeout,self.poll).until_not(lambda x:x.find_element(*loactor)).is_displayed()

    def movetoelement(self,locator):#封装鼠标悬停事件
        '''鼠标悬停事件
        '''
        mos=self.findElement(locator)
        ActionChains(self.driver).move_to_element(mos).perform()

    def is_text_in_element(self,locator,text):#判断元素的文本是否存
        '''判断给定的text是否在指定的元素上'''
        try:
            WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element(locator,text))
            return True
        except:
            return False

    def is_value_in_element(self,locator,text):#判断元素的文本是否存
        '''判断给定的text是否在指定的元素的value属性上'''
        try:
            WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element_value(locator,text))
            return True
        except:
            return False

    def is_element_exists(self,locator):#判断元素是否存在
        '''查找元素是否存在'''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_alert_exist(self):
        '''判断alert是否存在，alert存在就返回alert对象，不存在返回False'''
        alert=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.alert_is_present())
        return alert

    def js_scroll_end(self):#滚到到浏览器底部
        js_heig="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_heig)
        
    def js_scroll_top(self):#回到顶部
        js_heig="window.scrollTo(0,0)"
        self.driver.execute_script(js_heig)

    def js_focous(self,locator):#js聚焦
        target=self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)