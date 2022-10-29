from dataclasses import field
from msilib.schema import Class
from django.db import models

class Vino(models.Model):

    nombre = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    añada = models.IntegerField()

class Espumantes(models.Model):
    nombre = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    añada = models.IntegerField()

class Aceite(models.Model):
     nombre = models.CharField(max_length=50)
     varietal = models.CharField(max_length=50)


class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField()