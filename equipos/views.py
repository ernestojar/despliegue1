from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms  import  *
from django.db.models import Q

# Create your views here.


def Listar_equipo_futbol(request):
    lista =equipos_futbol.objects.all()
    return render(request, 'listar_equipos_futbol.html', {'lista': lista})

def Listar_equipo_baseball(request):
    lista =equipos_baseball.objects.all()
    return render(request, 'listar_equipos.baseball.html', {'lista': lista})

def Listar_equipo_NBA_profecional(request):
    lista =equipos_NBA_profecional.objects.all()
    return render(request, 'listar_equipos_NBA_profecional.html', {'lista': lista})

def Listar_equipo_NBA_colegial(request):
    lista =equipos_NBA_colegial.objects.all()
    return render(request, 'listar_equipos_NBA_colegial.html', {'lista': lista})

def Listar_equipo_NLF_profecional(request):
    lista =equipos_NLF_profecional.objects.all()
    return render(request, 'listar_equipos_NLF_profecional.html', {'lista': lista})

def Listar_equipo_NLF_colegial(request):
    lista =equipos_NLF_colegial.objects.all()
    return render(request, 'listar_equipos_NLF_colegial.html', {'lista': lista})

def Listar_equipo_hockey(request):
    lista =equipos_hockey.objects.all()
    return render(request, 'listar_equipos_hockey.html', {'lista': lista})




