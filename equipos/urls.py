from django.urls import path, include
from . import views

urlpatterns = [
    path('Listar_equipo_futbol/', views.Listar_equipo_futbol, name='listar_equipos_futbol'),
    
]