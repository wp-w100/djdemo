from django.shortcuts import render


# Create your views here.
def index(request):
    """在视图中调用模板引擎提供的渲染函数实现前后端不分离"""
    # data = {"name":"哪吒","age":1900}
    # return render(request,template_name="index.html",context=data)
    # return render(request,"index.html",data)

    name = "哪吒"
    age = 29
    return render(request, "index.html", locals())


def index2(request):
    """过滤器"""
    from datetime import datetime
    title = "我的标题"
    content = '我的个人主页：<a href="http://www.baidu.com">点击查看</a>'
    now = datetime.now()
    mobile = "13312345678"
    return render(request, "index.html", locals())
