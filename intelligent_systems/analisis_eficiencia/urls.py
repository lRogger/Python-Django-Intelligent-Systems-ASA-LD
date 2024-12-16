# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('resultados-encuesta-profesor/', views.obtener_resultados_encuesta_profesores, name='obtener_resultados_encuesta_profesores'),
    path('resultados-encuesta-estudiante/', views.obtener_resultados_encuesta_estudiantes, name='obtener_resultados_encuesta_estudiante'),
]