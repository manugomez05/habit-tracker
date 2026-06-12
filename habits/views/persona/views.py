from ...models.persona.model import Persona
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ...forms.persona.forms import PersonaForm
from ...permissions import es_administrador, es_lider, puede_gestionar_personas


@login_required(login_url='login')
def persona(request):
    personas = Persona.objects.all()
    template = loader.get_template('persona/persona.html')
    context = {
        'personas': personas,
        'es_admin': es_administrador(request.user),
        'es_lider': es_lider(request.user),
        'puede_gestionar_personas': puede_gestionar_personas(request.user),
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def verPersona(request, id):
    persona_obj = Persona.objects.get(id=id)
    return render(request, 'persona/ver_persona.html', {
        'persona': persona_obj,
        'es_admin': es_administrador(request.user),
        'es_lider': es_lider(request.user),
        'puede_gestionar_personas': puede_gestionar_personas(request.user),
    })

@login_required(login_url='login')
def crearPersona(request):
    if not puede_gestionar_personas(request.user):
        return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()

    return render(request, 'persona/crear_persona.html', {'form': form})

@login_required(login_url='login')
def modificarPersona(request, id):
    if not es_administrador(request.user):
        return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

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

@login_required(login_url='login')
def eliminarPersona(request, id):
    if not es_administrador(request.user):
        return HttpResponse('No tienes permiso para acceder a esta pagina', status=403)

    persona_obj = Persona.objects.get(id=id)
    if request.method == 'POST':
        persona_obj.delete()
        return redirect('lista_personas')
    else:
        context = {'persona': persona_obj}
        return render(request, 'persona/eliminar_persona.html', context)
