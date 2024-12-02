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
    # profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre_profesor = models.CharField(max_length=50)
    rango_edad = models.CharField(max_length=50)
    nivel_educacion = models.CharField(max_length=50)
    titulo_relacionado = models.BooleanField()
    cursos_pedagogicos = models.BooleanField()
    reconocimientos_academicos = models.BooleanField()
    preferencias_asignaturas = models.TextField()  
    metodologias_ensenanza = models.TextField()
    acepta_sistema_recomendacion = models.BooleanField()
    materias_impartidas = models.TextField()
    veces_impartidas = models.PositiveIntegerField(default=0)
    materias_no_relacionadas = models.BooleanField()
    desacuerdo_con_materias = models.BooleanField()
    conoce_sistemas_recomendacion = models.BooleanField()
    cree_en_sistemas_recomendacion = models.BooleanField()
    acepta_implementacion = models.BooleanField()

    # Escalas Likert (1-5)
    experiencia_software = models.PositiveIntegerField(default=1)  # 1-5
    familiaridad_conceptos_basicos = models.PositiveIntegerField(default=1)  # 1-5
    grado_academico_software = models.BooleanField()
    certificados_agiles = models.BooleanField()
    resolucion_problemas = models.PositiveIntegerField(default=1)  # 1-5
    procesos_software = models.TextField()
    normativas_internacionales = models.PositiveIntegerField(default=1)  # 1-5
    publicaciones_investigacion = models.PositiveIntegerField(default=1)  # 1-5
    participacion_proyectos = models.PositiveIntegerField(default=1)  # 1-5
    tecnicas_requerimientos = models.PositiveIntegerField(default=1)  # 1-5
    interaccion_equipos = models.PositiveIntegerField(default=1)  # 1-5
    familiaridad_uml = models.PositiveIntegerField(default=1)  # 1-5
    herramientas_diseno = models.PositiveIntegerField(default=1)  # 1-5
    modelado_proyectos = models.PositiveIntegerField(default=1)  # 1-5
    diseno_arquitecturas = models.PositiveIntegerField(default=1)  # 1-5
    patrones_arquitectura = models.PositiveIntegerField(default=1)  # 1-5
    elegir_arquitecturas = models.PositiveIntegerField(default=1)  # 1-5
    diseno_gui = models.PositiveIntegerField(default=1)  # 1-5
    principios_usabilidad = models.PositiveIntegerField(default=1)  # 1-5
    herramientas_gui = models.PositiveIntegerField(default=1)  # 1-5
    experiencia_lenguajes = models.PositiveIntegerField(default=1)  # 1-5
    metodologias_agiles = models.PositiveIntegerField(default=1)  # 1-5
    buenas_practicas = models.PositiveIntegerField(default=1)  # 1-5
    pruebas_usabilidad = models.PositiveIntegerField(default=1)  # 1-5
    psicologia_cognitiva = models.PositiveIntegerField(default=1)  # 1-5
    pruebas_software = models.PositiveIntegerField(default=1)  # 1-5
    automatizacion_pruebas = models.PositiveIntegerField(default=1)  # 1-5
    modelos_calidad = models.PositiveIntegerField(default=1)  # 1-5
    control_versiones = models.PositiveIntegerField(default=1)  # 1-5
    integracion_continua = models.PositiveIntegerField(default=1)  # 1-5
    herramientas_configuracion = models.PositiveIntegerField(default=1)  # 1-5
    normativas_auditoria = models.PositiveIntegerField(default=1)  # 1-5
    auditorias_software = models.PositiveIntegerField(default=1)  # 1-5
    analisis_critico = models.PositiveIntegerField(default=1)  # 1-5

    def __str__(self):
        return f"Encuesta de {self.profesor.nombre}"


class EncuestaEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    preguntas = models.JSONField()  # Guarda respuestas de la encuesta

    def __str__(self):
        return f"Encuesta de {self.estudiante.nombre}"
