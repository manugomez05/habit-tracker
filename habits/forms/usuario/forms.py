from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from habits.models.persona.model import Persona
from habits.models.rol.model import Rol

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Tu email'
    }))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Tu nombre'
    }))
    last_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Tu apellido'
    }))
    documento = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'placeholder': 'Tu DNI'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'documento', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Tu usuario'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este usuario ya existe.')
        return username
    
    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if documento and Persona.objects.filter(documento=documento).exists():
            raise forms.ValidationError('Este DNI ya está registrado.')
        return documento


class CambiarRolForm(forms.Form):
    persona = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        label='Persona',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(),
        label='Nuevo Rol',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class CrearUsuarioPersonaForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Usuario'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya esta registrado.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este usuario ya existe.')
        return username
