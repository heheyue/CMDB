from django.conf.urls import url
from django.contrib import admin
from modules.Project.views import *

urlpatterns = [
    #机器主页
    url(r'^index',Index),
    #添加项目
    url(r'^addproject',AddProject),
    #测试项目名称唯一性
    url(r'^chechprojectname',ChechProject),
    #更新项目信息
    url(r'^update',UpdateProject),
    #测试通道
    url(r'^test',Test)
]