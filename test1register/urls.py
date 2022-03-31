from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login-page', views.login_user, name='login_user'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout_user', views.logout_user, name='logout_user'),
]