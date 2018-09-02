#!/usr/bin/env python
# encoding:utf-8

from django.conf.urls import url

from cmdb import views

urlpatterns = [
    url(r'^$', view=views.cmdbIndex),
    url(r'^collect/$', view=views.collect),
    url(r'^getjson/$', view=views.getjson),
    url(r'^gettxt/$', view=views.gettxt),
]