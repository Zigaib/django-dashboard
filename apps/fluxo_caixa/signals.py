from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Despesa, Receita, Saldo

# Recebe uma despesa e cria um saldo
@receiver(post_save, sender=Despesa)
def despesa_saldo(sender, instance, created, **kwargs):
    if created:
        try:
            saldo_atual = Saldo.objects.latest('id')
        except:
            saldo_atual = Saldo.objects.create(saldo=0, valor=0, tipo='R')

        saldo = Saldo()
        saldo.saldo = saldo_atual.saldo - instance.valor
        saldo.tipo = 'D'
        saldo.descricao = instance.descricao
        saldo.valor = 0 if not instance.valor else -(instance.valor)
        saldo.save()

# Recebe uma receita e cria um saldo
@receiver(post_save, sender=Receita)
def receita_saldo(sender, instance, created, **kwargs):
    if created:
        try:
            saldo_atual = Saldo.objects.latest('id')
        except:
            saldo_atual = Saldo.objects.create(saldo=0, valor=0, tipo='R')

        saldo = Saldo()
        saldo.saldo = saldo_atual.saldo + instance.valor
        saldo.tipo = 'R'
        saldo.descricao = instance.descricao
        saldo.valor = 0 if not instance.valor else instance.valor
        saldo.save()

# Recebe uma despesa e atualiza o saldo
@receiver(post_delete, sender=Despesa)
def despesa_saldo_delete(sender, instance, **kwargs):
    try:
        saldo_atual = Saldo.objects.latest('id')
    except:
        saldo_atual = Saldo.objects.create(saldo=0, valor=0, tipo='R')

    saldo = Saldo()
    saldo.saldo = saldo_atual.saldo + instance.valor
    saldo.tipo = 'D'
    saldo.descricao = instance.descricao
    saldo.valor = 0 if not instance.valor else instance.valor
    saldo.save()

# Recebe uma receita e atualiza o saldo
@receiver(post_delete, sender=Receita)
def receita_saldo_delete(sender, instance, **kwargs):
    try:
        saldo_atual = Saldo.objects.latest('id')
    except:
        saldo_atual = Saldo.objects.create(saldo=0, valor=0, tipo='R')

    saldo = Saldo()
    saldo.saldo = saldo_atual.saldo - instance.valor
    saldo.tipo = 'R'
    saldo.descricao = instance.descricao
    saldo.valor = 0 if not instance.valor else -(instance.valor)
    saldo.save()