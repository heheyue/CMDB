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
from modules.DbModules.DbHostAll import *

@CheckLogin
def Index(request):
    # System_memu(request)
    system_memu_now = SysTem_MeMu.System_memua(request)
    for list in HOSTALL.SeleatHost(request):
        print(list.HostName)
    msg={
        'error_code':0,
        'data':{
            'navigation':['信息管理','主机管理'],
            'Tablemsg':{
                'th':['唯一编号','IP地址','HostName','所属项目','所属环境','所在集群'],
                'tr':[
                    ['asdhdjhk','123.123.123.123','localhosy','未分配','未分配','未分配'],
                    ['asdhdjhk','123.123.123.123','localhosy','未分配','未分配','未分配'],
                    ['asdhdjhk','123.123.123.123','localhosy','未分配','未分配','未分配'],
                ],
            },
            'system_memu': json.dumps(system_memu_now),
            'UserName': request.session.get('UserInfo')['username']
        },
        'error_msg':None
    }
    return render(request,'server_index.html',msg )

def AddHost(request):
    msg={
        'error_code':0,
        'data':{
            'add_user_check':False
        },
        'error_msg':None
    }
    UID=GenerateUID()
    pass

def SelectAllHost(request):
    msg={
        'error_code':0,
        'data':{
            'HostNum':0,
            'AllHost':{}
        },
        'error_msg':None
    }
    pass




def Test(request):
    UID=GenerateUID()
    print(UID)
    return HttpResponse(UID)