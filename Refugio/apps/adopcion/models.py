from __future__ import unicode_literals

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