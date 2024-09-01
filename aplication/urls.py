from django.urls import path
from . import views
from .views import *


urlpatterns = [   
    path('logout/',logout,name='logout'),
    path('',index,name='index'),
    path('Futbol', Futbol_def, name='futbol'),
    path('Baseball', Baseball_def, name='baseball'),
    path('NBA_profecional', NBA_profecional_def, name='NBA_profecional'),
    path('NBA_colegial', NBA_colegial_def, name='NBA_colegial'),
    path('NLF_profecional', NLF_profecional_def, name='NLF_profecional'),
    path('NLF_colegial', NLF_colegial_def, name='NLF_colegial'),
    path('Hockey', Hockey_def, name='hockey'),
      
    #Futbol
    path('Listar_Futbol/', views.Listar_Futbol, name='listar_futbol'),
    path('Crear_Futbol/', views.Crear_Futbol, name='crear_futbol'),
    path('Modificar_Futbol/<id>/', views.Modificar_Futbol, name='modificar_futbol'),
    path('Eliminar_Futbol/<id>/', views.Eliminar_Futbol, name='eliminar_futbol'),
    path('Buscar_Futbol/', views.Buscar_futbol, name='buscar_futbol'),
    path('Resultado_Futbol/<id>/', views.Resultado_Futbol, name='resultado_futbol'),
    path('Informe_Resultado/<id>/', views.Informe_Resultado, name='informe_resultado'),
    path('Resultado_Sistemas', views.Resultados_Sistemas, name='resultados_sistemas'),
    
    
    path('Listar_Baseball/', views.Listar_Baseball, name='listar_baseball'),
    path('Crear_Baseball/', views.Crear_Baseball, name='crear_baseball'),
    path('Eliminar_Baseball/<id>/', views.Eliminar_Baseball, name='eliminar_baseball'),
    path('Buscar_Baseball/', views.Buscar_Baseball, name='buscar_baseball'),
    path('Resultado_Baseball/<id>/', views.Resultado_Baseball, name='resultado_baseball'),
    path('Informe_Resultado_Baseball/<id>/', views.Informe_Resultado_Baseball, name='informe_resultado_b'),
    path('Resultado_Sistemas_Baseball', views.Resultados_Sistemas_Baseball, name='resultados_sistemas_b'),
    
    path('Listar_Hockey/', views.Listar_Hockey, name='listar_hockey'),
    path('Crear_Hockey/', views.Crear_Hockey, name='crear_hockey'),
    path('Eliminar_Hockey/<id>/', views.Eliminar_Hockey, name='eliminar_hockey'),
    path('Buscar_Hockey/', views.Buscar_Hockey, name='buscar_hockey'),
    path('Resultado_Hockey/<id>/', views.Resultado_Hockey, name='resultado_hockey'),
    path('Informe_Resultado_Hockey/<id>/', views.Informe_Resultado_Hockey, name='informe_resultado_h'),
    path('Resultado_Sistemas_Hockey', views.Resultados_Sistemas_Hockey, name='resultados_sistemas_h'),
    
    
    path('Listar_NBA/', views.Listar_NBA, name='listar_NBA_profecional'),
    path('Crear_NBA/', views.Crear_NBA, name='crear_NBA_profecional'),
    path('Eliminar_NBA/<id>/', views.Eliminar_NBA, name='eliminar_NBA_profecional'),
    path('Buscar_NBA/', views.Buscar_NBA, name='buscar_NBA_profecional'),
    path('Resultado_NBA/<id>/', views.Resultado_NBA, name='resultado_NBA_profecional'),
    path('Informe_Resultado_NBA/<id>/', views.Informe_Resultado_NBA, name='informe_resultado_nba'),
    path('Resultado_Sistemas_NBA', views.Resultados_Sistemas_NBA, name='resultados_sistemas_nba'),
    
    
    path('Listar_NBA_Colegial/', views.Listar_NBAC, name='listar_NBA_colegial'),
    path('Crear_NBA_Colegial/', views.Crear_NBAC, name='crear_NBA_colegial'),
    path('Eliminar_NBA_Colegial/<id>/', views.Eliminar_NBAC, name='eliminar_NBA_colegial'),
    path('Buscar_NBA_Colegial/', views.Buscar_NBAC, name='buscar_NBA_colegial'),
    path('Resultado_NBA_Colegial/<id>/', views.Resultado_NBAC, name='resultado_NBA_colegial'),
    path('Informe_Resultado_NBA_Colegial/<id>/', views.Informe_Resultado_NBAC, name='informe_resultado_nbac'),
    path('Resultado_Sistemas_NBA_Colegial', views.Resultados_Sistemas_NBAC, name='resultados_sistemas_nbac'),
    
    
    path('Listar_NLF/', views.Listar_NLF, name='listar_NLF_profecional'),
    path('Crear_NLF/', views.Crear_NLF, name='crear_NLF_profecional'),
    path('Eliminar_NLF/<id>/', views.Eliminar_NLF, name='eliminar_NLF_profecional'),
    path('Buscar_NLF/', views.Buscar_NLF, name='buscar_NLF_profecional'),
    path('Resultado_NLF/<id>/', views.Resultado_NLF, name='resultado_NLF_profecional'),
    path('Informe_Resultado_NLF/<id>/', views.Informe_Resultado_NLF, name='informe_resultado_nlf'),
    path('Resultado_Sistemas_NLF', views.Resultados_Sistemas_NLF, name='resultados_sistemas_nlf'),    
    
    
    path('Listar_NLF_Colegial/', views.Listar_NLFC, name='listar_NLF_colegial'),
    path('Crear_NLF_Colegial/', views.Crear_NLFC, name='crear_NLF_colegial'),
    path('Eliminar_NLF_Colegial/<id>/', views.Eliminar_NLFC, name='eliminar_NLF_colegial'),
    path('Buscar_NLF_Colegial/', views.Buscar_NLFC, name='buscar_NLF_colegial'),
    path('Resultado_NLF_Colegial/<id>/', views.Resultado_NLFC, name='resultado_NLF_colegial'),
    path('Informe_Resultado_NLF_Colegial/<id>/', views.Informe_Resultado_NLFC, name='informe_resultado_nlfc'),
    path('Resultado_Sistemas_NLF_Colegial', views.Resultados_Sistemas_NLFC, name='resultados_sistemas_nlfc'),
    
]