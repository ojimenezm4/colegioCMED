from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('crear_admin/', views.crear_admin, name='crear_admin'),
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('crear_profesor/', views.crear_profesor, name='crear_profesor'),
]
