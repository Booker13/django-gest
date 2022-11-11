from django.db import models

# Create your models here.

# Tabla - Tipo de cliente.
class Tipo_cliente(models.Model):
    tipo_cliente = models.CharField(max_length = 65, verbose_name = 'Tipo de Cliente')
    
    def __str__(self):
        return self.tipo_cliente

    class Meta:
        verbose_name = 'Tipos de Cliente'
        verbose_name_plural = 'Tipos de Clientes'
        ordering = ['id']

# Tabla - Clientes.
class Clientes(models.Model):
        # Identificación.
    nombre_cliente = models.CharField(max_length=65, verbose_name='Nombre o Razón Social')
    cifnif_cliente = models.CharField(max_length=15, verbose_name='NIF/CIF')
    tipo_cliente = models.ForeignKey(Tipo_cliente, on_delete=models.CASCADE, verbose_name='Tipo de Cliente')
        # Contacto 1.
    dir_cliente = models.CharField(max_length=65, null=True, blank=True, verbose_name='Dirección')
    pob_cliente = models.CharField(max_length=30, null=True, blank=True, verbose_name='Población')
    cpo_cliente = models.CharField(max_length=10, null=True, blank=True, verbose_name='Código Postal')
    pro_cliente = models.CharField(max_length=30, null=True, blank=True, verbose_name='Provincia')
    pai_cliente = models.CharField(max_length=30, null=True, blank=True, verbose_name='País')
        # Contacto 2.
    pco_cliente = models.CharField(max_length=65, null=True, blank=True, verbose_name='Persona de Contacto')
    tel1_cliente = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono 1')
    tel2_cliente = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono 2')
    fax_cliente = models.CharField(max_length=20, null=True,  blank=True, verbose_name='Fax')
    mov1_cliente = models.CharField(max_length=20, null=True, blank=True, verbose_name='Móvil 1')
    mov2_cliente = models.CharField(max_length=20, null=True, blank=True, verbose_name='Móvil 2')
    wha_cliente = models.CharField(max_length=20, null=True, blank=True, verbose_name='Whatsapp')
    email_cliente = models.EmailField(max_length=200, null=True, blank=True, verbose_name='Email')
    url_cliente = models.URLField(max_length=200, null=True, blank=True, verbose_name='Web')
        # Redes Sociales.
    fcb_cliente = models.URLField(max_length=200, null=True, blank=True, verbose_name='Facebook')
    twi_cliente = models.URLField(max_length=200, null=True, blank=True, verbose_name='Twitter')
    ins_cliente = models.URLField(max_length=200, null=True, blank=True, verbose_name='Instagram')
    you_cliente = models.URLField(max_length=200, null=True, blank=True, verbose_name='Youtube')


    def __str__(self):
        fila = self.nombre_cliente + ' - ' + self.cifnif_cliente
        return fila
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
