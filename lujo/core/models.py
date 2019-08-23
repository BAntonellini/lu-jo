from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(verbose_name="Nombre de categoría", max_length=100);

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
    
    def __str__(self):
        return self.nombre