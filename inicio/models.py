from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    dni = models.IntegerField()
