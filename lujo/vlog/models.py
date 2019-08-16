from django.db import models

PUBLICAR = (
    (0, "No"),
    (1, "Si"),
)

# Create your models here.
class Video(models.Model):
    video_url = models.URLField(verbose_name="Enlace de YouTube", max_length=200)
    publicar = models.IntegerField(choices=PUBLICAR, default=0)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __url__(self):
        return self.video_url
    

