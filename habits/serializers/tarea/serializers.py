from rest_framework import serializers
from ...models.tarea.model import Tarea


class TareaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'
