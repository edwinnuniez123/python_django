from django.db import models

# Create your models here.
class Cliente(models.Model):
    numero_cliente = models.IntegerField()
    nombre1 = models.CharField(max_length=12)
    nombre2 = models.CharField(max_length=12, blank=True)
    apellido1 = models.CharField(max_length=12)
    apellido2 = models.CharField(max_length=12, blank=True)
    direccion = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    identidad = models.IntegerField(unique=True)
    lugar_nacimiento = models.CharField(max_length=30)
	
    OPCIONES_GENERO = (
	    ('M', 'MASCULINO'),
	    ('F', 'FEMENINO'),
	    ('O', 'OTRO')  # hay que ser inclusivos
	)

    genero = models.CharField(max_length=1, choices=OPCIONES_GENERO, default='M')

    



class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_cuenta = models.IntegerField(unique=True)
    tipo_moneda = models.CharField(max_length=12)
    saldo = models.DecimalField(max_digits=5, decimal_places=2)
    
    opciones_estado = (
	    ('A', 'Activo'),
	    ('B', 'Bloqueado')
	)
    estado = models.CharField(max_length=1, choices=opciones_estado, default='A')

    opciones_tipocuenta = (
	    ('A', 'Ahorro'),
	    ('C', 'Cheque')
	)
    tipo_cuenta = models.CharField(max_length=1, choices=opciones_tipocuenta, default='A')

    
    
