import json
from django.shortcuts import render, redirect
from noticias.models import Noticia
from vlog.models import Video
from cursos.models import Curso
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from contacto.forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.urls import reverse


def home(request):
    ult_3_noticias = Noticia.objects.filter(
        estado=1).order_by('-fecha_publicacion')[:3]

    lista_videos = Video.objects.filter(publicar=1).order_by('-fecha_agregado')

    # array_video_ids contiene todos los ID de video de youtube.    
    array_video_ids = []
    for video in lista_videos:
        array_video_ids.append(video.video_url.split(
            "https://www.youtube.com/watch?v=")[1])
    # array_video_embed contiene todos los links de iframe de youtube
        # formato: https://www.youtube.com/embed/ + ID
    youtube_embed_url = "https://www.youtube.com/embed/"
    array_video_embed = []
    for i in array_video_ids:
        array_video_embed.append(youtube_embed_url + i)
    first_url_embed = array_video_embed[0]
    resto_url_embed = array_video_embed[1:]

    ult_3_cursos = Curso.objects.all().order_by('-fecha_creacion')[:3]

    # CONTACTO
    # Instanciar ContactForm en blanco
    contact_form = ContactForm()
    # Si la request es POST
    if request.method == 'POST': 
        # Actualizar formulario con información
        contact_form = ContactForm(data=request.POST) 
        if contact_form.is_valid():
            # Capturar inputs
            nombre = request.POST.get('nombre', '')
            apellido = request.POST.get('apellido', '')
            email = request.POST.get('email', '')
            tipoconsulta = request.POST.get('tipoconsulta', '')
            mensaje = request.POST.get('mensaje', '')

            remitente = settings.EMAIL_HOST_USER
            casilla_destino = "antonellinibruno@gmail.com"

            # Enviar correo y redireccionar a success/fail
            email = EmailMessage(
                "LU-JO - Contacto",
                "De {} {} <{}>\n\nEscribió sobre '{}':\n{}".format(nombre, apellido, email, tipoconsulta, mensaje),
                remitente,
                [settings.EMAIL_DESTINO],
                reply_to=[email]
            )

            try:
                email.send(fail_silently=False)
                # Success, redirect a SUCCESS
                return redirect(reverse('home')+"?success")
            except:
                # Error sending, redirect a FAIL
                return redirect(reverse('home')+"?fail")

    # FIN CONTACTO


    return render(request, "home.html", {'ult_3_noticias': ult_3_noticias,
                                         'first_url_embed': first_url_embed,
                                         'resto_url_embed': resto_url_embed,
                                         'ult_3_cursos': ult_3_cursos,
                                         'form': contact_form,
                                        })

def getcurso(request):
    curso_slug = request.GET.get('q')
    curso = Curso.objects.filter(codigo=curso_slug).values()
    return JsonResponse(curso.first())

    #curso = curso_serializer(curso)
    #return HttpResponse(json.dumps(curso), content_type='application/json')

"""
def curso_serializer(curso):
    print(curso)
    return {'titulo': curso.values('titulo'), 'fecha_hora': curso.values('fecha_hora'), 'imagen': curso.values('imagen'), 'resumen': curso.values('resumen')}
"""