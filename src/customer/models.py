from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name = 'profile', null = False)
    phone = models.CharField('Телефон', max_length=13)
    country = models.CharField(
        'Страна',
        max_length=30, 
        null=True, 
        blank = True, 
        default = '-'
        )
    city = models.CharField(
        'Город',
        max_length=30, 
        null=True, 
        blank = True, 
        default = '-'
        )
    postcode = models.CharField(
        'Индекс',
        max_length=10, 
        null=True, 
        blank = True, 
        default = '-'
        )
    аddress = models.CharField(
        'Адрес',
        max_length=100, 
        null=True, 
        blank = True, 
        default = '-'
        )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()