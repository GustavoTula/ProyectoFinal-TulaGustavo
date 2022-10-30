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
    return render(request,"Lista_personal", {"lista_personal":lista3})


def inicio(request):
    return render(request, "inicio.html")

def nosotros(request):
    return render(request, "nosotros.html")

def vinos(request):
    lista= Vino.objects.all()
    return render(request, "vinos.html", {"lista_vinos":lista})

def espumantes(request):
    lista1 = Espumante.objects.all()
    return render(request, "espumantes.html",{"lista_espumante":lista1})

def aceites(request):
    lista2 = Aceite.objects.all()
    return render(request, "aceites.html", {"lista_aceite":lista2})

def equipo(request):
    lista3 = Personal.objects.all()
    return render(request, "equipo.html", {"lista_personal":lista3})

def noticias(request):
    return render(request,"noticias.html")

def vinoFormulario(request):
    if request.method == 'POST':    
        miFormulario = VinoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            vino = Vino(nombre=data['vino'], varietal=data['varietal'], añada=data['añada'])
            vino.save()
            return redirect("Vinos")
    else:
        miFormulario=VinoFormulario()

    return render(request, "vinoFormulario.html", {"miFormulario":miFormulario})

def busquedaVarietal(request):
    return render(request, "busquedaVarietal.html")
def buscar(request):
    if request.GET["varietal"]:
        varietal = request.GET['varietal']
        vinos = Vino.objects.filter(varietal__icontains=varietal)
        añada = Vino.objects.filter(varietal__icontains=varietal)

        return render(request, "resultadoBusqueda.html", {"vinos":vinos, "varietal":varietal , "añada":añada})
    else:

        respuesta = "No enviaste datos"    

    return HttpResponse(respuesta)



def aceiteFormulario(request):
    if request.method == 'POST':    
        miFormulario = AceiteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            aceite = Aceite(nombre=data['aceite'], varietal=data['varietal'])
            aceite.save()
            return redirect("Aceites")
    else:
        miFormulario=AceiteFormulario()

    return render(request, "aceiteFormulario.html", {"miFormulario":miFormulario})

def espumanteFormulario(request):
    if request.method == 'POST':    
        miFormulario = EspumanteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            espumante = Espumante(nombre=data['espumante'], varietal=data['varietal'] , añada=data['añada'])
            espumante.save()
            return redirect("Espumantes")
    else:
        miFormulario=EspumanteFormulario()

    return render(request, "espumanteFormulario.html", {"miFormulario":miFormulario})

def equipoFormulario(request):
    if request.method == 'POST':    
        miFormulario = PersonalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            personal = Personal(nombre=data['nombre'], apellido=data['apellido'] , cargo=data['cargo'],email=data['email'])
            personal.save()
            return redirect("Equipo")
    else:
        miFormulario=PersonalFormulario()

    return render(request, "equipoFormulario.html", {"miFormulario":miFormulario})


