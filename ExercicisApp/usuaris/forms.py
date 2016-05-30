from django import forms
from django.forms import ModelChoiceField
from application.models import Tipus, Curs
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    usuari = forms.CharField(max_length=100)
    contrasenya = forms.CharField(max_length=200,widget=forms.PasswordInput)
#    nom = forms.CharField(max_length=50)
#    cognom = forms.CharField(max_length=100)


class RegisterForm(forms.Form):
    usuari = forms.CharField(max_length=100)
    contrasenya = forms.CharField(max_length=200,widget=forms.PasswordInput)
    nom = forms.CharField(max_length=50)
    cognom = forms.CharField(max_length=100)
    #email = forms.EmailField(max_length=100,)
    tipus = forms.ModelChoiceField(queryset=Tipus.objects.all(), empty_label=None)    # A LO MEJOR TENGO QUE PONER PERFIL.TIPUS
    curs = forms.ModelChoiceField(queryset=Curs.objects.all(), empty_label=None)      # SALEN MUCHOS CURSOS IGUALES PORQUE MUCHAS MATERIAS
                                                                                      # ESTAN EN UN CURSO
