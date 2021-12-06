from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
import uuid

MESSAGES = (
    ('', ''),
)

class User(AbstractBaseUser):
    def random_friend_id() -> str: return uuid.uuid4().hex[:10].upper()

    class Role(models.IntegerChoices):
        PLAYER = 1, _('player')
        ADMIN = 2, _('admin')
        SERVER = 3, _('server')

    username = models.CharField("Username", db_column="username", max_length=200, unique=True)
    email = models.EmailField("Email", db_column="email", max_length=200, unique=True)
    friend_code = models.CharField("Friend Code", db_column="friend_code", max_length=20, unique=True, default=random_friend_id)
    image = models.URLField("Image", db_column="image", default="https://none")
    full_name = models.CharField("Full Name", db_column="full_name", max_length=200)
    role = models.IntegerField("Role", db_column="role", choices=Role.choices, default=Role.PLAYER)
    create_at = models.DateTimeField("Created At", db_column="create_at", auto_now_add=True, editable=False)
    update_at = models.DateTimeField("Update At", db_column="update_at", auto_now=True)

    is_active = models.BooleanField("is Active", db_column="is_active", default=True)
    is_vip = models.BooleanField("is VIP", db_column="is_vip", default=False)
    is_donator = models.BooleanField("is Donator", db_column="is_donator", default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.username

class Friend(models.Model):
    user = models.ForeignKey(User, db_column="user", related_name="user_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(User, db_column="friend", related_name="friend_set", on_delete=models.CASCADE)
    create_at = models.DateTimeField("Create At", db_column="create_at", auto_now_add=True, editable=False)

    class Meta:
        db_table = "userfriend"
    
    def __str__(self) -> str:
        return f"{self.user} {self.friend}"

class Status(models.Model):
    user = models.OneToOneField(User, db_column="user", related_name="user_status_set", on_delete=models.CASCADE)
    total = models.IntegerField("Total", db_column="total", default=0)
    win = models.IntegerField("Win", db_column="win", default=0)
    lose = models.IntegerField("Lose", db_column="lose", default=0)
    level = models.IntegerField("level", db_column="level", default=0)
    point = models.IntegerField("point", db_column="point", default=0)
    create_at = models.DateTimeField("Created At", db_column="create_at", auto_now_add=True, editable=False)
    update_at = models.DateTimeField("Update At", db_column="update_at", auto_now=True)

    class Meta:
        db_table = "Status"

    def __str__(self) -> str:
        return self.user