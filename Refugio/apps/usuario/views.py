from __future__ import unicode_literals
from __future__ import absolute_import
#from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import RegistroForm

# Create your views here.

class RegistroUsuario(CreateView):
	"""vista basada en clase para crear un Usuario"""
	model = User
	template_name = "usuario/registrar2.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')