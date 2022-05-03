
from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.home, name='index'),
    path('add.html/',views.add, name='add'),
    path('carga/',views.cargaMasiva, name='carga'),
    path('datosestudiante/',views.infoestudiante, name='datosestudiante'),
    path('docu/',views.docu, name='docu'),
    path('pruebamensaje/',views.pruebamsg, name='pruebamsg'),
    #path('reportePDF.html/',views.reportePDF, name='reportePDF'),
    path('resumenporfecha.html/',views.resumenporfecha, name='resumenporfecha'),
    path('consulta/', views.consulta, name='consulta'),
    path('pdf/', views.reportePDF, name='reporte'),



]