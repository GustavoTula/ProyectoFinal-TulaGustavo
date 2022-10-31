from django.urls import path
from .views import aceites, buscar, buscarAñada, busquedaAñada, busquedaVarietal, equipo, inicio, lista_personal,  nosotros, noticias, personal, vino , lista_vino , espumante , lista_espumante , aceite , lista_aceite, vinos, espumantes 

#equipoFormulario, espumanteFormulario , aceiteFormulario , vinoFormulario
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
    #path('vinoFormulario/', vinoFormulario, name="VinoFormulario"),
    #path('aceiteFormulario/', aceiteFormulario, name="AceiteFormulario"),
    #path('espumanteFormulario/', espumanteFormulario, name="EspumanteFormulario"),
    #path('equipoFormulario/', equipoFormulario, name="EquipoFormulario"),
    path('busquedaVarietal/', busquedaVarietal, name="BusquedaVarietal"),
    path('buscar/', buscar , name="Buscar"),
    path('busquedaAñada/', busquedaAñada, name="BusquedaAñada"),
    path('buscarAñada/', buscarAñada , name="BuscarAñada"),
   
]