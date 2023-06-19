from django import forms

class formulario_api(forms.Form):
    USUARIO = forms.CharField()
    DNI = forms.IntegerField()

class Buscaformulario_api(forms.Form):
    dni = forms.CharField()

