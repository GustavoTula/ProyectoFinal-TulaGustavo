from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Vino , Espumante , Aceite , Personal
from .forms import VinoFormulario , EspumanteFormulario , AceiteFormulario , PersonalFormulario

def vino (request,nombre,varietal,añada):
    vino = Vino(nombre=nombre, varietal=varietal,añada=añada)
    vino.save()
    return render(request, "vino.html")

def lista_vino(request):
    lista= Vino.objects.all()
    return render(request, "Lista_vino.html", {"lista_vino": lista})




def espumante(request,nombre,varietal,añada):
    espumante = Espumante(nombre=nombre, varietal=varietal,añada=añada)
    espumante.save()
    return render (request,"espumante.html")

def lista_espumante(request):
    lista1 = Espumante.objects.all()
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
    return render(request, "Lista_personal.html", {"lista_personal": lista3})



def inicio(request):
    return render(request, "inicio.html")

def nosotros(request):
    return render(request, "nosotros.html")

def vinos(request):

    if request.method == 'POST':    
        miFormulario = VinoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            vino = Vino(nombre=data['vino'], varietal=data['varietal'], añada=data['añada'])
            vino.save()
            return redirect("Lista-Vinos")
    else:
        miFormulario=VinoFormulario()

    return render(request, "vinos.html", {"miFormulario":miFormulario})

def busquedaVarietal(request):
    return render(request, "busquedaVarietal.html")
def buscar(request):
    if request.GET["varietal"]:
        varietal = request.GET['varietal']
        vinos = Vino.objects.filter(varietal__icontains=varietal)
        añada = Vino.objects.filter(varietal__icontains=varietal)

        return render(request, "resultadoBusqueda.html", {"vinos":vinos, "varietal":varietal , "añada":añada})
    else:

        respuesta = "No asigno ningun varietal en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusqueda.html", {"respuesta":respuesta})



def espumantes(request):
    
    if request.method == 'POST':    
        miFormulario = EspumanteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            espumante = Espumante(nombre=data['espumante'], varietal=data['varietal'] , añada=data['añada'])
            espumante.save()
            return redirect("Lista-Espumantes")
    else:
        miFormulario=EspumanteFormulario()

    return render(request, "espumantes.html", {"miFormulario":miFormulario})

def busquedaAñada(request):
    return render(request, "busquedaAñada.html")

def buscarAñada(request):
    if request.GET["añada"]:
        añada = request.GET['añada']
        espumantes = Espumante.objects.filter(añada__icontains=añada)
        varietal = Espumante.objects.filter(añada__icontains=añada)

        return render(request, "resultadoBusquedaAñada.html", {"espumantes":espumantes, "varietal":varietal , "añada":añada})
    else:

        respuesta1= "No asigno ninguna añada en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaAñada.html", {"respuesta":respuesta1})

def aceites(request):

    if request.method == 'POST':    
        miFormulario = AceiteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            aceite = Aceite(nombre=data['aceite'], varietal=data['varietal'])
            aceite.save()
            return redirect("Lista-Aceites")
    else:
        miFormulario=AceiteFormulario()

    return render(request, "aceites.html", {"miFormulario":miFormulario})

def busquedaAceite(request):
    return render(request, "busquedaAceite.html")

def buscarAceite(request):
    if request.GET["aceite"]:
        aceite = request.GET['aceite']
        varietal =Aceite.objects.filter(nombre__icontains=aceite)

        return render(request,"resultadoBusquedaAceite.html", {"aceite":aceite, "varietal":varietal})
    else:

        respuesta="No asigno ningun aceite en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaAceite.html", {"respuesta":respuesta})


def equipo(request):

    if request.method == 'POST':    
        miFormulario = PersonalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            personal = Personal(nombre=data['nombre'], apellido=data['apellido'] , cargo=data['cargo'],email=data['email'])
            personal.save()
            return redirect("Lista-personal")
    else:
        miFormulario=PersonalFormulario()

    return render(request, "equipo.html", {"miFormulario":miFormulario})

def busquedaCargo(request):
    return render(request, "busquedaCargo.html")

def buscarCargo(request):
    if request.GET["cargo"]:
        cargo = request.GET['cargo']
        nombre =Personal.objects.filter(cargo__icontains=cargo)
        apellido =Personal.objects.filter(cargo__icontains=cargo)
        email =Personal.objects.filter(cargo__icontains=cargo)

        return render(request, "resultadoBusquedaCargo.html", {"nombre":nombre, "apellido":apellido,"cargo":cargo , "email":email})
    else:

        respuesta3= "No asigno ningun cargo en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaCargo.html", {"respuesta":respuesta3})





def noticias(request):
    return render(request,"noticias.html")

