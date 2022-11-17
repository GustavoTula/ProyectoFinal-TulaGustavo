from dataclasses import field
from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User

class Vino(models.Model):

    nombre = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    añada = models.IntegerField()

    class Meta:
        verbose_name= 'Mis Vino'
        ordering = ['nombre', 'varietal','añada',]
        unique_together = ['nombre', 'varietal','añada',]
    def __str__(self):
        return (f'Nombre:{self.nombre} - Varietal: {self.varietal} - Añada: {self.añada}')
class Espumante(models.Model):
    nombre = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    añada = models.IntegerField()
    
    class Meta:
        verbose_name= 'Mis Espumante'
        ordering = ['nombre', 'varietal','añada',]
        unique_together = ['nombre', 'varietal','añada',]
    def __str__(self):
        return (f'Nombre:{self.nombre} - Varietal: {self.varietal} - Añada: {self.añada}')
class Aceite(models.Model):
     nombre = models.CharField(max_length=50)
     varietal = models.CharField(max_length=50)
     class Meta:
        verbose_name='Mis Aceite'
        ordering = ['nombre', 'varietal',]
        unique_together = ['nombre', 'varietal',]
     def __str__(self):
         return (f'Nombre:{self.nombre} - Varietal: {self.varietal}')

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField()
    #user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name= "Los Miembro"
        ordering = ['nombre', 'apellido','cargo','email',]
        unique_together = ['nombre', 'apellido','cargo','email',]
    def __str__(self):
        return (f'Nombre:{self.nombre} - Apellido: {self.apellido} - Cargo: {self.cargo} - Email: {self.email}')

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    class Meta:
        verbose_name= "Los Avatare"
        ordering = ['user', 'imagen']
        unique_together = ['user', 'imagen']
    def __str__(self):
        return (f'Usuario: {self.user} - Imagen: {self.imagen}')