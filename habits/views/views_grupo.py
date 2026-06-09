
from habits.models.models_grupo import Grupo

from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms.forms_grupo import GrupoForm






def grupo(request):
    grupos = Grupo.objects.all()
    template = loader.get_template('grupo.html')
    context = {
        'grupos': grupos,
    }
    return HttpResponse(template.render(context,request))

def verGrupo(request, id):
    grupo = Grupo.objects.get(id=id)
    context = {'grupo': grupo}
    return render(request, 'ver_grupo.html', context)

def crearGrupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoForm()

    return render(request, 'crear_grupo.html', {'form': form})

def modificarGrupo(request, id):
    grupo = Grupo.objects.get(id=id)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoForm(instance=grupo)
    context = {'form': form}
    return render(request, 'modificar_grupo.html', context)

def eliminarGrupo(request, id):
    grupo = Grupo.objects.get(id=id)
    if request.method == 'POST':
        grupo.delete()
        return redirect('lista_grupos')
    else:
        context = {'grupo': grupo}
        return render(request, 'eliminar_grupo.html', context)
