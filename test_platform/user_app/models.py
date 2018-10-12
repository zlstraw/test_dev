from django.db import models
# Create your models here.
# ORM 创建数据库表
# 查询一个表  Table_name.objects.all()

# class = table user_app_project
class Project(models.Model):
    name = models.CharField("名称",max_length=50,blank=False,default="")
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=True)
    create_time = models.DateTimeField("创建时间",auto_now=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100,blank=False,default="")
    describe = models.TextField("描述",default="")
    create_time = models.DateTimeField("创建时间",auto_now=True)

    def __str__(self):
        return self.name