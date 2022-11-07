from django.db import models

class Comedouro(models.Model):
    local = models.CharField(max_length=100)
    hardware = models.CharField(max_length=100)

    def __str__(self):
        return self.local