from django.urls import path
from .views import CreatePersona, ListPersona, UpdatePersona, DeletePersona


urlpatterns=[

    path(r'crear_persona/', CreatePersona.as_view(), name='crear_persona'),
    path(r'listar_persona/', ListPersona.as_view(), name='listar_persona'),
    path(r'editar_persona/(?P<pk>\d+)/$', UpdatePersona.as_view(), name='editar_persona'),
    path(r'eliminar_persona/(?P<pk>\d+)/$', DeletePersona.as_view(), name='eliminar_persona'),





]