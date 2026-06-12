from django.urls import path
from habits.views.login import login_view, crear_usuario, home, logout_view, cambiar_rol

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('registro/', crear_usuario, name='registro'),
    path('logout/', logout_view, name='logout'),
    path('cambiar-rol/', cambiar_rol, name='cambiar_rol'),
]