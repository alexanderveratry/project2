from django.db import models


# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=64, )
    description = models.CharField(max_length=64)
    starting = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True)
    comentarios = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f"{self.id}: {self.title} starting in {self.starting}"