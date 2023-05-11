from django.shortcuts import render, redirect
from django.urls import reverse

from control_clinica.models import *

# Create your views here.

def listar_pacientes(request):
    contexto = {
        "pacientes": Paciente.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_clinica/lista_pacientes.html',
        context=contexto,
    )
    return http_response

def listar_diagnosticos(request):
    contexto = {
        "diagnosticos": Diagnostico.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_clinica/lista_diagnosticos.html',
        context=contexto,
    )
    return http_response

def listar_doctores(request):
    contexto = {
        "doctores": Paciente.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_clinica/lista_doctores.html',
        context=contexto,
    )
    return http_response

def listar_recetas(request):
    contexto = {
        "recetas": Receta.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_clinica/lista_recetas.html',
        context=contexto,
    )
    return http_response

def registrar_diagnostico(request):
    if request.method == "POST":
        data = request.POST #es un diccionario
        enfermedad = data["enfermedad"]
        estado = data["estado"]
        diagnostico = Diagnostico(enfermedad = enfermedad, estado = estado) #Creacion en la RAM
        diagnostico.save() #Almacenamiento en la base de datos
        #Redireccion al usuario a lista de diagnosticos
        url_exitosa = reverse('listar_diagnosticos')
        return redirect(url_exitosa)
    else: #GET
        http_response = render(
        request=request,
        template_name='control_clinica/formulario_diagnostico_a_mano.html',
        #context=contexto,
    )
    return http_response