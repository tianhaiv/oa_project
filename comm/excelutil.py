#coding:utf-8
from selenium import webdriver
import xlrd
class ExcelUtil():
    def __init__(self,excelpath,sheetname):
        self.data=xlrd.open_workbook(excelpath)
        self.table=self.data.sheet_by_name(sheetname)
        self.keys=self.table.row_values(0)#获取第一行作为关键字
        self.nrow=self.table.nrows#获取总行数
        self.ncol=self.table.ncols#获取中列数
    def dict_data(self):
        if self.nrow<=1:
            print("总行数小于1")
        else:
            r=[]
            j=1
            for i in range(self.nrow-1):
                s={}
                values=self.table.row_values(j)
                for k in range(self.ncol):
                    s[self.keys[k]]=values[k]
                r.append(s)
                j+=1
            return r
if __name__=="__main__":
    excelpath="F:\\pythonproject\\oa_test\\case\\username.xlsx"
    sheetname=u"Sheet1"
    data=ExcelUtil(excelpath,sheetname)
    print (data.dict_data())



