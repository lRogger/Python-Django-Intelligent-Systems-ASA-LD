from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    experiencia = models.IntegerField()  # Años de experiencia
    formacion = models.CharField(max_length=100)  # Formación académica
    especialidad = models.CharField(max_length=100)  # Especialidad en un área
    disponibilidad = models.BooleanField()  # Si está disponible para enseñar

    def __str__(self):
        return self.nombre
