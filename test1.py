#coding:utf-8
from selenium import  webdriver
import xlrd

driver=webdriver.Firefox()

data=xlrd.open_workbook(r"F:\pythonproject\oa_test\case\username.xlsx")
table=data.sheet_by_index(0)
rows=table.nrows
clos=table.ncols
