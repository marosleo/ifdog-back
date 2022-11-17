from django.db import models
from media.models import Image

class Cachorro(models.Model): #cards dos cachorros
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    altura = models.DecimalField(max_digits=8, decimal_places=2)
    nome_responsavel = models.CharField(max_length=100, default='')
    tel_responsavel = models.CharField(default='', max_length=100)
    castrado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
  
