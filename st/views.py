from django.views import generic
from .models import Tekstovi


class TekstoviView(generic.ListView):
    template_name = 'st/index.html'
    context_object_name = 'sve_objave'

    def get_queryset(self):
        return Tekstovi.objects.all()


class DetaljView(generic.DetailView):
    model = Tekstovi
    template_name = 'st/detalj.html'
