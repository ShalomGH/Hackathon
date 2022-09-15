import logging

import requests
from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('debug from index')
    return render(request, 'users/index.html')


def activation(request, uid, token):
    response = requests.post('http://localhost:8000/api/v1/auth/users/activation/', data={'uid': uid, 'token': token})
    if response.status_code == HTTPStatus.OK:
        return HttpResponse(f'Activation page<p>'
                            f'uid = {uid}<br>'
                            f'token = {token}')
    else:
        return HttpResponse(f'Bad request')
