# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.contrib.auth.decorators import user_passes_test

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from application.models import *

def index(request):
    return render(request, 'index.html')

@login_required
def repartir(request):
    if(request.user.perfil.tipus.nom == 'alumne'):
        return HttpResponseRedirect(reverse('exercicisapp:materies'))

    elif(request.user.perfil.tipus.nom == 'professor'):
        return HttpResponseRedirect(reverse('exercicisapp:selectalumne'))

    elif(request.user.perfil.tipus.nom == 'admin'):
        return HttpResponseRedirect(reverse('exercicisapp:index'))

        #########################################################################
        ####################### Views Navegacio Alumnes #########################
        #########################################################################

@login_required
def materies(request):
    if(request.user.perfil.tipus.nom == 'alumne' or request.user.perfil.tipus.nom == 'admin'):
        return render(request, 'application/Estudiant_Materia.html', {'materies': Materia.objects.all() })
    else:
        return HttpResponseRedirect(reverse('exercicisapp:index'))

@login_required
def tria_exercici(request, idmateria):
    if(request.user.perfil.tipus.nom == 'alumne' or request.user.perfil.tipus.nom == 'admin'):
        return render(request, 'application/Estudiant_Exercicis.html', {'exercicis': Exercici.objects.filter(materia = idmateria), 'materia': Materia.objects.get(id = idmateria), 'idmateria':idmateria})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:index'))


@login_required
def exercici(request, idmateria, idexercici):
    if(request.user.perfil.tipus.nom == 'alumne' or request.user.perfil.tipus.nom == 'admin'):

        try:
            resposta = Resposta_user.objects.get(exercici=idexercici, usuari = request.user.perfil)
        except Resposta_user.DoesNotExist:
            resposta = None

        esModificacio=(resposta!=None)
        addrespostaForm=modelform_factory(Resposta_user,exclude=(),)

        if not esModificacio:
           resposta=Resposta_user( usuari = request.user.perfil, exercici = idexercici)
        if request.method=='POST':
            form=addrespostaForm(request.POST, request.FILES, instance=resposta)
            if form.is_valid():
                resposta=form.save()
                messages.success(request,'resposta desat!')
                return HttpResponseRedirect(reverse('exercicisapp:asignatura', args = (idmateria,)))
            else:
                messages.error(request, 'Revisa els errors del formulari')
        else:
            form=addrespostaForm(instance=resposta);

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Desa'))
        return render(request, 'application/Exercici.html',
                              {'form':form,
                               'exercici':Exercici.objects.get(id=idexercici),
                               'idmateria':idmateria})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:index'))








    #########################################################################
    ##################### Views Navegacio Professors ########################
    #########################################################################

@login_required
def selectalumne(request):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):
        return render(request, 'application/Selecciona_alumne.html',
                               {'usuaris': User.objects.filter(perfil__curs = request.user.perfil.curs, perfil__tipus__nom = "alumne") })
    else:
        return HttpResponseRedirect(reverse('exercicisapp:index'))

@login_required
def materies_profesors(request, idalumne):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):
        return render(request, 'application/materies_profesors.html', {'materies': Materia.objects.all(), 'idalumne':idalumne})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:index'))

@login_required
def escollir_exercici(request, idalumne, idmateria):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):
        perfil = Perfil.objects.get(usuari__id=idalumne)
        resposta = get_object_or_404(Resposta_user, usuari = perfil.id)

        parametres =  {'exercicis': Exercici.objects.filter(materia__id = idmateria, resposta_user__usuari__id = perfil.id),
                       'materia': Materia.objects.get(id = idmateria),
                       'idalumne':idalumne,
                       'idmateria':idmateria}
        print idalumne
        return render(request,
                      'application/escollir_exercici_professor.html',
                      parametres,
                      )
    else:
        return HttpResponseRedirect(reverse('exercicisapp:index'))


@login_required
def corregir_exercici(request, idalumne, idmateria, idexercici):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):

        print idalumne
        perfil = Perfil.objects.get(usuari__id=idalumne)
        try:
            resposta = Resposta_user.objects.get(exercici__id=idexercici, usuari = perfil.id)
        except Resposta_user.DoesNotExist:
            resposta = None

        addrespostaForm=modelform_factory(Resposta_user,exclude=(),)


        if request.method=='POST':
            form=addrespostaForm(request.POST, request.FILES, instance=resposta)
            if form.is_valid():
                resposta=form.save()
                messages.success(request,'Corretgit!')
                return HttpResponseRedirect(reverse('exercicisapp:selectalumne'))
            else:
                messages.error(request, 'Revisa els errors del formulari')
        else:
            form=addrespostaForm(instance=resposta);

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Desa'))
        return render(request, 'application/corregir_exercici.html',
                               {'form':form,
                               'exercici':Exercici.objects.get(id=idexercici),
                               'idmateria':idmateria,
                               'idalumne':idalumne})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:index'))






        #########################################################################
        ########################## Views Formularis #############################
        #########################################################################


@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def addtipus(request, tipus_id=None):
    if(request.user.perfil.tipus.nom == 'admin'):
        esModificacio=(tipus_id!=None)
        addtipusForm=modelform_factory(Tipus,exclude=(),)
        if esModificacio:
            tipus=get_object_or_404(Tipus,pk=tipus_id)
        else:
            tipus=Tipus()
        if request.method=='POST':
            form=addtipusForm(request.POST, request.FILES, instance=tipus)
            if form.is_valid():
                tipus=form.save()
                messages.success(request,'tipus desat!')
                return HttpResponseRedirect(reverse('exercicisapp:materies'))
            else:
                messages.error(request, 'Revisa els errors del formulari')
        else:
            form=addtipusForm(instance=tipus);

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Afegir'))
        return render(request, 'form.html', {'form':form, 'actual':"Afegir Tipus"})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:repartir'))

@login_required
def addcurs(request, curs_id=None):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):
        esModificacio=(curs_id!=None)
        addcursForm=modelform_factory(Curs,exclude=(),)
        if esModificacio:
            curs=get_object_or_404(Curs,pk=curs_id)
        else:
            curs=Curs()
        if request.method=='POST':
            form=addcursForm(request.POST, request.FILES, instance=curs)
            if form.is_valid():
                curs=form.save()
                messages.success(request,'curs desat!')
                return HttpResponseRedirect(reverse('exercicisapp:materies'))
            else:
                messages.error(request, 'Revisa els errors del formulari')
        else:
            form=addcursForm(instance=curs);

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Afegir'))
        return render(request, 'form.html', {'form':form, 'actual':"Afegir Curs"})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:repartir'))

@login_required
def addmateria(request, materia_id=None):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):
        esModificacio=(materia_id!=None)
        addmateriaForm=modelform_factory(Materia,exclude=(),)
        if esModificacio:
            materia=get_object_or_404(Materia,pk=materia_id)
        else:
            materia=Materia()
        if request.method=='POST':
            form=addmateriaForm(request.POST, request.FILES, instance=materia)
            if form.is_valid():
                materia=form.save()
                messages.success(request,'materia desat!')
                return HttpResponseRedirect(reverse('exercicisapp:addmateria'))
            else:
                messages.error(request, 'Revisa els errors del formulari')
        else:
            form=addmateriaForm(instance=materia);

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Afegir'))
        return render(request, 'form.html', {'form':form, 'actual':"Afegir Matèria"})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:repartir'))

@login_required
def addexercici(request, exercici_id=None):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):
        esModificacio=(exercici_id!=None)
        addexerciciForm=modelform_factory(Exercici,exclude=(),)
        if esModificacio:
            exercici=get_object_or_404(Exercici,pk=exercici_id)
        else:
            exercici=Exercici()
        if request.method=='POST':
            form=addexerciciForm(request.POST, request.FILES, instance=exercici)
            if form.is_valid():
                exercici=form.save()
                messages.success(request,'exercici desat!')
                return HttpResponseRedirect(reverse('exercicisapp:addexercici'))
            else:
                messages.error(request, 'Revisa els errors del formulari')
        else:
            form=addexerciciForm(instance=exercici);

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Afegir'))
        return render(request, 'form.html', {'form':form, 'actual':"Afegir Exercici"})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:repartir'))

@login_required
def addresposta_possible(request, resposta_possible_id=None):
    if(request.user.perfil.tipus.nom == 'professor' or request.user.perfil.tipus.nom == 'admin'):
        esModificacio=(resposta_possible_id!=None)
        addresposta_possibleForm=modelform_factory(Resposta_possible,exclude=(),)
        if esModificacio:
            resposta_possible=get_object_or_404(Resposta_possible,pk=resposta_possible_id)
        else:
            resposta_possible=Resposta_possible()
        if request.method=='POST':
            form=addresposta_possibleForm(request.POST, request.FILES, instance=resposta_possible)
            if form.is_valid():
                resposta_possible=form.save()
                messages.success(request,'resposta_possible desat!')
                return HttpResponseRedirect(reverse('exercicisapp:addresposta_possible'))
            else:
                messages.error(request, 'Revisa els errors del formulari')
        else:
            form=addresposta_possibleForm(instance=resposta_possible);

        form.helper = FormHelper()
        form.helper.form_class = 'blueForms'
        form.helper.label_class = 'col-lg-2'
        form.helper.field_class = 'col-lg-10'
        form.helper.add_input(Submit('submit', 'Afegir'))
        return render(request, 'form.html', {'form':form})
    else:
        return HttpResponseRedirect(reverse('exercicisapp:repartir'))



@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminarMateria (request, idmateria):
    materia = get_object_or_404(Materia, pk=idmateria)
    messages.success(request, 'Materia eliminada correctament')

    materia.delete()
    return HttpResponseRedirect(reverse('exercicisapp:llista'))

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminarExercici (request, idexercici):
    exercici = get_object_or_404(Exercici, pk=idexercici)
    messages.success(request, 'Exercici eliminat correctament')

    exercici.delete()
    return HttpResponseRedirect(reverse('exercicisapp:llista'))

@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def llista(request):
    return render(request, 'llista.html', {'materies': Materia.objects.all(), 'usuaris': User.objects.all(), 'exercicis': Exercici.objects.all() })
