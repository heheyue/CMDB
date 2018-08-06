from django.shortcuts import render

# Create your views here.

from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.http import HttpResponse
import json
import hashlib
from django.contrib import auth
from modules.models import *
# from modules.views import *
from modules.PublicModules.views import *


#登录判断函数
def login(request):
    msg = {
        'error_code': 0,
        'data': {
            'login_checkbit':False,
            'login_checkmsg':None
        },
        'error_msg': None,
    }
    if request.method == 'POST':
        login_username=request.POST.get('login_username')
        login_userpwd=request.POST.get('login_userpwd')
        if login_username != '' and login_userpwd!= '':
            #print(login_userpwd)
            try:
                db_username_list=UserInfo.objects.get(username=login_username)
                md5 = hashlib.md5()
                md5.update(db_username_list.password.encode('utf-8'))
                if login_username == db_username_list.username and login_userpwd == md5.hexdigest():
                    msg['data']['login_checkbit'] = True
                    msg['data']['login_checkmsg'] = '登录成功'
                    request.session['LogInBit']=True
                    request.session['UserInfo']={'userid':db_username_list.id, 'username': db_username_list.username}
                    #print(db_username_list.id)
                    # logintoken=Token()
                    # token=logintoken.Set(userid=db_username_list.id)
                    # #print(token)
                    #request.session['UserInfo'] = {'userid': db_username_list.id, 'username': db_username_list.username}
                else:
                    msg['data']['login_checkbit'] = False
                    msg['data']['login_checkmsg'] = '用户名密码不正确'
            except Exception as e:
                msg['data']['login_checkbit'] = False
                msg['data']['login_checkmsg'] = '用户名密码不正确'
                #print (e)
            # exit()
            # print(md5.hexdigest())
        else:
            msg['error_code']=3
    else:
        msg['error_code']=1
    return HttpResponse(json.dumps(msg))
     #设置session和coki
     #RedirectView.as_view('/user/index')
     #取消地址从写。改为js图跳转
    #return HttpResponseRedirect('/user/index')

     #return HttpResponsePermanentRedirect('/user/index')
def logout(request):
    msg = {
        'error_code': 0,
        'data': {
            'logout_bit':False,
        },
        'error_msg': None,
    }
    auth.logout(request)
    msg['data']['logout_bit']=True
    return HttpResponse(json.dumps(msg))

#处理请求注册
def enrolment(request):
     return render(request,'enrolment.html')

#处理请求用户首页
@CheckLogin
def userindex(request):
    # if request.method == 'POST':
    # System_memu(request)
    system_memu_now=SysTem_MeMu.System_memua(request)
    # system_memu_now=[
    #     {
    #         'title': '首页',
    #         'icon': 'am-icon-home',
    #         'url': '/user/index',
    #         'active':True,
    #     },
    #     {
    #         'title': '信息统计',
    #         'icon': 'am-icon-area-chart',
    #         'system_memu': [
    #             {
    #                 'title': '主机信息',
    #                 'icon': 'am-icon-desktop',
    #                 'url': '/server/index',
    #             },
    #             {
    #                 'title': '项目信息',
    #                 'icon': 'am-icon-object-group',
    #                 'url': '/server/test'
    #             },
    #             {
    #                 'title': '公网IP映射信息',
    #                 'icon': 'am-icon-gg',
    #                 'url': '/user/index'
    #             },
    #             {
    #                 'title': '环境分类信息',
    #                 'icon': 'am-icon-arrows',
    #                 'url': '/user/index'
    #             },
    #         ]
    #     },
    #     {
    #         'title': '信息管理',
    #         'icon': 'am-icon-cubes',
    #         'system_memu': [
    #             {
    #                 'title': '主机管理',
    #                 'icon': 'am-icon-cube',
    #                 'url': '/server/index',
    #                 # 'system_memu':[
    #                 #     {
    #                 #         'title':'所有主机',
    #                 #         'icon':'am-icon-angle-right',
    #                 #         'url':'/server/index',
    #                 #     },
    #                 #     {
    #                 #         'title':'管理主机',
    #                 #         'icon':'am-icon-angle-right',
    #                 #         'url':'/user/index'
    #                 #     }
    #                 # ],
    #             },
    #             {
    #                 'title': '项目管理',
    #                 'icon': 'am-icon-diamond',
    #                 'system_memu': [
    #                     {
    #                         'title': '所有项目',
    #                         'icon': 'am-icon-angle-right',
    #                         'url': '/project/index',
    #                     },
    #                     {
    #                         'title': '管理项目',
    #                         'icon': 'am-icon-angle-right',
    #                         'url': '/user/index',
    #                     },
    #                 ],
    #             },
    #             {
    #                 'title': '端口管理',
    #                 'icon': 'am-icon-chain',
    #                 'system_memu': [
    #                     {
    #                         'title': '公网IP信息',
    #                         'icon': 'am-icon-angle-right',
    #                         'url': '/user/index',
    #                     },
    #                     {
    #                         'title': '公网端口映射信息',
    #                         'icon': 'am-icon-angle-right',
    #                         'url': '/user/index',
    #                     },
    #                     {
    #                         'title': '端口信息管理',
    #                         'icon': 'am-icon-angle-right',
    #                         'url': '/user/index',
    #                     },
    #                 ]
    #                 # 'url':'/user/index',
    #             }
    #         ]
    #     },
    #     # {
    #     #     'title': '项目信息管理',
    #     #     'icon': 'am-icon-area-chart',
    #     #     'url':'/user/index'
    #     #
    #     # },
    # ]
    msg={
        'error_code':0,
        'data':
            {
            'system_memu': json.dumps(system_memu_now),
            'UserName': request.session.get('UserInfo')['username'],
        },
        'error_msg':None,
    }
    return render(request,'index.html',msg)

#添加用户的唯一性检测接口
def add_user_check(request):
    msg={
        'error_code':0,
        'data':{
            'add_user_name_checkbit':False,
            'add_user_email_checkbit':False,
            'add_user_phone_checkbit':False,
        },
        'error_msg':None,
    }
    if request.method == 'POST':
        check_user_name = request.POST.get('add_user_name')
        check_user_email = request.POST.get('add_user_email')
        check_user_phone = request.POST.get('add_user_phone')
        # print(check_user_name)
        # print(check_user_email)
        # print(check_user_phone)
        if check_user_name != '' and check_user_name !=None:
            user_info_list=UserInfo.objects.filter(username=check_user_name)
            if len(user_info_list)==0:
                msg['data']['add_user_name_checkbit']=True
            else:
                pass
        elif check_user_email != None and check_user_email != '':
            user_info_list = UserInfo.objects.filter(email=check_user_email)
            if len(user_info_list)==0:
                msg['data']['add_user_email_checkbit'] = True
            else:
                pass
        elif check_user_phone != None and check_user_phone != '':
            user_info_list = UserInfo.objects.filter(phone=check_user_phone)
            if len(user_info_list)==0:
                msg['data']['add_user_phone_checkbit'] = True
            else:
                pass
        else:
            msg['error_code']=3
            msg['error_msg']='请检查提交参数'
    else:
        msg['error_code']=1
    return HttpResponse(json.dumps(msg))

def add_user(request):
    msg={
        'error_code':0,
        'data':{
            'add_user_check':False
        },
        'error_msg':None
    }
    if request.method == 'POST':
        username = request.POST.get('add_user_name')
        password = request.POST.get('add_user_pwd')
        email = request.POST.get('add_user_email')
        phone =  request.POST.get('add_user_phone')
        if username and password and email and phone :
            try:
                UserInfo.objects.create(username=username,password=password,email=email,phone=phone)
                msg['data']['add_user_check'] = True
            except Exception as error:
                msg['error_code']=2
                msg['error_msg']=error
                #打印log，暂时没有添加
                print(error)
        else:
            msg['error_code']=3
            msg['error_msg']='必填项存在空'
    else:
        msg['error_code']=1
    return HttpResponse(json.dumps(msg))