from django.template import loader
from django.http import HttpResponse
import requests
from .models import Tarea, Persona, Grupo
from django.shortcuts import redirect, render, get_object_or_404
from .forms import TareaForm, PersonaForm, GrupoForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonaSerializer, GrupoSerializer, TareaSerializer

# Create your views here.
def home(request):
    personas = Persona.objects.all()
    grupos = Grupo.objects.all()
    tareas = Tarea.objects.all()
    
    # Obtener datos del clima de Mendoza
    datos_clima = None
    error_clima = None
    ciudad = 'Mendoza'
    api_key = "fcb21c268804bdf1d4be1ec680fbb2c4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            if 'main' in datos and 'weather' in datos:
                datos_clima = {
                    'temperatura': datos['main']['temp'],
                    'descripcion': datos['weather'][0]['description'],
                    'icono': datos['weather'][0]['icon'],
                }
    except Exception as e:
        error_clima = str(e)
    
    return render(request, 'home.html', {
        'personas': personas,
        'grupos': grupos,
        'tareas': tareas,
        'datos_clima': datos_clima,
        'error_clima': error_clima,
        'ciudad': ciudad,
    })

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


def tareas(request):
    tareas = Tarea.objects.all()
    template = loader.get_template('tareas.html')
    context = {
        'tareas': tareas,
    }
    return HttpResponse(template.render(context, request))

def verTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    context = {'tarea': tarea}
    return render(request, 'ver_tarea.html', context)


def crearTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:       
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})

def modificarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    context = {'form': form}
    return render(request, 'modificar_tarea.html', context)

def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    else:
        context = {'tarea': tarea}
        return render(request, 'eliminar_tarea.html', context)
    
@api_view(['GET'])
def api_personas(request):

    personas = Persona.objects.all()

    serializer = PersonaSerializer(
        personas,
        many=True
    )

    return Response(serializer.data)

@api_view(['POST'])
def api_crear_persona(request):

    serializer = PersonaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201) #201 Corresponde a created.

    return Response(serializer.errors, status=400) #400 Corresponde a bad request (datos incorrectos).

@api_view(['PUT'])
def api_modificar_persona(request, id):
    persona = Persona.objects.get(id=id)
    serializer = PersonaSerializer(persona, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def api_eliminar_persona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return Response(status=204) #204 Corresponde a no content (eliminado correctamente).

@api_view(['GET'])
def api_grupo(request):
    grupo = Grupo.objects.all()
    serializer = GrupoSerializer (
        grupo, 
        many = True
    )
    return Response(serializer.data)

@api_view(['POST'])
def api_crear_grupo(request):
    serializer = GrupoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def api_modificar_grupo(request,id):
    grupo = Grupo.objects.get(id=id)
    serializer = GrupoSerializer(grupo, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def api_eliminar_grupo(request,id):
    grupo = Grupo.objects.get(id=id)
    grupo.delete()
    return Response(status=204)
 
@api_view(['GET', 'POST'])
def api_tareas(request):
    if request.method == 'GET':
        tareas = Tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data)

    serializer = TareaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def api_tarea_detail(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == 'GET':
        serializer = TareaSerializer(tarea)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TareaSerializer(tarea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    tarea.delete()
    return Response(status=204)

def clima(request):
    ciudad = 'Mendoza'
    datos_clima = None
    error = None
    
    api_key = "fcb21c268804bdf1d4be1ec680fbb2c4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            datos = response.json()
            if 'main' in datos and 'weather' in datos:
                datos_clima = {
                    'temperatura': datos['main']['temp'],
                    'descripcion': datos['weather'][0]['description'],
                    'icono': datos['weather'][0]['icon'],
                }
            else:
                error = "No se pudieron obtener los datos del clima."
        else:
            error = f"Error al obtener el clima (código {response.status_code})"
    except Exception as e:
        error = f"Error de conexión: {str(e)}"
    
    return render(request, 'clima.html', {'datos_clima': datos_clima, 'ciudad': ciudad, 'error': error})