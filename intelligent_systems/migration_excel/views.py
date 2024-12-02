
import pandas as pd
from django.shortcuts import render
from .forms import CargarExcelForm
from .utils import cargar_encuesta_profesores_desde_excel, cargar_encuesta_estudiantes_desde_excel
from django.contrib import messages

def migration_Excel_View(request):
    if request.method == 'POST':
        
        # messages.info(request, "holi.")
        archivo_excel_estudiantes = request.FILES['archivo_excel_estudiantes']
        archivo_excel_profesores = request.FILES['archivo_excel_profesores']

        if archivo_excel_profesores:
            cargar_encuesta_profesores_desde_excel(archivo_excel_profesores)
        if archivo_excel_estudiantes:
            cargar_encuesta_estudiantes_desde_excel(archivo_excel_estudiantes)

    return render(request, 'migration_excel.html', {'form': CargarExcelForm()})
