from django import forms

#from django.forms.forms import forms



class FileForm(forms.Form):
    file= forms.FileField(label="file")

