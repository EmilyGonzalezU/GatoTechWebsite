import django_filters
from .models import Mouse, Teclado, Monitor, Audifono

# Mouse filter
class MouseFilter(django_filters.FilterSet):
    class Meta:
        model = Mouse
        fields = {
            'marca': ['iexact', 'in'],
            'mouse_sensor': ['exact'],
            'mouse_tipo_conexion': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

# Teclado filter
class TecladoFilter(django_filters.FilterSet):
    class Meta:
        model = Teclado
        fields = {
            'marca': ['iexact', 'in'],
            'teclado_tipo': ['exact'],
            'teclado_tipo_conexion': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

# Monitor filter
class MonitorFilter(django_filters.FilterSet):
    class Meta:
        model = Monitor
        fields = {
            'marca': ['iexact', 'in'],
            'monitor_tamano_pantalla': ['exact'],
            'monitor_tipo_panel': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }

# Audífonos filter
class AudifonoFilter(django_filters.FilterSet):
    class Meta:
        model = Audifono
        fields = {
            'marca': ['iexact', 'in'],
            'audifono_tipo_conexion': ['exact'],
            'audifono_tipo_auricular': ['exact'],
            'precio_normal': ['gte', 'lte'],
        }
