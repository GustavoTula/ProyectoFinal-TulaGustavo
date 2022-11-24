from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ( 
    VinoDelete, 
    VinoUpdate, 
    VinoCreate, 
    VinoDetail , 
    VinoList,
    EspumanteDelete,
    EspumanteUpdate, 
    EspumanteCreate, 
    EspumanteDetail , 
    EspumanteList,
    AceiteDelete, 
    AceiteUpdate, 
    AceiteCreate, 
    AceiteDetail , 
    AceiteList,
    PersonalDelete, 
    PersonalUpdate, 
    PersonalCreate, 
    PersonalDetail , 
    PersonalList,
    editarVinos, 
    eliminarVinos, 
    listaVinos, 
    listaEspumantes, 
    listaAceites, 
    aceites, 
    listaEquipo, 
    buscar, 
    buscarAceite, 
    buscarAñada, 
    buscarCargo, 
    busquedaAceite, 
    busquedaAñada, 
    busquedaCargo, 
    busquedaVarietal, 
    equipo, 
    inicio, 
    lista_personal,
    nosotros, 
    noticias, 
    personal, 
    vino , 
    lista_vino , 
    espumante , 
    lista_espumante , 
    aceite , 
    lista_aceite, 
    vinos, 
    espumantes,
    loginRequest,
    register,
    editRegister,
    agregarAvatar,
    eliminarEspumantes,
    editarEspumantes,
    eliminarAceites,
    editarAceites,
    eliminarEquipo,
    editarEquipo,
    contacto,
)


urlpatterns = [
    path('agrega-vino/<nombre>/<varietal>/<añada>', vino),
    path('lista-vino/', lista_vino, name="Lista-Vinos"),
    path('agrega-espumantes/<nombre>/<varietal>/<añada>', espumante),
    path('lista-espumantes/', lista_espumante, name="Lista-Espumantes"),
    path('agrega-aceite/<nombre>/<varietal>', aceite),
    path('lista-aceite/', lista_aceite, name="Lista-Aceites"),
    path('agrega-personal/<nombre>/<apellido>/<cargo>/<email>', personal),
    path('lista-personal/', lista_personal, name="Lista-Personal"),

    path('inicio/', inicio, name= "Inicio"),
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

    
    path('listaVinos/', listaVinos , name="ListaVinos"),
    path('listaAceites/', listaAceites , name="ListaAceites"),
    path('listaEspumantes/', listaEspumantes, name="ListaEspumantes"),
    path('listaEquipo/', listaEquipo, name="ListaEquipo"),
    path('eliminarVinos/<int:id>', eliminarVinos, name="EliminarVinos"),
    path('editarVinos/<int:id>', editarVinos, name="EditarVinos"),
    path('eliminarEspumantes/<int:id>', eliminarEspumantes, name="EliminarEspumantes"),
    path('editarEspumantes/<int:id>', editarEspumantes, name="EditarEspumantes"),
    path('eliminarAceites/<int:id>', eliminarAceites, name="EliminarAceites"),
    path('editarAceites/<int:id>', editarAceites, name="EditarAceites"),
    path('eliminarEquipo/<int:id>', eliminarEquipo, name="EliminarEquipo"),
    path('editarEquipo/<int:id>', editarEquipo, name="EditarEquipo"),

    path('vinoList/', VinoList.as_view(), name="VinoList"),
    path('vinoDetail/<pk>', VinoDetail.as_view(), name="VinoDetail"),
    path('vinoCreate/', VinoCreate.as_view(), name="VinoCreate"),
    path('vinoUpdate/<pk>', VinoUpdate.as_view(), name="VinoUpdate"),
    path('vinoDelete/<pk>', VinoDelete.as_view(), name="VinoDelete"),

    path('espumanteList/', EspumanteList.as_view(), name="EspumanteList"),
    path('espumanteDetail/<pk>', EspumanteDetail.as_view(), name="EspumanteDetail"),
    path('espumanteCreate/', EspumanteCreate.as_view(), name="EspumanteCreate"),
    path('espumanteUpdate/<pk>', EspumanteUpdate.as_view(), name="EspumanteUpdate"),
    path('espumanteDelete/<pk>', EspumanteDelete.as_view(), name="EspumanteDelete"),

    path('aceiteList/', AceiteList.as_view(), name="AceiteList"),
    path('aceiteteDetail/<pk>', AceiteDetail.as_view(), name="AceiteDetail"),
    path('aceiteCreate/', AceiteCreate.as_view(), name="AceiteCreate"),
    path('aceiteUpdate/<pk>', AceiteUpdate.as_view(), name="AceiteUpdate"),
    path('aceiteDelete/<pk>', AceiteDelete.as_view(), name="AceiteDelete"),


    path('personalList/', PersonalList.as_view(), name="PersonalList"),
    path('personalDetail/<pk>', PersonalDetail.as_view(), name="PersonalDetail"),
    path('personalCreate/', PersonalCreate.as_view(), name="PersonalCreate"),
    path('personalUpdate/<pk>', PersonalUpdate.as_view(), name="PersonalUpdate"),
    path('personalDelete/<pk>', PersonalDelete.as_view(), name="PersonalDelete"),

    path('login', loginRequest, name="Login"),
    path('register', register, name="Register"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editRegister', editRegister, name="EditRegister"),
    path('agregarAvatar', agregarAvatar, name="AgregarAvatar"),

    path('contacto/', contacto, name="Contacto"),
]   
