from user.models import User
from django.db import models


MESSAGES = {
    "unique": "...",
    "required": "...",
    "max_lenght": "...",
    "invalid_choice": "...",
    "null": "...",
    "blank": "...",
}

class Mission(models.Model):
    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    number = models.IntegerField(verbose_name="Mission Number", db_column="number", unique=True, error_messages=MESSAGES)
    name = models.CharField(verbose_name="Mission Name", db_column="name", unique=True, max_length=120, error_messages=MESSAGES)
    difficulty = models.CharField(verbose_name="Difficulty", db_column="difficulty", choices=DIFFICULTY, default='easy', max_length=50, error_messages=MESSAGES)
    word = models.CharField(verbose_name="Word", db_column="word", max_length=500, error_messages=MESSAGES)
    point = models.IntegerField(verbose_name="Mission Point", db_column="point", error_messages=MESSAGES)
    time = models.IntegerField(verbose_name="Mission Time", db_column="time", error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Missions"
        db_table = "Mission"

    def __str__(self) -> str:
        return f"{self.number}-{self.name}"

class CampaignRanking(models.Model):
    user = models.OneToOneField(User, verbose_name="User", db_column="user", on_delete=models.CASCADE, error_messages=MESSAGES)
    win = models.IntegerField(verbose_name="win", db_column="win", default=0, error_messages=MESSAGES)
    lose = models.IntegerField(verbose_name="lose", db_column="lose", default=0, error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Campaign Ranking"
        db_table = "CampaignRanking"

    @property
    def rank(self):
        return self.win / self.lose

    def __str__(self) -> str:
        return f"{self.user.username}-{self.rank}"
