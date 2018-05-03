#coding:utf-8
import configparser
import email
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import os

curpath = os.path.dirname(os.path.realpath(__file__))
inipath = os.path.join(curpath, "config.ini")

def sendemail(reportfile):
    # 读取配置文件中的内容
    cf=configparser.ConfigParser()
    cf.read(inipath)
    host=cf.get('EMAIL','mail_host')
    mail_user=cf.get('EMAIL','mail_user')
    mail_pass=cf.get('EMAIL','mail_pass')
    mail_from=cf.get('EMAIL','mail_from')
    mail_to = cf.get('EMAIL','mail_tolist')
    mail_tolist=mail_to.split(',')
    mail_cc=cf.get('EMAIL','mail_cclist')
    mail_cclist=mail_cc.split(',')
    msg = MIMEMultipart()
 #  msg['Subject'] = 'python test!'
    msg['From'] = mail_from
    msg['To']=mail_to
   # msg['To'] = ';'.join(mail_tolist)
    msg['Cc']=';'.join(mail_cclist)
   #构造文字内容
    content = '''你好，小白:
   这是一封自动发送的邮件。'''
    text = email.mime.text.MIMEText(content,'plain','utf-8')
    msg.attach(text)
   #构造图片链接
   #sendimagefile=open(r'F:\pythonproject\test.png','rb').read()
   #image=MIMEImage(sendimagefile)
   #image.add_header('Content-ID','<image1>')
   #image["Content-Disposition"]='attachment;filename="test.png"'
   #msg.attach(image)
   #构造附件
    sendfile=open(reportfile,'rb').read()
    puretext=MIMEText(sendfile,'html','utf-8')
    htmlpart=MIMEApplication(open(reportfile,'rb').read())
    htmlpart.add_header('Content-Disposition','attachment',filename=os.path.basename(os.path.realpath(reportfile)))
    msg.attach(puretext)
    msg.attach(htmlpart)
    sub=os.path.basename(reportfile)+u"自动化测试报告-"+time.strftime("%Y/%m/%d",time.localtime(time.time()))
    msg['Subject']=sub
   # #构造html
   #  html='''
   # <html>u
   # <head></head>
   # <body>
   # <p>Hi!<br>
   #    This is the test result.<br>
   #    details see in the  attachment!<br>
   #    </p>
   #    </body>
   #    </html>
   #    '''
   #  text_html=MIMEText(html,'html','utf-8')
   #  text_html["Content-Disposition"]='attachment;filename="texthtml.html"'
   #  msg.attach(text_html)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(host, '25')
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(mail_from, mail_tolist+mail_cclist, msg.as_string())
        smtp.quit()
        print('邮件发送成功！')
    except:
        print('邮件发送失败！')

def createFolder(test_path):#c创建文件夹
    reportFolder=test_path+"\\report\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))
    log_path=reportFolder+"\\logs"
    screen_path=reportFolder+"\\Screenshoots"
    report_path=reportFolder+"\\report"
    pathlist=[report_path,log_path,screen_path]
    for paths in pathlist:
        if os.path.exists(paths):
            pass
        else:
            os.makedirs(paths)
    logFile=log_path+"\\"+time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))+".log"
    f=open(logFile,'a')
    f.close()
    reportfile=report_path+"\\TestReport-"+time.strftime("%Y-%m-%d_%H%M%S",time.localtime(time.time()))+".html"
    return reportfile


if __name__=="__main__":
    sendemail("F:\\pythonproject\\oa_test\\report\\result.html")