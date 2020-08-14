# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:fengzhuang
# File_name:run.py
# Author: huang chao
# Time:2020年07月27日

import unittest
import time
import os
from config.HTMLTestRunner import HTMLTestRunner
# 测试用例脚本的路径
case_path =r'D:\data\pychon xm\tenxun\Test_Case'
# 测试报告的存放路径
report_path =r'D:\data\pychon xm\tenxun\report'
# 在测试用例脚本文件路径下查找以test开头的测试用例
discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime('%Y%m%d%H%M%S')   # 获取当前时间
    report_name = os.path.join(report_path,'%s.html'%(now))    # 测试报告的存放和重命名
    with open(report_name,'wb') as f:

        runner = HTMLTestRunner(
            stream=f,
            title=u'自动化测试',
            tester=u'贺连彪',
            verbosity=2
        )

        run = HTMLTestRunner()   # 类的实例化
        runner.run(discover)    # 用类的实例化调用测试脚本中的测试用例