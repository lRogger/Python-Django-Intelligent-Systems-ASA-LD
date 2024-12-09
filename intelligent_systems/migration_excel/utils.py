import pandas as pd
from academico.models import Profesor, Estudiante, EncuestaProfesor, EncuestaEstudiante

def cargar_encuesta_profesores_desde_excel(archivo):
    data = pd.read_excel(archivo)
    for _, row in data.iterrows():
        profesor, _ = Profesor.objects.get_or_create(nombre=row['Como se llama usted?'])

        

        proceso_software_procesos_software = row['Experiencia en la implementación de procesos de software, como Scrum, Waterfall, o DevOps. ']
        proceso_software_procesos_software = (
            normalize_likert(proceso_software_procesos_software, 0, 10)  # Normaliza si es numérico
            if isinstance(proceso_software_procesos_software, (int, float))
            else likert_mapping.get(proceso_software_procesos_software, 3)  # Mapea si es texto; por defecto 3
        )

        EncuestaProfesor.objects.create(
            profesor=profesor,
            # rango_edad=row['Rango de edad al que pertenece'],
            # nivel_educacion=row['¿Cuál es su nivel de educación?'],
            # titulo_relacionado=row['¿Su titulo profesional esta relacionado con el área de enseñanza que imparte?'],
            # cursos_pedagogicos=row['¿Ha tomado cursos de capacitación pedagógica?'],
            # reconocimientos_academicos=row['¿Ha recibido algún reconocimiento académico en su carrera docente?'],
        

            # ? Proceso de Software
            proceso_software_procesos_software=row['Experiencia en la implementación de procesos de software, como Scrum, Waterfall, o DevOps.'],
            proceso_software_normativas_internacionales=row['Conocimiento en normativas y estándares internacionales de procesos de software (CMMI, ISO 9001, etc.).'],
            proceso_software_publicaciones_investigacion=row['Publicaciones o trabajos de investigación en temas relacionados con la mejora de procesos de software.'],
        )


def cargar_encuesta_estudiantes_desde_excel(archivo):
    data = pd.read_excel(archivo)
    for _, row in data.iterrows():
        estudiante, _ = Estudiante.objects.get_or_create(nombre=row['estudiante'])
        EncuestaEstudiante.objects.create(
            estudiante=estudiante,
            preguntas={
                'pregunta_1': row['pregunta_1'],
                'pregunta_2': row['pregunta_2'],
                'pregunta_3': row['pregunta_3'],
                # Agrega más preguntas según las columnas del Excel
            }
        )

def normalize_likert(value, original_min, original_max):
    return 1 + 4 * (value - original_min) / (original_max - original_min)

likert_mapping = {
    # ! 1
    "Muy malo": 1,
    "Muy bajo": 1,
    "Muy poco": 1,
    "Nunca": 1,
    "Ninguna": 1,
    "Totalmente en desacuerdo": 1,
    # ! 2
    "Malo": 2,
    "Bajo": 2,
    "Poco": 2,
    "Poca": 2,
    "Casi nunca": 2,
    "Rara vez": 2,
    "En desacuerdo": 2,
    # ! 3
    "Regular": 3,
    "Moderado": 3,
    "Moderada": 3,
    "Moderadamente": 3,
    "Neutral": 3,
    "Aveces": 3,
    "A veces": 3,
    # ! 4
    "Bueno": 4,
    "Buena": 4,
    "Alto": 4,
    "Alta": 4,
    "Prepado": 4,
    "Casi siempre": 4,
    "Frecuentemente": 4,
    "Competente": 4,
    "Familiarizado": 4,
    "Bastante": 4,
    "De acuerdo": 4,
    # ! 5
    "Excelente": 5,
    "Muy buena": 5,
    "Muy bueno": 5,
    "Muy alto": 5,
    "Muy alta": 5,
    "Muy preparado": 5,
    "Siempre": 5,
    "Muy competente": 5,
    "Muy familiarizado": 5,
    "Totalmente de acuerdo": 5,
}