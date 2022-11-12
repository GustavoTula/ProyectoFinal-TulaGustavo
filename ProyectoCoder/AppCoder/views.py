from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Vino , Espumante , Aceite , Personal
from .forms import VinoFormulario , EspumanteFormulario , AceiteFormulario , PersonalFormulario, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


@login_required
def inicio(request):
    return render(request, "inicio.html")
@login_required
def nosotros(request):
    return render(request, "nosotros.html")

@staff_member_required(login_url='/app-coder/login') #CREAR UN HTML QUE INDIQUE QUE NO TIENE PERMISO DE MIRAR ESTA PESTAÑA SINO ES MIEMBRO
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

def eliminarVinos(request, id):
    if request.method == 'POST':
         vino = Vino.objects.get(id=id)
         vino.delete()

         return redirect('ListaVinos')

def editarVinos(request, id):

    vino = Vino.objects.get(id=id)

    if request.method == 'POST':
         miFormulario = VinoFormulario(request.POST)
         print(miFormulario)

         if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data

            vino.nombre = data["vino"]
            vino.varietal = data["varietal"]
            vino.añada = data["añada"]

            vino.save()

            return redirect("ListaVinos")
    else:
        
        miFormulario = VinoFormulario(initial={

            "vino": vino.nombre, 
            "varietal": vino.varietal, 
            "añada": vino.añada,
            
            })
    return render(request, "editarVinos.html", {"miFormulario":miFormulario, "id":vino.id})

def listaVinos(request):
    vinoss = Vino.objects.all()
    return render(request, "listaVinos.html", {"listaVinos": vinoss})

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


class VinoList(LoginRequiredMixin, ListView): #Buscar mixin decoradores para staff members
    model = Vino
    template_name = "vino-list.html"
class VinoDetail(LoginRequiredMixin, DetailView): #Buscar mixin decoradores para staff
    model = Vino
    template_name = "vino-detail.html"
class VinoCreate(LoginRequiredMixin, CreateView): #Buscar mixin decoradores para staff
    model= Vino
    template_name = "vino-create.html"
    success_url = "/app-coder/vinoList"
    fields = ['nombre' , 'varietal', 'añada']
    

class VinoUpdate(LoginRequiredMixin, UpdateView): #Buscar mixin decoradores para staff
    model = Vino
    template_name = "vino-update.html"
    success_url = "/app-coder/vinoList"
    fields = ['nombre' , 'varietal', 'añada']

class VinoDelete(LoginRequiredMixin, DeleteView): #Buscar mixin decoradores para staff
    model = Vino
    template_name = "vino-delete.html"
    success_url = "/app-coder/vinoList"

@staff_member_required(login_url='/app-coder/login')
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

def listaEspumantes(request):

    espumantess = Espumante.objects.all()
    return render(request, "listaEquipo.html", {"Nombre":espumantess})

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
@staff_member_required(login_url='/app-coder/login')
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

def listaAceites(request):

    aceitess = Aceite.objects.all()
    return render(request, "listaEquipo.html", {"Nombre":aceitess})

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

@staff_member_required(login_url='/app-coder/login')
def equipo(request):

    if request.method == 'POST':    
        miFormulario = PersonalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            personal = Personal(nombre=data['nombre'], apellido=data['apellido'] , cargo=data['cargo'],email=data['email'])
            personal.save()
            return redirect("Lista-Personal")
    else:
        miFormulario=PersonalFormulario()

    return render(request, "equipo.html", {"miFormulario":miFormulario})

def listaEquipo(request):

    miembros = Personal.objects.all()
    return render(request, "listaEquipo.html", {"Nombre":miembros})

def busquedaCargo(request):
    return render(request, "busquedaCargo.html")

def buscarCargo(request):
    if request.GET["cargo"]:
        cargo = request.GET['cargo']
        nombre =Personal.objects.filter(cargo__icontains=cargo)
        apellido =Personal.objects.filter(cargo__icontains=cargo)
        email =Personal.objects.filter(cargo__icontains=cargo)

        return render(request, "resultadoBusquedaCargo.html", {"nombre":nombre, "apellido":apellido, "cargo":cargo , "email":email})
    else:

        respuesta3= "No asigno ningun cargo en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaCargo.html", {"respuesta":respuesta3})

@login_required
def noticias(request):
    return render(request,"noticias.html")


def loginRequest(request):
    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data = request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data['username']
            contrasenia = data['password']

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "inicio.html", {"mensaje":f"Error,datos incorrectos. Intente nuevamente"})
        else:
            return render(request, "inicio.html", {"mensaje":f"Los datos ingresados son inexistentes"})

    else:
        miFormulario = AuthenticationForm()

        return render(request, "login.html", {'miFormulario': miFormulario})

def register(request):
    if request.method == 'POST':

        #miFormulario = UserCreationForm(request.POST)
        miFormulario = UserRegisterForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            username = data['username']
            miFormulario.save()
            return render(request, "inicio.html", {"mensaje":f"{username} creado exitosamente"})
        else:
            return render(request, "inicio.html", {"mensaje":f"Error,al crear {username},intentar nuevamente"})

    else:
        #miFormulario=UserCreationForm()
        miFormulario = UserRegisterForm()
        return render(request, "register.html", {"miFormulario":miFormulario}) 
    

def editRegister(request):
    usuario = request.user
   

    if request.method == 'POST':
         miFormulario = UserEditForm(request.POST)
         if miFormulario.is_valid():


            data = miFormulario.cleaned_data

            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']
            usuario.save()
            return render(request, "inicio.html")
    else:

        miFormulario=UserEditForm(initial={'email':usuario.email})
    
    return render(request, "editPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})
