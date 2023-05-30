from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from control_clinica.forms import *
from control_clinica.models import *

# Create your views here.
#Vistas de pacientes
class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name='control_clinica/lista_pacientes.html'

class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ('apellido', 'nombre', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_pacientes')

class PacienteDetailView(LoginRequiredMixin, DetailView):
    model = Paciente

class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ('apellido', 'nombre', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_pacientes')

class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('listar_pacientes')

#Vistas de diagnosticos
class DiagnosticoListView(LoginRequiredMixin, ListView):
    model = Diagnostico
    template_name='control_clinica/lista_diagnosticos.html'

class DiagnosticoCreateView(LoginRequiredMixin, CreateView):
    model = Diagnostico
    fields = ('enfermedad', 'estado')
    success_url = reverse_lazy('listar_diagnosticos')

class DiagnosticoDetailView(LoginRequiredMixin, DetailView):
    model = Diagnostico

class DiagnosticoUpdateView(LoginRequiredMixin, UpdateView):
    model = Diagnostico
    fields = ('enfermedad', 'estado')
    success_url = reverse_lazy('listar_diagnosticos')

class DiagnosticoDeleteView(LoginRequiredMixin, DeleteView):
    model = Diagnostico
    success_url = reverse_lazy('listar_diagnosticos')

#Vistas de doctores
class DoctoresListView(ListView):
    model = Doctor
    template_name='control_clinica/lista_doctores.html'

class DoctoresCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    fields = ('apellido', 'nombre', 'dni', 'email', 'telefono', 'especialidad', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_doctores')

class DoctoresDetailView(LoginRequiredMixin, DetailView):
    model = Doctor

class DoctoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    fields = ('apellido', 'nombre', 'dni', 'email', 'telefono', 'especialidad', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_doctores')

class DoctoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy('listar_doctores')

#Vistas de recetas
class RecetasListView(LoginRequiredMixin, ListView):
    model = Receta
    template_name='control_clinica/lista_recetas.html'

class RecetasCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    fields = ('medicamento', 'frecuencia_horaria', 'numero_dias')
    success_url = reverse_lazy('listar_recetas')

class RecetasDetailView(LoginRequiredMixin, DetailView):
    model = Receta

class RecetasUpdateView(LoginRequiredMixin, UpdateView):
    model = Receta
    fields = ('medicamento', 'frecuencia_horaria', 'numero_dias')
    success_url = reverse_lazy('listar_recetas')

class RecetasDeleteView(LoginRequiredMixin, DeleteView):
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

#Vista de citas
class CitasListView(LoginRequiredMixin, ListView):
    model = Cita
    template_name='control_clinica/lista_citas.html'

class CitasCreateView(LoginRequiredMixin, CreateView):
    model = Cita
    fields = ('titulo', 'especialidad', 'descripcion', 'fecha_cita')
    success_url = reverse_lazy('listar_citas')
    
class CitasDetailView(LoginRequiredMixin, DetailView):
    model = Cita

class CitasUpdateView(LoginRequiredMixin, UpdateView):
    model = Cita
    fields = ('titulo', 'especialidad', 'descripcion', 'fecha_cita')
    success_url = reverse_lazy('listar_citas')

class CitasDeleteView(LoginRequiredMixin, DeleteView):
    model = Cita
    success_url = reverse_lazy('listar_citas')

@login_required
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

@login_required
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

@login_required
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

# ACERCA DE MI
def about(request):
    return render(request, 'control_clinica/acerca_de_mi.html', {})