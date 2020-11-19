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
from django.shortcuts import render,redirect

def index(request):
    #return HttpResponse('dasjkda')
    return render(request,'login.html')
# #认证装饰器
# def CheckLogin(function):
#     def CheckSession(request, *args, **kwargs):
#         msg = {
#             'error_code': 0,
#             'error_msg': None,
#         }
#         if request.session.get('LogInBit',False):
#             #print('aaa')
#             return function(request,*args,**kwargs)
#             #print('bbb')
#         else:
#             return redirect('/')
#             #msg['error_code']=4
#             #msg['error_msg']='session过期，请从新登录'
#             #return HttpResponse(json.dumps(msg))
#     return CheckSession
# @CheckLogin
# def test(request):
#     print('aaaok')

    #aa=Token()
    #aa.test()
# class Token(object):
#     now_time=time.time()
#     #print(now_time)
#     def __generate_token(self):
#         str=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#         strs=''.join([''.join(random.sample(str,5)),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(self.now_time))])
#         #print (strs)
#         md5 = hashlib.md5()
#         md5.update(strs.encode('utf-8'))
#         GenerateToken=md5.hexdigest()
#         print(GenerateToken)
#         return GenerateToken
#
#     def Set(self,userid):
#         self.db_token_info=UserToken.objects.filter(userid=userid)
#         if len(self.db_token_info) >= 0:
#             for i in self.db_token_info:
#                 try:
#                     i.delete()
#                 except Exception as e:
#                     print(e)
#         else:
#             pass
#         # print(self.__generate_token())
#         # print(userid)
#         token=self.__generate_token()
#         try:
#             UserToken.objects.create(userid=userid,usertoken=token,usertimeout=self.now_time+settings.TOKEN_TIMEOUT)
#         except Exception as e:
#             print(e)
#         return token
#     def Update(self,userid,usertoken):
#         try:
#             self.db_token_info=UserToken.objects.get(userid=userid,usertoken=usertoken)
#             self.db_token_info.usertoken=usertoken
#             self.db_token_info.usertimeout=self.now_time+settings.TOKEN_TIMEOUT
#             self.db_token_info.save()
#         except Exception as e:
#             pass
#     def Deleat(self,userid):
#         self.db_token_info=UserToken.objects.filter(userid=userid)
#         if len(self.db_token_info) >= 0:
#             for i in self.db_token_info:
#                 try:
#                     i.delete()
#                 except Exception as e:
#                     print(e)
#         else:
#             pass
#
#     def Check(self,userid,usertoken):
#         self.db_token_info=UserToken.objects.get(userid=userid)
#         if self.db_token_info.usertoken == usertoken:
#             return True
#         else:
#             return False
    # def test(self):
    #     # print(settings.TOKEN_TIMEOUT)
    #     # print(self.now_time)
    #     # print(self.now_time+settings.TOKEN_TIMEOUT)
    #     #self.Set(15)
    #     #self.Update(15,'ucibk')
    #     self.Deleat(15)