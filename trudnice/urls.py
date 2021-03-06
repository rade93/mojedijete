from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'trudnice'

urlpatterns = [
    # /st/
    path('', views.ObjavaView.as_view(), name='trudnice'),
    # /st/<st_id>/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetaljView.as_view(), name="detalj"),
]
