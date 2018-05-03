#coding:utf-8
from comm.base import Base
import time
class LeavePage(Base):
    rlzy_loc=("xpath","//*[@alias='hr']")#人力资源模块
    xjsq_loc=("link text","休假申请")#休假申请
    xzxj_loc=("xpath",".//*[@class='fn-mb20 fn-mt20']/a[1]")#新增休假申请
    iframe="fnIfame"
    typename_loc=("id","typeName")
    #self.typeVALUE="ill"
    starttime_loc=("id","startTime")
    endtime_loc=("id","endTime")
    days_loc=("id","day")
    area_loc=("name","reason")
    wjsc_loc1=("xpath","//*[@class='fnUpAttach']/a")#文件上传
    wjsc_loc2=("name","UploadFile")#文件上传
    wjsc_loc3=("xpath","//*[@class='base-btn']/span")#文件上传
    submit_loc=("xpath","//*[@type='submit']")
    confirm_loc=("xpath","//*[@class='base-btn base-btn-green'][1]/span")
    confirm1_doc=("xpath","//*[@class='base-btn base-btn-green']")
    text_loc=("xpath","//*[@id='list']/tbody/tr[1]/td[5]")


    def addleave(self,typevalue,starttime,endtime,day,reason,file):
        self.click(self.rlzy_loc)
        self.click(self.xjsq_loc)
        self.toiframe(self.iframe)
        self.click(self.xzxj_loc)
        self.select(self.typename_loc,typevalue)
        self.sendKeys(self.starttime_loc,starttime)
        self.sendKeys(self.endtime_loc,endtime)
        self.sendKeys(self.days_loc,day)
        self.sendKeys(self.area_loc,reason)
        self.upload(self.wjsc_loc1,self.wjsc_loc2,file,self.wjsc_loc3)
        self.click(self.submit_loc)
        time.sleep(2)
        self.findElements(self.confirm_loc).click()
        time.sleep(2)
        self.findElement(self.confirm1_doc).click()

    def is_leave_success(self):
        try:
            text=self.findElement(self.text_loc).text
            return text
        except:
            print("新增休假申请失败")
            return None

