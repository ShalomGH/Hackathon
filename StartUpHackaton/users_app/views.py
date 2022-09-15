import logging

from django.contrib import messages
from django.http import HttpResponse

from django.shortcuts import render, redirect

from users_app.forms import UserRegistrationForm

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('debug from index')
    return render(request, 'users/index.html')


def register(request):
    if request.method == 'POST':
        user = UserRegistrationForm(request.POST)
        if user.is_valid():
            user.save()
            username = user.cleaned_data.get('username')
            print(f'Account created for {username}!')
            return redirect('/')
    else:
        user = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': user})
