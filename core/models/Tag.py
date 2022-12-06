from django.db import models
from django.utils import timezone
from core.models import Comedouro, Cachorro
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from media.models import Image


class Tag(models.Model):
    local  = models.ForeignKey(Comedouro,on_delete=models.PROTECT)
    cachorro = models.ForeignKey(Cachorro,on_delete=models.PROTECT)
    hora = models.DateTimeField(auto_now=True)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )

    def __str__(self):
        return self.cachorro.nome