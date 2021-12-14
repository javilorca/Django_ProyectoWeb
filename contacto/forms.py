from django import forms

class FormularioContacto(forms.Form):

    nombre= forms.CharField(label='Nombre', required=True, max_length=30)

    email= forms.CharField(label='Email', required=True, max_length=40)

    contenido=forms.CharField(label="Contenido", widget=forms.Textarea ,max_length=300)