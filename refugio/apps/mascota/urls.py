
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from apps.mascota.views import listadousuarios, listado, index, mascota_views, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

from django.conf.urls import url
from . import views


urlpatterns = [
    #path('$/', index),
   #url(r'^$/', views.index, name='index'),
 
   #path('nuevo', views.mascota_views, name='mascota_crear'),
   #path('listar', views.mascota_list, name='mascota_listar'),
   #path('editar/<int:id_mascota>/', views.mascota_edit, name='mascota_editar'),
   #path('eliminar/<int:id_mascota>/', views.mascota_delete, name='mascota_eliminar'),
   path('mascota/', views.index, name = 'index'),
   
   #path('nuevo', MascotaCreate.as_view(), name='mascota_crear'),
   #path('listar', MascotaList.as_view(), name='mascota_listar'),
   #path('editar/<int:pk>/', MascotaUpdate.as_view(), name='mascota_editar'),
   #path('eliminar/<int:pk>/', MascotaDelete.as_view(), name='mascota_eliminar'),

   path('nuevo', login_required(MascotaCreate.as_view()), name='mascota_crear'),
   path('listar', login_required(MascotaList.as_view()), name='mascota_listar'),
   path('editar/<int:pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
   path('eliminar/<int:pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
   path('listado', views.listado, name = 'listado'),
   path('listadousuarios', views.listadousuarios, name = 'listadousuarios'),
]