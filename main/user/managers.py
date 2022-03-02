from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("User must have and email address!")

        user = self.model(username=username, email=email.lower())
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        if not username:
            raise ValueError("User must have and email address!")

        user = self.model(username=username, email=email.lower())
        user.set_password(password)
        user.role = 3
        user.save(using=self._db)
        return user
