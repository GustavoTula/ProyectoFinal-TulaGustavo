from django import forms

class VinoFormulario(forms.Form):
    vino = forms.CharField(max_length=50)
    varietal = forms.CharField()
    añada = forms.IntegerField()

class AceiteFormulario(forms.Form):
    aceite = forms.CharField(max_length=50)
    varietal = forms.CharField()

class EspumanteFormulario(forms.Form):
    espumante = forms.CharField(max_length=50)
    varietal = forms.CharField()
    añada = forms.IntegerField()

class PersonalFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField()
    cargo = forms.CharField()
    email = forms.EmailField()