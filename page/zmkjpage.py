#coding:utf-8
from comm.base import Base
import time
class ZmkjPage(Base):
    rlzy_loc=("xpath","//*[@alias='hr']")#人力资源模块
    zmkjsq_loc=("link text","证明开具申请")#证明开具申请
    xzzm_loc=("xpath",".//*[@class='ui-btn ui-btn-fill ui-btn-green-empty'][1]")#新增证明开具申请
    iframe="fnIfame"
    time_loc=("name","enrollmentTime")
    zmtype_loc=("xpath","//*[@id='form']/div[4]/input")
    zmdanw_loc=("name","unit")
    textarea_loc=("xpath","//textarea")
    submit_loc=("xpath","//*[@type='submit']")
    confirm_loc=("xpath","//*[@class='base-btn base-btn-green'][1]/span")
    confirm1_doc=("xpath","//*[@class='base-btn base-btn-green']/span")
    text_loc=("xpath",".//*[@id='list']/tbody/tr[1]/td[5]")


    def addzmkj(self,starttime,typevalue,zmdanwei,textarea):
        self.click(self.rlzy_loc)
        self.click(self.zmkjsq_loc)
        self.toiframe(self.iframe)
        self.click(self.xzzm_loc)
        self.sendKeys(self.time_loc,starttime)
        self.sendKeys(self.zmtype_loc,typevalue)
        self.sendKeys(self.zmdanw_loc,zmdanwei)
        self.sendKeys(self.textarea_loc,textarea)
        self.click(self.submit_loc)
        time.sleep(2)
        self.findElements(self.confirm_loc).click()
        time.sleep(2)
        self.findElement(self.confirm1_doc).click()

    def is_zmkj_success(self):
        try:
            text=self.findElement(self.text_loc).text
            return text
        except:
            print("新增证明开具申请失败")
            return None
