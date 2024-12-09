# urls.py
from django.urls import path, include

urlpatterns = [
    path('academico/', include('academico.urls')),
]
