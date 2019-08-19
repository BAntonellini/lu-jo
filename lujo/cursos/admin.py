from django.contrib import admin
from .models import Curso

# Register your models here.
class CursosAdmin(admin.ModelAdmin):
    readonly_field = ('fecha_creacion')
    prepopulated_fields = {'codigo': ('titulo',)}

admin.site.register(Curso, CursosAdmin)