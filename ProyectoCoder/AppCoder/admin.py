from django.contrib import admin
from .models import *


class VinoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'varietal','añada',]
    search_fields = ['nombre', 'varietal','añada',]
    list_filter = ['nombre', 'varietal','añada',]

class EspumanteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'varietal','añada',]
    search_fields = ['nombre', 'varietal','añada',]
    list_filter = ['nombre', 'varietal','añada',]

class AceiteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'varietal',]
    search_fields = ['nombre', 'varietal',]
    list_filter = ['nombre', 'varietal',]

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','cargo','email',]
    search_fields = ['nombre', 'apellido','cargo','email',]
    list_filter = ['nombre', 'apellido','cargo','email',]

admin.site.register(Vino, VinoAdmin)

admin.site.register(Espumante, EspumanteAdmin)

admin.site.register(Aceite, AceiteAdmin)

admin.site.register(Personal, PersonalAdmin)

admin.site.register(Avatar)