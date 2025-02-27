from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("index/", views.index),
    path("index2/", views.index2),
    path("index3/", views.index3),
    path("index4/", views.index4),
    path("index5/", views.index5),
    path("index6/", views.index6),
    path("index7/", views.index7),
    path("index8/", views.index8),
    path("index9/", views.index9,name="index9"), # name 设置路径别名
    path("index10/", views.index10),
    path("index11/", views.index11),
]
