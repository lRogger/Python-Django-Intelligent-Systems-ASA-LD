from django.db.models import Avg
from .models import EncuestaProfesor, EncuestaEstudiante

def obtener_datos_encuestas():
    # Datos de profesores (Promedio por materia)
    datos_profesores = EncuestaProfesor.objects.values(
        'id', 'profesor__nombre', 
        'introduccion_pregunta_1',
        'introduccion_pregunta_2',
        'introduccion_pregunta_3',
        'proceso_software_pregunta_1',
        'proceso_software_pregunta_2',
        'proceso_software_pregunta_3',
        'ing_requerimientos_pregunta_1',
        'ing_requerimientos_pregunta_2',
        'ing_requerimientos_pregunta_3',
        'model_software_pregunta_1',
        'model_software_pregunta_2',
        'model_software_pregunta_3',
        'dise_arqui_software_pregunta_1',
        'dise_arqui_software_pregunta_2',
        'dise_arqui_software_pregunta_3',
        'hombre_maquina_pregunta_1',
        'hombre_maquina_pregunta_2',
        'hombre_maquina_pregunta_3',
        'construccion_software_pregunta_1',
        'construccion_software_pregunta_2',
        'construccion_software_pregunta_3',
        'experiencia_usuario_pregunta_1',
        'experiencia_usuario_pregunta_2',
        'experiencia_usuario_pregunta_3',
        'calidad_software_pregunta_1',
        'calidad_software_pregunta_2',
        'calidad_software_pregunta_3',
        'validacion_software_pregunta_1',
        'validacion_software_pregunta_2',
        'validacion_software_pregunta_3',
        'configuracion_software_pregunta_1',
        'configuracion_software_pregunta_2',
        'configuracion_software_pregunta_3',
        'auditoria_software_pregunta_1',
        'auditoria_software_pregunta_2',
        'auditoria_software_pregunta_3',
        # Agregar otras materias según corresponda
    )
    
    # Datos de estudiantes (Promedio de experiencia por materia y profesor)
    # datos_estudiantes = EncuestaEstudiante.objects.values('asignatura', 'profesor').annotate(
    #     promedio_experiencia=Avg('pregunta_1')  # Ajusta esto para incluir más preguntas
    # )

# , list(datos_estudiantes)
    return list(datos_profesores)
