from django import forms

class DiagnosticoFormulario(forms.Form):
    enfermedad = forms.CharField(required=True, max_length=164)
    estado = forms.CharField(required=True, max_length=164)

class PacienteFormulario(forms.Form):
    apellido = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    telefono = forms.CharField(required=False, max_length=20)
    dni = forms.CharField(required=True, max_length=32)
    fecha_nacimiento = forms.DateField(required=True)

class DoctorFormulario(forms.Form):
    apellido = forms.CharField(required=True, max_length=256)
    nombre = forms.CharField(required=True, max_length=256)
    dni = forms.CharField(required=True, max_length=32)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True, max_length=20)
    especialidad = forms.CharField(required=True, max_length=128)
    fecha_nacimiento = forms.DateField(required=True)

class RecetaFormulario(forms.Form):
    medicamento = forms.CharField(required=True, max_length=256)
    frecuencia_horaria = forms.CharField(required=True, max_length=5)
    numero_dias = forms.CharField(required=True, max_length=5)

class CitaFormulario(forms.Form):
    titulo = forms.CharField(max_length=256)
    especialidad = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=256)
    fecha_cita = forms.DateField()