from django.db import models
from core.models import Categoria

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título del Curso")
    tema = models.ManyToManyField(Categoria, verbose_name="Temática", null=True, blank=True)
    resumen = models.TextField(max_length=500, verbose_name="Descripción del Curso")
    fecha_hora = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Fecha y hora")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="cursos")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
    
