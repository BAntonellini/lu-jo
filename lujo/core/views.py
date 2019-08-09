from django.shortcuts import render
from noticias.models import Noticia

# Create your views here.
def home(request):
    lista_noticias = Noticia.objects.filter(estado=1).order_by('-fecha_publicacion')
    ult_3_noticias = lista_noticias[:3]

    return render(request, "home.html", {'ult_3_noticias':ult_3_noticias,

    })


