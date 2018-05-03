#coding:utf-8
import unittest
from comm.HTMLTestRunner import HTMLTestRunner
import time

rescover=unittest.defaultTestLoader.discover(r"F:\pythonproject\oa_test\case", 'test*.py')
nowtime=time.strftime('%Y-%m-%d_%H%M%S')
reportpath="F:\\pythonproject\\oa_test\\report\\"+nowtime+"-report"+".html"

fp=open(reportpath,'wb')

runer=HTMLTestRunner(fp,
                     verbosity=2,
                     title="测试报告",
                     description="详情如下:"
)

runer.run(rescover)
fp.close()
