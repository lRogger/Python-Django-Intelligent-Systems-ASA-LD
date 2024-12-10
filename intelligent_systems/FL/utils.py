import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def logica_difusa(datos_profesores):
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
    for datos in datos_profesores:
        # Actualiza los cálculos para incluir más preguntas en las variables difusas
        preguntas_conocimiento = [
            datos['introduccion_pregunta_1'], datos['introduccion_pregunta_2'], datos['introduccion_pregunta_3'],
            datos['proceso_software_pregunta_1'], datos['proceso_software_pregunta_2']
        ]
        preguntas_experiencia = [
            datos['proceso_software_pregunta_3'], datos['ing_requerimientos_pregunta_1'], 
            datos['ing_requerimientos_pregunta_2'], datos['ing_requerimientos_pregunta_3']
        ]

        # Promedio de preguntas
        simulador.input['conocimiento'] = np.mean(preguntas_conocimiento)
        simulador.input['experiencia'] = np.mean(preguntas_experiencia)

        # Ejecutar simulación
        simulador.compute()
        resultados.append({
            'profesor': datos['profesor__nombre'],
            'materia': 'Introducción a la Ingeniería de Software',  # Cambiar dinámicamente si es necesario
            'probabilidad': simulador.output['probabilidad']
        })

    return resultados
