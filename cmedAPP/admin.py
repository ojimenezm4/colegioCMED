from django.contrib import admin
from .models import Ciclo, Curso, Asistencia, Nota, Horario


# Registro del modelo Ciclo
@admin.register(Ciclo)
class CicloAdmin(admin.ModelAdmin):
    list_display = ('año', 'activo')
    list_filter = ('activo',)
    search_fields = ('año',)

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('dias_semana', 'hora_inicio', 'hora_fin', 'activo')
    list_filter = ('activo',)
    search_fields = ('hora_inicio', 'hora_fin')

    def get_dias_semana(self, obj):
        return ', '.join([dia.dia for dia in obj.dias_semana.all()])

    get_dias_semana.short_description = 'Días de la semana'

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor', 'horario', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'horario')

# Registro del modelo Asistencia
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'alumno', 'curso', 'asistio', 'activo')
    list_filter = ('activo', 'asistio')
    search_fields = ('fecha', 'alumno__nombre', 'curso__nombre')

# Registro del modelo Nota
@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'alumno', 'curso', 'activo')
    list_filter = ('activo',)
    search_fields = ('valor', 'alumno__nombre', 'curso__nombre')
