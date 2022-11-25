
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar
import datetime



#from .views import UserCreationForm
class VinoFormulario(forms.Form):
    vino = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Marca/Etiqueta",
                "required": "false",
            }
        )
    )
    varietal = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Tipo de uva/s utilizado",
                "required": "false",
            }      
        )
    )
    añada = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Año cosecha del vino",
                "required":"false"  
            }
        )
    )

class AceiteFormulario(forms.Form):
    aceite = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Marca/Etiqueta",
                "required": "false",
            }
        )
    )
    
    varietal = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Metodo de aceituna utilizada",
                "required": "false",
            }
        )

    )

class EspumanteFormulario(forms.Form):
    espumante = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Marca/Etiqueta",
                "required": "false",
            }
        )
    )
    varietal = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Tipo de uva/s utilizado",
                "required": "false",
            }      
        )

    )
    añada = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Año cosecha del vino",
                "required":"false"  
            }
        )
    )

class PersonalFormulario(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Nuevo miembro...",
                "required": "false",
            }
        )
    )
    apellido = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Apellido...",
                "required": "false",
            }
        )
    )
    cargo = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Puesto de trabajo...",
                "required": "false",
            }
        )
    )
    email = forms.EmailField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Correo electronico...",
                "required": "false",
            }
        )
    )



class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ('imagen',)


class UserRegisterForm(UserCreationForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    username = forms.CharField(label='Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    #avatar =forms.ImageField()
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2','first_name','last_name']
        help_texts = {k: "" for k in fields}
        unique_together = ['username', 'email', 'password1','password2','first_name','last_name']
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
        unique_together = ['username', 'email', 'password1','password2','first_name','last_name']
    def clean_password(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError("Las contraseñas no coinciden!,verificar.")
        return password2


class ContactoFormulario(forms.Form):
    
    asunto=forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Motivo del correo...",
                "required": "false",
            }
        )



    )
    email=forms.EmailField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "comment-text",
                "placeholder":"Correo electronico...",
                "required": "false",
            }
        )    
    )
    mensaje=forms.CharField(
        label="Mensaje",
        required=False,
        max_length="500",
        min_length="10",
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class":"comment-text",
                "placeholder":"Escribe aqui tus comentarios...",
                "required":"True",
                "cols": "30",
                "rows":"5",
             }
        )
    )
    
class DateForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today) 
      
