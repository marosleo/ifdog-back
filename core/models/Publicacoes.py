from django.db import models
from django.utils import timezone

class Publicacoes(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    publicado = publicado = models.DateTimeField(default=timezone.now)
    autor  = models.ForeignKey("core.Usuario",on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
