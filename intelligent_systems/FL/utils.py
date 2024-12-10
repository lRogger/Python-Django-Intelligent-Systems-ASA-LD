import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def logica_difusa_profesores(datos_profesores):
    # Variables difusas
    conocimiento = ctrl.Antecedent(np.arange(1, 6, 1), 'conocimiento')
    experiencia = ctrl.Antecedent(np.arange(1, 6, 1), 'experiencia')
    probabilidad = ctrl.Consequent(np.arange(1, 6, 1), 'probabilidad')

    # Membership functions
    conocimiento.automf(3)  # Bajo, medio, alto
    experiencia.automf(3)
    probabilidad['baja'] = fuzz.trimf(probabilidad.universe, [1, 1, 3])
    probabilidad['media'] = fuzz.trimf(probabilidad.universe, [2, 3, 4])
    probabilidad['alta'] = fuzz.trimf(probabilidad.universe, [3, 5, 5])

    # Reglas
    rule1 = ctrl.Rule(conocimiento['poor'] & experiencia['poor'], probabilidad['baja'])
    rule2 = ctrl.Rule(conocimiento['average'] & experiencia['average'], probabilidad['media'])
    rule3 = ctrl.Rule(conocimiento['good'] & experiencia['good'], probabilidad['alta'])

    # Controlador
    control = ctrl.ControlSystem([rule1, rule2, rule3])
    simulador = ctrl.ControlSystemSimulation(control)

    resultados = []

    # Define las materias y sus preguntas asociadas
    materias = {
        'Introducción a la Ingeniería de Software': [
            'introduccion_pregunta_1', 'introduccion_pregunta_2', 'introduccion_pregunta_3'
        ],
        'Proceso de Software': [
            'proceso_software_pregunta_1', 'proceso_software_pregunta_2', 'proceso_software_pregunta_3'
        ],
        'Ingeniería de Requerimientos': [
            'ing_requerimientos_pregunta_1', 'ing_requerimientos_pregunta_2', 'ing_requerimientos_pregunta_3'
        ],
        'Modelamiento de Software': [
            'model_software_pregunta_1', 'model_software_pregunta_2', 'model_software_pregunta_3',
        ],
        'Diseño y arquitectura de Software': [
            'dise_arqui_software_pregunta_1', 'dise_arqui_software_pregunta_2', 'dise_arqui_software_pregunta_3',
        ],
        'Interacción Hombre-maquina': [
            'hombre_maquina_pregunta_1', 'hombre_maquina_pregunta_2', 'hombre_maquina_pregunta_3',
        ],
        'Construccion de Software': [
            'construccion_software_pregunta_1', 'construccion_software_pregunta_2', 'construccion_software_pregunta_3',
        ],
        'Diseño y experiencia de Usuario': [
            'experiencia_usuario_pregunta_1', 'experiencia_usuario_pregunta_2', 'experiencia_usuario_pregunta_3',
        ],
        'Calidad de Software': [
            'calidad_software_pregunta_1', 'calidad_software_pregunta_2', 'calidad_software_pregunta_3',
        ],
        'Verificación y validacion de Software': [
            'validacion_software_pregunta_1', 'validacion_software_pregunta_2', 'validacion_software_pregunta_3',
        ],
        'Gestion de la configuración del Software': [
            'configuracion_software_pregunta_1', 'configuracion_software_pregunta_2', 'configuracion_software_pregunta_3',
        ],
        'Auditoria de Software': [
            'auditoria_software_pregunta_1', 'auditoria_software_pregunta_2', 'auditoria_software_pregunta_3',
        ],
    }

    for datos in datos_profesores:
        for materia, preguntas in materias.items():
            # Obtén las respuestas asociadas a la materia
            respuestas = [datos[p] for p in preguntas]

            # Calcula el promedio de las respuestas
            promedio_respuestas = np.mean(respuestas)

            # Simulación para esta materia
            simulador.input['conocimiento'] = promedio_respuestas
            simulador.input['experiencia'] = promedio_respuestas  # Puedes ajustar esto si experiencia tiene otra lógica

            simulador.compute()

            resultados.append({
                'profesor': datos['profesor__nombre'],
                'materia': materia,
                'probabilidad': round(((simulador.output['probabilidad'] - 1) / 4) * 100, 2),
                'probabilidad_escala_original': float(simulador.output['probabilidad']),
            })

    return resultados


def obtener_resultados(request):
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