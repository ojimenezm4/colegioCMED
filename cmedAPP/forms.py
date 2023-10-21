from django import forms

from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['dias_semana', 'hora_inicio', 'hora_fin']

from .models import Ciclo

class CicloForm(forms.ModelForm):
    class Meta:
        model = Ciclo
        fields = ['grado', 'año', 'activo']