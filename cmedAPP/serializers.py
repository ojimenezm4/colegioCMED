
from rest_framework import serializers
from .models import Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id', 'dias_semana', 'hora_inicio', 'hora_fin', 'activo']