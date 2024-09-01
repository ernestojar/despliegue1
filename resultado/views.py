from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms  import  *
from django.db.models import Q
from .views  import  *

# Create your views here.


def crear_resultado_futbol(request, partido_id):
    partido = get_object_or_404(futbol, pk=partido_id)
    
    # Intenta obtener el resultado_futbol asociado al partido
    try:
        resultado = partido.resultado_futbol
    except resultado_futbol.DoesNotExist:
        # Si no existe, crea uno nuevo
        resultado = None
    
    if request.method == 'POST':
        if resultado is not None:
            # Si hay un resultado_futbol asociado, usa el formulario con el objeto instance
            form = resultado_futbol_form(request.POST, instance=resultado)
        else:
            # Si no hay un resultado_futbol asociado, crea uno nuevo
            form = resultado_futbol_form(request.POST)
        
        if form.is_valid():
            if resultado is not None:
                # Si estamos actualizando un resultado_futbol existente, guarda los cambios
                form.save()
            else:
                # Si estamos creando un nuevo resultado_futbol, guarda el nuevo objeto
                resultado = form.save(commit=False)
                resultado.partido = partido  # Asigna el partido al nuevo resultado_futbol
                resultado.save()
            return redirect('listar_futbol')  # Redirige a la vista Listar_Futbol
    else:
        if resultado is not None:
            form = resultado_futbol_form(instance=resultado)
        else:
            form = resultado_futbol_form()

    return render(request, 'add_resultados_futbol.html', {'form': form})



