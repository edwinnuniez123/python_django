from django.urls import path

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from django.conf.urls import url
from . import views


urlpatterns = [
    #path('index$/', index_adopcion),
    path('adopcion/index', views.index_adopcion, name='index_adopcion'),
    #url(r'^adopcion/index$', views.index_adopcion, name='index_adopcion'),
    path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<int:pk>/', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<int:pk>/', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]