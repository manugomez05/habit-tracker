from ...models.persona.model import Persona
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ...forms.persona.forms import PersonaForm


def persona(request):
    personas = Persona.objects.all()
    template = loader.get_template('persona/persona.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))

def verPersona(request, id):
    persona_obj = Persona.objects.get(id=id)
    return render(request, 'persona/ver_persona.html', {'persona': persona_obj})

def crearPersona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()

    return render(request, 'persona/crear_persona.html', {'form': form})

def modificarPersona(request, id):
    persona_obj = Persona.objects.get(id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona_obj)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')

    else:
        form = PersonaForm(instance=persona_obj)
        context = {'form': form}
    return render(request, 'persona/modificar_persona.html', context)

def eliminarPersona(request, id):
    persona_obj = Persona.objects.get(id=id)
    if request.method == 'POST':
        persona_obj.delete()
        return redirect('lista_personas')
    else:
        context = {'persona': persona_obj}
        return render(request, 'persona/eliminar_persona.html', context)
