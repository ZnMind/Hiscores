from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, player_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', player_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]