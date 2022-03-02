from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OnlineRanking, Room, RoomMember
from user.models import User


@receiver(post_save, sender=User)
def create_user_online_model(sender, instance=None, created=False, **kwargs):
    if created:
        OnlineRanking.objects.create(user=instance)

# @receiver(post_save, sender=Room)
# def add_room_craetor_to_members(sender, instance=None, craeted=False, **kwargs):
# if craeted:
# RoomMember.objects.create(room_id=instance.id, members_id=instance.creator.id)
