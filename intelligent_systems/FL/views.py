from django.shortcuts import render
from django.http import JsonResponse
from .utils import logica_difusa_profesores
from academico import utils as utils_academico

# Create your views here.
def migration_FL_View(request):
    return render(request, 'migration_FL.html', {})



def obtener_resultados_FL_profesores(request):
    # Recuperar el id desde los query parameters
    profesor_id = request.GET.get('id')

    if profesor_id is None:
        return JsonResponse({'error': 'El parámetro id es obligatorio.'}, status=400)

    try:
        # Convertir a entero si es necesario
        profesor_id = int(profesor_id)
    except ValueError:
        return JsonResponse({'error': 'El parámetro id debe ser un número válido.'}, status=400)

    # Obtener los datos del profesor específico
    datos_profesores = utils_academico.obtener_datos_encuestas(profesor_id=profesor_id)

    if not datos_profesores:
        return JsonResponse({'error': f'No se encontraron datos para el profesor con id {profesor_id}.'}, status=404)

    # Procesar con la lógica difusa
    resultados = logica_difusa_profesores(datos_profesores)

    return JsonResponse(resultados, safe=False)

