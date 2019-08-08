from django.db import models
from core.models import Categoria

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    copete = models.TextField(verbose_name="Copete", max_length=50)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="noticias")
    cuerpo = models.TextField(verbose_name="Cuerpo de la noticia", max_length=None)
    categorias = models.ManyToManyField(Categoria, verbose_name="Temas y/o categorías", null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de última edición")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo