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