from django.shortcuts import render

# Create your views here.
def listar_pacientes(request):
    contexto = {
        "pacientes": [
            {"nombre": "Eva", "apellido": "Garcia"},
            {"nombre": "Valeria", "apellido": "Rojas"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_clinica/lista_pacientes.html',
        context=contexto,
    )
    return http_responde

def listar_diagnosticos(request):
    contexto = {
        "diagnosticos": [
            {"enfermedad": "Gripe", "estado": "leve"},
            {"enfermedad": "Gripe", "estado": "moderado"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_clinica/lista_diagnosticos.html',
        context=contexto,
    )
    return http_responde