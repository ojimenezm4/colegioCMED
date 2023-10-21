from django.contrib import admin

from core.models import Anuncio


# Register your models here.
@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_y_hora')
    list_filter = ('fecha_y_hora',)
    search_fields = ('titulo', 'fecha_y_hora')

