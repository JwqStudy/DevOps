#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/7/7 14:48
# @Author : JWQ
# @File   : test.py

from util.saltapi import SaltServer

saltServer = SaltServer()
# result1 = saltServer.runModules('*', 'cmd.run', 'w')
# print(result1)

result2 = saltServer.runRunner('dailycheck.checkserver')
print(result2)
# for i in result2.get('data')[0]:
#     print(i)

# result3 = saltServer.runRunner('check.checkserver')
# print(result3)


# masterserver = MasterServer('192.168.137.10')
# print(masterserver.publicKey())



