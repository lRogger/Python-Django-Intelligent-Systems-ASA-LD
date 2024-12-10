from django.urls import path, include

from . import views
from migration_excel import views as migration_excel_views
from analisis_eficiencia import views as analisis_eficiencia_views

urlpatterns=[
    path('', views.homeLayout, name='index'),
    path('migration/', migration_excel_views.migration_Excel_View, name='migration_excel'),
    path('analisis-eficiencia/', analisis_eficiencia_views.analisis_Eficiencia_View, name='analisis_eficiencia'),
]