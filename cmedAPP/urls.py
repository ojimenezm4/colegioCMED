from django.contrib import admin
from django.urls import path

from cmedAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('colegio/', views.CicloListView.as_view(), name='ciclo-list'),
    path('ciclo/list/', views.CicloListView.as_view(), name='ciclo-list'),
    path('ciclo/create/', views.CicloCreateView.as_view(), name='ciclo-create'),
    path('ciclo/update/<int:pk>/', views.CicloUpdateView.as_view(), name='ciclo-update'),
    path('ciclo/delete/<int:pk>/', views.CicloDeleteView.as_view(), name='ciclo-delete'),
    path('ciclo/<int:pk>/', views.ciclo_detail, name='ciclo-detail'),

]


