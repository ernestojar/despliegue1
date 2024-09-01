from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    
  path('crear_resultado/<int:partido_id>/', views.crear_resultado_futbol, name='crear_resultado_futbol'),

  
]