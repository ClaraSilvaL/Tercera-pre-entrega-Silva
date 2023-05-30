from django.contrib import admin

from control_clinica.models import *
# Register your models here.
admin.site.register(Diagnostico)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Receta)
admin.site.register(Cita)