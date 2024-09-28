
from django.shortcuts import redirect
from django.urls import path
from . import views


urlpatterns = [
    # path('sign-up', views.sign_up, name='sign_up'),
    # path('', lambda request: redirect('sign_up')),
    path('sign-up', views.signup, name='signup'),
    path('', lambda request: redirect('signup')),
    path('signin', views.signin, name='signin'),
    path('home', views.home, name='home'),
]