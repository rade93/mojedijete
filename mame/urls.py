from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'mame'

urlpatterns = [
    # /st/
    path('', views.ObjavaView.as_view(), name='mame'),
    # /st/<st_id>/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetaljView.as_view(), name="detalj"),
]
