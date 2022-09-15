from django import forms
from django.forms import ModelForm

from users_app.models import User


# define the class of a form
class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # write the name of models for which the form is made
        model = User

        # Custom fields
        fields = ["username", "password"]

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(UserRegistrationForm, self).clean()

        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        print(f'{username=}  {password=}')

        # conditions to be met for the username length
        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if len(password) < 8:
            self._errors['text'] = self.error_class([
                'Password Should Contain a minimum of 9 characters'])

        # return any errors if found
        return self.cleaned_data
