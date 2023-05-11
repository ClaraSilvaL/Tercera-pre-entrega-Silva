"""
URL configuration for sistema_clinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from control_clinica.views import listar_pacientes, listar_diagnosticos, registrar_diagnostico, listar_doctores, listar_recetas, \
    registrar_doctor, registrar_paciente, registrar_receta, buscar_doctor, buscar_paciente, buscar_estado, buscar_receta

urlpatterns = [
    path('pacientes/', listar_pacientes, name='listar_pacientes'),
    path('diagnosticos/', listar_diagnosticos, name='listar_diagnosticos'),
    path('doctores/', listar_doctores, name='listar_doctores'),
    path('recetas/', listar_recetas, name='listar_recetas'),
    path('registrar-diagnostico/', registrar_diagnostico, name='registrar_diagnostico'),
    path('registrar-doctor/', registrar_doctor, name='registrar_doctor'),
    path('registrar-paciente/', registrar_paciente, name='registrar_paciente'),
    path('registrar-receta/', registrar_receta, name='registrar_receta'),
    path('buscar-doctor/', buscar_doctor, name='buscar_doctor'),
    path('buscar-paciente/', buscar_paciente, name='buscar_paciente'),
    path('buscar-diagnostico/', buscar_estado, name='buscar_estado'),
    path('buscar-receta/', buscar_receta, name='buscar_receta'),
]