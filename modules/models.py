from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11,unique=True)
    add_time = models.DateField(auto_now_add=True)
# class UserToken(models.Model):
#     userid=models.IntegerField(unique=True)
#     usertoken=models.CharField(max_length=32,)
#     usertimeout=models.CharField(max_length=20)
#     userlogintime=models.DateTimeField(auto_now_add=True)

class HostAll(models.Model):
    # ID=models.AutoField()
    UID=models.CharField(max_length=10,unique=True)
    # IP=models.GenericIPAddressField(unique=True,protocol='ipv4')
    HostName=models.CharField(max_length=50)
    # RootName=models.CharField(max_length=20)
    # RootPwd=models.CharField(max_length=50)
    Info=models.CharField(max_length=1024)
    AddTime=models.DateField(auto_now_add=True)


class ProjectAll(models.Model):
    ProjectID=models.CharField(max_length=25,unique=True)
    ProjectName=models.CharField(max_length=50,unique=True)
    ProjectFrom=models.CharField(max_length=50)
    ProjectUser=models.CharField(max_length=50)
    ProjectMsg=models.CharField(max_length=100)






#-
# class HostUser(models.Model):
#     UserName=models.CharField(max_length=20)
#     UserPwd=models.CharField(max_length=50)
# class HostOneToOne(models.Model):
#     # HostID=models.ForeignKey(HostAll.id)
#     HostUID=models.OneToOneField(HostAll)
#     IP=models.GenericIPAddressField(unique=True)
#     RootPWD=models.OneToOneField(HostUser)
