from django.db import models

'''
项目表
'''
class Project(models.Model):
    name = models.CharField("名称",max_length=50,blank=False,default="")
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=True)
    create_time = models.DateTimeField("创建时间",auto_now=True)

    def __str__(self):
        return self.name

'''
模块表
 '''
class Module(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100,blank=False,default="")
    describe = models.TextField("描述",default="")
    create_time = models.DateTimeField("创建时间",auto_now=True)

    def __str__(self):
        return self.name
