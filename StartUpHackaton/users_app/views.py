import logging

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from users_app.create_form import CreateUser

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('debug from index')
    return render(request, 'users/index.html')


def register(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = CreateUser()
    return render(request, 'users/register.html', {'form': form})
