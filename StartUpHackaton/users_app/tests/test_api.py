from rest_framework.test import APITestCase

from users_app.models import User


class UsersAppApiTest(APITestCase):
    def setUp(self):
        self.data = {'username': 'normal_user',
                     'password': '123456789KDmd;',
                     're_password': '123456789KDmd;',
                     'email': 'sema1106@mail.ru',
                     'phone': '89836249244'}
        url = '/api/v1/auth/users/'
        self.response = dict(self.client.post(url, data=self.data).json())

    def test_response(self):
        self.assertEqual(self.data['username'], self.response['username'])
        self.assertEqual(self.data['phone'], self.response['phone'])
        self.assertEqual(self.data['email'], self.response['email'])

    def test_database(self):
        normal_user = User.objects.get(username=self.data['username'])
        self.assertEqual(self.data['username'], normal_user.username)
        self.assertEqual(self.data['email'], normal_user.email)
        self.assertEqual(self.data['phone'], normal_user.phone)
