from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.manager import BaseManager
from django.utils.translation import ugettext_lazy as _
import uuid
from .managers import UserManager

MESSAGES = {
    "unique": "...",
    "required": "...",
    "max_lenght": "...",
    "invalid_choice": "...",
    "null": "...",
    "blank": "...",
}

class User(AbstractBaseUser):
    def random_friend_id() -> str: return uuid.uuid4().hex[:10].upper()

    class Role(models.IntegerChoices):
        PLAYER = 1, _('player')
        ADMIN = 2, _('admin')
        OWNER = 3, _('owner')

    username = models.CharField("Username", db_column="username", max_length=200, unique=True, error_messages=MESSAGES)
    email = models.EmailField("Email", db_column="email", max_length=200, unique=True, error_messages=MESSAGES)
    friend_code = models.CharField("Friend Code", db_column="friend_code", max_length=20, unique=True, default=random_friend_id, error_messages=MESSAGES)
    image = models.URLField("Image", db_column="image", default="https://none", error_messages=MESSAGES)
    full_name = models.CharField("Full Name", db_column="full_name", max_length=200, error_messages=MESSAGES)
    role = models.IntegerField("Role", db_column="role", choices=Role.choices, default=Role.PLAYER, error_messages=MESSAGES)
    create_at = models.DateTimeField("Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField("Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    is_active = models.BooleanField("is Active", db_column="is_active", default=True, error_messages=MESSAGES)
    is_vip = models.BooleanField("is VIP", db_column="is_vip", default=False, error_messages=MESSAGES)
    is_donator = models.BooleanField("is Donator", db_column="is_donator", default=False, error_messages=MESSAGES)
    is_email_verified = models.BooleanField("is Email verified", db_column="is_email_verified", default=False, error_messages=MESSAGES)

    objects = UserManager()
    defmanager = models.Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = "Users"
        db_table = "User"

    def __str__(self) -> str:
        return self.username

class Friend(models.Model):
    user = models.ForeignKey(User, db_column="user", related_name="user_set", on_delete=models.CASCADE, error_messages=MESSAGES)
    friend = models.ForeignKey(User, db_column="friend", related_name="friend_set", on_delete=models.CASCADE, error_messages=MESSAGES)
    create_at = models.DateTimeField("Create At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Friends"
        db_table = "Friend"
    
    def __str__(self) -> str:
        return f"{self.user} {self.friend}"

class Status(models.Model):
    user = models.OneToOneField(User, db_column="user", related_name="user_status_set", on_delete=models.CASCADE, error_messages=MESSAGES)
    total = models.IntegerField("Total", db_column="total", default=0, error_messages=MESSAGES)
    win = models.IntegerField("Win", db_column="win", default=0, error_messages=MESSAGES)
    lose = models.IntegerField("Lose", db_column="lose", default=0, error_messages=MESSAGES)
    level = models.IntegerField("level", db_column="level", default=0, error_messages=MESSAGES)
    point = models.IntegerField("point", db_column="point", default=0, error_messages=MESSAGES)
    create_at = models.DateTimeField("Created At", db_column="create_at", auto_now_add=True, editable=False, error_messages=MESSAGES)
    update_at = models.DateTimeField("Update At", db_column="update_at", auto_now=True, error_messages=MESSAGES)

    class Meta:
        verbose_name_plural = "Status"
        db_table = "Status"

    def __str__(self) -> str:
        return self.user
