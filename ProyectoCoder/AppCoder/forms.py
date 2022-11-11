from django import forms
#from django.contrib.auth.forms import UserCreationForm
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

#class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    #class Meta:
        #model = User
        #fields = ['username', 'email', 'password1','password2']
        #help_texts = {k: "" for k in fields}
        