from ...models.tarea.model import Tarea
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ...forms.tarea.forms import TareaFormCrear, TareaFormEditar


@login_required(login_url='login')
def tareas(request):
    """Solo muestra tareas asignadas al usuario autenticado"""
    persona = request.user.perfil.persona
    tareas_list = Tarea.objects.filter(personas=persona)
    template = loader.get_template('tarea/tareas.html')
    context = {
        'tareas': tareas_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def verTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    context = {'tarea': tarea}
    return render(request, 'tarea/ver_tarea.html', context)

@login_required(login_url='login')
def crearTarea(request):
    """Crear tarea sin marcar como completada"""
    if request.method == 'POST':
        form = TareaFormCrear(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:       
        form = TareaFormCrear()
    return render(request, 'tarea/crear_tarea.html', {'form': form})

@login_required(login_url='login')
def modificarTarea(request, id):
    """Editar tarea con opción de completada"""
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        form = TareaFormEditar(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaFormEditar(instance=tarea)
    context = {'form': form}
    return render(request, 'tarea/modificar_tarea.html', context)

@login_required(login_url='login')
def completarTarea(request, id):
    """Toggle completada sin ir a editar"""
    tarea = Tarea.objects.get(id=id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')

@login_required(login_url='login')
def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    else:
        context = {'tarea': tarea}
        return render(request, 'tarea/eliminar_tarea.html', context)
