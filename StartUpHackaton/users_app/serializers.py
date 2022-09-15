# import re
#
# # from rest_framework import serializers
#
# from users_app.models import User
#
#
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=8, write_only=True)
#
#     # username is 4-30 characters long
#     # no _ or . at the beginning and at the end
#     # no __ or _. or ._ or .. inside
#     # username must consist only of numbers, Latin letters and . _
#     @staticmethod
#     def validate_username(value: str) -> str:
#         if re.match(r'^(?=.{4,30}$)', value) is None:
#             raise serializers.ValidationError('The Username must be 4-30 characters long')
#         elif re.match(r'(?![_.])+.+(?<![_.])$', value) is None:
#             raise serializers.ValidationError('No _ or . at the beginning and at the end')
#         elif re.match(r'(?!.*[_.]{2})', value) is None:
#             raise serializers.ValidationError('No __ or _. or ._ or .. inside username')
#         elif re.fullmatch(r'[a-zA-Z0-9._]+', value) is None:
#             raise serializers.ValidationError('The Username must consist only of numbers, Latin letters and . _')
#         else:
#             return value
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'phone')
#         extra_kwargs = {
#             "password": {"write_only": True},
#         }
#
