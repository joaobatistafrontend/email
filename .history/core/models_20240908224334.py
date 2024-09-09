from django.db import models
class Parlamentares(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self) :
        return f'{self.nome}'
class Acompanhante(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Email continua único
    parlamentares = models.ManyToManyField(Parlamentares)  # Permite associação com vários parlamentares
#     def __str__(self) :
#         return f'nome-{self.nome} email-{self.email} parlamenta-{self.parlamentare}'

# from django.db import models
# class Parlamentares(models.Model):
#     nome = models.CharField(max_length=255)


#     def __str__(self) :
#         return f'{self.nome}'

# class Acompanhante(models.Model):
#     nome = models.CharField(max_length=255)
#     email = models.EmailField()
#     parlamentare = models.ForeignKey(Parlamentares, on_delete=models.CASCADE)


#     def __str__(self) :
#         return f'nome-{self.nome} email-{self.email} parlamenta-{self.parlamentare}'