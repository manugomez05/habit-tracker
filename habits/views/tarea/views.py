from ...models.tarea.model import Tarea
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ...forms.tarea.forms import TareaForm


def tareas(request):
    tareas_list = Tarea.objects.all()
    template = loader.get_template('tarea/tareas.html')
    context = {
        'tareas': tareas_list,
    }
    return HttpResponse(template.render(context, request))

def verTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    context = {'tarea': tarea}
    return render(request, 'tarea/ver_tarea.html', context)


def crearTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:       
        form = TareaForm()
    return render(request, 'tarea/crear_tarea.html', {'form': form})

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
    return render(request, 'tarea/modificar_tarea.html', context)

def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    else:
        context = {'tarea': tarea}
        return render(request, 'tarea/eliminar_tarea.html', context)
