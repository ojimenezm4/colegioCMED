# views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import authentication_classes, permission_classes

from .models import Anuncio
from .forms import AnuncioForm

def index(request):
    anuncios = Anuncio.objects.filter(activo=True)

    return render(request, 'core/index.html', {'anuncios': anuncios})

def crear_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)

        if form.is_valid():
            nueva_publicacion = form.save()
            return JsonResponse({'success': True})

        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = AnuncioForm()
    return render(request, 'core/index.html', {'form': form})


def editar_anuncio(request, anuncio_id):
    anuncio = Anuncio.objects.get(id=anuncio_id)
    if request.method == 'POST':
        form = AnuncioForm(request.POST, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AnuncioForm(instance=anuncio)
    return render(request, 'core/anuncios/editar_anuncio.html', {'form': form, 'anuncio': anuncio})



def eliminar_anuncio(request, anuncio_id):
    try:
        anuncio = Anuncio.objects.get(id=anuncio_id)
        anuncio.delete()  # Llama al método delete personalizado
    except Anuncio.DoesNotExist:
        # Puedes manejar aquí la situación en la que la oficina no se encuentra
        pass

    return redirect('index')  # Redirige a la lista de oficinas o a donde desees