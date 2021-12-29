from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _
import uuid

MESSAGES = {
    "unique": "...",
    "required": "...",
    "max_lenght": "...",
    "invalid_choice": "...",
    "null": "...",
    "blank": "...",
}

class Room(models.Model):

    def random_room_code() -> str: return uuid.uuid4().hex[:20].lower()

    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    class NumberOFUsers(models.IntegerChoices):
        Two = 2, _('Two')
        Three = 3, _('Three')
        Four = 4, _('Four')
        Five = 5, _('Five')
        Six = 6, _('Six')
        Seven = 7, _('Seven')
        Eight = 8, _('Eight')

    class Round(models.IntegerChoices):
        Two = 2, _('Two')
        Three = 3, _('Three')
        Four = 4, _('Four')

    class Time(models.IntegerChoices):
        ten_sec = 10, _('Ten Sec')
        twenty_sec = 20, _('Twenty Sec')
        thirty_sec = 30, _('Thirty Sec')

    class RoomType(models.IntegerChoices):
        Public = 1, _('public')
        Friend = 2, _('Friend')
        Private = 3, _('Private')

    creator = models.ForeignKey(User, verbose_name="Creator", db_column="creator", on_delete=models.CASCADE, error_messages=MESSAGES)
    time_of_draw = models.IntegerField(verbose_name="Time", db_column="time", choices=Time.choices, default=Time.thirty_sec, error_messages=MESSAGES)
    round = models.IntegerField(verbose_name="round", db_column="round", choices=Round.choices, default=Round.Two, error_messages=MESSAGES)
    number_of_users = models.IntegerField(verbose_name="number of user", db_column="number_of_users", choices=NumberOFUsers.choices, default=NumberOFUsers.Three, error_messages=MESSAGES)
    room_type = models.IntegerField(verbose_name="Room Type", db_column="room_type", choices=RoomType.choices, default=RoomType.Public, error_messages=MESSAGES)
    difficulty = models.CharField(verbose_name="Difficulty", db_column="difficulty", choices=DIFFICULTY, default='easy', max_length=50, error_messages=MESSAGES)
    room_code = models.CharField(verbose_name="Room Code", db_column="room_code", max_length=30, unique=True, default=random_room_code, error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Rooms"
        db_table = "Room"

    def __str__(self) -> str:
        return f"{self.creator} - {self.number_of_users}"

class RoomMember(models.Model):
    room = models.ForeignKey(Room, verbose_name="Room", db_column="room", on_delete=models.CASCADE, error_messages=MESSAGES)
    members = models.ForeignKey(User, verbose_name="Members", db_column="memebrs", on_delete=models.CASCADE, error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "RoomMember"
        db_table = "RoomMember"


    def __str__(self) -> str:
        return self.room

class Word(models.Model):
    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    word = models.CharField(verbose_name="Word", db_column="word", max_length=120, error_messages=MESSAGES)
    lenght = models.IntegerField(verbose_name="lenght", db_column="lenght", error_messages=MESSAGES)
    difficulty = models.CharField(verbose_name="Difficulty", db_column="difficulty", choices=DIFFICULTY, default='easy', max_length=50, error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Words"
        db_table = "Word"

    def __str__(self) -> str:
        return self.word

class OnlineRanking(models.Model):
    user = models.OneToOneField(User, verbose_name="User", db_column="user", on_delete=models.CASCADE, error_messages=MESSAGES)
    win = models.IntegerField(verbose_name="Win Count", db_column="win", default=0, error_messages=MESSAGES)
    lose = models.IntegerField(verbose_name="Lose Count", db_column="lose", default=0, error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "OnlineRanking"
        db_table = "OnlineRanking"

    @property
    def rank(self):
        return self.win / self.lose

    def __str__(self) -> str:
        return self.user