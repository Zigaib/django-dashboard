from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Feminino')), default='M')
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    sobre = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='apps/static/assets/img/avatar/' , null=True, blank=True)
    cargo = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.avatar:
            self.avatar.name = self.avatar.name.replace('apps/', '')
        if self.user.first_name:
            self.user.first_name = self.user.username.capitalize()
        if self.user.last_name:
            self.user.last_name = self.user.username.capitalize()
        self.user.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        User.objects.filter(pk=instance.pk).update(first_name=instance.username.capitalize(), last_name=instance.last_name.capitalize())

@receiver(pre_save, sender=Profile)
def save_profile(sender, instance, **kwargs):
    if instance.cargo:
        instance.cargo = instance.cargo.capitalize()