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

    def random_friend_id() -> str: return uuid.uuid4().hex[:20].lower()

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

    creator = models.OneToOneField(User, on_delete=models.CASCADE)
    members = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.CharField(verbose_name="Difficulty", db_column="difficulty", choices=DIFFICULTY, default='easy', max_length=50, error_messages=MESSAGES)
    number_of_users = models.IntegerField(verbose_name="number of user", db_column="number_of_users", choices=NumberOFUsers.choices, default=NumberOFUsers.Three, error_messages=MESSAGES)
    room_code = models.CharField(verbose_name="Room Code", db_column="friend_code", max_length=20, unique=True, default=random_friend_id, error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Rooms"
        db_table = "Room"

    def __str__(self) -> str:
        return f"{self.creator} - {self.number_of_users}"

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
        ...

    @property
    def rank(self):
        return self.win / self.lose

    def __str__(self) -> str:
        return self.user