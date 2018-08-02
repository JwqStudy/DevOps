#!/usr/bin/env python
# encoding:utf-8

from django.conf.urls import url

from public import views

urlpatterns = [
    url(r'^$', view=views.index),
]