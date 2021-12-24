from django.db import models
from user.models import User

MESSAGES = {
    "unique": "...",
    "required": "...",
    "max_lenght": "...",
    "invalid_choice": "...",
    "null": "...",
    "blank": "...",
}

class Categorty(models.Model):
    name = models.CharField(verbose_name="Name", db_column="name", max_length=60, unique=True, error_messages=MESSAGES)
    slug = models.SlugField(verbose_name="Slug", db_column="slug", max_length=120, unique=True, error_messages=MESSAGES)
    create_at = models.DateTimeField(verbose_name="Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField(verbose_name="Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Category"

    def __str__(self) -> str:
        return self.name
    

class Word(models.Model):
    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    word = models.CharField(verbose_name="Word", db_column="word", max_length=120, error_messages=MESSAGES)
    lenght = models.IntegerField(verbose_name="lenght", db_column="lenght", error_messages=MESSAGES)
    category = models.ForeignKey(Categorty, verbose_name="Category", db_column="category", on_delete=models.CASCADE, error_messages=MESSAGES)
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