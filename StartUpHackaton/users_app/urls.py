from django.urls import path

from users_app import views
from users_app.views import index


urlpatterns = [
    path('', index, name='home'),
    path('email/activate/<str:uid>/<str:token>/', views.activation),
]

