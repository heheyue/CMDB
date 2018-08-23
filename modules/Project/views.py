from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# from modules.models import UserToken
import time
import json
import random
import hashlib
from functools import wraps
from CMDB import settings
from django.shortcuts import render,render_to_response,redirect
from modules.PublicModules.views import GenerateUID
from modules.PublicModules.views import *
from modules.DbModules.DbProjectAll import *

#返回项目管理首页
@CheckLogin
def Index(request):
    system_memu_now=SysTem_MeMu.System_memua(request)
    trlist=[]
    for list in PROJECTALL.SeleatProject(request):
        trlist.append({
            'ProjectId':list.id,
            'ProjectUID':list.ProjectID,
            'ProjectName':list.ProjectName,
            'ProjectFrom':list.ProjectFrom,
            'ProjectUser':list.ProjectUser,
            'ProjectMsg':list.ProjectMsg,
        }
            # [list.ProjectID,list.ProjectName,list.ProjectFrom,list.ProjectUser,list.ProjectMsg]
        )
    # print(trlist)
    msg={
        'error_code':0,
        'data':{
            'navigation':['信息管理','项目管理'],
            'Tablemsg': {
                # 'th':['项目编号', '项目名称', '项目所属部门', '项目负责人','项目描述'],
                'tr':trlist,
            },
            'system_memu': json.dumps(system_memu_now),
            # 'add_user_check':False
            'UserName':request.session.get('UserInfo')['username'],
        },
        'error_msg':None
    }
    return render(request,'project_index.html',msg )

# 处理添加项目
@CheckLogin
def AddProject(request):
    msg={
        'error_code':0,
        'data':{
            'add_project_check':False
        },
        'error_msg':None
    }
    UID=GenerateUID()
    ProjectName=request.POST.get('add_ProjectName')
    ProjectFrom=request.POST.get('add_ProjectFrom')
    ProjectUser=request.POST.get('add_ProjectUser')
    ProjectMsg=request.POST.get('add_ProjectMsg')
    # print( UID ,ProjectName ,ProjectFrom ,ProjectUser ,ProjectMsg)
    if UID and ProjectName and ProjectFrom and ProjectUser and ProjectMsg:
        PROJECT=PROJECTALL
        remsg=PROJECT.AddProject(UID=UID,Name=ProjectName,From=ProjectFrom,User=ProjectUser,Msg=ProjectMsg)
        # print( remsg )
        if remsg['error_code'] == 0:
            msg['data']['add_project_check'] = True
        else:
            msg['error_code'] = 2
            msg['error_msg']=remsg['error_msg']
    return HttpResponse(json.dumps(msg))

#添加项目之前唯一性检测
@CheckLogin
def ChechProject(request):
    system_memu_now = SysTem_MeMu.System_memua(request)
    msg = {
        'error_code': 0,
        'data': {
            'add_ProjectName_checkbit': False,
        },
        'error_msg': None,
    }

    if request.method == 'POST':
        check_ProjectName = request.POST.get('add_ProjectName')
        if check_ProjectName != '' and check_ProjectName != None:
            user_info_list = ProjectAll.objects.filter(ProjectName=check_ProjectName)
            if len(user_info_list) == 0:
                msg['data']['add_ProjectName_checkbit'] = True
            else:
                pass
        else:
            msg['error_code'] = 3
            msg['error_msg'] = '请检查提交参数'
    else:
        msg['error_code'] = 1
    return HttpResponse(json.dumps(msg))

#处理update请求和update get的信息
@CheckLogin
def UpdateProject(request):
    system_memu_now=SysTem_MeMu.System_memua(request)
    msg = {
        'error_code': 0,
        'data': {
            'UserName':request.session.get('UserInfo')['username'],
            'system_memu': json.dumps(system_memu_now),
            'navigation': ['信息管理', '项目管理','项目信息变更'],
            'ProjectInfo':'',
            'UpCheck':False,
        },
        'error_msg': None,
    }
    # 处理get带ID的请求
    if request.method == 'GET':
        ID=request.GET.get('ID')
        if ID != None:
        # print(ID)
        # print(PROJECTALL.SelectById(ID).id)
            msg['data']['ProjectInfo']=PROJECTALL.SelectById(ID)
        else:
            pass
        return render(request,'project_update.html',msg)
    #处理update请求(更新项目信息)
    elif request.method == 'POST':
        ID=request.POST.get('Update_Project_Id')
        Update_Project_From=request.POST.get('Update_Project_From')
        Update_Project_User=request.POST.get('Update_Project_User')
        Updat_Project_Msg=request.POST.get('Updat_Project_Msg')
        if ID and Update_Project_From and Update_Project_User and Updat_Project_Msg:
            Project=PROJECTALL
            UpCheck=Project.UpDateProgect(id=ID,UID='',From=Update_Project_From,User=Update_Project_User,Msg=Updat_Project_Msg )
            if UpCheck['error_code'] == 0:
                msg['data']['UpCheck'] = True
            else:
                msg['error_code']=2
                msg['error_msg']=UpCheck.error_msg
        else:
            msg['error_code']=3
            msg['error_msg']='必填项缺少'
        return HttpResponse(json.dumps(msg))
    else:
        return render(request, 'project_update.html', msg)
# 删除项目
@CheckLogin
def DeleatProject(request):
    Project=PROJECTALL
    msg = {
        'error_code': 0,
        'data': {
            'DeleatBit':False,
        },
        'error_msg': None,
    }

    if request.method == 'POST':
        if request.POST.get('DeleatId'):
            # print(request.POST.get('DeleatId'))
            CheckBit=Project.DeleatProject(id=request.POST.get('DeleatId'),UID='')
            if CheckBit['error_code'] == 0:
                msg['data']['DeleatBit']=True
            else:
                msg['error_code']=2
                msg['error_msg']=CheckBit['error_msg']
        else:
            msg['error_code']=3
            msg['error_msg']='参数为空'
    else:
        msg['error_code']=1
    return HttpResponse(json.dumps(msg))

# 测试通道
# def Test(request):
#     UID=GenerateUID()
#     print(UID)
#     return HttpResponse(UID)
