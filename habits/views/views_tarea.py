from .models.models_tarea import Tarea
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms.forms_tarea import TareaForm



def tareas(request):
    tareas = Tarea.objects.all()
    template = loader.get_template('tareas.html')
    context = {
        'tareas': tareas,
    }
    return HttpResponse(template.render(context, request))

def verTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    context = {'tarea': tarea}
    return render(request, 'ver_tarea.html', context)


def crearTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:       
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})

def modificarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    context = {'form': form}
    return render(request, 'modificar_tarea.html', context)

def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    else:
        context = {'tarea': tarea}
        return render(request, 'eliminar_tarea.html', context)
    