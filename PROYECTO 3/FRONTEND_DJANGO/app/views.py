from multiprocessing import context
from django.shortcuts import render


# Create your views here.
import requests

endpoint='http://localhost:4000/'
def home(request):
    respon=requests.get(endpoint+'almacenardatosxml')
    # a=1
    print('que hace esto')
    return render(request,'index.html')


def add(request):
    pass

def infoestudiante(request):
    return render(request,'datosestudiante.html')

def docu(request):
    pass


def pruebamsg(request):
    pass

def reportePDF(request):
    pass

def resumenporfecha(request):
    pass

def cargaMasiva(request):
    ctx= {
        'content': None,
        'response': None,
    }
    return render(request,'carga.html',ctx)