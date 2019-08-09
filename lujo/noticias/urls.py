from . import views
from django.urls import path

urlpatterns = [
    path('<slug:codigo>/', views.DetalleNoticia.as_view(), name='noticia'),
]
