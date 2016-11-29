from __future__ import unicode_literals 
from __future__ import absolute_import

from django.conf.urls import  url, include

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete


urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^nuevo2$', MascotaCreate.as_view(), name='mascota_crear2'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
    url(r'^listar2$', MascotaList.as_view(), name='mascota_listar2'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^editar2/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar2'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
    url(r'^eliminar2/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar2'),

]
