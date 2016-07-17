# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 10:16:07 2016

@author: Andy
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
    url(r'^insert/$', views.insertDatabase, name='insertDatabase'),
    url(r'^vocab/$', views.vocab, name='vocab'),
]