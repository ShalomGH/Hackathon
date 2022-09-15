from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users_app.managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    email = models.EmailField(null=True, blank=True, unique=True)
    email_verified = models.BooleanField(default=False)

    company_id = models.IntegerField(default=0, blank=True)
    post = models.IntegerField(default=0)
    avatar_path = models.TextField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        # unique_together = ('username', 'email')
