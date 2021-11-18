from django.contrib import admin

# Register your models here.
from .models import Cliente, Cuenta

admin.site.register(Cliente)
admin.site.register(Cuenta)
