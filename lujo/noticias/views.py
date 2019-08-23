from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Noticia

# Create your views here.
""" class ListaNoticias(generic.ListView):
    queryset = Noticia.objects.filter(estado=1).order_by('-fecha_publicacion')
    template_name = 'home.html' """

class DetalleNoticia(DetailView):
    model = Noticia
    template_name = 'noticia.html'
    slug_field = 'codigo'
    slug_url_kwarg = 'codigo'
    print(model)