import logging

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, redirect

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('debug from index')
    return render(request, 'users/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    template_name = 'users/register.html'
    return render(request, template_name, context)
