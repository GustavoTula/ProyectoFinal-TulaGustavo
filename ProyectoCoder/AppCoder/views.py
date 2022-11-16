from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator

from .forms import (AceiteFormulario, EspumanteFormulario, PersonalFormulario,
                    UserEditForm, UserRegisterForm, VinoFormulario, AvatarFormulario)
from .models import Aceite, Avatar, Espumante, Personal, Vino


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
    
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "inicio.html", {"url":avatares[0].imagen.url})

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


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
class VinoList(LoginRequiredMixin, ListView): #Buscar mixin decoradores para staff members
    model = Vino
    template_name = "vino-list.html"
class VinoDetail(LoginRequiredMixin, DetailView): #Buscar mixin decoradores para staff
    model = Vino
    template_name = "vino-detail.html"
class VinoCreate(StaffRequiredMixin, CreateView): #Buscar mixin decoradores para staff
    model= Vino
    template_name = "vino-create.html"
    success_url = "/app-coder/vinoList"
    fields = ['nombre' , 'varietal', 'añada']
class VinoUpdate(StaffRequiredMixin, UpdateView): #Buscar mixin decoradores para staff
    model = Vino
    template_name = "vino-update.html"
    success_url = "/app-coder/vinoList"
    fields = ['nombre' , 'varietal', 'añada']
class VinoDelete(StaffRequiredMixin, DeleteView): #Buscar mixin decoradores para staff
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

def eliminarEspumantes(request, id):
    if request.method == 'POST':
         espumante = Espumante.objects.get(id=id)
         espumante.delete()

         return redirect('ListaEspumantes')

def editarEspumantes(request, id):

    espumante = Espumante.objects.get(id=id)

    if request.method == 'POST':
         miFormulario = EspumanteFormulario(request.POST)
         print(miFormulario)

         if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data

            espumante.nombre = data["espumante"]
            espumante.varietal = data["varietal"]
            espumante.añada = data["añada"]

            espumante.save()

            return redirect("ListaEspumantes")
    else:
        
        miFormulario = EspumanteFormulario(initial={

            "espumante": espumante.nombre, 
            "varietal": espumante.varietal, 
            "añada": espumante.añada,
            
            })
    return render(request, "editarEspumantes.html", {"miFormulario":miFormulario, "id":espumante.id})


def listaEspumantes(request):
    espumantess = Espumante.objects.all()
    return render(request, "listaEspumantes.html", {"listaEspumantes":espumantess})

def busquedaAñada(request):
    return render(request, "busquedaAñada.html")

def buscarAñada(request):
    if request.GET["añada"]:
        añada = request.GET['añada']
        espumantes = Espumante.objects.filter(añada__icontains=añada)
        varietal = Espumante.objects.filter(añada__icontains=añada)

        return render(request, "resultadoBusquedaAñada.html", {"espumantes":espumantes, "varietal":varietal , "añada":añada})
    else:

        respuesta= "No asigno ninguna añada en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaAñada.html", {"respuesta1":respuesta})

class EspumanteList(LoginRequiredMixin, ListView): #Buscar mixin decoradores para staff members
    model = Espumante
    template_name = "espumante-list.html"
class EspumanteDetail(LoginRequiredMixin, DetailView): #Buscar mixin decoradores para staff
    model = Espumante
    template_name = "espumante-detail.html"
class EspumanteCreate(LoginRequiredMixin, CreateView): #Buscar mixin decoradores para staff
    model= Espumante
    template_name = "espumante-create.html"
    success_url = "/app-coder/espumanteList"
    fields = ['nombre' , 'varietal', 'añada']
class EspumanteUpdate(LoginRequiredMixin, UpdateView): #Buscar mixin decoradores para staff
    model = Espumante
    template_name = "espumante-update.html"
    success_url = "/app-coder/espumanteList"
    fields = ['nombre' , 'varietal', 'añada']
class EspumanteDelete(LoginRequiredMixin, DeleteView): #Buscar mixin decoradores para staff
    model = Espumante
    template_name = "espumante-delete.html"
    success_url = "/app-coder/espumanteList"



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

def eliminarAceites(request, id):
    if request.method == 'POST':
         aceite = Aceite.objects.get(id=id)
         aceite.delete()

         return redirect('ListaAceites')

def editarAceites(request, id):

    aceite = Aceite.objects.get(id=id)

    if request.method == 'POST':
         miFormulario = AceiteFormulario(request.POST)
         print(miFormulario)

         if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data

            aceite.nombre = data["aceite"]
            aceite.varietal = data["varietal"]

            aceite.save()

            return redirect("ListaAceites")
    else:
        
        miFormulario = AceiteFormulario(initial={

            "aceite": aceite.nombre, 
            "varietal": aceite.varietal,
            
            })
    return render(request, "editarAceites.html", {"miFormulario":miFormulario, "id":aceite.id})

def listaAceites(request):

    aceitess = Aceite.objects.all()
    return render(request, "listaAceites.html", {"listaAceites":aceitess})

def busquedaAceite(request):
    return render(request, "busquedaAceite.html")

def buscarAceite(request):
    if request.GET["aceite"]:
        aceites = request.GET['aceite']
        varietal =Aceite.objects.filter(nombre__icontains=aceites)

        return render(request,"resultadoBusquedaAceite.html", {"aceites":aceites, "varietal":varietal})
    else:

        respuesta="No asigno ningun aceite en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaAceite.html", {"respuesta2":respuesta})


class AceiteList(LoginRequiredMixin, ListView): #Buscar mixin decoradores para staff members
    model = Aceite
    template_name = "aceite-list.html"
class AceiteDetail(LoginRequiredMixin, DetailView): #Buscar mixin decoradores para staff
    model = Aceite
    template_name = "aceite-detail.html"
class AceiteCreate(LoginRequiredMixin, CreateView): #Buscar mixin decoradores para staff
    model= Aceite
    template_name = "aceite-create.html"
    success_url = "/app-coder/aceiteList"
    fields = ['nombre' , 'varietal']
class AceiteUpdate(LoginRequiredMixin, UpdateView): #Buscar mixin decoradores para staff
    model = Aceite
    template_name = "aceite-update.html"
    success_url = "/app-coder/aceiteList"
    fields = ['nombre' , 'varietal']
class AceiteDelete(LoginRequiredMixin, DeleteView): #Buscar mixin decoradores para staff
    model = Aceite
    template_name = "aceite-delete.html"
    success_url = "/app-coder/aceiteList"

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

def eliminarEquipo(request, id):
    if request.method == 'POST':
         personal = Personal.objects.get(id=id)
         personal.delete()

         return redirect('ListaEquipo')

def editarEquipo(request, id):

    personal = Personal.objects.get(id=id)

    if request.method == 'POST':
         miFormulario = PersonalFormulario(request.POST)
         print(miFormulario)

         if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data

            personal.nombre = data["nombre"]
            personal.apellido = data["apellido"]
            personal.cargo = data["cargo"]
            personal.email = data["email"]

            personal.save()

            return redirect("ListaEquipo")
    else:
        
        miFormulario = PersonalFormulario(initial={

            "nombre": personal.nombre, 
            "apellido": personal.apellido, 
            "cargo": personal.cargo,
            "email": personal.email,
            
            })
    return render(request, "editarEquipo.html", {"miFormulario":miFormulario, "id":personal.id})

def listaEquipo(request):
    miembros = Personal.objects.all()
    return render(request, "listaEquipo.html", {"listaEquipo":miembros})

def busquedaCargo(request):
    return render(request, "busquedaCargo.html")

def buscarCargo(request):
    if request.GET["cargo"]:
        cargos = request.GET['cargo']
        nombre =Personal.objects.filter(cargo__icontains=cargos)
        apellido =Personal.objects.filter(cargo__icontains=cargos)
        email =Personal.objects.filter(cargo__icontains=cargos)

        return render(request, "resultadoBusquedaCargo.html", {"nombre":nombre, "apellido":apellido, "cargo":cargos , "email":email})
    else:

        respuesta= "No asigno ningun cargo en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaCargo.html", {"respuesta3":respuesta})

class PersonalList(LoginRequiredMixin, ListView): #Buscar mixin decoradores para staff members
    model = Personal
    template_name = "personal-list.html"
class PersonalDetail(LoginRequiredMixin, DetailView): #Buscar mixin decoradores para staff
    model = Personal
    template_name = "personal-detail.html"
class PersonalCreate(LoginRequiredMixin, CreateView): #Buscar mixin decoradores para staff
    model= Personal
    template_name = "personal-create.html"
    success_url = "/app-coder/personalList"
    fields = ['nombre' , 'apellido', 'cargo', 'email']
class PersonalUpdate(LoginRequiredMixin, UpdateView): #Buscar mixin decoradores para staff
    model = Personal
    template_name = "personal-update.html"
    success_url = "/app-coder/personalList"
    fields = ['nombre' , 'apellido', 'cargo', 'email']
class PersonalDelete(LoginRequiredMixin, DeleteView): #Buscar mixin decoradores para staff
    model = Personal
    template_name = "personal-delete.html"
    success_url = "/app-coder/personalList"   

@login_required
def noticias(request):
    return render(request,"noticias.html")


def loginRequest(request):
    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data = request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            usuario = data['username']
            psw = data['password']
            
            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)
                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})

            else:

                return render(request, "inicio.html", {"mensaje":f"Error,datos incorrectos. Intente nuevamente"})
        
        return render(request, "inicio.html", {"mensaje":f"Los datos ingresados son inexistentes"})

    else:
        miFormulario = AuthenticationForm()

        return render(request, "login.html", {'miFormulario': miFormulario})

def register(request):
    if request.method == 'POST':

        miFormulario = UserRegisterForm(request.POST)

        if miFormulario.is_valid():
            username = miFormulario.cleaned_data['username']

            miFormulario.save()

            return render(request, "inicio.html", {"mensaje":f"{username} creado exitosamente"})

        else:

            return render(request, "inicio.html", {"mensaje":f"Error,al crear ,intentar nuevamente"})

    else:
        
        miFormulario = UserRegisterForm()
        return render(request, "register.html", {"miFormulario":miFormulario}) 
    

def editRegister(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data['email']
            usuario.set_password(data['password1'])
            usuario.set_password(data['password2'])
            
            usuario.save()

            return render(request, "inicio.html", {"mensaje": f'Datos actualizados correctamente'})
        
        return render(request, "editRegister.html",{"mensaje":f'Contraseñas no coinciden'})

    else:

        miFormulario=UserEditForm(instance=request.user)
    
        return render(request, "editRegister.html",{"miFormulario":miFormulario, "usuario":usuario})        

def agregarAvatar(request):
    if request.method == 'POST':

        miFormulario=AvatarFormulario(request.POST, request.FILES)
       
        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            #miFormulario.save()
            return redirect("Inicio")
    else:
        miFormulario=AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario":miFormulario})    
    

