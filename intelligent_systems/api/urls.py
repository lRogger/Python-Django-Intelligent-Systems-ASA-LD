# urls.py
from django.urls import path, include

urlpatterns = [
    path('academico/', include('academico.urls')),
    path('FL/', include('FL.urls')),
]
