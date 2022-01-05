from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CampaignRanking
from user.models import User

@receiver(post_save, sender=User)
def create_user_campaign_model(sender, instance=None, created=False, **kwargs):
    if created:
        CampaignRanking.objects.create(user=instance)