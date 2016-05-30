# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .forms import LoginForm, RegisterForm
from application.models import Perfil
from application.views import *


def vista_login(request):
    if request.method=='POST':
        form=LoginForm( request.POST)
        if form.is_valid():
            username = form.cleaned_data['usuari']
            password = form.cleaned_data['contrasenya']
            seguent = request.GET.get('next', default=None)
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if bool( seguent ):
                        return HttpResponseRedirect (seguent)
                    else:
                        return HttpResponseRedirect (reverse('exercicisapp:repartir'))
                else:
                    messages.error(request, 'Error, usuari inactiu.')
            else:
                messages.error(request, 'Error, usuari o contrasenya incorrectes.')
    else:
        form = LoginForm()

    form.helper = FormHelper()
    form.helper.form_class = 'blueForms'
    form.helper.label_class = 'col-lg-2'
    form.helper.field_class = 'col-lg-10'
    form.helper.add_input(Submit('submit', 'Entrar'))
    return render(request, 'login.html', {'form':form, 'pagetitle' : 'Login', 'titulo' : 'Login',})

def vista_logout(request):
    logout(request)
    return HttpResponseRedirect (reverse('exercicisapp:index'))

#@login_required
# Ha de ser profesor
def registrar(request):
    if(request.user.perfil.tipus.nom == 'professor'):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                #cleaned_data = form.cleaned_data
                username = form.cleaned_data['usuari']
                #email = cleaned_data.get('email')
                password = form.cleaned_data['contrasenya']
                first_name = form.cleaned_data['nom']
                last_name = form.cleaned_data['cognom']
                usuari = User()
                usuari.username = username
                usuari.set_password(password)
                #usuari.email = email
                usuari.first_name = first_name
                usuari.last_name = last_name
                usuari.save()
                perfil = Perfil.objects.get(usuari = usuari)
                perfil.tipus = form.cleaned_data['tipus']
                perfil.curs = form.cleaned_data['curs']
                perfil.save()
                messages.success(request, 'Usuari Registrat!')
                return HttpResponseRedirect(reverse('exercicisapp:repartir'))
            else:
                messages.error(request, "Usuari no existent!")
        else:

            form = RegisterForm()

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Entrar'))
        return render(request, 'login.html', {'form':form, 'pagetitle' : 'Registrar', 'titulo' : 'Registrar',})
    else:
        return HttpResponseRedirect (reverse('exercicisapp:index'))

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminarUser (request, iduser):
    print "si"
    user = get_object_or_404(User, pk=iduser)
    print "no"
    perfil = get_object_or_404(Perfil, usuari=iduser)
    print "wokrs"
    messages.success(request, 'User eliminat correctament')

    user.delete()
    perfil.delete()
    return HttpResponseRedirect(reverse('exercicisapp:llista'))
