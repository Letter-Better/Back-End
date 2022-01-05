from django.contrib import admin
from .models import Room, RoomMember, OnlineRanking, Word

admin.site.register(Room)
admin.site.register(RoomMember)
admin.site.register(Word)
admin.site.register(OnlineRanking)

