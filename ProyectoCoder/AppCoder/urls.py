from django.urls import path
from .views import eliminarVinos, listaVinos, listaEspumantes, listaAceites, aceites, listaEquipo, buscar, buscarAceite, buscarAñada, buscarCargo, busquedaAceite, busquedaAñada, busquedaCargo, busquedaVarietal, equipo, inicio, lista_personal,  nosotros, noticias, personal, vino , lista_vino , espumante , lista_espumante , aceite , lista_aceite, vinos, espumantes 


urlpatterns = [
    path('agrega-vino/<nombre>/<varietal>/<añada>', vino),
    path('lista-vino/', lista_vino, name="Lista-Vinos"),
    path('agrega-espumantes/<nombre>/<varietal>/<añada>', espumante),
    path('lista-espumantes/', lista_espumante, name="Lista-Espumantes"),
    path('agrega-aceite/<nombre>/<varietal>', aceite),
    path('lista-aceite/', lista_aceite, name="Lista-Aceites"),
    path('agrega-personal/<nombre>/<apellido>/<cargo>/<email>', personal),
    path('lista-personal/', lista_personal, name="Lista-Personal"),

    path('', inicio, name= "Inicio"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('vinos/', vinos, name="Vinos"),
    path('espumantes/', espumantes, name="Espumantes"),
    path('aceites/', aceites, name="Aceites"),
    path('equipo/', equipo, name="Equipo"),
    path('noticias/', noticias, name="Noticias"),
    path('busquedaVarietal/', busquedaVarietal, name="BusquedaVarietal"),
    path('buscar/', buscar , name="Buscar"),
    path('busquedaAñada/', busquedaAñada, name="BusquedaAñada"),
    path('buscarAñada/', buscarAñada , name="BuscarAñada"),
    path('busquedaAceite/', busquedaAceite, name="BusquedaAceite"),
    path('buscarAceite/', buscarAceite , name="BuscarAceite"),
    path('busquedaCargo/', busquedaCargo, name="BusquedaCargo"),
    path('buscarCargo/', buscarCargo , name="BuscarCargo"),
    path('listaEquipo/', listaEquipo , name="ListaEquipo"),
    path('listaVinos/', listaVinos , name="ListaVinos"),
    path('listaAceites/', listaAceites , name="ListaAceites"),
    path('listaEspumantes/', listaEspumantes, name="listaEspumantes"),
    path('eliminarVinos/<int:id>', eliminarVinos, name="EliminarVinos"),
   
   
]