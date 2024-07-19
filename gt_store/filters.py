import django_filters
from .models import (
    Mouse, Teclado, Monitor, Audifono, 
    Pc, Notebook, Procesador, Placa_madre, 
    Tarjeta_video, almacenamiento, Fuente_poder, Ram, Gabinete
)

class MouseFilter(django_filters.FilterSet):
    class Meta:
        model = Mouse
        fields = {
            'marca': ['iexact', 'in'],
            'mouse_sensor': ['exact'],
            'mouse_tipo_conexion': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class TecladoFilter(django_filters.FilterSet):
    class Meta:
        model = Teclado
        fields = {
            'marca': ['iexact', 'in'],
            'teclado_tipo': ['exact'],
            'teclado_tipo_conexion': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class MonitorFilter(django_filters.FilterSet):
    class Meta:
        model = Monitor
        fields = {
            'marca': ['iexact', 'in'],
            'monitor_tamano_pantalla': ['exact'],
            'monitor_resolucion_pantalla': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class AudifonoFilter(django_filters.FilterSet):
    class Meta:
        model = Audifono
        fields = {
            'marca': ['iexact', 'in'],
            'audifono_tipo_auricular': ['exact'],
            'audifono_tipo_conexion': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class PcFilter(django_filters.FilterSet):
    class Meta:
        model = Pc
        fields = {
            'marca': ['iexact', 'in'],
            'tipo_pc': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class NotebookFilter(django_filters.FilterSet):
    class Meta:
        model = Notebook
        fields = {
            'marca': ['iexact', 'in'],
            'tipo_notebook': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class ProcesadorFilter(django_filters.FilterSet):
    class Meta:
        model = Procesador
        fields = {
            'marca': ['iexact', 'in'],
            'procesador_nucleos': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class PlacaMadreFilter(django_filters.FilterSet):
    class Meta:
        model = Placa_madre
        fields = {
            'marca': ['iexact', 'in'],
            'placa_madre_socket': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class TarjetaVideoFilter(django_filters.FilterSet):
    class Meta:
        model = Tarjeta_video
        fields = {
            'marca': ['iexact', 'in'],
            'tarjeta_video_memoria': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class AlmacenamientoFilter(django_filters.FilterSet):
    class Meta:
        model = almacenamiento
        fields = {
            'marca': ['iexact', 'in'],
            'almacenamiento_tipo': ['exact'],
            'almacenamiento_capacidad': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class FuentePoderFilter(django_filters.FilterSet):
    class Meta:
        model = Fuente_poder
        fields = {
            'marca': ['iexact', 'in'],
            'fuente_poder_potencia': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class RamFilter(django_filters.FilterSet):
    class Meta:
        model = Ram
        fields = {
            'marca': ['iexact', 'in'],
            'ram_capacidad': ['exact'],
            'ram_tipo': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

class GabineteFilter(django_filters.FilterSet):
    class Meta:
        model = Gabinete
        fields = {
            'marca': ['iexact', 'in'],
            'gabinete_formato': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }
