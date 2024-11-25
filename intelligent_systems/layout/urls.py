from django.urls import path

from . import views

urlpatterns=[
    path('', views.homeLayout, name='index'),
]