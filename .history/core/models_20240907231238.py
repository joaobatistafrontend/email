from django.db import models

class Acompanhante(models.Model):
    nome = models.CharField(max_length='255')