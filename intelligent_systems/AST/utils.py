class ASTRecomendacion:
    def __init__(self, profesores):
        self.profesores = profesores

    def evaluar_docente(self, docente):
        puntuacion = 0

        # Asignar pesos a métricas importantes (ajustables según el caso)
        pesos = {
            'experiencia_software': 10,
            'familiaridad_conceptos_basicos': 8,
            'normativas_internacionales': 5,
            'certificados_agiles': 7,
            'publicaciones_investigacion': 6,
            'interaccion_equipos': 8,
        }

        # Sumar puntuación basada en pesos
        puntuacion += docente.experiencia_software * pesos['experiencia_software']
        puntuacion += docente.familiaridad_conceptos_basicos * pesos['familiaridad_conceptos_basicos']
        puntuacion += docente.normativas_internacionales * pesos['normativas_internacionales']
        puntuacion += docente.certificados_agiles * pesos['certificados_agiles']
        puntuacion += docente.publicaciones_investigacion * pesos['publicaciones_investigacion']
        puntuacion += docente.interaccion_equipos * pesos['interaccion_equipos']

        return puntuacion

    def recomendar(self):
        evaluaciones = [
            (docente, self.evaluar_docente(docente))
            for docente in self.profesores
        ]
        return sorted(evaluaciones, key=lambda x: x[1], reverse=True)
