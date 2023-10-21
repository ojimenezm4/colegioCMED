from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Agregar otros campos personalizados según tus necesidades

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        activo = "Activo" if self.is_active else "No Activo"
        return f"{self.email} ({activo})"
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

class Personal(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    imagen_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    is_profesor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    condiciones = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        user_type = "Admin" if self.is_admin else ("Profesor" if self.is_profesor else "Alumno")
        return f"{self.nombres} {self.apellidos} ({user_type})"

    def delete(self, *args, **kwargs):
        self.activo = False
        self.save()


class Alumno(models.Model):
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE, primary_key=True)
    encargado = models.CharField(max_length=100, blank=True, null=True)
    telefono_encargado = models.CharField(max_length=15, blank=True, null=True)
    activo = models.BooleanField(default=True)
    # Agregar otros campos específicos de Alumno según tus necesidades
    def __str__(self):
        return f"{self.personal.nombres} {self.personal.apellidos}"

    def delete(self, *args, **kwargs):
        # Cambiar el estado a inactivo en lugar de eliminar
        self.activo = False
        self.save()


class Profesor(models.Model):
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE, primary_key=True)
    profesion = models.CharField(max_length=100, blank=True, null=True)
    # Agregar otros campos específicos de Maestro según tus necesidades
    activo = models.BooleanField(default=True)

    # Agregar otros campos específicos de Alumno según tus necesidades
    def __str__(self):
        return f"{self.personal.nombres} {self.personal.apellidos}"

    def delete(self, *args, **kwargs):
        # Cambiar el estado a inactivo en lugar de eliminar
        self.activo = False
        self.save()