from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect
# 判断用户是否登陆
@login_required
def project_manage(request):
    username = request.session.get('user1', '')  # 读取浏览器session
    # 将数据库数据展示出来
    project_all = Project.objects.all()
    return render(request, "project_manage.html", {
        "user": username,
        "projects": project_all,
        "type":"list",

    })

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            Project.objects.create(name=name,describe=describe)
            return HttpResponseRedirect('/manage/project_manage/')

    else:
        form = ProjectForm()

    return render(request,'project_manage.html',{
        'form':form ,
        "type":"add",
    })

def edit_project(request,pid):
    if request.method == 'POST':
        pass
    else:
        form = ProjectForm()

    return render(request,'project_manage.html',{
        'form':form ,
        'type':'edit',
    })

def del_project(request):
    pass
