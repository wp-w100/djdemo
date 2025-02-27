from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET

# Create your views here.
"""
require_http_methods 用于限制用户访问函数视图的http访问方法
"""


@require_http_methods(["POST", "GET"])  # 常用
# @require_POST # 上面一句代码的简写
def index(request):
    print(request)
    return HttpResponse("ok,index")


@require_http_methods(["GET"])  # 常用
def goods(request):
    print(request)
    return HttpResponse("ok,goods")
