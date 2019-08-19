from django.contrib import admin
from .models import Video

# Register your models here.
class VlogAdmin(admin.ModelAdmin):
    readonly_field = ('fecha_agregado')

admin.site.register(Video, VlogAdmin)


