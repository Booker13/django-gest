django-gest v0.1.1 - 07/11/2022
===============================

Mantenimiento.

Mantenimiento de clientes. CRUD. v0.1.1 - 08/11/2022
----------------------------------------------------

-- INFORMACIÓN DE IDENTIFICACIÓN --
id - id del cliente - AutoField (IntegerField) - 1
nombre_cliente - nombre o razón social del cliente - CharField (65) - Sistemas Informáticos Lite, S.L.
cifnif_cliente - NIF/CIF del cliente - CharField (15) - A58818501
tipo_cliente - Tipo de cliente - [Tipo_cliente] - Selector

-- INFORMACIÓN DE CONTACTO 1 --
dir_cliente - Dirección - CharField (65) - Avda. de la Victoria, 32, Local
pob_cliente - Población - CharField (30) - Cumbres de Sosiego
cpo_cliente - Código Postal - CharField (10) - 24510 
pro_cliente - Provincia - CharField (20) - Nomera
pai_cliente - País - CharField (20) - España
-- INFORMACIÓN DE CONTACTO 2 --
pco_cliente - Persona de contacto - CharField (65) - Ana Belén García Matas
tel1_cliente - Teléfono 1 - CharField (20) - +34 912 45 62 39
tel2_cliente - Teléfono 2 - CharField (20) - +34 912 45 67 87
fax_cliente - Fax - CharField (20) - +34 912 45 62 43
mov1_cliente - Móvil - CharField (20) - +34 675 34 29 07
mov2_cliente - Móvil - CharField (20) - +34 675 34 29 07
wha_cliente - Whatsapp - CharField (20) - +34 675 34 29 07
email_cliente - E-Mail - EmailField (200) - infolite@infolite.com
url_cliente - URL - URLField (200) - https//:www.infolite.com

-- INFORMACIÓN DE REDES SOCIALES --
fcb_cliente - Página de Facebook - URLField (200) - https://www.facebook.com/sistemas.lite.1
twi_cliente - Página de Twitter - URLField (200) - https://twitter.com/sisinfolite
ins_cliente - Página de Instagram - URLField (200) - https://www.instagram.com/sisinfolite
you_cliente - Página de Youtube - URLField (200) - 

-- INFORMACIÓN DE ESTADO --
act_cliente - Cliente activo - BooleanField - True/False

-- INFORMACIÓN COMERCIAL --
age_cliente - Agente asignado - IntegerField - 1 - Gonzalo Navas Merino - tb_agentes
zon_cliente - Zona de ventas - IntegerField - 1 - Zona Norte - tb_zonas
fpa_cliente - Forma de pago - IntegerField - 1 - Efectivo - tb_formas_pago
-- INFORMACIÓN DE FACTURACIÓN --
trf_cliente - Tarifa de precios - IntegerField - 1 - Tarifa General - tb_tarifas
irp_cliente - Sujeto a IRPF - BooleanField - True/False
irt_cliente - Porcentaje de IRPF - DecimalField (5 dígitos - 2 decimales) - 15,00
tiv_cliente - Tipo de IVA a aplicar - IntegerField - 1 - IVA General 21% - tb_impuestos
rec_cliente - Recargo de equivalencia - BooleanField - True/False - t
dto_cliente - Porcentaje de descuento - DecimalField (5 dígitos - 2 decimales) - 5,00
-- INFORMACIÓN BANCARIA -- tb_bancos_clientes
enb_cliente - Nombre de la entidad - CharField (65) - Bankinter Consumer Finance, E.F.C., S.A.
iban_cliente - IBAN - CharField (34) - 0000 0000 0000 0000 0000 0000
bic_cliente - BIC - CharField (11) - BKBKESMMXXX
dib_cliente - Dirección de la oficina - CharField (65) - C/. Francisco de Vitoria, 33
pba_cliente - Población de la oficina - CharField (30) - Zaragoza
cpb_cliente - Código Postal de la oficina - CharField (20) - 50008
prb_cliente - Provincia de la oficina - CharField (20) - Zaragoza
tlb_cliente - Teléfono de la oficina - CharField (20) - +34 976 48 28 83
emb_cliente - E-Mail de la oficina - CharField (100) - bankimist@bankinter.com
-- OBSERVACIONES --
obs_cliente - Observaciones y notas - TextField - Observaciones

