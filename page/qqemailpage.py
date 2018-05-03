#coding:utf-8
from comm.base import Base

class QqEmailPage(Base):
    login_iframe="login_frame"
    loginpg_loc=( "id","switcher_plogin")
    username_loc=("id","u")
    password_loc=("id","p")
    submit_loc=("id","login_button")
    xyj_loc=("id","composebtn")
    main_frame="mainFrame"
    sjr_loc=("xpath","//*[@id='toAreaCtrl']/div[2]/input")
    suj_loc=("id","subject")
    iframe_loc=("xpath","//iframe")
    text_loc=("css selector","[accesskey='q']")
    send_loc=("name","sendbtn")
    def login(self,usename,password):
        self.toiframe(self.login_iframe)
        self.click(self.loginpg_loc)
        self.sendKeys(self.username_loc,usename)
        self.sendKeys(self.password_loc,password)
        self.click(self.submit_loc)
    def writeemail(self,recever,title,text):
        self.click(self.xyj_loc)
        self.toiframe(self.main_frame)
        self.sendKeys(self.sjr_loc,recever)
        self.sendKeys(self.suj_loc,title)
        #ele=self.findElement(self.iframe_loc)
        #self.toiframe(ele)
        #self.sendKeys(self.text_loc,text)
        #self.driver.switch_to.parent_frame()
        js_content="document.getElementsByClassName('qmEditorIfrmEditArea')[0].contentWindow.document.body.innerHTML='%s'" % text
        self.driver.execute_script(js_content)
        self.click(self.send_loc)