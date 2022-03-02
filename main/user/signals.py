from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import User, Status, UserMission


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_status(sender, instance=None, created=False, **kwargs):
    if created:
        Status.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_mission(sender, instance=None, created=False, **kwargs):
    if created:
        UserMission.objects.create(user=instance)
