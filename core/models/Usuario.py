from django.contrib.auth.models import AbstractUser
from django.db import models
from media.models import Image


class Usuario(AbstractUser):
    typeuser = models.BooleanField(default=False)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )