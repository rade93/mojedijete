from django.views import generic
from .models import NovaObjava


class ObjavaView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'sve_objave'

    def get_queryset(self):
        return NovaObjava.objects.all()


class DetaljView(generic.DetailView):
    model = NovaObjava
    template_name = 'blog/detalj.html'
