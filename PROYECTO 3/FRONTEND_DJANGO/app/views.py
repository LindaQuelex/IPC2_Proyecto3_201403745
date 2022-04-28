from multiprocessing import context
from urllib import response
from urllib.request import Request
from django.shortcuts import render
import requests
from app.forms import FileForm
from xml.etree import ElementTree as ET


# Create your views here.
import requests

endpoint='http://localhost:4000/'
def home(request):
    respon=requests.post(endpoint+'almacenardatosxml')
    # a=1
    print('que hace esto')
    return render(request,'index.html')

def add(request):
    pass

def infoestudiante(request):

    return render(request,'datosestudiante.html')

def docu(request):
    
    return render(request, 'docu.html')

def pruebamsg(request):
     
     return render(request, "pruebamensaje.html")

def reportePDF(request):
    pass

def resumenporfecha(request):
    pass

def cargaMasiva(request):
    ctx= {
        'content': None,
        'response': None,
    }
    # if Request.method== 'GET':
    #     form =FileForm()

    if request.method=='POST':
        form=FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            print(request.FILES)
            xml_binary=f.read()#.decode('UTF-8')
       

            print(xml_binary)
            xml=xml_binary.decode('UTF-8')
            ctx['content']=xml
            response = requests.post(endpoint+'almacenardatosxml', data=xml_binary)
 
            if response.ok:
                # archivosalida=open('ARCHIVO_SALIDA.xml','w',encoding='utf-8')
                # archivosalida.close()
                filename='C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/LAB IPC2/PROYECTO 3/IPC2_Proyecto3_201403745/PROYECTO 3/ARCHIVO_SALIDA.xml'
                salida =open(filename, encoding='utf-8')
                salida2=salida.read()
                print (salida2)
                ctx['response']= salida2
                
    else: 
        return render(request, 'carga.html')
    return render(request,'carga.html',ctx)
