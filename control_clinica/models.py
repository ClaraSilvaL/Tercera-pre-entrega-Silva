from django.db import models

# Create your models here.
class Diagnostico(models.Model):
    enfermedad = models.CharField(max_length=164)
    estado = models.CharField(max_length=164)
    
    def __str__(self):
        return f"{self.enfermedad} | {self.estado}"

class Paciente(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Doctor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Receta(models.Model):
    medicamento = models.CharField(max_length=256)
    frecuencia_horaria = models.CharField(max_length=5)
    numero_dias = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.medicamento} | frec. horaria: {self.frecuencia_horaria} | nro dias: {self.numero_dias}"