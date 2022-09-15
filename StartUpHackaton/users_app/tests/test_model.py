from django.test import TestCase

from users_app.models import User


class UserModelTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='normalname', email='normal@user.com', password='foo')

    def test_model_username(self):
        self.assertEqual('normalname', self.test_user.username)

    def test_user_email(self):
        self.assertEqual('normal@user.com', self.test_user.email)

    def test_user_company(self):
        self.assertEqual(0, self.test_user.company_id)

    def test_user_post(self):
        self.assertEqual(0, self.test_user.post)

    def test_user_avatar_path(self):
        self.assertEqual(None, self.test_user.avatar_path)

    def test_user_flags(self):
        self.assertFalse(self.test_user.email_verified)
        self.assertFalse(self.test_user.phone_verified)
        self.assertFalse(self.test_user.is_active)
        self.assertFalse(self.test_user.is_staff)
        self.assertFalse(self.test_user.is_superuser)

