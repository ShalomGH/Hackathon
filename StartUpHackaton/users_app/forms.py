import logging

from django import forms
from django.forms import ModelForm

from users_app.models import User

logger = logging.getLogger(__name__)


class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=True)
        instance.is_superuser = False
        instance.is_staff = False
        instance.is_active = True
        print('save')
        if commit:
            instance.save()
        return instance

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']


    def clean(self):
        super(UserRegistrationForm, self).clean()

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        logger.info(f'{username=}   {email=}   {password=}   {password_confirm=}')

        # todo: email validation
        self.cleaned_data.update({"is_superuser": False, "is_active": True, "is_staff": False})

        if password != password_confirm:
            print('Пароли не совпадают')
            self._errors['password_confirmation'] = self.error_class([
                'Пароли не совпадают'])

        print(self.cleaned_data)
        return self.cleaned_data


class UserEditingForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        super(UserEditingForm, self).clean()

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        logger.info(f'{username=}   {email=}   {password=}   {password_confirm=}')

        return self.cleaned_data
