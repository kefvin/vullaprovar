from django.conf.urls import url, include
from usuaris.views import *
from xmlcopygenerator.views import xmlcopygenerator
from application import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', vista_login, name="login"),
    url(r'^repartir$', views.repartir, name="repartir"),
    url(r'^sortir$', vista_logout, name="logout"),

    #ALUMNES
    url(r'^materies/$', views.materies, name='materies'),
    url(r'^materia/(?P<idmateria>[0-9]+)$', views.tria_exercici, name='asignatura'),
    url(r'^materia/(?P<idmateria>[0-9]+)/exercici/(?P<idexercici>[0-9]+)$', views.exercici, name='exercici'),

    #PROFESSORS
    url(r'^selectalumne/$', views.selectalumne, name='selectalumne'),
    url(r'^selectalumne/(?P<idalumne>[0-9]+)/materies_profesors/$', views.materies_profesors, name='materies_profesors'),
    url(r'^selectalumne/(?P<idalumne>[0-9]+)/materies_profesors/(?P<idmateria>[0-9]+)/escollir_exercici/$', views.escollir_exercici, name='escollir_exercici'),
    url(r'^selectalumne/(?P<idalumne>[0-9]+)/materies_profesors/(?P<idmateria>[0-9]+)/escollir_exercici/(?P<idexercici>[0-9]+)/corregir_exercici/$', views.corregir_exercici, name='corregir_exercici'),


    url(r'^register/$', registrar, name='createuser'),
    url(r'^addcurs/$', views.addcurs, name='addcurs'),
    url(r'^addmateria/$', views.addmateria, name='addmateria'),
    url(r'^addexercici/$', views.addexercici, name='addexercici'),
    url(r'^addresposta_possible/$', views.addresposta_possible, name='addresposta_possible'),

    #ADMIN
    url(r'^llista/$', views.llista, name='llista'),
    url(r'^addtipus/$', views.addtipus, name='addtipus'),
    url(r'^xmlcopygenerator/$', xmlcopygenerator, name='xmlcopygenerator'),
    url(r'^eliminarMateria/(?P<idmateria>[0-9]+)$', views.eliminarMateria, name='eliminarMateria'),
    url(r'^eliminarExercici/(?P<idexercici>[0-9]+)$', views.eliminarExercici, name='eliminarExercici'),
    url(r'^eliminarUser/(?P<iduser>[0-9]+)$', eliminarUser, name='eliminarUser'),
]
