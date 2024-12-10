from anytree import Node, RenderTree
from academico import utils as utils_academico


def arbol_sintaxis_profesores(datos_profesores):
    # Estructura de materias con sus preguntas
    materias_preguntas = utils_academico.arreglo_materias()

    resultados = []
    for datos in datos_profesores:
        # Crear el nodo raíz del árbol para cada profesor
        raiz = Node(f"Evaluación del Profesor: {datos['profesor__nombre']}")

        for materia, preguntas in materias_preguntas.items():
            nodo_materia = Node(materia, parent=raiz)
            valores_preguntas = []

            for pregunta in preguntas:
                if pregunta in datos:  # Verificar si la pregunta está en los datos
                    valor_pregunta = datos[pregunta]
                    valores_preguntas.append(valor_pregunta)
                    Node(f"{pregunta}: {valor_pregunta}", parent=nodo_materia, value=valor_pregunta)

            # Calcular el puntaje promedio para la materia
            if valores_preguntas:
                puntaje_materia = sum(valores_preguntas) / len(valores_preguntas)
            else:
                puntaje_materia = 0  # Si no hay preguntas, el puntaje es 0

            # Guardar el resultado por materia
            resultados.append({
                'profesor': datos['profesor__nombre'],
                'materia': materia,
                'puntaje': puntaje_materia,
                'probabilidad': round((puntaje_materia / 5) * 100, 2)
            })

    return resultados