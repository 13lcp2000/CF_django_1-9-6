from __future__ import unicode_literals 
from __future__ import absolute_import

from django import forms

from apps.mascota.models import Mascota 
from apps.adopcion.models import Solicitud

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'genero',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]

		labels = {			
			'nombre': 'Nombre',
			'genero': 'Genero',
			'edad_aproximada': 'Edad Proximada',
			'fecha_rescate': 'Fecha de Rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'genero': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}
			