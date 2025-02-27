from django.urls import path
from . import views

app_name = "cookie"
urlpatterns = [
    path("set_session/", views.set_session),
    path("get_session/", views.get_session),
    path("del_session/", views.del_session),
]
