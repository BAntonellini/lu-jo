from django.contrib import admin
from .models import Noticia

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_publicacion', 'fecha_modificacion')

admin.site.register(Noticia, NewsAdmin)



