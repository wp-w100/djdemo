from django.views import View
from django.http.response import HttpResponse, JsonResponse


# Create your views here.


class UserView(View):
    # 类视图中的公共方法/公共属性
    def ret(self, data):
        print(self.request.method)  # 在类视图中，不仅可以通过视图方法中的参数，接收路由传递过来的请求对象，还可以通过self.request来或路由转发过来的请求对象
        return HttpResponse(data)

    def get(self, request):
        """只允许通过get请求访问,建议编写读取数据的页面,一般例如:首页,列表页,详情页"""
        # 视图中的视图方法里面的代码，与原来的函数视图中的代码，是一模一样的。原来怎么写，现在还是怎么写。
        return self.ret("hello, get")

    def post(self, request):
        """只允许通过post请求访问,一般用于上传,添加数据的页面"""
        return self.ret("hello, post")

    def put(self, request):
        """只允许通过put请求访问,一般用于修改,更新数据的页面"""
        return self.ret("hello, put")

    def patch(self, request):
        """只允许通过patch请求访问,一般用于修改,更新数据的页面"""
        return self.ret("hello, patch")

    def delete(self, request):
        """只允许通过delete请求访问,一般用于处理删除数据的页面"""
        return self.ret("hello, delete")
