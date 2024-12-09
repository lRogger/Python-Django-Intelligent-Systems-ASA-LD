
# import pandas as pd
from django.shortcuts import render
from .forms import CargarExcelForm
from .utils import cargar_encuesta_profesores_desde_excel, cargar_encuesta_estudiantes_desde_excel
from django.contrib import messages
from django.db import transaction

def migration_Excel_View(request):
    if request.method == 'POST':
        
        archivo_excel_estudiantes = request.FILES['archivo_excel_estudiantes']
        archivo_excel_profesores = request.FILES['archivo_excel_profesores']

        if not archivo_excel_estudiantes or not archivo_excel_profesores:
            messages.error(request, f"Por favor, cargue ambos archivos")
        else:
            try:
                with transaction.atomic():  # Bloque de transacción
                    if archivo_excel_profesores:
                        cargar_encuesta_profesores_desde_excel(archivo_excel_profesores)
                    if archivo_excel_estudiantes:
                        cargar_encuesta_estudiantes_desde_excel(archivo_excel_estudiantes)
                    messages.success(request, f"Subida de archivos correctamente")
            except Exception as e:
                messages.error(request, str(e))

    return render(request, 'migration_excel.html', {'form': CargarExcelForm()})
