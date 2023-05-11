from django.shortcuts import render

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

def registrar_diagnostico(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_clinica/formulario_diagnostico_a_mano.html',
        context=contexto,
    )
    return http_response