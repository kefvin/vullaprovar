# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
#from utils import MarkdownTextField

#         PREGUNTAR AL DANI SI TIENE EL CORREO DEL MARKDOWN

# Create your models here.
class Perfil(models.Model):
#   ID
#   Usuari = models.CharField(max_length=50)
#   Password = models.CharField(max_length=50)
#   Nom = models.CharField(max_length=50)
   usuari = models.OneToOneField(User)
   tipus = models.ForeignKey('Tipus',null=True,blank=True)
   curs = models.ForeignKey('Curs',null=True,blank=True)

   def __unicode__(self):
       return u'%s' %(self.id)

class Tipus(models.Model):
    # ID
    nom = models.CharField(max_length=50) # Pofessor, alumne...

    def __unicode__(self):
        return u'%s' %(self.nom)

class Curs(models.Model):
    # ID
    nivell = models.IntegerField(unique=True)
    materia = models.ManyToManyField('Materia')

    def __unicode__(self):
        return u'%s' %(self.nivell)

class Materia(models.Model):
    # ID
    nom = models.CharField(max_length=50) # Mates, Catala....
    icon = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __unicode__(self):
        return u'%s' %(self.nom)

class Exercici (models.Model):
    # ID
    tema = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    enunciat = models.TextField(max_length=500)      #MarkdownTextField
    materia = models.ForeignKey('Materia')

    def __unicode__(self):
        return u'%s' %(self.id)



class Resposta_user(models.Model):
    # ID
    resposta = models.TextField(max_length=500)      #MarkdownTextField
    comentari_professor = models.TextField(max_length=500, null=True, blank=True)
    exercici = models.OneToOneField('Exercici')
    usuari = models.OneToOneField('Perfil')

    def __unicode__(self):
        return u'%s' %(self.id)

# signals.py
from django.db.models import signals
from django.dispatch import receiver

@receiver(signals.post_save, sender=User)
def assigna_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create( usuari = instance )
