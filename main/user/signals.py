from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Status
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Status.objects.create(user=instance)
