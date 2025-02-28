from django.urls import path
from . import views

urlpatterns = [
    # path("index", views.视图类名.as_view()),
    path("user/", views.UserView.as_view()),  # as_view 获取客户端本次HTTP请求 GET,POST,PUT...

]
