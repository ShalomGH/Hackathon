import logging

import requests
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('debug from index')
    return render(request, 'users/index.html')


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
