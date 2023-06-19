from django import forms
from .models import Notebook

class formulario_api(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = '__all__'

class BuscarNotebooksForm(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)