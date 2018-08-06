from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from modules.views import *
from modules.user.views import *

urlpatterns = [
    #登录首页
    url(r'^$',index),
    #登录处理
    url(r'^login',login),
    #登出处理
    url(r'^logout',logout),
    #注册用户
    url(r'enrolment',enrolment),
    #用户首页
    url(r'index',userindex),
    #添加用户的唯一性检测项
    url(r'useraddcheck',add_user_check),
    #用户添加接口
    url(r'adduser',add_user),
]