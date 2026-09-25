from django.shortcuts import render, redirect, get_object_or_404
from .models import Rutina
from .forms import RutinaForm

def gestionar_rutinas(request, id=None):
    if id:
        rutina = get_object_or_404(Rutina, id=id)
        accion = 'Editar'
    else:
        rutina = None
        accion = 'Crear'

    if request.method == 'POST':
        form = RutinaForm(request.POST, instance=rutina)
        if form.is_valid():
            form.save()
            return redirect('gestionar_rutinas')
    else:
        form = RutinaForm(instance=rutina)

    rutinas = Rutina.objects.all()
    
    return render(request, 'entrenamientos/rutinas.html', {
        'form': form,
        'rutinas': rutinas,
        'accion': accion
    })

def eliminar_rutina(request, id):
    rutina = get_object_or_404(Rutina, id=id)
    rutina.delete()
    return redirect('gestionar_rutinas')