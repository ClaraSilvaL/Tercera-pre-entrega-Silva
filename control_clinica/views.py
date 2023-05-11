from django.shortcuts import render, redirect
from django.urls import reverse

from control_clinica.forms import *
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
        "doctores": Doctor.objects.all(),
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

def registrar_diagnostico_version_1(request):
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

def registrar_diagnostico(request):
    if request.method == "POST":
        formulario = DiagnosticoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            enfermedad = data["enfermedad"]
            estado = data["estado"]
            diagnostico = Diagnostico(enfermedad = enfermedad, estado = estado) #Creacion en la RAM
            diagnostico.save() #Almacenamiento en la base de datos
            
            #Redireccion al usuario a lista de diagnosticos
            url_exitosa = reverse('listar_diagnosticos')
            return redirect(url_exitosa)
        
    else: #GET
        formulario = DiagnosticoFormulario()
    http_response = render(
        request=request,
        template_name='control_clinica/formulario_diagnostico.html',
        context={'formulario': formulario},
    )
    return http_response

def registrar_doctor(request):
    if request.method == "POST":
        formulario_doctor = DoctorFormulario(request.POST)

        if formulario_doctor.is_valid():
            data = formulario_doctor.cleaned_data
            apellido = data["apellido"]
            nombre = data["nombre"]
            dni = data["dni"]
            email = data["email"]
            telefono = data["telefono"]
            especialidad = data["especialidad"]
            fecha_nacimiento = data["fecha_nacimiento"]
            doctor = Doctor(apellido = apellido, nombre = nombre, dni = dni, email = email, telefono = telefono, especialidad = especialidad, fecha_nacimiento = fecha_nacimiento) #Creacion en la RAM
            doctor.save() #Almacenamiento en la base de datos
            
            #Redireccion al usuario a lista de diagnosticos
            url_exitosa = reverse('listar_doctores')
            return redirect(url_exitosa)
        
    else: #GET
        formulario_doctor = DoctorFormulario()
    http_response = render(
        request=request,
        template_name='control_clinica/formulario_doctor.html',
        context={'formulario_doctor': formulario_doctor},
    )
    return http_response

def registrar_paciente(request):
    if request.method == "POST":
        formulario_paciente = PacienteFormulario(request.POST)

        if formulario_paciente.is_valid():
            data = formulario_paciente.cleaned_data
            apellido = data["apellido"]
            nombre = data["nombre"]         
            telefono = data["telefono"]
            dni = data["dni"]
            fecha_nacimiento = data["fecha_nacimiento"]
            paciente = Paciente(apellido = apellido, nombre = nombre, telefono = telefono, dni = dni, fecha_nacimiento = fecha_nacimiento) #Creacion en la RAM
            paciente.save() #Almacenamiento en la base de datos
            
            #Redireccion al usuario a lista de diagnosticos
            url_exitosa = reverse('listar_pacientes')
            return redirect(url_exitosa)
        
    else: #GET
        formulario_paciente = PacienteFormulario()
    http_response = render(
        request=request,
        template_name='control_clinica/formulario_paciente.html',
        context={'formulario_paciente': formulario_paciente},
    )
    return http_response

def registrar_receta(request):
    if request.method == "POST":
        formulario = RecetaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            medicamento = data["medicamento"]
            frecuencia_horaria = data["frecuencia_horaria"]
            numero_dias = data["numero_dias"]
            receta = Receta(medicamento = medicamento, frecuencia_horaria = frecuencia_horaria, numero_dias = numero_dias) #Creacion en la RAM
            receta.save() #Almacenamiento en la base de datos
            
            #Redireccion al usuario a lista de diagnosticos
            url_exitosa = reverse('listar_recetas')
            return redirect(url_exitosa)
        
    else: #GET
        formulario_receta = RecetaFormulario()
    http_response = render(
        request=request,
        template_name='control_clinica/formulario_receta.html',
        context={'formulario_receta': formulario_receta},
    )
    return http_response