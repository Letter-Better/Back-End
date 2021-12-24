from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OnlineRanking
from user.models import User

@receiver(post_save, sender=User)
def create_user_online_model(sender, instance=None, created=False, **kwargs):
    if created:
        OnlineRanking.objects.create(user=instance)