from django import forms

class formulario_api(forms.Form):
    USUARIO = forms.CharField()
    DNI = forms.IntegerField()