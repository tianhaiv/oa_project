#coding:utf-8
from comm.base import Base
import time
class BdkPage(Base):
    rlzy_loc=("xpath","//*[@alias='hr']")#人力资源模块
    bdksq_loc=("link text","不打卡考勤申请")#不打卡申请申请
    xzbdk_loc=("xpath",".//*[@class='ui-btn ui-btn-fill ui-btn-green-empty'][1]")#新增不打卡申请
    iframe="fnIfame"
    textarea_loc=("name","reason")
    isread_loc=("id","isRead")
    submit_loc=("xpath","//*[@type='submit']")
    confirm_loc=("xpath","//*[@class='base-btn base-btn-green'][1]/span")
    confirm1_doc=("xpath","//*[@class='base-btn base-btn-green']/span")
    text_loc=("xpath",".//*[@id='list']/tbody/tr/td[1]")


    def addbdk(self,reason):
        self.click(self.rlzy_loc)
        self.click(self.bdksq_loc)
        self.toiframe(self.iframe)
        self.click(self.xzbdk_loc)
        self.sendKeys(self.textarea_loc,reason)
        self.click(self.isread_loc)
        self.click(self.submit_loc)
        time.sleep(2)
        self.findElements(self.confirm_loc).click()
        time.sleep(2)
        self.findElement(self.confirm1_doc).click()

    def is_bdk_success(self):
        try:
            text=self.findElement(self.text_loc).text
            return text
        except:
            print("新增不打卡申请失败")
            return None
