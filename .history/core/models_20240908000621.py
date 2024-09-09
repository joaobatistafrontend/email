from django.db import models
class Parlamentares(models.Model):
    nome = models.CharField(max_length=255)
    

class Acompanhante(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    parlamentares = models.ForeignKey(Parlamentares, on_delete=)