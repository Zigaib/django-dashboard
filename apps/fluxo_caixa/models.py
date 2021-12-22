from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Tipo_Operacao(models.Model):
    tipo = models.CharField(max_length=1, choices=(('E', 'Entrada'), ('S', 'Saída')), default='E')
    descricao = models.CharField(max_length=100)

class Lancamento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_documento = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.ForeignKey(Tipo_Operacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ('data',)
