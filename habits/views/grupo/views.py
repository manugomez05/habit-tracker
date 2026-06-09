from ...models.grupo.model import Grupo
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ...forms.grupo.forms import GrupoForm


def grupo(request):
    grupos = Grupo.objects.all()
    template = loader.get_template('grupo/grupo.html')
    context = {
        'grupos': grupos,
    }
    return HttpResponse(template.render(context, request))

def verGrupo(request, id):
    grupo_obj = Grupo.objects.get(id=id)
    context = {'grupo': grupo_obj}
    return render(request, 'grupo/ver_grupo.html', context)

def crearGrupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoForm()

    return render(request, 'grupo/crear_grupo.html', {'form': form})

def modificarGrupo(request, id):
    grupo_obj = Grupo.objects.get(id=id)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo_obj)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoForm(instance=grupo_obj)
    context = {'form': form}
    return render(request, 'grupo/modificar_grupo.html', context)

def eliminarGrupo(request, id):
    grupo_obj = Grupo.objects.get(id=id)
    if request.method == 'POST':
        grupo_obj.delete()
        return redirect('lista_grupos')
    else:
        context = {'grupo': grupo_obj}
        return render(request, 'grupo/eliminar_grupo.html', context)
