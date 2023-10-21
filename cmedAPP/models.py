from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.db import models
from autenticacion.models import Alumno, Profesor

class Ciclo(models.Model):
    alumno= models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True, related_name='cursos')
    grado = models.CharField(max_length=100)
    año = models.PositiveSmallIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.grado} - {self.año}"

class Horario(models.Model):
    dias_semana = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.dias_semana} - {self.hora_inicio} a {self.hora_fin}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.ForeignKey(Horario, on_delete=models.SET_NULL, null=True)
    ciclo = models.OneToOneField(Ciclo, on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} | {self.ciclo.grado} - {self.ciclo.año}"

class Asistencia(models.Model):
    fecha = models.DateField()
    curso = models.OneToOneField(Curso, on_delete=models.SET_NULL, null=True)
    alumno = models.OneToOneField(Alumno, on_delete=models.SET_NULL, null=True)
    asistio = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)

class Nota(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    alumno = models.OneToOneField(Alumno, on_delete=models.SET_NULL, null=True)
    curso = models.OneToOneField(Curso, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
       return f"Nota de {self.alumno.nombres} {self.alumno.apellidos} en {self.curso.nombre}: {self.valor}"
