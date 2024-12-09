import pandas as pd
from academico.models import Profesor, Estudiante, EncuestaProfesor, EncuestaEstudiante

def cargar_encuesta_profesores_desde_excel(archivo):
    data = pd.read_excel(archivo)
    for _, row in data.iterrows():
        profesor, _ = Profesor.objects.get_or_create(nombre=row['Como se llama usted?'])

        introduccion_pregunta_1=normalizar_respuesta(row['¿Cómo calificaría su familiaridad con los principios básicos de la ingeniería de software, incluyendo el ciclo de vida del software, procesos y modelos?'])
        introduccion_pregunta_2=normalizar_respuesta(row['¿Qué tan preparado se siente para impartir la materia de Introducción a Ingeniería de Software, considerando su experiencia y conocimientos en el área?'])
        introduccion_pregunta_3=normalizar_respuesta(row['¿Qué tan familiarizado se siente con el proceso de resolución de problemas, incluyendo la identificación de datos de entrada, procesos y salidas?'])

        proceso_software_pregunta_1=normalizar_respuesta(row['¿Cómo calificaría su experiencia en la implementación de procesos de software, como Scrum, Waterfall o DevOps?'])
        proceso_software_pregunta_2=normalizar_respuesta(row['¿Cómo calificaría su conocimiento sobre normativas y estándares internacionales de procesos de software (como CMMI, ISO 9001, etc.)?'])
        proceso_software_pregunta_3=normalizar_respuesta(row['¿Con qué frecuencia ha realizado publicaciones o trabajos de investigación en temas relacionados con la mejora de procesos de software?'])

        ing_requerimientos_pregunta_1=normalizar_respuesta(row['¿Qué tan frecuentemente ha participado en proyectos donde se han identificado y documentado requerimientos?'])
        ing_requerimientos_pregunta_2=normalizar_respuesta(row['¿Qué tan competente se siente en el uso de técnicas como entrevistas, encuestas y análisis de stakeholders para la recopilación de información?"'])
        ing_requerimientos_pregunta_3=normalizar_respuesta(row['¿Qué tan hábil se considera al interactuar con clientes y equipos multidisciplinarios para comprender y definir requerimientos?'])

        model_software_pregunta_1=normalizar_respuesta(row['¿Qué tan familiarizado se siente con el uso de UML, BPMN u otras herramientas similares para la modelación de procesos y requerimientos?'])
        model_software_pregunta_2=normalizar_respuesta(row['¿Cuál es su nivel de experiencia en el uso de herramientas de diseño y modelado, como Enterprise Architect, Visual Paradigm, entre otras?'])
        model_software_pregunta_3=normalizar_respuesta(row['¿Qué tan frecuentemente ha participado en proyectos de modelado de software a gran escala o que involucren arquitecturas complejas?'])

        dise_arqui_software_pregunta_1=normalizar_respuesta(row['¿Cuál es su nivel de experiencia en el diseño de arquitecturas de software en proyectos reales, incluyendo arquitecturas monolíticas, distribuidas y de microservicios?'])
        dise_arqui_software_pregunta_2=normalizar_respuesta(row['¿Qué tan familiarizado está con patrones de arquitectura de software, como MVC, MVVM, Singleton, entre otros?'])
        dise_arqui_software_pregunta_3=normalizar_respuesta(row['¿Qué tan preparado se siente para enseñar sobre la selección de arquitecturas de software adecuadas, considerando los requerimientos del sistema y las limitaciones del entorno?'])

        hombre_maquina_pregunta_1=normalizar_respuesta(row['¿Se siente capacitado para impartir una materia sobre diseño de interfaces gráficas de usuario (GUI) y experiencia de usuario (UX) basada en su experiencia y conocimientos en estas áreas?'])
        hombre_maquina_pregunta_2=normalizar_respuesta(row['¿Usted posee conocimiento en principios de usabilidad, accesibilidad y diseño centrado en el usuario?'])
        hombre_maquina_pregunta_3=normalizar_respuesta(row['¿Qué tan preparado consideras que está el docente para impartir clases sobre el uso de herramientas de diseño como Sketch, Figma y Adobe XD?'])

        construccion_software_pregunta_1=normalizar_respuesta(row['¿Qué tan cómodo te sientes impartiendo clases sobre desarrollo de software utilizando diversas tecnologías y lenguajes de programación?'])
        construccion_software_pregunta_2=normalizar_respuesta(row['¿Cuál es tu nivel de conocimiento y experiencia en el trabajo con metodologías ágiles como Scrum, Kanban u otras?'])
        construccion_software_pregunta_3=normalizar_respuesta(row['¿Cómo evaluarías tu capacidad para aplicar buenas prácticas de desarrollo, como el uso de patrones de diseño, principios SOLID y el refactoring?'])

        experiencia_usuario_pregunta_1=normalizar_respuesta(row['¿Cómo calificarías tu experiencia en el diseño de interfaces que favorezcan la experiencia del usuario?'])
        experiencia_usuario_pregunta_2=normalizar_respuesta(row['¿Cómo evaluarías tu capacidad para realizar pruebas de usabilidad, llevar a cabo entrevistas con usuarios y analizar datos relacionados con la experiencia del usuario?'])
        experiencia_usuario_pregunta_3=normalizar_respuesta(row['¿Cómo calificarías tu capacidad para evaluar y aplicar buenas prácticas de desarrollo, tales como el uso de patrones de diseño, la implementación de los principios SOLID y la realización de refactoring en tus proyectos?'])

        configuracion_software_pregunta_1=normalizar_respuesta(row['¿Considera que su experiencia profesional facilita la enseñanza de herramientas de control de versiones?'])
        configuracion_software_pregunta_2=normalizar_respuesta(row['¿Cree que su experiencia laboral ayuda a explicar la importancia de la gestión de cambios en proyectos reales?'])
        configuracion_software_pregunta_3=normalizar_respuesta(row['¿Piensa que sus conocimientos prácticos mejoran la comprensión de los estudiantes sobre la gestión de la configuración?'])

        calidad_software_pregunta_1=normalizar_respuesta(row['¿Cómo calificarías tu conocimiento y experiencia en la implementación de pruebas de software, incluyendo pruebas unitarias, de integración, de sistema y de aceptación?'])
        calidad_software_pregunta_2=normalizar_respuesta(row['¿Cuál es tu nivel de familiaridad con herramientas de automatización de pruebas, como Selenium, JUnit, TestNG, entre otras?'])
        calidad_software_pregunta_3=normalizar_respuesta(row['¿Cuál es tu nivel de conocimiento sobre modelos de calidad de software, como TMMi (Test Maturity Model integration) o ISO/IEC 25010?'])

        validacion_software_pregunta_1=normalizar_respuesta(row['¿Cuál es tu nivel de dominio en el uso de herramientas de control de versiones, como Git, SVN, entre otras?'])
        validacion_software_pregunta_2=normalizar_respuesta(row['Cuál es tu nivel de familiaridad con herramientas de integración continua y despliegue, como Jenkins, GitLab CI, CircleCI, entre otras?'])
        validacion_software_pregunta_3=normalizar_respuesta(row['¿Cuál es tu nivel de experiencia con herramientas de automatización y gestión de configuración, como Ansible, Puppet, Chef, entre otras?'])

        auditoria_software_pregunta_1=normalizar_respuesta(row['¿Cuál es tu nivel de familiaridad con normativas internacionales y procesos de auditoría de software, como ISO/IEC 27001, CMMI, ITIL, entre otras?'])
        auditoria_software_pregunta_2=normalizar_respuesta(row['¿Cuál es tu nivel de experiencia en la realización de auditorías de código, documentación y procesos de desarrollo de software?'])
        auditoria_software_pregunta_3=normalizar_respuesta(row['¿Cómo evaluarías tu capacidad de análisis crítico y detección de posibles fallos o inconsistencias en el proceso de desarrollo de software?'])
        # proceso_software_procesos_software = row['Experiencia en la implementación de procesos de software, como Scrum, Waterfall, o DevOps. ']
        # proceso_software_procesos_software = (
        #     normalize_likert(proceso_software_procesos_software, 0, 10)  # Normaliza si es numérico
        #     if isinstance(proceso_software_procesos_software, (int, float))
        #     else likert_mapping.get(proceso_software_procesos_software, 3)  # Mapea si es texto; por defecto 3
        # )

        EncuestaProfesor.objects.create(
            profesor=profesor,
            # rango_edad=row['Rango de edad al que pertenece'],
            # nivel_educacion=row['¿Cuál es su nivel de educación?'],
            # titulo_relacionado=row['¿Su titulo profesional esta relacionado con el área de enseñanza que imparte?'],
            # cursos_pedagogicos=row['¿Ha tomado cursos de capacitación pedagógica?'],
            # reconocimientos_academicos=row['¿Ha recibido algún reconocimiento académico en su carrera docente?'],
            # ? Introducción a la ingenieria de Software
            introduccion_pregunta_1=introduccion_pregunta_1,
            introduccion_pregunta_2=introduccion_pregunta_2,
            introduccion_pregunta_3=introduccion_pregunta_3,
            # ? Proceso de Software
            proceso_software_pregunta_1=proceso_software_pregunta_1,
            proceso_software_pregunta_2=proceso_software_pregunta_2,
            proceso_software_pregunta_3=proceso_software_pregunta_3,
            # ? Ingenieria de Requerimientos
            ing_requerimientos_pregunta_1=ing_requerimientos_pregunta_1,
            ing_requerimientos_pregunta_2=ing_requerimientos_pregunta_2,
            ing_requerimientos_pregunta_3=ing_requerimientos_pregunta_3,
            # ? Modelamiento de Software
            model_software_pregunta_1=model_software_pregunta_1,
            model_software_pregunta_2=model_software_pregunta_2,
            model_software_pregunta_3=model_software_pregunta_3,
            # ? Diseño y arquitectura de Software
            dise_arqui_software_pregunta_1=dise_arqui_software_pregunta_1,
            dise_arqui_software_pregunta_2=dise_arqui_software_pregunta_2,
            dise_arqui_software_pregunta_3=dise_arqui_software_pregunta_3,
            # ? Interacción Hombre-maquina
            hombre_maquina_pregunta_1=hombre_maquina_pregunta_1,
            hombre_maquina_pregunta_2=hombre_maquina_pregunta_2,
            hombre_maquina_pregunta_3=hombre_maquina_pregunta_3,
            # ? Construccion de Software
            construccion_software_pregunta_1=construccion_software_pregunta_1,
            construccion_software_pregunta_2=construccion_software_pregunta_2,
            construccion_software_pregunta_3=construccion_software_pregunta_3,
            # ? Diseño y experiencia de Usuario
            experiencia_usuario_pregunta_1=experiencia_usuario_pregunta_1,
            experiencia_usuario_pregunta_2=experiencia_usuario_pregunta_2,
            experiencia_usuario_pregunta_3=experiencia_usuario_pregunta_3,
            # ? Calidad de Software
            calidad_software_pregunta_1=calidad_software_pregunta_1,
            calidad_software_pregunta_2=calidad_software_pregunta_2,
            calidad_software_pregunta_3=calidad_software_pregunta_3,
            # ? Verificación y validacion de Software
            validacion_software_pregunta_1=validacion_software_pregunta_1,
            validacion_software_pregunta_2=validacion_software_pregunta_2,
            validacion_software_pregunta_3=validacion_software_pregunta_3,
            # ? Gestion de la configuración del Software
            configuracion_software_pregunta_1=configuracion_software_pregunta_1,
            configuracion_software_pregunta_2=configuracion_software_pregunta_2,
            configuracion_software_pregunta_3=configuracion_software_pregunta_3,
            # ? Auditoria de Software
            auditoria_software_pregunta_1=auditoria_software_pregunta_1,
            auditoria_software_pregunta_2=auditoria_software_pregunta_2,
            auditoria_software_pregunta_3=auditoria_software_pregunta_3,
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

def normalizar_respuesta(respuesta):
    """Normaliza la respuesta según su tipo (numérico o texto)."""
    if isinstance(respuesta, (int, float)):
        return normalize_likert(respuesta, 0, 10)  # Normaliza si es numérico
    return likert_mapping.get(respuesta, 3)  # Mapea si es texto; por defecto 3


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