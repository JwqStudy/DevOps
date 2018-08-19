#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/7/7 22:47
# @Author : JWQ
# @File   : installApp.py
#调用脚本安装相关软件

import subprocess

def nginx():
    resultBean = dict()
    __salt__['pkg.install']('nginx') #调用cp模块传送shell脚本到minion端
    cmd = 'service nginx restart'   #执行minion端的shell脚本
    status, output = subprocess.getstatusoutput(cmd)
    if status == 0:
        resultBean['code'] = 0
        resultBean['message'] = 'success'
        resultBean['data'] = output
    else:
        resultBean['code'] = -1
        resultBean['message'] = 'install nginx error'
        resultBean['data'] = output
    return resultBean

def tomcat():
    pass

def keepalived():
    pass

def mysql():
    pass

def jdk():
    pass

def httpd():
    pass

def redis():
    pass
