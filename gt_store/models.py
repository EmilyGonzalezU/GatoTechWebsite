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
    nombre_producto = models.CharField(max_length=60, blank=False, null=False, default='nombre_producto')
    descripcion = models.CharField(max_length=100, blank=False, null=True)
    descuento = models.CharField(max_length=60, blank=True, null=True, default=' ')
    precio_anterior = models.CharField(max_length=60, blank=True, null=True, default=' ')
    precio_transferencia = models.CharField(max_length=60, blank=False, null=True)
    precio_normal = models.CharField(max_length=60, blank=False, null=True)
    imagen = models.ImageField(upload_to='gt_store/', null=True, blank=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='pc')


    def __str__(self):
        return str(self.marca)

class Pc (Product):

    TIPO_PC = [
        ('pc_gamer', 'Pc Gamer'),
        ('pc_oficina', 'Pc Oficina')
    ]

    pc_procesador = models.CharField(max_length=60, blank=True, null=True)
    pc_memoria_ram = models.CharField(max_length=60, blank=True, null=True)
    pc_almacenamiento = models.CharField(max_length=60, blank=True, null=True)
    pc_tarjeta_video = models.CharField(max_length=60, blank=True, null=True)
    pc_fuente_poder = models.CharField(max_length=60, blank=True, null=True)
    pc_placa_madre = models.CharField(max_length=60, blank=True, null=True)
    pc_refrigeracion = models.CharField(max_length=60, blank=True, null=True)
    pc_gabinete = models.CharField(max_length=60, blank=True, null=True)
    tipo_pc = models.CharField(max_length=60, choices=TIPO_PC, default='pc_gamer')

    def __str__(self):
        return str(self.marca)

class Notebook(Product):
    TIPO_NOTE = [
        ('notebook_gamer', 'Notebook Gamer'),
        ('notebook_oficina', 'Notebook Oficina')
    ]
    
    notebook_procesador = models.CharField(max_length=60, blank=True, null=True)
    notebook_memoria_ram = models.CharField(max_length=60, blank=True, null=True)
    notebook_almacenamiento = models.CharField(max_length=60, blank=True, null=True)
    notebook_tarjeta_video = models.CharField(max_length=60, blank=True, null=True)
    notebook_tamano_pantalla = models.CharField(max_length=60, blank=True, null=True)
    notebook_resolucion_pantalla = models.CharField(max_length=60, blank=True, null=True)
    notebook_bateria = models.CharField(max_length=60, blank=True, null=True)
    tipo_notebook = models.CharField(max_length=60, choices=TIPO_NOTE, default='notebook_gamer')

    def __str__(self):
        return str(self.marca)
    
class Procesador(Product):
    procesador_velocidad = models.CharField(max_length=60, blank=True, null=True)
    procesador_nucleos = models.IntegerField(blank=True, null=True)
    procesador_hilos = models.IntegerField(blank=True, null=True)
    procesador_socket = models.CharField(max_length=60, blank=True, null=True)

    
    def __str__(self):
        return str(self.marca)
    
class Placa_madre(Product):
    placa_madre_socket = models.CharField(max_length=60, blank=True, null=True)
    placa_madre_formato = models.CharField(max_length=60, blank=True, null=True)
    placa_madre_chipset = models.CharField(max_length=60, blank=True, null=True)
    placa_madre_soporte_ram = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.marca)
    
class Ram(Product):
    ram_capacidad = models.CharField(max_length=60, blank=True, null=True)
    ram_tipo = models.CharField(max_length=60, blank=True, null=True)
    ram_velocidad = models.IntegerField(blank=True, null=True)
    ram_latencia = models.CharField(max_length=60, blank=True, null=True)
    
    def __str__(self):
        return str(self.marca)

class Tarjeta_video(Product):
    tarjeta_video_memoria = models.CharField(max_length=60, blank=True, null=True)
    tarjeta_video_tipo_memoria = models.CharField(max_length=60, blank=True, null=True)
    tarjeta_video_velocidad_reloj = models.CharField(max_length=60, blank=True, null=True)
    tarjeta_video_interfaz = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.marca)

class Fuente_poder (Product):
    fuente_poder_potencia = models.CharField(max_length=60, blank=True, null=True)
    fuente_poder_certificacion = models.CharField(max_length=60, blank=True, null=True)
    fuente_poder_modularidad = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.marca)


class almacenamiento(Product):
    TIPO_ALMACENAMIENTO = [
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
        ('NVME', 'NVME')
    ]

    almacenamiento_tipo = models.CharField(max_length=60, choices=TIPO_ALMACENAMIENTO, default='SSD')
    almacenamiento_velocidad_lectura = models.IntegerField(blank=True, null=True)
    almacenamiento_velocidad_escritura = models.IntegerField(blank=True, null=True)
    almacenamiento_capacidad = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.marca)

class Gabinete(Product):
    FORMATO_GABINETE = [
        ('ATX', 'ATX'),
        ('Mini_ATX', 'Mini ATX'),
        ('Micro_ATX', 'Micro ATX')
    ]

    gabinete_numero_bahias = models.IntegerField(blank=True, null=True)
    gabinete_nro_ventiladores = models.IntegerField(blank=True, null=True)
    gabinete_formato = models.CharField(max_length=50, choices=FORMATO_GABINETE, default='ATX')

    def __str__(self):
        return str(self.marca)

class Mouse(Product):
    mouse_dpi = models.IntegerField(blank=True, null=True)
    mouse_sensor = models.CharField(max_length=60, blank=True, null=True)
    mouse_tipo_conexion = models.CharField(max_length=60, blank=True, null=True)
    mouse_numero_botones = models.IntegerField(blank=True, null=True)
    mouse_retroiluminacion = models.BooleanField(default=False)

    def __str__(self):
        return str(self.marca)
    
class Teclado(Product):
    teclado_tipo_conexion = models.CharField(max_length=60, blank=True, null=True)
    teclado_tipo = models.CharField(max_length=60, blank=True, null=True)
    teclado_distribucion = models.CharField(max_length=60, blank=True, null=True)
    teclado_retroiluminacion = models.BooleanField(default=False)

    def __str__(self):
        return str(self.marca)
    
class Audifono(Product):
    audifono_tipo_conexion = models.CharField(max_length=60, blank=True, null=True)
    audifono_microfono = models.BooleanField(default=False)
    audifono_tipo_auricular = models.CharField(max_length=60, blank=True, null=True)
    audifono_cancelacion_ruido = models.BooleanField(default=False)


    def __str__(self):
        return str(self.marca)

class Monitor(Product):
    monitor_tamano_pantalla = models.CharField(max_length=60, blank=True, null=True)
    monitor_resolucion_pantalla = models.CharField(max_length=60, blank=True, null=True)
    monitor_frecuencia = models.IntegerField(blank=True, null=True)
    monitor_tipo_panel = models.CharField(max_length=60, blank=True, null=True)


    def __str__(self):
        return str(self.marca)