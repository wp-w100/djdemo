from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def set_session(request):
    """保存session"""
    request.session["name"] = "xiaombai"
    request.session["id"] = 10
    return HttpResponse("set_session")


def get_session(request):
    """读取session"""
    # 提取单个session
    print(request.session.get("name"))
    print(request.session.get("id"))

    # 提取所有session
    print(dict(request.session.items()))

    # 提取当前session的默认有效期
    print(request.session.get_session_cookie_age())  # 1209600,默认14天
    return HttpResponse("get_session")


def del_session(request):
    """删除session"""
    # 删除单个session,使用pop删除不存在的session，会报错，所以加判断避免报错
    # if request.session.get("name"):
    #     print(request.session.pop("name"))

    # 清空session,慎用
    request.session.clear()

    return HttpResponse("del_session")
