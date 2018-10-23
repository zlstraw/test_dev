from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project
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
    return render(request, "project_manage.html",{"type":"add"})
