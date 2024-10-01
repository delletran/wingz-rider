from django.contrib.auth.models import BaseUserManager
from django.db import models


class USER_ROLE(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    RIDER = 'rider', 'Rider'
    DRIVER = 'driver', 'Driver'
    OTHER = 'other', 'Other'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('role', USER_ROLE.ADMIN)

        return self.create_user(email, password, **kwargs)

