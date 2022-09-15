from django.urls import path

from users_app import views

urlpatterns = [
    path('email/activate/<str:uid>/<str:token>/', views.activation),
]
