# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:fengzhuang
# File_name:test_case_login.py
# Author: huang chao
# Time:2020年07月25日
import unittest
from commom.Android_Helper import Login1
from config.ce_shishu_ju import shuju
from parameterized import parameterized,param
import json
import logging.config

class Login2(unittest.TestCase):
    cs = Login1()
    hh = cs.cha
    sj = shuju()
    @parameterized.expand([param(i[0],int(i[1])) for i in sj])
    def test1(self,username,password):
        html = self.hh(username,password)
        print(html)
        try:
            html = json.loads(html)
            self.assertIn('success',html,msg='请求成功')
            logging.info('clicking agreement')
        except:
            self.assertIn('resultcode', html,msg='请求错误')
            logging.info('no agreement')


if __name__ == '__main__':
    unittest.main()

