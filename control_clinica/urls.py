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

from control_clinica.views import buscar_doctor, buscar_paciente, buscar_estado, buscar_receta, \
    PacienteListView, PacienteCreateView, PacienteDetailView, PacienteDeleteView, PacienteUpdateView, \
    DiagnosticoListView, DiagnosticoCreateView, DiagnosticoDetailView, DiagnosticoDeleteView, DiagnosticoUpdateView, \
    DoctoresListView, DoctoresCreateView, DoctoresDetailView, DoctoresDeleteView, DoctoresUpdateView, \
    RecetasListView, RecetasCreateView, RecetasDetailView, RecetasDeleteView, RecetasUpdateView

urlpatterns = [
    #URLS de pacientes
    path('pacientes/', PacienteListView.as_view(), name='listar_pacientes'),
    path("pacientes/<int:pk>", PacienteDetailView.as_view(), name="ver_paciente"),
    path("registrar-pacientes/", PacienteCreateView.as_view(), name="registrar_paciente"),
    path("editar-paciente/<int:pk>", PacienteUpdateView.as_view(), name="editar_paciente"),
    path("eliminar-paciente/<int:pk>", PacienteDeleteView.as_view(), name="eliminar_paciente"),
    path('buscar-paciente/', buscar_paciente, name='buscar_paciente'),
    #URLS de diagnostico
    path('diagnosticos/', DiagnosticoListView.as_view(), name='listar_diagnosticos'),
    path("diagnosticos/<int:pk>", DiagnosticoDetailView.as_view(), name="ver_diagnostico"),
    path("registrar-diagnosticos/", DiagnosticoCreateView.as_view(), name="registrar_diagnostico"),
    path("editar-diagnostico/<int:pk>", DiagnosticoUpdateView.as_view(), name="editar_diagnostico"),
    path("eliminar-diagnostico/<int:pk>", DiagnosticoDeleteView.as_view(), name="eliminar_diagnostico"),
    path('buscar-diagnostico/', buscar_estado, name='buscar_estado'),
    #URLS de doctores
    path('doctores/', DoctoresListView.as_view(), name='listar_doctores'),
    path("doctores/<int:pk>", DoctoresDetailView.as_view(), name="ver_doctor"),
    path("registrar-doctores/", DoctoresCreateView.as_view(), name="registrar_doctor"),
    path("editar-doctor/<int:pk>", DoctoresUpdateView.as_view(), name="editar_doctor"),
    path("eliminar-doctor/<int:pk>", DoctoresDeleteView.as_view(), name="eliminar_doctor"),
    path('buscar-doctor/', buscar_doctor, name='buscar_doctor'),
    #URLS de recetas
    path('recetas/', RecetasListView.as_view(), name='listar_recetas'),
    path("recetas/<int:pk>", RecetasDetailView.as_view(), name="ver_receta"),
    path("registrar-recetas/", RecetasCreateView.as_view(), name="registrar_receta"),
    path("editar-receta/<int:pk>", RecetasUpdateView.as_view(), name="editar_receta"),
    path("eliminar-receta/<int:pk>", RecetasDeleteView.as_view(), name="eliminar_receta"),
    path('buscar-receta/', buscar_receta, name='buscar_receta'),
]