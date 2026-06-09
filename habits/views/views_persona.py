from .models.models_persona import Persona
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms.forms_persona import PersonaForm





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
