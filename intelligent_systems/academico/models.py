from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)


    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    carrera = models.CharField(max_length=255)
    semestre = models.IntegerField()

    def __str__(self):
        return self.nombre


class EncuestaProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre_profesor = models.CharField(max_length=50)
    rango_edad = models.CharField(max_length=50)
    nivel_educacion = models.CharField(max_length=50)
    titulo_relacionado = models.PositiveIntegerField(default=1)  # 1-5
    cursos_pedagogicos = models.BooleanField()
    reconocimientos_academicos = models.BooleanField()
    preferencias_asignaturas = models.TextField()  
    metodologias_ensenanza = models.TextField()
    acepta_sistema_recomendacion = models.PositiveIntegerField(default=1)  # 1-5
    materias_impartidas = models.TextField()
    veces_impartidas = models.PositiveIntegerField(default=0)
    materias_no_relacionadas = models.PositiveIntegerField(default=1)  # 1-5
    desacuerdo_con_materias = models.PositiveIntegerField(default=1)  # 1-5
    conoce_sistemas_recomendacion = models.PositiveIntegerField(default=1)  # 1-5
    cree_en_sistemas_recomendacion = models.PositiveIntegerField(default=1)  # 1-5
    acepta_implementacion = models.PositiveIntegerField(default=1)  # 1-5

    # ! Preguntas relacionadas a experiencia en materias
    # ? Introducción a la ingenieria de Software
    introduccion_experiencia_software = models.PositiveIntegerField(default=1)  # 1-5
    introduccion_familiaridad_conceptos_basicos = models.PositiveIntegerField(default=1)  # 1-5
    introduccion_grado_academico_software = models.TextField()
    introduccion_certificados_agiles = models.TextField()
    # ? Proceso de Software
    proceso_software_introduccion_resolucion_problemas = models.PositiveIntegerField(default=1)  # 1-5
    proceso_software_procesos_software = models.PositiveIntegerField(default=1)  # 1-5
    proceso_software_normativas_internacionales = models.PositiveIntegerField(default=1)  # 1-5
    proceso_software_publicaciones_investigacion = models.PositiveIntegerField(default=1)  # 1-5
    # ? Ingenieria de Requerimientos
    ing_requerimientos_participacion_proyectos = models.PositiveIntegerField(default=1)  # 1-5
    ing_requerimientos_tecnicas_requerimientos = models.PositiveIntegerField(default=1)  # 1-5
    ing_requerimientos_interaccion_equipos = models.PositiveIntegerField(default=1)  # 1-5
    # ? Modelamiento de Software
    model_software_familiaridad_uml = models.PositiveIntegerField(default=1)  # 1-5
    model_software_herramientas_diseno = models.PositiveIntegerField(default=1)  # 1-5
    model_software_modelado_proyectos = models.PositiveIntegerField(default=1)  # 1-5
    # ? Diseño y arquitectura de Software
    dise_arqui_software_diseno_arquitecturas = models.PositiveIntegerField(default=1)  # 1-5
    dise_arqui_software_patrones_arquitectura = models.PositiveIntegerField(default=1)  # 1-5
    dise_arqui_software_elegir_arquitecturas = models.PositiveIntegerField(default=1)  # 1-5
    # ? Interacción Hombre-maquina
    hombre_maquina_diseno_gui = models.PositiveIntegerField(default=1)  # 1-5
    hombre_maquina_principios_usabilidad = models.PositiveIntegerField(default=1)  # 1-5
    hombre_maquina_herramientas_gui = models.PositiveIntegerField(default=1)  # 1-5
    # ? Construccion de Software
    construccion_software_experiencia_lenguajes = models.PositiveIntegerField(default=1)  # 1-5
    construccion_software_metodologias_agiles = models.PositiveIntegerField(default=1)  # 1-5
    construccion_software_buenas_practicas = models.PositiveIntegerField(default=1)  # 1-5
    # ? Diseño y experiencia de Usuario
    experiencia_usuario_diseno_interfaces = models.PositiveIntegerField(default=1)  # 1-5
    experiencia_usuario_pruebas_usabilidad = models.PositiveIntegerField(default=1)  # 1-5
    experiencia_usuario_psicologia_cognitiva = models.PositiveIntegerField(default=1)  # 1-5
    # ? Calidad de Software
    calidad_software_pruebas_software = models.PositiveIntegerField(default=1)  # 1-5
    calidad_software_automatizacion_pruebas = models.PositiveIntegerField(default=1)  # 1-5
    calidad_software_modelos_calidad = models.PositiveIntegerField(default=1)  # 1-5
    # ? Verificación y validacion de Software
    validacion_software_control_versiones = models.PositiveIntegerField(default=1)  # 1-5
    validacion_software_integracion_continua = models.PositiveIntegerField(default=1)  # 1-5
    validacion_software_herramientas_configuracion = models.PositiveIntegerField(default=1)  # 1-5
    # ? Auditoria de Software
    auditoria_software_normativas_auditoria = models.PositiveIntegerField(default=1)  # 1-5
    auditoria_software_auditorias_software = models.PositiveIntegerField(default=1)  # 1-5
    auditoria_software_analisis_critico = models.PositiveIntegerField(default=1)  # 1-5

    def __str__(self):
        return f"Encuesta de {self.profesor.nombre}"


class EncuestaEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    preguntas = models.JSONField()  # Guarda respuestas de la encuesta

    def __str__(self):
        return f"Encuesta de {self.estudiante.nombre}"
