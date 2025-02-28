from django.urls import path,re_path
from . import views

urlpatterns = [
    # path("url路径",视图函数/视图类,name="路径别名")
    path("index/", views.index),
    # re_path(r"^url路径/(?P<参数变量名>正则模式)/$", 视图函数/视图类),
    re_path(r"^info/(?P<id>\d+)/$", views.info),
    re_path(r"^goods/(?P<cat_id>\d+)/(?P<attr_id>\d+)/$", views.goods),

    path("rev/<int:num>/", views.inbuild_reverse),
    path("rev/<str:content>/", views.inbuild_reverse2),
]
