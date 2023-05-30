from django.test import TestCase

from control_clinica.models import Cita
# Create your tests here.

class CitaTests(TestCase):

    def test_creacion_cita(self):
        #caso uso esperado
        cita = Cita(titulo="Dolor de cabeza", especialidad="Pediatria", descripcion="Malestar general", fecha_cita="2023-05-29")
        cita.save()

        #Comprueba que la cita fue guardada
        self.assertEqual(Cita.objects.count(), 1)
        self.assertIsNotNone(cita.id)

    def test_creacion_cita_1(self):
        #caso uso esperado
        cita = Cita(titulo="Dolor de cabeza", especialidad="Odontologia", descripcion="Malestar general", fecha_cita="2023-05-29")
        cita.save()

        #Comprueba que la cita fue guardada
        self.assertEqual(Cita.objects.count(), 0)
        