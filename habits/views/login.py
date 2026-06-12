# views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from habits.forms.usuario.forms import UsuarioForm, CambiarRolForm, CrearUsuarioPersonaForm
from habits.models.usuario.model import Usuario
from habits.models.persona.model import Persona
from habits.models.rol.model import Rol
from habits.permissions import (
    es_administrador,
    es_lider,
    puede_gestionar_personas,
    puede_gestionar_tareas,
)

@login_required(login_url='login')
def home(request):
    from habits.models.tarea.model import Tarea
    
    personas = Persona.objects.all()
    if puede_gestionar_tareas(request.user):
        tareas = Tarea.objects.all()
    else:
        try:
            tareas = Tarea.objects.filter(personas=request.user.perfil.persona)
        except Exception:
            tareas = Tarea.objects.none()
    
    context = {
        'personas': personas,
        'tareas': tareas,
        'es_admin': es_administrador(request.user),
        'es_lider': es_lider(request.user),
        'puede_gestionar_personas': puede_gestionar_personas(request.user),
        'puede_gestionar_tareas': puede_gestionar_tareas(request.user),
    }
    return render(request, 'home.html', context)

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Validar que los campos no estén vacíos
        if not username:
            error = 'El usuario es requerido'
        elif not password:
            error = 'La contraseña es requerida'
        else:
            # Autenticar usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = 'Usuario o contraseña incorrectos'
    
    return render(request, 'login.html', {'error': error})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Obtener el rol "Integrante" por defecto
            rol_integrante = Rol.objects.get(nombre='Integrante')
            
            # Crear registro en Persona con rol por defecto
            persona = Persona.objects.create(
                nombre=user.first_name,
                apellido=user.last_name,
                documento=form.cleaned_data['documento'],
                rol=rol_integrante
            )
            
            # Crear el perfil de Usuario vinculado con Persona
            Usuario.objects.create(user=user, persona=persona)
            
            login(request, user)
            return redirect('home')
    else:
        form = UsuarioForm()
    
    return render(request, 'crear_usuario.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def crear_usuario_persona(request, id):
    if not es_administrador(request.user):
        return HttpResponseForbidden('No tienes permiso para acceder a esta pagina')

    persona = get_object_or_404(Persona, id=id)
    if hasattr(persona, 'usuario'):
        return redirect('verPersona', id=persona.id)

    if request.method == 'POST':
        form = CrearUsuarioPersonaForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = persona.nombre
            user.last_name = persona.apellido
            user.email = form.cleaned_data['email']
            user.save()
            Usuario.objects.create(user=user, persona=persona)
            return redirect('verPersona', id=persona.id)
    else:
        form = CrearUsuarioPersonaForm()

    return render(request, 'crear_usuario_persona.html', {
        'form': form,
        'persona': persona,
    })

@login_required(login_url='login')
def cambiar_rol(request):
    """Vista para que administradores cambien los roles de otros usuarios"""
    
    # Verificar si el usuario es administrador
    if not es_administrador(request.user):
        return HttpResponseForbidden('No tienes permiso para acceder a esta página')
    
    error = None
    success = None
    
    if request.method == 'POST':
        form = CambiarRolForm(request.POST)
        if form.is_valid():
            persona = form.cleaned_data['persona']
            nuevo_rol = form.cleaned_data['rol']
            persona.rol = nuevo_rol
            persona.save()
            success = f'Rol de {persona.nombre} {persona.apellido} actualizado a {nuevo_rol.nombre}'
    else:
        form = CambiarRolForm()
    
    personas = Persona.objects.all()
    
    return render(request, 'cambiar_rol.html', {
        'form': form,
        'personas': personas,
        'error': error,
        'success': success
    })
