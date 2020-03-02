from django.db import models

# Create your models here.

class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=255)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=10)
