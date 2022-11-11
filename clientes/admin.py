from django.contrib import admin
from .models import Clientes, Tipo_cliente

# Register your models here.

admin.site.register([Clientes, Tipo_cliente])