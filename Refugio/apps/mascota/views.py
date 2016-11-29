from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

# Create your views here.

def index(request):
	#return HttpResponse("This is the index funtion working xD")
	#return render(request, 'mascota/index.html')#
	return render(request, 'base/base2.html')

def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
	"""Esta vista ordena la matriz mascotas"""
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

class MascotaList(ListView):
	"""Esta vista no ordena matricez y es una vista basada en clase"""
	model = Mascota
	template_name = 'mascota/mascota_list2.html'

class MascotaCreate(CreateView):
	"""Esta la vista basada en clase de las mascotas"""
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form2.html'
	success_url = reverse_lazy('mascota:mascota_listar2')

class MascotaUpdate(UpdateView):
	"""clase para actualizar la mascota"""
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form2.html'
	success_url = reverse_lazy('mascota:mascota_listar2')

class MascotaDelete(DeleteView):
	"""clase para eliminar la mascota del sistema"""
	model = Mascota
	#form_class = MascotaForm
	template_name = 'mascota/mascota_delete2.html'
	success_url = reverse_lazy('mascota:mascota_listar2')		