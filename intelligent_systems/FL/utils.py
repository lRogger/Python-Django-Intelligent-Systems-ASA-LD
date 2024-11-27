import skfuzzy as fuzz
import numpy as np

class FLRecomendacion:
    def __init__(self):
        # Universos de discurso adaptados a Likert (1-5)
        self.likert = np.arange(1, 6, 1)  # Escala Likert 1-5
        self.resultado = np.arange(0, 101, 1)  # Resultado final (0-100)

        # Funciones de membresía
        self.bajo = fuzz.trimf(self.likert, [1, 1, 3])
        self.medio = fuzz.trimf(self.likert, [2, 3, 4])
        self.alto = fuzz.trimf(self.likert, [3, 5, 5])
        self.res_bajo = fuzz.trimf(self.resultado, [0, 0, 50])
        self.res_alto = fuzz.trimf(self.resultado, [50, 100, 100])

    def evaluar(self, experiencia, familiaridad, interaccion):
        # Fuzzificación
        exp_baja = fuzz.interp_membership(self.likert, self.bajo, experiencia)
        exp_media = fuzz.interp_membership(self.likert, self.medio, experiencia)
        exp_alta = fuzz.interp_membership(self.likert, self.alto, experiencia)

        fam_baja = fuzz.interp_membership(self.likert, self.bajo, familiaridad)
        fam_media = fuzz.interp_membership(self.likert, self.medio, familiaridad)
        fam_alta = fuzz.interp_membership(self.likert, self.alto, familiaridad)

        int_baja = fuzz.interp_membership(self.likert, self.bajo, interaccion)
        int_media = fuzz.interp_membership(self.likert, self.medio, interaccion)
        int_alta = fuzz.interp_membership(self.likert, self.alto, interaccion)

        # Reglas difusas
        activacion_baja = np.fmax(exp_baja, np.fmax(fam_baja, int_baja))
        activacion_alta = np.fmax(exp_alta, np.fmax(fam_alta, int_alta))

        # Agregación
        agregado = np.fmax(activacion_baja, activacion_alta)

        # Defuzzificación
        resultado = fuzz.defuzz(self.resultado, agregado, 'centroid')
        return resultado
