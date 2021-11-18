from django.db import models

from apps.adopcion.models import Persona

# Create your models here.

class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self): 					# str es para python 3, para python 2.7 es unicode
		return '{}'.format(self.nombre)

class Mascota(models.Model):
	#folio = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=30)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	#vacuna = models.ManyToManyField(Vacuna)
	vacuna = models.ManyToManyField(Vacuna, blank=True)