from django.db import models

PUBLICAR = (
    (0, "No"),
    (1, "Si"),
)

# Create your models here.
class Video(models.Model):
    video_titulo = models.CharField(verbose_name="Título", max_length=100, unique=True)
    video_url = models.URLField(verbose_name="Enlace de YouTube", max_length=200)
    fecha_agregado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha agregado")
    publicar = models.IntegerField(choices=PUBLICAR, default=0)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        ordering = ['-fecha_agregado']


    def __url__(self):
        return self.video_url
    def __str__(self):
        return self.video_titulo
    

