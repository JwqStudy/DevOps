#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/7/7 22:52
# @Author : JWQ
# @File   : installMinionid.py
#调用runner安装minion

import json
import subprocess

def checkIP(ip):
    status, output = subprocess.getstatusoutput('ping {0} -c 1 -w 1'.format(ip)) #这里是要判断ip是否存活，然后执行不同操作
    return status

def publicKey(ip):
    resultBean = dict()
    clientstatus = checkIP(ip)
    cmd = "sh /srv/salt/_shell/rosterip/addIP.sh {0} && sh /srv/salt/_shell/mvpub.sh {1}".format(ip, ip)
    if clientstatus == 0:
        status, output = subprocess.getstatusoutput(cmd)
        resultBean['code'] = status
        resultBean['message'] = "The IP:{0} install publicKey success".format(ip)
        resultBean['data'] = 'success'
        return json.dumps(resultBean)
    else:
        resultBean['code'] = -1
        resultBean['message'] = "The IP:{0} is not alive".format(ip)
        resultBean['data'] = 'error'
        return json.dumps(resultBean)



def installMinion(ip):
    resultBean = dict()
    clientstatus = checkIP(ip)
    cmd = "sh /srv/salt/_shell/installminion.sh {0}".format(ip)
    if clientstatus == 0:
        status, output = subprocess.getstatusoutput(cmd)
        resultBean['code'] = status
        resultBean['message'] = "The IP:{0} install minion success".format(ip)
        resultBean['data'] = output
        return json.dumps(resultBean)
    else:
        resultBean['code'] = -1
        resultBean['message'] = "The IP:{0} is not alive".format(ip)
        resultBean['data'] = 'error'
        return json.dumps(resultBean)
