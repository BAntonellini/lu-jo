from django.contrib import admin
from .models import Noticia

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'estado')
    list_filter = ('estado', 'categorias')
    search_fields = ['titulo', 'cuerpo']
    prepopulated_fields = {'codigo': ('titulo',)}


    





    readonly_fields = ('fecha_publicacion', 'fecha_modificacion')

admin.site.register(Noticia, NewsAdmin)



