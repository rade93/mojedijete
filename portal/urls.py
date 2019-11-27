from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'portal'

urlpatterns = [
    # /st/
    path('', views.ObjavaView.as_view(), name='portal'),
]
