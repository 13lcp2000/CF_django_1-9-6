from __future__ import unicode_literals 
from __future__ import absolute_import
from django import forms

from apps.adopcion.models import Persona, Solicitud

class SolicitudForm(forms.ModelForm):
	
	class Meta:
		model = Solicitud

		fields =[
			'numero_mascotas',
			'razones',
		]

		labels = {
			'numero_mascotas': 'Numero de mascotas',
			'razones': 'Razones para adoptar'
		}

		widgets = {
			'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
			'razones': forms.Textarea(attrs={'class':'form-control'}),
		}

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields=[
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]
		labels={
			'nombre':'Nombre',
			'apellidos':'Apellidos',
			'edad':'Edad',
			'telefono':'Telefono',
			'email':'Correo Electronico',
			'domicilio':'Domicilio',
		}
		widgets={
			'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
			'razones':forms.Textarea(attrs={'class':'form-control'}),
		}
