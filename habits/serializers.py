from rest_framework import serializers
from .models_base import Persona, Grupo, Tarea

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Persona

        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Grupo

        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tarea

        fields = '__all__'