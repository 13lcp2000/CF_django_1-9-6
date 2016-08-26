from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

from apps.adopcion.models import Persona


# Create your models here.


class Vacuna(models.Model):
	"""docstring for ClassName"""
	nombre = models.CharField(max_length=50)

		

class Mascota(models.Model):
	"""clase que me permite generar una mascota"""
	folio = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	genero = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna)