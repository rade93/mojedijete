from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'st'

urlpatterns = [
    # /st/
    path('', views.TekstoviView.as_view(), name='st'),
    # /st/<st_id>/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetaljView.as_view(), name="detalj"),
]