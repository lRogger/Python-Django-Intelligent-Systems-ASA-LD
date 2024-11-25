from django.urls import path, include

from . import views
from AST.views import *
from FL.views import *

urlpatterns=[
    path('', views.homeLayout, name='index'),
    path('AST/', views.migration_AST, name='migration_AST'),
    path('FL/', views.migration_FL_View, name='migration_FL'),
]