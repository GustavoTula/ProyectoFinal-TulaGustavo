from django.shortcuts import render, redirect
from .forms import SignupUsuario
from django.contrib.auth import login
# Create your views here.
def inicioChat(request):
    return render(request, "inicioChat.html")

def crearUsuario(request):
    if request.method == 'POST':

        miFormulario=SignupUsuario(request.POST)

        if miFormulario.is_valid():

            user = miFormulario.save()

            login(request, user)

            return redirect('InicioChat')
    else:
        
        miFormulario=SignupUsuario()

    return render(request, "crearUsuario.html", {"miFormulario":miFormulario})    