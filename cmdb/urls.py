#!/usr/bin/env python
# encoding:utf-8

from django.conf.urls import url

from cmdb import views

urlpatterns = [
    url(r'^summary/$', view=views.cmdbIndex),
    url(r'^autocollect/$', view=views.autocollect),
    url(r'^manualcollect/$', view=views.manualcollect),
    url(r'^getjson/$', view=views.getjson),
    url(r'^gettxt/$', view=views.gettxt),
]