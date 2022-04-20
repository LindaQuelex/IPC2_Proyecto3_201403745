
from django.urls import path, include
from . import views

urlpatterns={
    path('',views.home, name='index'),
    path('add.html/',views.add, name='add'),
    path('carga.html/',views.cargaMasiva, name='carga'),
    path('datosestudiante.html/',views.infoestudiante, name='datosestudiante'),
    path('docu.html/',views.docu, name='docu'),
    path('pruebamsg.html/',views.pruebamsg, name='pruebamsg'),
    path('reportePDF.html/',views.reportePDF, name='reportePDF'),
    path('resumenporfecha.html/',views.resumenporfecha, name='resumenporfecha'),

}