from django import forms
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.contrib.auth.models import User
#from .views import UserCreationForm
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

class UserRegisterForm(UserCreationForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    username = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2','first_name','last_name']
        help_texts = {k: "" for k in fields}

    def clean_password(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError("Las contraseñas no coinciden!,verificar.")
        return password2

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','first_name', 'last_name']
        help_texts= {k:"" for k in fields}

    def clean_password(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError("Las contraseñas no coinciden!,verificar.")
        return password2