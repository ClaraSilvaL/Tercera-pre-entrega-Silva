from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def saludar(request):
    saludo = "Bienvenido al sistema"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='control_clinica/base.html',
        context=contexto,
    )
    return http_responde

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_clinica/index.html',
        context=contexto,
    )
    return http_response