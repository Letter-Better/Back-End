from django import db
from django.db import models

MESSAGES = {
    "unique": "...",
    "required": "...",
    "max_lenght": "...",
    "invalid_choice": "...",
    "null": "...",
    "blank": "...",
}

class categorty(models.Model):
    name = models.CharField(verbose_name="Name", db_column="name", max_length=60, unique=True, error_messages=MESSAGES)
    slug = models.SlugField(verbose_name="Slug", db_column="slug", max_length=120, unique=True, error_messages=MESSAGES)

    class Meta:
        ...

    def __str__(self) -> str:
        return self.name
    

class word(models.Model):
    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    word = models.CharField(verbose_name="Word", db_column="word", max_length=120, error_messages=MESSAGES)
    lenght = models.IntegerField(verbose_name="lenght", db_column="lenght", error_messages=MESSAGES)
    category = models.ForeignKey(categorty, verbose_name="Category", db_column="category", on_delete=models.CASCADE, error_messages=MESSAGES)
    difficulty = models.CharField(verbose_name="Difficulty", db_column="difficulty", choices=DIFFICULTY, default='easy', max_length=50, error_messages=MESSAGES)

    class Meta:
        ...

    def __str__(self) -> str:
        return self.word
