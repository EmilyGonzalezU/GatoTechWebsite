from django.db import models

class Product(models.Model):
    CATEGORIAS = [
        ('pc', 'PC'),
        ('notebook', 'Notebook'),
        ('mouse', 'Mouse'),
        ('teclado', 'Teclado'),
        ('audifonos', 'Audifonos'),
        ('procesador', 'Procesador'),
        ('ram', 'Memoria RAM'),
        ('placa_madre', 'Placa Madre'),
        ('tarjeta_video', 'Tarjeta de Video'),
        ('fuente_poder', 'Fuente de Poder'),
        ('almacenamiento', 'Almacenamiento'),
        ('gabinete', 'Gabinete'),
        ('monitor', 'Monitor'),
    ]

    id_producto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=60, blank=False, null=False)
    descripcion = models.CharField(max_length=100, blank=False, null=True)
    descuento = models.CharField(max_length=60, blank=True, null=True)
    precio_anterior = models.CharField(max_length=60, blank=True, null=True)
    precio_transferencia = models.CharField(max_length=60, blank=False, null=True)
    precio_normal = models.CharField(max_length=60, blank=False, null=True)
    imagen = models.ImageField(upload_to='gt_store/', null=True, blank=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='pc')

   
    procesador = models.CharField(max_length=60, blank=True, null=True)
    memoria_ram = models.CharField(max_length=60, blank=True, null=True)
    almacenamiento = models.CharField(max_length=60, blank=True, null=True)
    tarjeta_video = models.CharField(max_length=60, blank=True, null=True)
    fuente_poder = models.CharField(max_length=60, blank=True, null=True)
    placa_madre = models.CharField(max_length=60, blank=True, null=True)
    refrigeracion = models.CharField(max_length=60, blank=True, null=True)
    gabinete = models.CharField(max_length=60, blank=True, null=True)


    tamano_pantalla = models.CharField(max_length=60, blank=True, null=True)
    resolucion_pantalla = models.CharField(max_length=60, blank=True, null=True)
    bateria = models.CharField(max_length=60, blank=True, null=True)

    dpi = models.IntegerField(blank=True, null=True)
    tracking = models.CharField(max_length=60, blank=True, null=True)
    sensor = models.CharField(max_length=60, blank=True, null=True)
    tipo_conexion = models.CharField(max_length=60, blank=True, null=True)
    boton = models.BooleanField(default=False)
    numero_botones = models.IntegerField(blank=True, null=True)
    retroiluminacion = models.BooleanField(default=False)

    tipo_teclado = models.CharField(max_length=60, blank=True, null=True)
    distribucion = models.CharField(max_length=60, blank=True, null=True)

    microfono = models.BooleanField(default=False)
    tipo_auricular = models.CharField(max_length=60, blank=True, null=True)
    cancelacion_ruido = models.BooleanField(default=False)

    velocidad = models.CharField(max_length=60, blank=True, null=True)
    nucleos = models.IntegerField(blank=True, null=True)
    hilos = models.IntegerField(blank=True, null=True)
    socket = models.CharField(max_length=60, blank=True, null=True)

    capacidad = models.CharField(max_length=60, blank=True, null=True)
    tipo_ram = models.CharField(max_length=60, blank=True, null=True)
    velocidad = models.IntegerField(blank=True, null=True)
    latencia = models.CharField(max_length=60, blank=True, null=True)

    formato = models.CharField(max_length=60, blank=True, null=True)
    chipset = models.CharField(max_length=60, blank=True, null=True)
    soporte_ram = models.CharField(max_length=60, blank=True, null=True)

    memoria = models.CharField(max_length=60, blank=True, null=True)
    tipo_memoria = models.CharField(max_length=60, blank=True, null=True)
    velocidad_reloj = models.CharField(max_length=60, blank=True, null=True)
    interfaz = models.CharField(max_length=60, blank=True, null=True)

    potencia = models.CharField(max_length=60, blank=True, null=True)
    certificacion = models.CharField(max_length=60, blank=True, null=True)
    modularidad = models.CharField(max_length=60, blank=True, null=True)

    tipo_almacenamiento = models.CharField(max_length=60, blank=True, null=True)
    velocidad_lectura = models.IntegerField(blank=True, null=True)
    velocidad_escritura = models.IntegerField(blank=True, null=True)
    
    numero_bahias = models.IntegerField(blank=True, null=True)
    ventilacion = models.BooleanField(default=False)
    nro_ventiladores = models.IntegerField(blank=True, null=True)

    frecuencia = models.IntegerField(blank=True, null=True)
    tipo_panel = models.CharField(max_length=60, blank=True, null=True)


   
    def __str__(self):
        return str(self.marca)
    