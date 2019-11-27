from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'pitanja'

urlpatterns = [
    # /index/
    path('', views.ObjavaView, name='pitanja'),
]
