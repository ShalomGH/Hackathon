import logging

from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('debug from index')
    return render(request, 'users/index.html')


def register(request):
    form = UserCreationForm()
    context = {'form': form}
    template_name = 'users/register.html'
    return render(request, template_name, context)
