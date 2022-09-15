from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users_app.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=40, unique=True)

    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=50)

    email = models.EmailField('email address', null=True, blank=True, unique=True)
    email_verified = models.BooleanField(default=False)

    phone = models.CharField('phone number', max_length=30, null=True, unique=True)
    phone_verified = models.BooleanField(default=False)

    company_id = models.IntegerField(default=0, blank=True)
    post = models.IntegerField(default=0)
    avatar_path = models.TextField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    is_active = models.BooleanField('active', default=False)
    is_staff = models.BooleanField('staff', default=False)
    is_verified = models.BooleanField('verified', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        unique_together = ('username', 'email', 'phone')
