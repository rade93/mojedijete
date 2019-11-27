from django.views import generic
from .models import NovaObjava
from django.core.paginator import Paginator
from django.shortcuts import render


class ObjavaView(generic.ListView):
    template_name = 'vijesti/index.html'
    context_object_name = 'sve_objave'

    def get_queryset(self):
        return NovaObjava.objects.all()


class DetaljView(generic.DetailView):
    model = NovaObjava
    template_name = 'vijesti/detalj.html'
