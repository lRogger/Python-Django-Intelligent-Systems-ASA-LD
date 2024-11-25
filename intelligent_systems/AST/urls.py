from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatters = [
    path('AST/', views.migration_AST_View, name='AST')
]