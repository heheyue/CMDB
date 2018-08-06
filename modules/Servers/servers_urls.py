from django.conf.urls import url
from django.contrib import admin
from modules.Servers.views import *

urlpatterns = [
    #机器主页
    url(r'^index',Index),
    #添加机器
    url(r'^addhost',AddHost),
    #测试通道
    url(r'^test',Test)
]