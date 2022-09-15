from django.urls import path

from users_app import views as user_views
from users_app.views import index


urlpatterns = [
    path('', index),
    path('register/', user_views.register, name='register'),
]

