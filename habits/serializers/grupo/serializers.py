from rest_framework import serializers
from ...models.grupo.model import Grupo


class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupo
        fields = '__all__'
