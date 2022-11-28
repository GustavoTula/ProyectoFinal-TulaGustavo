from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings


from .forms import (AceiteFormulario, EspumanteFormulario, PersonalFormulario,
                    UserEditForm, UserRegisterForm, VinoFormulario, AvatarFormulario,ContactoFormulario)
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
    
        avatar = Avatar.objects.filter(user=request.user.id)
        return render(request, "inicio.html", {"url":avatar[0].imagen.url})


def nosotros(request):
    return render(request, "nosotros.html")

@staff_member_required(login_url="errorNoEsMiemStaff.html") 
def vinos(request):

    if request.method == 'POST':    
        miFormulario = VinoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            vino = Vino(nombre=data['vino'], varietal=data['varietal'], añada=data['añada'])
            vino.save()
            return render(request, "vinoFormCreado.html")
    else:
        miFormulario=VinoFormulario()

    return render(request, "vinos.html", {"miFormulario":miFormulario})
@user_passes_test(lambda u: u.is_superuser)
def eliminarVinos(request, id):
     if request.method == 'POST':
         vino = Vino.objects.get(id=id)
         vino.delete()

         return redirect('ListaVinos')     
@staff_member_required(login_url="errorNoEsMiemStaff.html") 
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
@login_required
def busquedaVarietal(request):
    return render(request, "busquedaVarietal.html")
@login_required    
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

class UserPassesTestMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(UserPassesTestMixin,self).dispatch(request, *args, **kwargs)
    
class VinoList(LoginRequiredMixin, ListView): 
    model = Vino
    template_name = "vino-list.html"
class VinoDetail(LoginRequiredMixin, DetailView): 
    model = Vino
    template_name = "vino-detail.html"
class VinoCreate(StaffRequiredMixin, CreateView): 
    model= Vino
    template_name = "vino-create.html"
    success_url = "/vinoList"
    fields = ['nombre' , 'varietal', 'añada']
class VinoUpdate(StaffRequiredMixin, UpdateView): 
    model = Vino
    template_name = "vino-update.html"
    success_url = "/vinoList"
    fields = ['nombre' , 'varietal', 'añada']
class VinoDelete(UserPassesTestMixin, DeleteView): 
    model = Vino
    template_name = "vino-delete.html"
    success_url = "/vinoList"

@staff_member_required(login_url="errorNoEsMiemStaff.html") 
def espumantes(request):
    
    if request.method == 'POST':    
        miFormulario = EspumanteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            espumante = Espumante(nombre=data['espumante'], varietal=data['varietal'] , añada=data['añada'])
            espumante.save()
            return render(request, "espumanteFormCreado.html")
    else:
        miFormulario=EspumanteFormulario()

    return render(request, "espumantes.html", {"miFormulario":miFormulario})
@user_passes_test(lambda u: u.is_superuser)
def eliminarEspumantes(request, id):
    if request.method == 'POST':
         espumante = Espumante.objects.get(id=id)
         espumante.delete()

         return redirect('ListaEspumantes')
@staff_member_required(login_url="errorNoEsMiemStaff.html") 
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
@login_required
def busquedaAñada(request):
    return render(request, "busquedaAñada.html")
@login_required
def buscarAñada(request):
    if request.GET["añada"]:
        añada = request.GET['añada']
        espumantes = Espumante.objects.filter(añada__icontains=añada)
        varietal = Espumante.objects.filter(añada__icontains=añada)

        return render(request, "resultadoBusquedaAñada.html", {"espumantes":espumantes, "varietal":varietal , "añada":añada})
    else:

        respuesta= "No asigno ninguna añada en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaAñada.html", {"respuesta1":respuesta})

class EspumanteList(LoginRequiredMixin, ListView): 
    model = Espumante
    template_name = "espumante-list.html"
class EspumanteDetail(LoginRequiredMixin, DetailView): 
    model = Espumante
    template_name = "espumante-detail.html"
class EspumanteCreate(StaffRequiredMixin, CreateView): 
    model= Espumante
    template_name = "espumante-create.html"
    success_url = "/espumanteList"
    fields = ['nombre' , 'varietal', 'añada']
class EspumanteUpdate(StaffRequiredMixin, UpdateView): 
    model = Espumante
    template_name = "espumante-update.html"
    success_url = "/espumanteList"
    fields = ['nombre' , 'varietal', 'añada']
class EspumanteDelete(UserPassesTestMixin, DeleteView): 
    model = Espumante
    template_name = "espumante-delete.html"
    success_url = "/espumanteList"



@staff_member_required(login_url="errorNoEsMiemStaff.html") 
def aceites(request):

    if request.method == 'POST':    
        miFormulario = AceiteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            aceite = Aceite(nombre=data['aceite'], varietal=data['varietal'])
            aceite.save()
            return render(request, "aceiteFormCreado.html")
    else:
        miFormulario=AceiteFormulario()

    return render(request, "aceites.html", {"miFormulario":miFormulario})
@user_passes_test(lambda u: u.is_superuser)
def eliminarAceites(request, id):
    if request.method == 'POST':
         aceite = Aceite.objects.get(id=id)
         aceite.delete()

         return redirect('ListaAceites')
@staff_member_required(login_url="errorNoEsMiemStaff.html") 
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
@login_required
def busquedaAceite(request):
    return render(request, "busquedaAceite.html")
@login_required
def buscarAceite(request):
    if request.GET["aceite"]:
        aceites = request.GET['aceite']
        varietal =Aceite.objects.filter(nombre__icontains=aceites)

        return render(request,"resultadoBusquedaAceite.html", {"aceites":aceites, "varietal":varietal})
    else:

        respuesta="No asigno ningun aceite en la busqueda, por favor intentar de nuevo"    

    return render(request, "resultadoBusquedaAceite.html", {"respuesta2":respuesta})


class AceiteList(LoginRequiredMixin, ListView): 
    model = Aceite
    template_name = "aceite-list.html"
class AceiteDetail(LoginRequiredMixin, DetailView):
    model = Aceite 
    template_name = "aceite-detail.html"
class AceiteCreate(StaffRequiredMixin, CreateView): 
    model= Aceite
    template_name = "aceite-create.html"
    success_url = "/aceiteList"
    fields = ['nombre' , 'varietal']
class AceiteUpdate(StaffRequiredMixin, UpdateView): 
    model = Aceite
    template_name = "aceite-update.html"
    success_url = "/aceiteList"
    fields = ['nombre' , 'varietal']
class AceiteDelete(UserPassesTestMixin, DeleteView): 
    model = Aceite
    template_name = "aceite-delete.html"
    success_url = "/aceiteList"

@staff_member_required(login_url="errorNoEsMiemStaff.html") 
def equipo(request):

    if request.method == 'POST':    
        miFormulario = PersonalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            personal = Personal(nombre=data['nombre'], apellido=data['apellido'] , cargo=data['cargo'],email=data['email'])
            personal.save()
            return render(request, "personalFormCreado.html")
    else:
        miFormulario=PersonalFormulario()

    return render(request, "equipo.html", {"miFormulario":miFormulario})
@user_passes_test(lambda u: u.is_superuser)
def eliminarEquipo(request, id):
    if request.method == 'POST':
         personal = Personal.objects.get(id=id)
         personal.delete()

         return redirect('ListaEquipo')
@staff_member_required(login_url="errorNoEsMiemStaff.html") 
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
@login_required
def busquedaCargo(request):
    return render(request, "busquedaCargo.html")
@login_required
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

class PersonalList(LoginRequiredMixin, ListView): 
    model = Personal
    template_name = "personal-list.html"
class PersonalDetail(LoginRequiredMixin, DetailView): 
    model = Personal
    template_name = "personal-detail.html"
class PersonalCreate(StaffRequiredMixin, CreateView): 
    model= Personal
    template_name = "personal-create.html"
    success_url = "/personalList"
    fields = ['nombre' , 'apellido', 'cargo', 'email']
class PersonalUpdate(StaffRequiredMixin, UpdateView): 
    model = Personal
    template_name = "personal-update.html"
    success_url = "/personalList"
    fields = ['nombre' , 'apellido', 'cargo', 'email']
class PersonalDelete(UserPassesTestMixin, DeleteView): 
    model = Personal
    template_name = "personal-delete.html"
    success_url = "/personalList"   

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
                
                return render(request, "crearAvatar.html", {"mensaje": f'Bienvenido {usuario}'})

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

            return render(request, "registroCreado.html", {"mensaje":f"{username} creado exitosamente"})

        else:

            return render(request, "registroErroneo.html", {"mensaje":f"Error,al crear ,intentar nuevamente"})

    else:
        
        miFormulario = UserRegisterForm()
        return render(request, "register.html", {"miFormulario":miFormulario}) 
    
@login_required
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

            return render(request, "editRealizado.html", {"mensaje": f'Datos actualizados correctamente'})
        
        return render(request, "editRegister.html",{"mensaje":f'Contraseñas no coinciden'})

    else:

        miFormulario=UserEditForm(instance=request.user)
    
        return render(request, "editRegister.html",{"miFormulario":miFormulario, "usuario":usuario})        
@login_required
def agregarAvatar(request):
    if request.method == 'POST':

        miFormulario=AvatarFormulario(request.POST, request.FILES)
       
        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return redirect("Inicio")
    else:
        miFormulario=AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario":miFormulario})    
    
def contacto(request):

    if request.method == "POST":
        miFormulario = ContactoFormulario(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            send_mail(
                
                infForm['asunto'],
                infForm['mensaje'],
                infForm.get('email',''),['vinotecawinemaker@gmail.com'],)

            return render(request, "mensajeGracias.html", )

    else:
            
        miFormulario=ContactoFormulario()
 
    return render(request, "contactoFormulario.html", {"miFormulario":miFormulario})      