from django.db import models

# Creacion de los modelos
class Usuario(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    nacionalidad = models.CharField(max_length=30)
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField()
    fecha_de_alta = models.DateField()
    domicilio = models.CharField(max_length=100)
    
    def __str__(self):
        return self.apellido
    
class Artista(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=30)
    
    def __str__(self):
        return self.apellido
    

class Album(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_lanzamiento = models.DateField()
    estilo = models.DateField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    