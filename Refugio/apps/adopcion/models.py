from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models

# Create your models here.

class Persona(models.Model):
	"""Clase que me permite generar una persona"""
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()
	
	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg

	def __unicode__(self):
		return '{} {}'.format(self.nombre, self.apellidos)


class Solicitud(models.Model):
	"""esta es la solicitud"""
	persona = models.ForeignKey(Persona, null=True, blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()

