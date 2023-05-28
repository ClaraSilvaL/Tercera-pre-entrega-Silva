from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from control_clinica.forms import *
from control_clinica.models import *

# Create your views here.
#Vistas de pacientes
class PacienteListView(ListView):
    model = Paciente
    template_name='control_clinica/lista_pacientes.html'

class PacienteCreateView(CreateView):
    model = Paciente
    fields = ('apellido', 'nombre', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_pacientes')

class PacienteDetailView(DetailView):
    model = Paciente

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ('apellido', 'nombre', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_pacientes')

class PacienteDeleteView(DeleteView):
    model = Paciente
    success_url = reverse_lazy('listar_pacientes')

#Vistas de diagnosticos
class DiagnosticoListView(ListView):
    model = Diagnostico
    template_name='control_clinica/lista_diagnosticos.html'

class DiagnosticoCreateView(CreateView):
    model = Diagnostico
    fields = ('enfermedad', 'estado')
    success_url = reverse_lazy('listar_diagnosticos')

class DiagnosticoDetailView(DetailView):
    model = Diagnostico

class DiagnosticoUpdateView(UpdateView):
    model = Diagnostico
    fields = ('enfermedad', 'estado')
    success_url = reverse_lazy('listar_diagnosticos')

class DiagnosticoDeleteView(DeleteView):
    model = Diagnostico
    success_url = reverse_lazy('listar_diagnosticos')

#Vistas de doctores
class DoctoresListView(ListView):
    model = Doctor
    template_name='control_clinica/lista_doctores.html'

class DoctoresCreateView(CreateView):
    model = Doctor
    fields = ('apellido', 'nombre', 'dni', 'email', 'telefono', 'especialidad', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_doctores')

class DoctoresDetailView(DetailView):
    model = Doctor

class DoctoresUpdateView(UpdateView):
    model = Doctor
    fields = ('apellido', 'nombre', 'dni', 'email', 'telefono', 'especialidad', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_doctores')

class DoctoresDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('listar_doctores')

#Vistas de recetas
class RecetasListView(ListView):
    model = Receta
    template_name='control_clinica/lista_recetas.html'

class RecetasCreateView(CreateView):
    model = Receta
    fields = ('medicamento', 'frecuencia_horaria', 'numero_dias')
    success_url = reverse_lazy('listar_recetas')

class RecetasDetailView(DetailView):
    model = Receta

class RecetasUpdateView(UpdateView):
    model = Receta
    fields = ('medicamento', 'frecuencia_horaria', 'numero_dias')
    success_url = reverse_lazy('listar_recetas')

class RecetasDeleteView(DeleteView):
    model = Receta
    success_url = reverse_lazy('listar_recetas')

def buscar_doctor(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        doctores = Doctor.objects.filter(apellido__exact=busqueda)
        contexto = {
            "doctores": doctores,
        }
        http_response = render(
        request=request,
        template_name='control_clinica/lista_doctores.html',
        context=contexto,
    )
    return http_response

def buscar_paciente(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        pacientes = Paciente.objects.filter(apellido__exact=busqueda)
        contexto = {
            "pacientes": pacientes,
        }
        http_response = render(
        request=request,
        template_name='control_clinica/lista_pacientes.html',
        context=contexto,
    )
    return http_response

def buscar_estado(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        diagnosticos = Diagnostico.objects.filter(estado__exact=busqueda)
        contexto = {
            "diagnosticos": diagnosticos,
        }
        http_response = render(
        request=request,
        template_name='control_clinica/lista_diagnosticos.html',
        context=contexto,
    )
    return http_response

def buscar_receta(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        recetas = Receta.objects.filter(medicamento__exact=busqueda)
        contexto = {
            "recetas": recetas,
        }
        http_response = render(
        request=request,
        template_name='control_clinica/lista_recetas.html',
        context=contexto,
    )
    return http_response