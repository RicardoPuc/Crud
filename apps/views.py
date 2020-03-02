from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class CreatePersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'apps/crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class ListPersona(ListView):
    model = Persona
    template_name = 'apps/listar_persona.html'

class UpdatePersona(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'apps/crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class DeletePersona(DeleteView):
    model = Persona
    template_name = 'apps/eliminar_persona.html'
    success_url = reverse_lazy('listar_persona')

