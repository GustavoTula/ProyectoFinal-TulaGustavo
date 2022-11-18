from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import (
    inicioChat,
    crearUsuario,

)
urlpatterns = [

    path("", inicioChat, name='InicioChat'),
    path('crearUsuario/', crearUsuario, name='CrearUsuario'),
    path('iniciarSesion/', LoginView.as_view(template_name='iniciarSesion.html'), name='IniciarSesion'),
    path('desloguear/', LogoutView.as_view(template_name="desloguear.html"), name='Desloguear'),

]
