from dataclasses import field
from msilib.schema import Class
from django.db import models

class Vino(models.Model):

    nombre = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    añada = models.IntegerField()
    def __str__(self):

        return (f'Nombre:{self.nombre} - Varietal: {self.varietal} - Añada: {self.añada}')
class Espumante(models.Model):
    nombre = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    añada = models.IntegerField()
    def __str__(self):

        return (f'Nombre:{self.nombre} - Varietal: {self.varietal} - Añada: {self.añada}')
class Aceite(models.Model):
     nombre = models.CharField(max_length=50)
     varietal = models.CharField(max_length=50)
     def __str__(self):
         return (f'Nombre:{self.nombre} - Varietal: {self.varietal}')

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):

        return (f'Nombre:{self.nombre} - Apellido: {self.apellido} - Cargo: {self.cargo} - Email: {self.email}')
