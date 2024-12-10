# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('resultados-encuesta-profesor/', views.obtener_resultados_encuesta_profesores, name='obtener_resultados_encuesta_profesores'),
]