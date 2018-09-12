#!/usr/bin/env python
# encoding:utf-8

from django.conf.urls import url

from public import views

urlpatterns = [
    # url(r'^$', view=views.publicIndex),
    url(r'settingEmail/$', view=views.settingEmail, name="settingEmail"),
    url(r'settingPasswd/$', view=views.settingPasswd, name="settingPasswd"),
    url(r'check/email/(?P<email>\S+)/$', view=views.checkEmail, name="checkEmail"),
]