
from django.shortcuts import redirect
from django.urls import path
from . import views


urlpatterns = [
    path('sign-up', views.sign_up, name='sign_up'),
    path('', lambda request: redirect('sign_up')),
]