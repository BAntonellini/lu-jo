from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    url(r'^getcurso$', views.getcurso, name="getcurso"),
]