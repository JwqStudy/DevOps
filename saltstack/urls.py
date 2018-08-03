#!/usr/bin/env python
# coding:utf-8
from django.conf.urls import url

from saltstack import views

urlpatterns = [
    url(r'^$', view=views.index),
    url(r'installapp/$', view=views.installApp),
    url(r'applist/$', view=views.applist),
    url(r'init/$', view=views.init),
]