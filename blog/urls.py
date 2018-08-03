#!/usr/bin/env python
# encoding:utf-8

from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', view=views.blogIndex),
]