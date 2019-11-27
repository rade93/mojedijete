from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'naslovna'

urlpatterns = [
    # /index/
    path('', views.NaslovnaView, name='naslovna'),
]
