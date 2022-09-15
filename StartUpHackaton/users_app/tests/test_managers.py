from django.test import TestCase

from users_app.models import User


class TestUserManager(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='test_superuser', email='test_superuser@user.com', password='password')
        User.objects.create_user(username='test_user', email='test_user@user.com', password='password')

    def test_create_user_without_username(self):
        self.assertRaisesRegexp(ValueError,
                                'The Username must be set',
                                User.objects.create_user, username='', email='normal@user.com', password='password')

    def test_create_user_without_email(self):
        self.assertRaisesRegexp(ValueError,
                                'The Email must be set',
                                User.objects.create_user, username='Username', email='', password='password')

    def test_create_user_without_password(self):
        self.assertRaisesRegexp(ValueError,
                                'The Password must be set',
                                User.objects.create_user, username='Username', email='normal@user.com', password='')

    def test_create_superuser_extra_fields(self):
        test_superuser = User.objects.get(username='test_superuser')
        self.assertTrue(test_superuser.is_active)
        self.assertTrue(test_superuser.is_superuser)
        self.assertTrue(test_superuser.is_staff)
