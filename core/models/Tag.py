from django.db import models
from django.utils import timezone
from core.models import Comedouro, Cachorro

class Tag(models.Model):
    local  = models.ForeignKey(Comedouro,on_delete=models.PROTECT)
    cachorro = models.ForeignKey(Cachorro,on_delete=models.PROTECT)
    hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cachorro.nome