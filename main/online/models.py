from django.db import models

class categorty(models.Model):
    name = models.CharField()
    slug = models.SlugField()


class word(models.Model):
    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    word = models.CharField()
    lenght = models.IntegerField()
    category = models.ForeignKey(categorty)
    difficulty = models.CharField(verbose_name="Difficulty", db_column="difficulty", choices=DIFFICULTY, default='easy', max_length=50, error_messages=MESSAGES)


