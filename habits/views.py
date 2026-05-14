from django.template import loader
from django.http import HttpResponse
from .models import Persona
# Create your views here.

def persona(request):
    personas= Persona.objects.all().values()
    template = loader.get_template('persona.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context,request))
