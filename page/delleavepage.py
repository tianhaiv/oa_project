#coding:utf-8
from comm.base import Base
import time
class DeLeavePage(Base):
    rlzy_loc=("xpath","//*[@alias='hr']")#人力资源模块
    xjsq_loc=("link text","休假申请")#休假申请
    iframe="fnIfame"
    cancel_loc=()
    delete_loc=()


    def deleave(self):
        self.click(self.rlzy_loc)
        self.click(self.xjsq_loc)
        self.toiframe(self.iframe)

    def is_leave_success(self):
        try:
            text=self.findElement(self.text_loc).text
            return text
        except:
            print("新增休假申请失败")
            return None

