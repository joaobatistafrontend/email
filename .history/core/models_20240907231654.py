from django.db import models

class Acompanhante(models.Model):
    nome = models.(max_length='105')
    email = models.EmailField()