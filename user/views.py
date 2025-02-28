from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("ok")


def info(request, id):
    return HttpResponse(f"id={id}的用户资料")


def goods(request, cat_id, attr_id):
    return HttpResponse(f"cat_id={cat_id},arrt_id={attr_id}")


"""路由转换器[了解]"""


def inbuild_reverse(request, num):
    """内置路由转换器"""
    return HttpResponse(f"num={num}")


def inbuild_reverse2(request, content):
    """内置路由转换器"""
    return HttpResponse(f"content={content}")
