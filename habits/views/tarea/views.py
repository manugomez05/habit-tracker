from ...models.tarea.model import Tarea
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from ...forms.tarea.forms import TareaFormCrear, TareaFormEditar
from ...permissions import es_administrador, puede_gestionar_tareas


def usuario_tiene_tarea_asignada(user, tarea):
    try:
        persona = user.perfil.persona
    except ObjectDoesNotExist:
        return False
    return tarea.personas.filter(id=persona.id).exists()


@login_required(login_url='login')
def tareas(request):
    """Solo muestra tareas asignadas al usuario autenticado."""
    if puede_gestionar_tareas(request.user):
        tareas_list = Tarea.objects.all()
    else:
        try:
            persona = request.user.perfil.persona
            tareas_list = Tarea.objects.filter(personas=persona)
        except ObjectDoesNotExist:
            tareas_list = Tarea.objects.none()

    template = loader.get_template('tarea/tareas.html')
    context = {
        'tareas': tareas_list,
        'es_admin': es_administrador(request.user),
        'puede_gestionar_tareas': puede_gestionar_tareas(request.user),
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def verTarea(request, id):
    tarea = Tarea.objects.get(id=id)

    if not puede_gestionar_tareas(request.user):
        if not usuario_tiene_tarea_asignada(request.user, tarea):
            return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

    context = {
        'tarea': tarea,
        'es_admin': es_administrador(request.user),
        'puede_gestionar_tareas': puede_gestionar_tareas(request.user),
    }
    return render(request, 'tarea/ver_tarea.html', context)


@login_required(login_url='login')
def crearTarea(request):
    """Crear tarea sin marcar como completada."""
    if not puede_gestionar_tareas(request.user):
        return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

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
    """Editar tarea con opcion de completada."""
    if not puede_gestionar_tareas(request.user):
        return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

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
    """Toggle completada sin ir a editar."""
    tarea = Tarea.objects.get(id=id)
    if not puede_gestionar_tareas(request.user) and not usuario_tiene_tarea_asignada(request.user, tarea):
        return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')


@login_required(login_url='login')
def eliminarTarea(request, id):
    if not es_administrador(request.user):
        return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')

    context = {'tarea': tarea}
    return render(request, 'tarea/eliminar_tarea.html', context)
