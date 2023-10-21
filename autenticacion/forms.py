from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class AdminCreationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password2'}), label="Confirmar contraseña")
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15, required=False)
    direccion = forms.CharField(max_length=200, required=False)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    imagen_perfil = forms.ImageField(required=False)
    condiciones = forms.CharField(max_length=500, required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser .objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está en uso.")
        return email

class AlumnoCreationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password2'}), label="Confirmar contraseña")

    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15, required=False)
    direccion = forms.CharField(max_length=200, required=False)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    imagen_perfil = forms.ImageField(required=False)
    condiciones = forms.CharField(max_length=500, required=False)

    #campos Alumno

    encargado = forms.CharField(max_length=100)
    telefono_encargado = forms.CharField(max_length=100)

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser .objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está en uso.")
        return email



class ProfesorCreationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password2'}), label="Confirmar contraseña")
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15, required=False)
    direccion = forms.CharField(max_length=200, required=False)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    imagen_perfil = forms.ImageField(required=False)
    condiciones = forms.CharField(max_length=500, required=False)

    #campos Maestro

    profesion = forms.CharField(max_length=100)

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser .objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está en uso.")
        return email
