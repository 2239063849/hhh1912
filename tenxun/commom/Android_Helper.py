# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:fengzhuang
# File_name:Android_Helper.py
# Author: huang chao
# Time:2020年07月25日
import requests
import json
import logging
import logging.config


logging.config.fileConfig('../config/log.conf')
logging = logging.getLogger()
class Login1(object):
    def cha(self,username,password):
        url = 'http://127.0.0.1:8880/register'
        head = {
            'Content-Type':'application/json'
                }
        # datas = "key=%s&chars=%s" %(key,chars)
        datas1 = {"key":f"{username}","chars":f"{password}"}
        datas1=json.dumps(datas1)
        # res = requests.get(url,params=datas,headers=head)
        res = requests.post(url, data=datas1, headers=head)
        return res.text
        # print(res.text)
if __name__ == '__main__':  # 判断现在执行的文件是不是本文件
    hhh = Login1()
    print(hhh.cha('adminhh','123456'))

