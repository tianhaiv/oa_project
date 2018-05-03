#coding:utf-8
from comm.base import Base
import time
class CxkqPage(Base):
    rlzy_loc=("xpath","//*[@alias='hr']")#人力资源模块
    cxkqsq_loc=("link text","诚信考勤")#诚信考勤申请
    xzcx_loc=("xpath",".//*[@class='ui-btn ui-btn-fill ui-btn-green-empty'][1]")#新增诚信考勤申请
    iframe="fnIfame"
    begindate_loc=("xpath","//*[@id='beginDate']")

    sjd_loc=("xpath","//*[@class='fn-pl20'][2]/input")
    typename_loc=("xpath","//*[@value='公出']")
    projectarea_loc=("name","customerProject")
    remark_loc=("name","remark")
    submit_loc=("xpath","//*[@type='submit']")
    confirm_loc=("xpath","//*[@class='base-btn base-btn-green'][1]/span")
    confirm1_doc=("xpath","//*[@class='base-btn base-btn-green']/span")
    text_loc=("xpath",".//*[@id='list']/tbody/tr[1]/td[5]")

    def addcxkq(self,begindate,projectarea,remark):
        self.click(self.rlzy_loc)
        self.click(self.cxkqsq_loc)
        self.toiframe(self.iframe)
        self.click(self.xzcx_loc)
        self.sendKeys(self.begindate_loc,begindate)
        self.click(self.sjd_loc)
        self.click(self.typename_loc)
        self.sendKeys(self.projectarea_loc,projectarea)
        self.sendKeys(self.remark_loc,remark)
        self.click(self.submit_loc)
        time.sleep(2)
        self.findElements(self.confirm_loc).click()
        time.sleep(2)
        self.findElement(self.confirm1_doc).click()
    def is_cxkq_success(self):
        try:
            text=self.findElement(self.text_loc).text
            return text
        except:
            print("新增诚信考勤申请失败")
            return None
