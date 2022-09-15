from django.test import TestCase
from rest_framework import serializers

from users_app.serializers import UserSerializer


class TestUserSerializer(TestCase):
    def setUp(self):
        data = {
            "username": "r_ooae",
            "email": "sema1106@mail.ruddge",
            "phone": "8983624927",
            "password": "adda",
        }
        self.serializer = UserSerializer(data=data)

    def test_short_password(self):
        self.assertRaisesRegexp(serializers.ValidationError,
                                'Ensure this field has at least 8 characters.',
                                self.serializer.is_valid, raise_exception=True)

    def test_username_validation(self):
        self.assertRaisesRegexp(serializers.ValidationError,
                                'The Username must be 4-30 characters long',
                                self.serializer.validate_username, value='afw')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'No _ or . at the beginning and at the end',
                                self.serializer.validate_username, value='_Username')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'No _ or . at the beginning and at the end',
                                self.serializer.validate_username, value='Username_')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'No _ or . at the beginning and at the end',
                                self.serializer.validate_username, value='.Username')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'No _ or . at the beginning and at the end',
                                self.serializer.validate_username, value='Username.')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'No __ or _. or ._ or .. inside username',
                                self.serializer.validate_username, value='User_.name')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'No __ or _. or ._ or .. inside username',
                                self.serializer.validate_username, value='User__name')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'No __ or _. or ._ or .. inside username',
                                self.serializer.validate_username, value='User..name')
        self.assertRaisesRegexp(serializers.ValidationError,
                                'The Username must consist only of numbers, Latin letters and . _',
                                self.serializer.validate_username, value='User.^name')
