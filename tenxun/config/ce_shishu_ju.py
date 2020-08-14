# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:tenxun
# File_name:ce_shishu_ju.py
# Author: HLB
# Time:2020年08月13日
import xlrd
def shuju():
    lis = []
    f = xlrd.open_workbook('../config/hlb.xlsx')
    sheet = f.sheets()[0]
    aaa = sheet.nrows
    for i in range(1,aaa):
        lis.append(sheet.row_values(i))
    return lis
if __name__=="__main__":
    print(shuju())



