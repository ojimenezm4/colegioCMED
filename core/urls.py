from django.urls import path
from . import views

urlpatterns = [
    path('crear_anuncio/', views.crear_anuncio, name='crear_anuncio'),
    path('anuncios/editar/<int:anuncio_id>/', views.editar_anuncio, name='editar_anuncio'),
    path('anuncios/eliminar/<int:anuncio_id>/', views.eliminar_anuncio, name='eliminar_anuncio'),
    path('', views.index, name='index'),
]


