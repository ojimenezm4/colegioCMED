from django.db import models


class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=500)
    fecha_y_hora = models.DateTimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha_y_hora.strftime('%d-%m-%Y %H:%M')}"

    def delete(self, *args, **kwargs):
        # Cambiar el estado a inactivo en lugar de eliminar
        self.activo = False
        self.save()
