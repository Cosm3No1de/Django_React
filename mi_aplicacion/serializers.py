from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'completada', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']

    def validate_titulo(self, value):
        if not value.strip():
            raise serializers.ValidationError("El título no puede estar vacío.")
        if len(value) > 100:
            raise serializers.ValidationError("El título es demasiado largo (máximo 100 caracteres).")
        return value

    def validate_descripcion(self, value):
        if value and len(value) > 500:
            raise serializers.ValidationError("La descripción es demasiado larga (máximo 500 caracteres).")
        return value

    # Ejemplo de validación a nivel de objeto (varios campos)
    # def validate(self, data):
    #     if data.get('completada') and not data.get('descripcion'):
    #         raise serializers.ValidationError("Las tareas completadas deben tener una descripción.")
    #     return data