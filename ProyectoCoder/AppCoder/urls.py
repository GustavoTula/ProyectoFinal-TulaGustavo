from django.urls import path

from .views import aceites, vino , lista_vino , espumantes , lista_espumantes , aceites , lista_aceites

urlpatterns = [
    path('agrega-vino/<nombre>/<varietal>/<añada>', vino),
    path('lista-vino/', lista_vino),
    path('agrega-espumantes/<nombre>/<varietal>/<añada>', espumantes),
    path('lista-espumantes/', lista_espumantes),
    path('agrega-aceite/<nombre>/<varietal>', aceites),
    path('lista-aceite', lista_aceites),

]