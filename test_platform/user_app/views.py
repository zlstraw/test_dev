from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# 首页
def index(request):
    return render(request,"index.html")

#处理登陆请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")


        if username == "" or password == "":
            return render(request, "index.html",{"error":"用户名或者密码null"})
        else:
            # 验证用户是否存在
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                # 记录用户登陆状态
                auth.login(request,user)
                request.session['user1'] = username
                return HttpResponseRedirect('/project_manage/')
            else:
                return render(request,"index.html",{"error":"用户名或密码错误"})

# 判断用户是否登陆
@login_required
def project_manage(request):
    username = request.session.get('user1','')  # 读取浏览器session
    return render(request,"project_manage.html",{"user": username})

# 退出登录
def logout(request):
    auth.logout(request)   # 清除用户的登陆状态
    response = HttpResponseRedirect('/')
    return response
