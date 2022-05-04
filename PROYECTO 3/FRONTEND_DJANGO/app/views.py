from bdb import GENERATOR_AND_COROUTINE_FLAGS
from multiprocessing import context
from urllib import response
from urllib.request import Request
from django.shortcuts import render
import requests
from app.forms import FileForm
from xml.etree import ElementTree as ET
import os
import webbrowser
from django.http import FileResponse
from fpdf import FPDF


# Create your views here.
import requests


class PDF(FPDF):
    pass

    def texts(self, name):
        with open(name, 'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,20.0)
        self.set_text_color(76.0,32.0,250.0)
        self.set_font('Arial','', 16)
        self.multi_cell(0,10,txt)

    def titles(self,title):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B',16)
        self.set_text_color(128,128,128)
        self.cell(w=210.0,h=20.0,align='C', txt=title, border=0 )


        


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
    ctx= {
        'content': None,
        'response': None,
    }
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
                ctx['response']='no se pudo realizar el análisis'
                
                
    else: 
        return render(request, 'pruebamensaje.html')


    return render(request, "pruebamensaje.html", ctx)

def reportePDF(request):
    generarPDF= PDF()
    generarPDF.add_page()
    print(generarPDF.texts('C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/LAB IPC2/PROYECTO 3/IPC2_Proyecto3_201403745/PROYECTO 3/ARCHIVO_SALIDA.xml'))
    generarPDF.titles('REPORTE')
    generarPDF.output('REPORTE.pdf','F')
    pdf=open('C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/LAB IPC2/PROYECTO 3/IPC2_Proyecto3_201403745/PROYECTO 3/FRONTEND_DJANGO/REPORTE.pdf','rb')

    return FileResponse(pdf) 
    

def reset(request):
    with open('C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/LAB IPC2/PROYECTO 3/IPC2_Proyecto3_201403745/PROYECTO 3/ARCHIVO_SALIDA.xml', 'r+') as f:
        f.truncate(0)
    return render(request,'carga.html')

def resumenporfecha(request):
    pass

def consulta(request):
    ctx= {
        'response': None,
    }

    if request.method=='GET':
        try:
            filename='C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/LAB IPC2/PROYECTO 3/IPC2_Proyecto3_201403745/PROYECTO 3/ARCHIVO_SALIDA.xml'
            salida =open(filename, encoding='utf-8')
            salida2=salida.read()
            print (salida2)
            ctx['response']= salida2
        except:
            ctx['response']='NO HAY BASE DE DATOS'
    return render(request, "consulta.html", ctx)


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
