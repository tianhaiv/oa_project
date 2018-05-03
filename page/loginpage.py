#coding:utf-8
import time
from comm.base import Base

class LoginPage(Base):
    username_loc=("id","username")
    passwd_loc=("id","passwords")
    summit_loc=("id","submit-a")
    text_loc=("xpath","//*[@class='fn-left']/span[1]")
    def login(self,username,password):
        self.clear(self.username_loc)
        self.sendKeys(self.username_loc,username)
        self.clear(self.passwd_loc)
        self.sendKeys(self.passwd_loc,password)
        self.click(self.summit_loc)

    def is_login_success(self):
       try:
            t=self.findElements(self.text_loc).text
            return t
       except:
            print ("登录失败")
            return None


