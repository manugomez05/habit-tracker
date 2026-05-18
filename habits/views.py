from django.template import loader
from django.http import HttpResponse
from .models import Persona, Grupo
from django.shortcuts import redirect,render
from .forms import PersonaForm, GrupoForm

# Create your views here.
def persona(request):
    personas = Persona.objects.all()
    template = loader.get_template('persona.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))

def verPersona(request, id):
    persona_obj = Persona.objects.get(id=id)
    return render(request, 'ver_persona.html', {'persona': persona_obj})


def crearPersona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()

    return render(request, 'crear_persona.html', {'form': form})

def modificarPersona(request,id):
    persona= Persona.objects.get(id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')

    else:
        form = PersonaForm(instance=persona)
        context = {'form': form}
    return render(request, 'modificar_persona.html', context)

def eliminarPersona(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    else:
        context = {'persona': persona}
        return render(request, 'eliminar_persona.html', context)

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
