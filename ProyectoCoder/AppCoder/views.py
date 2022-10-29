from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Vino , Espumantes , Aceite , Personal

def vino (request,nombre,varietal,añada):
    vino = Vino(nombre=nombre, varietal=varietal,añada=añada)
    vino.save()
    return render(request, "vino.html")

def lista_vino(request):
    lista= Vino.objects.all()
    return render(request, "Lista_vino.html", {"lista_vino": lista})




def espumante(request,nombre,varietal,añada):
    espumante = Espumantes(nombre=nombre, varietal=varietal,añada=añada)
    espumante.save()
    return render (request,"espumante.html")

def lista_espumante(request):
    lista1 = Espumantes.objects.all()
    return render(request, "Lista_espumante.html", {"lista_espumante": lista1})




def aceite(request,nombre,varietal):
    aceite = Aceite(nombre=nombre, varietal=varietal)
    aceite.save()
    return render (request,"aceite.html")

def lista_aceite(request):
    lista2 = Aceite.objects.all()
    return render(request, "Lista_aceite.html", {"lista_aceite": lista2})



def personal(request,nombre,apellido,cargo,email):
    personal = Personal(nombre=nombre, apellido=apellido,cargo=cargo,email=email)
    personal.save()
    return render(request, "personal.html")

def lista_personal(request):
    lista3 = Personal.objects.all()
    return render(request,"Lista_personal", {"lista_personal":lista3})


def inicio(request):
    return render(request, "inicio.html")

def nosotros(request):
    return render(request, "nosotros.html")

def vinos(request):
    return render(request, "vinos.html")

def espumantes(request):
    return render(request, "espumantes.html")

def aceites(request):
    return render(request, "aceites.html")

def equipo(request):
    return render(request, "miembros.html")

def noticias(request):
    return noticias(request,"noticias.html")

