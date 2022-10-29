from django.urls import path
from .views import aceites, inicio, nosotros, noticias, vino , lista_vino , espumante , lista_espumante , aceite , lista_aceite, vinos, espumantes

urlpatterns = [
    path('agrega-vino/<nombre>/<varietal>/<añada>', vino),
    path('lista-vino/', lista_vino),
    path('agrega-espumantes/<nombre>/<varietal>/<añada>', espumante),
    path('lista-espumantes/', lista_espumante),
    path('agrega-aceite/<nombre>/<varietal>', aceite),
    path('lista-aceite', lista_aceite),

    path('', inicio, name= "Inicio"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('vinos/', vinos, name="Vinos"),
    path('espumantes/', espumantes, name="Espumantes"),
    path('aceites/', aceites, name="Aceites"),
    path('equipo/', espumantes, name="Espumantes"),
    path('noticias/', noticias, name="Noticias"),


]