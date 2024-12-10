from django.shortcuts import render
from academico import utils as utils_academico
from django.http import JsonResponse
from django.contrib import messages
from AST.utils import arbol_sintaxis_profesores
from FL.utils import logica_difusa_profesores

# from intelligent_systems.academico import urls as utils_academico

# Create your views here.
def analisis_Eficiencia_View(request):
    return render(request, 'analisis_comparativo.html', {})


def obtener_resultados_encuesta_profesores(request):
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

    # Procesar datos
    resultadosAST = arbol_sintaxis_profesores(datos_profesores)
    resultadosFL = logica_difusa_profesores(datos_profesores)

    top_ast = sorted(resultadosAST, key=lambda x: x['probabilidad'], reverse=True)[:3]
    top_fl = sorted(resultadosFL, key=lambda x: x['probabilidad'], reverse=True)[:3]

    for item in top_ast:
        item['algoritmo'] = 'Árbol de Sintaxis Abstracta'
    for item in top_fl:
        item['algoritmo'] = 'Lógica Difusa'


    return JsonResponse({
        'ast_values': resultadosAST,
        'fl_values': resultadosFL,
        'comparation_values': top_ast + top_fl
    }, safe=False)