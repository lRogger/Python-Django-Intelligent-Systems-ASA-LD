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
    

    # Combinar los resultados de AST y FL por materia y profesor
    combinados = []

    def buscar_puntaje(lista, profesor, materia):
        # Busca el puntaje en la lista dada por profesor y materia
        promedio_probabilidad = []
        for item in lista:
            if item['profesor'] == profesor and item['materia'] == materia:
                promedio_probabilidad.append(item['probabilidad'])

        if not promedio_probabilidad:
            return 0  # Retornar un valor predeterminado
        return sum(promedio_probabilidad) / len(promedio_probabilidad)  # Retorna 0 si no encuentra coincidencia
    
    lista_materias = utils_academico.listado_materias()
    lista_profesores = utils_academico.listado_docentes()

    for materia in lista_materias:
        for profesor in lista_profesores:
            puntaje_ast_prof = buscar_puntaje(ast_profesores, profesor, materia)
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
                'puntaje_ast_prof': round(puntaje_ast_prof, 2),
                'puntaje_ast_est': round(puntaje_ast_est, 2),
                'promedio_ast': round(promedio_ast, 2),
                'promedio_fl': round(promedio_fl, 2),
                'puntaje_fl_prof': round(puntaje_fl_prof, 2),
                'puntaje_fl_est': round(puntaje_fl_est, 2),
            })

    # Ordenar los combinados por puntaje promedio de mayor a menor
    combinados = sorted(combinados, key=lambda x: x['puntaje_promedio'], reverse=True)

    # Asignar docentes a materias
    materias_asignadas = set()
    profesores_asignados = set()
    asignaciones = []

    for materia in lista_materias:
        objetos_filtrados = [obj for obj in combinados if obj["materia"] == materia]

        for objeto in objetos_filtrados:
            # Verificar si el profesor ya está asignado a otra materia
            if objeto["profesor"] in [asignacion["profesor"] for asignacion in asignaciones]:
                continue  # Saltar este profesor si ya está asignado

            # Asignar el profesor a la materia
            asignaciones.append({
                "profesor": objeto["profesor"],
                "materia": objeto["materia"],
                "puntaje_promedio": objeto["puntaje_promedio"],
                "puntaje_ast_prof": objeto["puntaje_ast_prof"],
                "puntaje_ast_est": objeto["puntaje_ast_est"],
                "promedio_ast": objeto["promedio_ast"],
                "promedio_fl": objeto["promedio_fl"],
                "puntaje_fl_prof": objeto["puntaje_fl_prof"],
                "puntaje_fl_est": objeto["puntaje_fl_est"],
            })
            break  # Detener el ciclo cuando se haya asignado la materia a un profesor disponible
    
    asignaciones = sorted(asignaciones, key=lambda x: x['puntaje_promedio'], reverse=True)

    return asignaciones


def buscar_maestro_compatible(materia, objetos, posicion):
    objetos_filtrados = [obj for obj in objetos if obj["materia"] == materia]
    objetos_ordenados = sorted(objetos_filtrados, key=lambda obj: obj["puntaje_promedio"], reverse=True)
    # Iterar sobre los objetos ordenados y asignar al primer docente disponible
    for obj in objetos_ordenados:
        # Verificar si la materia ya fue asignada al docente
        if not any(asig["docente"] == obj["docente"] and asig["materia"] == materia for asig in asignaciones):
            asignaciones.append({"docente": obj["docente"], "materia": obj["materia"], "puntaje": obj["puntaje_promedio"]})
            return obj  # Retornar el objeto asignado
    return None  # Retornar None si no hay más opciones disponibles
    return