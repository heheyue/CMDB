from django.db import models
from modules.models import ProjectAll


class PROJECTALL(object):

    def __init__(self):
        pass
    #添加
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
    #删除by   id  ProjectID
    def DeleatProject(id,UID):
        '''
         删除by   id  ProjectID
         id,UID

        '''
        msg = {
            'error_code': 0,
            'data': {
            },
            'error_msg': None
        }
        # print(id)
        try:
            if id:
                Project=ProjectAll.objects.get(id=id).delete()
            elif UID:
                # print ('aaaa')
                Project=ProjectAll.objects.get(ProjectID=UID).delete()
            else:
                # print ('bbb')
                msg['error_code']=3
                msg['error_msg']='缺少唯一字段'
        except Exception as e:
            print (e)
            msg['error_code']=2
            msg['error_msg']=e
        return msg
    #列出所有项目
    def SeleatProject(self):
        project_list = ProjectAll.objects.all()
        return project_list
    #通过ID查询项目
    def SelectById(Id):
        project_list = ProjectAll.objects.filter(id=Id)
        print(project_list)
        return project_list

    #通过id或者ProjectID 更新项目
    def UpDateProgect(id,UID,From,User,Msg):
        msg = {
            'error_code': 0,
            'data': {
            },
            'error_msg': None
        }

        # print (id,UID,From,User,Msg)
        try:
            if id:
                Project=ProjectAll.objects.get(id=id)
                Project.ProjectFrom=From
                Project.ProjectUser=User
                Project.ProjectMsg=Msg
                Project.save()
            elif UID:
                # print ('aaaa')
                Project=ProjectAll.get(ProjectID=UID)
                Project.ProjectFrom=From
                Project.ProjectUser=User
                Project.ProjectMsg=Msg
                Project.save()
            else:
                # print ('bbb')
                msg['error_code']=3
                msg['error_msg']='缺少唯一字段'
        except Exception as e:
            print (e)
            msg['error_code']=2
            msg['error_msg']=e
        return msg
