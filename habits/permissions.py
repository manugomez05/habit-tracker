from django.http import HttpResponseForbidden


def obtener_rol_usuario(user):
    try:
        return user.perfil.persona.rol.nombre
    except Exception:
        return None


def es_administrador(user):
    return obtener_rol_usuario(user) == 'Administrador'


def es_lider(user):
    return obtener_rol_usuario(user) == 'Lider'


def puede_gestionar_personas(user):
    return es_administrador(user) or es_lider(user)


def puede_gestionar_tareas(user):
    return es_administrador(user) or es_lider(user)


def requiere_permiso(user, permiso):
    if permiso(user):
        return None
    return HttpResponseForbidden('No tienes permiso para acceder a esta pagina')
