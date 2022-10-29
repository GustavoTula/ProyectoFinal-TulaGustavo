from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Vino , Espumantes , Aceite , Personal

def vino (request,nombre,varietal,añada):
    vino = Vino(nombre=nombre, varietal=varietal,añada=añada)
    vino.save()
    return render(request, "vino.html")

def lista_vino(request):
    lista= Vino.objects.all()
    return render(request, "Lista_vinos.html", {"lista_vinos": lista})




def espumantes(request,nombre,varietal,añada):
    espumantes = Espumantes(nombre=nombre, varietal=varietal,añada=añada)
    espumantes.save()
    return render (request,"espumantes.html")

def lista_espumantes(request):
    lista1 = Espumantes.objects.all()
    return render(request, "Lista_espumantes.html", {"lista_espumantes": lista1})




def aceites(request,nombre,varietal):
    aceites = Aceite(nombre=nombre, varietal=varietal)
    aceites.save()
    return render (request,"aceite.html")

def lista_aceites(request):
    lista2 = Aceite.objects.all()
    return render(request, "Lista_aceites.html", {"lista_aceites": lista2})



def personal(request,nombre,apellido,cargo,email):
    personal = Personal(nombre=nombre, apellido=apellido,cargo=cargo,email=email)
    personal.save()
    return render(request, "personal.html")

def lista_personal(request):
    lista3 = Personal.objects.all()
    return render(request,"Lista_personal", {"lista_personal":lista3})
