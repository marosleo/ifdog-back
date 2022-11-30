from django.db import models
from django.utils import timezone

class Comentarios(models.Model):
    texto = models.TextField()
    autor  = models.ForeignKey("core.Usuario",on_delete=models.CASCADE)

    def __str__(self):
        return self.texto