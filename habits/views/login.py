# views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from habits.forms.usuario.forms import UsuarioForm, CambiarRolForm
from habits.models.usuario.model import Usuario
from habits.models.persona.model import Persona
from habits.models.rol.model import Rol

def es_administrador(user):
    """Verifica si el usuario es administrador"""
    try:
        return user.perfil.persona.rol.nombre == 'Administrador'
    except:
        return False

@login_required(login_url='login')
def home(request):
    from habits.models.tarea.model import Tarea
    
    personas = Persona.objects.all()
    tareas = Tarea.objects.all()
    
    context = {
        'personas': personas,
        'tareas': tareas,
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