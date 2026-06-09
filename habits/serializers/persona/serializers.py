from rest_framework import serializers
from ...models.persona.model import Persona


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'
