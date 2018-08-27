#!/usr/bin/env python
# coding:utf-8
from django.conf.urls import url

from saltstack import views

urlpatterns = [
    url(r'installapp/$', view=views.installApp),
    url(r'applist/$', view=views.applist),
    url(r'init/$', view=views.init),
    url(r'dailycheck/$', view=views.dailyCheck),
    url(r'ip/$', view=views.ip),
]