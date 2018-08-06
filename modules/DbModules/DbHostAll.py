from modules.models import HostAll
from django.db import models
class HOSTALL(object):
    def __init__(self):
        pass
    def AddHost(self,UID,HostName,Info,AddTime):
        msg = {
            'error_code': 0,
            'data': {
                'AddHost': '添加成功'
            },
            'error_msg': None
        }
        try:
            HostAll.objects.create(UID=UID,HostName=HostName,Info=Info,AddTime=AddTime)
            return msg
        except Exception as e:
            msg['error_code']=2
            msg['error_msg']=e
            return msg
    def DeleatHost(self):
        pass
    def UpdateHost(self):
        pass
    def SeleatHost(self):
        return HostAll.objects.all()