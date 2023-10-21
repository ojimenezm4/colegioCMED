from django.contrib import admin

from autenticacion.models import Personal, CustomUser, Alumno, Profesor


@admin.register(CustomUser)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    list_filter = ('email',)
    search_fields = ('email', 'is_active')

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'activo')
    list_filter = ('apellidos',)
    search_fields = ('nombres', 'apellidos')


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'activo')

    def nombres(self, obj):
        return obj.personal.nombres

    def apellidos(self, obj):
        return obj.personal.apellidos

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'activo')

    def nombres(self, obj):
        return obj.personal.nombres

    def apellidos(self, obj):
        return obj.personal.apellidos