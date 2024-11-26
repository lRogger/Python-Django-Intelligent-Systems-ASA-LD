
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CargarExcelForm
from academico.models import Docente, Materia

def migration_Excel_View(request):
    if request.method == 'POST' and request.FILES['archivo_excel']:
        # Leemos el archivo Excel
        archivo = request.FILES['archivo_excel']
        df = pd.read_excel(archivo)

        # Procesar el DataFrame y migrar los datos a la base de datos
        # Asegúrate de que el archivo tenga las columnas necesarias: 'nombre', 'experiencia', etc.

        for index, row in df.iterrows():
            # Crear o actualizar materia
            materia, created = Materia.objects.get_or_create(nombre=row['Materia'], descripcion=row['Descripcion'])

            # Crear o actualizar docente
            docente, created = Docente.objects.get_or_create(
                nombre=row['Docente'],
                experiencia=row['Experiencia'],
                formacion=row['Formacion'],
                especialidad=row['Especialidad'],
                disponibilidad=row['Disponibilidad']
            )

            # Asignar docente a materia (si es necesario, dependiendo de la lógica de tu aplicación)
            # Ejemplo: docente.materia = materia

        return HttpResponse("Datos cargados exitosamente desde el Excel.")

    return render(request, 'migration_excel.html', {'form': CargarExcelForm()})
