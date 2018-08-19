#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/7/7 14:12
# @Author : JWQ
# @File   : saltapi.py
#定义modules和runner接口

import json
import requests


class SaltServer(object):
    def __init__(self):
        self.session = requests.session()
        self.token = self.getToken()
        self.url = "http://192.168.137.130:8000"
        # print(self.token)
        # print(self.session.cookies)

    def getToken(self):
        url = "http://192.168.137.130:8000/login"
        headers = {"Accept": "application/json"}
        data = {
            "username": "saltapi",
            "password": "saltapi",
            "eauth": "pam"
        }
        res = self.session.post(url=url, headers=headers, data=data)
        text = res.text
        result = json.loads(text)
        token = result.get("return")[0].get("token")
        # headerToken = dict()
        # headerToken["X-Auth-Token"] = token
        return token

    def resBean(self, datas):
        resultBean = dict()
        res = self.session.post(url=self.url, data=datas)
        text = res.text
        data = json.loads(text).get("return")
        try:
            resultBean['code'] = 0
            resultBean['message'] = "success"
            resultBean['data'] = data
        except Exception as e:
            resultBean['code'] = -1
            resultBean['message'] = "error"
            resultBean['data'] = e
        finally:
            return resultBean

    def runModules(self, minionid, fun, arg=None):
        data = {
            # "X-Auth-Token": self.getToken(),
            "client": "local",
            "tgt": minionid,
            "fun": fun,
            "arg": arg
        }
        return self.resBean(data)

    def runRunner(self, fun, **kwargs):
        data = {
            # "X-Auth-Token": self.getToken(),
            "client": "runner",
            "fun": fun
        }
        data.update(kwargs)
        return self.resBean(data)





