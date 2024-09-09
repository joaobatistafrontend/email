from django.db import models
class Parlamentares()


class Acompanhante(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()