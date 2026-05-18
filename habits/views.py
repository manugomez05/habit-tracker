from django.template import loader
from django.http import HttpResponse
from .models import Persona
from django.shortcuts import redirect,render
from .forms import PersonaForm

# Create your views here.
def persona(request):
    personas= Persona.objects.all().values()
    template = loader.get_template('persona.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context,request))

def crearPersona(request):
    if request.method == 'POST':

        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:

        form = PersonaForm()
        context = {'form':form}
    return render(request, 'habits/crear_persona.html', context)
