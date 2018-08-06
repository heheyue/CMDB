from django.db import models
from modules.models import ProjectAll


class PROJECTALL(object):

    def __init__(self):
        pass
    def AddProject(UID,Name,From,User,Msg):
        msg = {
            'error_code': 0,
            'data': {
                'AddHost': ''
            },
            'error_msg': None
        }
        try:
            ProjectAll.objects.create(ProjectID=UID,ProjectName=Name,ProjectFrom=From,ProjectUser=User,ProjectMsg=Msg)
            return msg
        except Exception as e:
            msg['error_code']=2
            msg['error_msg']=e
            return msg

    def DeleatProject(self):
        pass
    def SeleatProject(self):
        project_list = ProjectAll.objects.all()
        return project_list
    def SelectById(Id):
        project_list = ProjectAll.objects.filter(id=Id)
        print(project_list)
        return project_list

    def UpDateProgect(UID,Name,From,User,Msg):
        msg = {
            'error_code': 0,
            'data': {

            },
            'error_msg': None
        }
        try:
            pass
        except Exception as e:
            pass
