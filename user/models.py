from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import USER_ROLE, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'db_user'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-pk', 'first_name', 'last_name']

    USERNAME_FIELD = ('email')
    REQUIRED_FIELDS = ['password']

    id_user = models.AutoField(primary_key=True)
    role = models.CharField(
        max_length=10,
        choices=USER_ROLE.choices,
        default=USER_ROLE.OTHER
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return f'{self.pk} | {self.first_name} {self.last_name} ({self.role})'
