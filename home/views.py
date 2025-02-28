from django.http.response import HttpResponse


# Create your views here.
def index(request):
    print(request.GET)  # 获取当前请求的查询字符串
    """
    <QueryDict: {'name': ['xiaoming'], 'pwd': ['123']}>
    """
    # 获取单个查询参数
    print(request.GET.get("name"))
    print(request.GET.get("pwd"))

    # 获取多个查询参数，结果是一个列表
    print(request.GET.getlist("name"))  # ['xiaoming']
    print(request.GET.getlist("lve"))  # ['swimming','shopping','game']

    # 当客户端没有传递参数时，可以使用get或者getlist的第二个参数default设置默认值
    print(request.GET.getlist("size", 0))

    return HttpResponse("ok,用户中心")


def index2(request):
    """request.POST"""
    # 获取请求体数据，注意：request.POST只能获取POST的请求体，不能获取PUT/PATCH的请求体
    # print(request.POST)

    # 获取单个属性值
    # print(request.POST.get("name"))
    # print(request.POST.get("age"))

    # 获取多个属性值
    # print(request.POST.getlist("lve")) # ['say','swimming',]

    """request.body 获取请求体数据，"""
    print(request.body)  # b'{\r\n    "name": "xiaohong",\r\n    "age": 17\r\n}'

    # 接受客户端发送的json格式
    import json
    data = json.loads(request.body)
    print(data)
    return HttpResponse("ok,用户中心2")


def index3(request):
    """获取包括系统环境，客户端环境和http请求的请求头等元素信息"""
    # print(request.META) # 获取原生请求头
    # print(request.method) # 获取客户端的请求方法

    """获取http请求中的请求头"""
    print(request.headers)
    """
    {
        'Content-Length': '44', 
        'Content-Type': 'application/json',
        'User-Agent': 'PostmanRuntime/7.43.0', 
        'Accept': '*/*', 
        'Postman-Token': '13e1ddf7-7a5a-4ebb-a05e-c792e39d1caf',
        'Host': '127.0.0.1:8000', 
        'Accept-Encoding': 'gzip, deflate, br', 
        'Connection': 'keep-alive'
      }
    
    """

    """获取自定义的http请求头"""
    print(request.META.get("HTTP_COMPANY"))
    print(request.headers.get("company"))  # 强烈建议使用这个

    return HttpResponse("ok,用户中心")


def index4(request):
    """获取客户端上传的文件,可以接收一个文件,也可以接收多个文件"""
    print(request.FILES)  # request.FILES只能接收POST请求上传的文件，其他请求无法获取
    """
    <MultiValueDict: {'avatar': [<InMemoryUploadedFile: shu.png (image/png)>]}>
    """

    # print(request.FILES.get("avatar"))
    # file = request.FILES.get("avatar")
    # print(file, type(file))  # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>

    # 一次性处理多个上传文件
    import os
    for file in request.FILES.getlist("avatar"):
        with open(f"./{file.name}", "wb") as f:
            f.write(file.read())

    for file in request.FILES.getlist("avatar"):
        with open(f"{os.path.dirname(__file__)}/{file.name}", "wb") as f:
            f.write(file.read())

    return HttpResponse("ok,用户中心")


def index5(request):
    """响应：html数据"""

    return HttpResponse(content="<h1>html代码<h1/>", content_type="text/html", status=200, headers={"token": 123})


import json


def index6(request):
    """响应：json数据"""
    # data = {
    #     "id": 1,
    #     "title": "大江大河"
    # }
    #
    # json_data = json.dumps(data)
    data = [
        {"id": 1, "name": "小米"},
        {"id": 2, "name": "小艾"},
    ]
    json_data = json.dumps(data)

    return HttpResponse(content=json_data, content_type="text/json")


from django.http.response import JsonResponse


def index7(request):
    """直接返回json数据"""
    # 字典格式
    # data = {
    #     "id": 1,
    #     "title": "大江大河"
    # }

    # 列表格式
    data = [
        {"id": 1, "name": "小米"},
        {"id": 2, "name": "小艾"},
    ]

    # JsonResponse 并不能直接支持列表转换成json格式，需要关闭安全监测，把safe参数的值设置为False
    return JsonResponse(data, safe=False)


def index8(request):
    """返回其他数据格式内容"""

    """返回图片"""
    # with open("./shu.png", "rb") as f:
    #     img = f.read()
    # return HttpResponse(content=img, content_type="image/png")

    """返回压缩包"""
    with open("./Redis-x64-5.0.14.1.zip", "rb") as f:
        zip = f.read()
    return HttpResponse(content=zip, content_type="application/x-gzip")


def index9(request):
    """自定义响应头"""

    response = HttpResponse("ok!!!")
    response["company"] = "baidu"
    response["data"] = "2023"

    return response


from django.http.response import HttpResponseRedirect


def index10(request):
    """站外跳转/重定向"""

    # 第一种方式：
    response = HttpResponse(status=302)
    response["Location"] = "https://www.163.com"
    return response

    # 第二种方式：
    # return HttpResponseRedirect("https://www.qq.com")


from django.shortcuts import redirect
from django.urls import reverse


def index11(request):
    """站内跳转"""
    # 除了要跳转正则路由以外，其他的路径直接写上去即可，不需要reverse进行解析
    url = reverse("home:index9")  # reverse("namespace:name"),namespace就是路径的前缀命名空间，name就是路径别名
    return redirect(url)

    # return redirect("/home/index9")
