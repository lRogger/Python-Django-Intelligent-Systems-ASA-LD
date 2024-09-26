from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'Rol: {self.id}: {self.nombre} Estado: {self.estado}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    estado = models.BooleanField(default=True)


    def __str__(self):
        return f'Usuario: {self.id}: {self.nombre} {self.apellido} {self.email}  Estado: {self.estado}'