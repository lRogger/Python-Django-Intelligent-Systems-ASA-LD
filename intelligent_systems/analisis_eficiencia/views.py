from django.shortcuts import render
from academico import utils as utils_academico
from django.http import JsonResponse
from django.contrib import messages
from AST.utils import arbol_sintaxis_profesores, arbol_sintaxis_estudiantes
from FL.utils import logica_difusa_profesores, logica_difusa_estudiantes

# from intelligent_systems.academico import urls as utils_academico

# Create your views here.
def analisis_Eficiencia_View(request):
    return render(request, 'analisis_comparativo.html', {})

def lista_docentes_asignados_View(request):
    return render(request, 'docentes_asignados.html', {})

def obtener_resultados_encuesta_estudiantes(request):
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
    datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes(profesor_id=profesor_id)

    if not datos_estudiantes:
        return JsonResponse({'error': f'No se encontraron datos para el profesor con id {profesor_id}.'}, status=404)

    # Procesar datos
    resultadosAST = arbol_sintaxis_estudiantes(datos_estudiantes)
    resultadosFL = logica_difusa_estudiantes(datos_estudiantes)

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


def obtener_resultados_asignacion_docentes(request):
    try:
        datos_profesores = utils_academico.obtener_datos_encuestas()
        datos_estudiantes = utils_academico.obtener_datos_encuestas_estudiantes()
        ast_estudiantes = arbol_sintaxis_estudiantes(datos_estudiantes)
        fl_estudiantes = logica_difusa_estudiantes(datos_estudiantes)
        ast_profesores = arbol_sintaxis_profesores(datos_profesores)
        fl_profesores = logica_difusa_profesores(datos_profesores)
        resultados = asignacion_docentes(ast_profesores, fl_profesores, ast_estudiantes, fl_estudiantes)
        return JsonResponse(resultados, safe=False)
    except Exception as e:
        messages.error(request, str(e))

    


def asignacion_docentes(ast_profesores, fl_profesores, ast_estudiantes, fl_estudiantes):

    # Calcular compatibilidad por algoritmo
    compatibilidad = calcular_compatibilidad_por_algoritmo(ast_profesores, fl_profesores)

    # Combinar los resultados de AST y FL por materia y profesor
    combinados = []

    def buscar_puntaje(lista, profesor, materia):
        # Busca el puntaje en la lista dada por profesor y materia
        for item in lista:
            if item['profesor'] == profesor and item['materia'] == materia:
                return item['probabilidad']
        return 0  # Retorna 0 si no encuentra coincidencia

    # Generar una lista combinada
    for item_ast_prof in ast_profesores:
        profesor = item_ast_prof['profesor']
        materia = item_ast_prof['materia']
        puntaje_ast_prof = item_ast_prof['probabilidad']
        puntaje_fl_prof = buscar_puntaje(fl_profesores, profesor, materia)
        puntaje_ast_est = buscar_puntaje(ast_estudiantes, profesor, materia)
        puntaje_fl_est = buscar_puntaje(fl_estudiantes, profesor, materia)

        # Calcular promedios por algoritmo
        promedio_ast = (puntaje_ast_prof + puntaje_ast_est) / 2
        promedio_fl = (puntaje_fl_prof + puntaje_fl_est) / 2

        # Calcular el puntaje promedio general ponderado
        puntaje_promedio = (0.5 * promedio_ast + 0.5 * promedio_fl)

        puntaje_promedio_ponderado = (0.4 * puntaje_ast_prof + 0.3 * puntaje_fl_prof +
                            0.2 * puntaje_ast_est + 0.1 * puntaje_fl_est)

        combinados.append({
            'profesor': profesor,
            'materia': materia,
            'puntaje_promedio': round(puntaje_promedio, 2),
            'promedio_ast': round(promedio_ast, 2),
            'promedio_fl': round(promedio_fl, 2)
        })

    # Ordenar los combinados por puntaje promedio de mayor a menor
    combinados = sorted(combinados, key=lambda x: x['puntaje_promedio'], reverse=True)

    # Asignar docentes a materias
    materias_asignadas = set()
    profesores_asignados = set()
    asignaciones = []

    for item in combinados:
        profesor = item['profesor']
        materia = item['materia']

        # Asignar solo si el profesor y la materia no han sido asignados aún
        if profesor not in profesores_asignados and materia not in materias_asignadas:
            asignaciones.append({
                'profesor': profesor,
                'materia': materia,
                'puntaje_promedio': item['puntaje_promedio'],
                'promedio_ast': item['promedio_ast'],
                'promedio_fl': item['promedio_fl']
            })
            profesores_asignados.add(profesor)
            materias_asignadas.add(materia)

    return asignaciones


def calcular_compatibilidad_por_algoritmo(resultados_ast, resultados_fl):
    # Agrupa resultados por algoritmo
    compatibilidad_ast = {}
    compatibilidad_fl = {}

    # Sumar los puntajes por profesor y materia en cada algoritmo
    for item in resultados_ast:
        clave = f"{item['profesor']} - {item['materia']}"
        compatibilidad_ast[clave] = item['probabilidad']

    for item in resultados_fl:
        clave = f"{item['profesor']} - {item['materia']}"
        compatibilidad_fl[clave] = item['probabilidad']

    return {
        "compatibilidad_ast": compatibilidad_ast,
        "compatibilidad_fl": compatibilidad_fl
    }
