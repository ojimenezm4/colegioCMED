from django.contrib.auth import logout, login
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import ListView, UpdateView, DeleteView
from rest_framework import generics, authentication, exceptions
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny  # Importa AllowAny

from autenticacion.models import CustomUser, Personal, Alumno, Profesor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import CustomLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Vista para admins
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AdminCreationForm, AlumnoCreationForm, ProfesorCreationForm
from .models import Personal

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Lógica de autenticación personalizada aquí
        email = request.META.get('HTTP_EMAIL')
        if not email:
            return None

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No se ha encontrado un usuario con este email.')

        return (user, None)


@csrf_exempt
@require_POST
def custom_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return JsonResponse({'error': 'Credenciales incorrectas'}, status=400)


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AdminCreationForm
from .models import Personal

def crear_admin(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear un nuevo usuario
            user = CustomUser.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.save()

            # Crear un nuevo administrador (Personal)
            admin = Personal(user=user, nombres=form.cleaned_data['nombres'], apellidos=form.cleaned_data['apellidos'],
                             telefono=form.cleaned_data['telefono'], direccion=form.cleaned_data['direccion'],
                             fecha_nacimiento=form.cleaned_data['fecha_nacimiento'], imagen_perfil=form.cleaned_data['imagen_perfil'],
                             is_admin=True,is_profesor=False, condiciones=form.cleaned_data['condiciones'])
            admin.save()
            token, created = Token.objects.get_or_create(user=user)
            return redirect('index')
    else:
        form = AdminCreationForm()

    return render(request, 'autenticacion/crear_admin.html', {'form': form})



def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear un nuevo usuario
            user = CustomUser.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.save()

            # Crear un nuevo administrador (Personal)
            personal = Personal(user=user, nombres=form.cleaned_data['nombres'], apellidos=form.cleaned_data['apellidos'],
                             telefono=form.cleaned_data['telefono'], direccion=form.cleaned_data['direccion'],
                             fecha_nacimiento=form.cleaned_data['fecha_nacimiento'], imagen_perfil=form.cleaned_data['imagen_perfil'],
                             is_admin=False,is_profesor=False, condiciones=form.cleaned_data['condiciones'])
            personal.save()

            alumno = Alumno(personal=personal,
                            encargado=form.cleaned_data['encargado'],
                            telefono_encargado=form.cleaned_data['apellidos'])
            alumno.save()

            token, created = Token.objects.get_or_create(user=user)
            return redirect('index')
    else:
        form = AlumnoCreationForm()

    return render(request, 'autenticacion/crear_alumno.html', {'form': form})




def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear un nuevo usuario
            user = CustomUser.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.save()

            # Crear un nuevo administrador (Personal)
            personal = Personal(user=user, nombres=form.cleaned_data['nombres'], apellidos=form.cleaned_data['apellidos'],
                             telefono=form.cleaned_data['telefono'], direccion=form.cleaned_data['direccion'],
                             fecha_nacimiento=form.cleaned_data['fecha_nacimiento'], imagen_perfil=form.cleaned_data['imagen_perfil'],
                             is_admin=False,is_profesor=True, condiciones=form.cleaned_data['condiciones'])
            personal.save()

            profesor = Profesor(personal=personal,
                            profesion=form.cleaned_data['profesion'])
            profesor.save()

            token, created = Token.objects.get_or_create(user=user)
            return redirect('index')
    else:
        form = ProfesorCreationForm()

    return render(request, 'autenticacion/crear_profesor.html', {'form': form})

'''
# Vista para crear un maestro
def crear_maestro(request):
    if request.method == 'POST':
        # Procesar el formulario para crear un nuevo maestro
        user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
        user.email = request.POST['email']
        user.save()

        personal = Personal(user=user, nombres=request.POST['nombres'], apellidos=request.POST['apellidos'], telefono=request.POST['telefono'], direccion=request.POST['direccion'], is_maestro=True, condiciones=request.POST['condiciones'])
        personal.save()

        maestro = Maestro(personal=personal, profesion=request.POST['profesion'])
        maestro.save()
        return redirect('listar_maestros')
    return render(request, 'crear_maestro.html')

# Vista para crear un alumno
from django.shortcuts import render, redirect
from .models import CustomUser, Personal, Alumno

def crear_alumno(request):
    if request.method == 'POST':
        # Procesar el formulario para crear un nuevo alumno
        user = CustomUser.objects.create_user(email=request.POST['email'], password=request.POST['password'])
        user.is_active = True  # Asegurarse de que el usuario esté activo
        user.save()

        personal = Personal(
            user=user,
            nombres=request.POST['nombres'],
            apellidos=request.POST['apellidos'],
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion']
        )
        personal.save()

        alumno = Alumno(
            personal=personal,
            encargado=request.POST['encargado'],
            numero_encargado=request.POST['numero_encargado']
        )
        alumno.save()

        return redirect('listar_alumnos')

    return render(request, 'crear_alumno.html')
'''