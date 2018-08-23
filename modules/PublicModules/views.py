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

#认证装饰器
def CheckLogin(function):
    def CheckSession(request, *args, **kwargs):
        msg = {
            'error_code': 0,
            'error_msg': None,
        }
        if request.session.get('LogInBit',False):
            #print('aaa')
            return function(request,*args,**kwargs)
            #print('bbb')
        else:
            return redirect('/')
            #msg['error_code']=4
            #msg['error_msg']='session过期，请从新登录'
            #return HttpResponse(json.dumps(msg))
    return CheckSession
#生成随机UID
def GenerateUID():
        str=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        strs = ''.join(
            [''.join(random.sample(str, 5)),time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))])
        # strs=''.join([''.join(random.sample(str,5)),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))])
        #print (strs)
        # md5 = hashlib.md5()
        # md5.update(strs.encode('utf-8'))
        # GenerateToken=md5.hexdigest()
        # print(strs)
        return strs

class SysTem_MeMu(object):
    def __init__(self,system_memu,path):
        self.list=[]
        self.system_memu=system_memu
        self.path=path

    def __for(self,system_memu,path):
        print('----------------------------------')
        print(system_memu)
        print(len(system_memu))
        for i in range(len(system_memu)):
            print(i)
            if 'system_memu' in system_memu[i]:
                self.list.append(i)
                self.__for(system_memu=system_memu[i]['system_memu'],path=path)
            else:
                if system_memu[i]['url']==path:
                    print('11')
                    system_memu[i]['active'] = True
                    print(system_memu)
                else:
                    self.list=[]
    def change_memeu(self):
        print(self.system_memu)
        print(self.path)
        self.__for(system_memu=self.system_memu,path=self.path)
        print(self.list)
        # print(len(system_memu))
    def System_memua(self):
        system_memu=[
            {
                'title': '首页',
                'icon': 'am-icon-home',
                'url': '/user/index',
            },
            # {
            #     'title': '信息统计',
            #     'icon': 'am-icon-area-chart',
            #     'system_memu': [
            #         {
            #             'title': '主机信息',
            #             'icon': 'am-icon-desktop',
            #             'url': '/server/index',
            #         },
            #         {
            #             'title': '项目信息',
            #             'icon': 'am-icon-object-group',
            #             'url': '/server/test'
            #         },
            #         {
            #             'title': '公网IP映射信息',
            #             'icon': 'am-icon-gg',
            #             'url': '/user/index'
            #         },
            #         {
            #             'title': '环境分类信息',
            #             'icon': 'am-icon-arrows',
            #             'url': '/user/index'
            #         },
            #     ]
            # },
            {
                'title': '信息管理',
                'icon': 'am-icon-cloud',
                'system_memu': [
                    {
                        'title': '主机管理',
                        'icon': 'am-icon-cube',
                        'url': '/server/index',
                        # 'system_memu':[
                        #     {
                        #         'title':'所有主机',
                        #         'icon':'am-icon-angle-right',
                        #         'url':'/server/index',
                        #     },
                        #     {
                        #         'title':'管理主机',
                        #         'icon':'am-icon-angle-right',
                        #         'url':'/user/index'
                        #     }
                        # ],
                    },
                    {
                        'title':'集群管理',
                        'icon':'am-icon-cubes',
                        'url': '/server/index',
                    },
                    {
                        'title':'分类管理',
                        'icon':'am-icon-bookmark',
                        'url': '/server/index',
                    },
                    {
                        'title': '项目管理',
                        'icon': 'am-icon-diamond',
                        'url': '/project/index',
                        # 'system_memu': [
                        #     {
                        #         'title': '所有项目',
                        #         'icon': 'am-icon-angle-right',
                        #         'url': '/project/index',
                        #     },
                        #     {
                        #         'title': '管理项目',
                        #         'icon': 'am-icon-angle-right',
                        #         'url': '/user/index',
                        #     },
                        # ],
                    },
                    {
                        'title': '端口管理',
                        'icon': 'am-icon-chain',
                        'system_memu': [
                            {
                                'title': '公网IP信息',
                                'icon': 'am-icon-angle-right',
                                'url': '/user/index',
                            },
                            {
                                'title': '公网端口映射信息',
                                'icon': 'am-icon-angle-right',
                                'url': '/user/index',
                            },
                            {
                                'title': '端口信息管理',
                                'icon': 'am-icon-angle-right',
                                'url': '/user/index',
                            },
                        ]
                        # 'url':'/user/index',
                    }
                ]
            },
            # {
            #     'title': '项目信息管理',
            #     'icon': 'am-icon-area-chart',
            #     'url':'/user/index'
            #
            # },
        ]
        return system_memu
