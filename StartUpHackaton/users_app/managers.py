import logging

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    def create_user(self, username: str, email: str, password: str, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        if not password:
            raise ValueError(_('The Password must be set'))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        if extra_fields.get('is_superuser'):
            logger.info(_(f'Superuser created  {username=} {email=}'))
        else:
            logger.info(_(f'User created:  {username=} {email=}'))
        return user

    def create_superuser(self, username: str, email: str, password: str, **extra_fields):
        """
        Change extra_fields to create a Superuser.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **extra_fields)
