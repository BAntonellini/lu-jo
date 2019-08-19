from django.shortcuts import render
from noticias.models import Noticia
from vlog.models import Video


def home(request):
    lista_noticias = Noticia.objects.filter(
        estado=1).order_by('-fecha_publicacion')
    ult_3_noticias = lista_noticias[:3]

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

    print(first_url_embed)

    for videoembed in resto_url_embed:
        print(videoembed)


    return render(request, "home.html", {'ult_3_noticias': ult_3_noticias,
                                         'first_url_embed': first_url_embed,
                                         'resto_url_embed': resto_url_embed
                                        })
