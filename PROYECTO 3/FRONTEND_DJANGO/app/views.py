from django.shortcuts import render

# Create your views here.
import requests

endpoint='http://localhost:4000/'
def home(request):
    respon=requests.get(endpoint+'showpositivos')