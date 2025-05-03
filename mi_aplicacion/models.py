# mi_aplicacion/models.py
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.titulo.strip():
            raise ValidationError({'titulo': 'El título no puede estar vacío.'})
        if len(self.titulo) > 100:
            raise ValidationError({'titulo': 'El título es demasiado largo (máximo 100 caracteres).'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
# Create your models here.
