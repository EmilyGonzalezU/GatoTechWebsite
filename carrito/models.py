from django.db import models
from gt_store.models import Product
from django.contrib.auth.models import User

class Pedido(models.Model):
    nombre_usuario = models.CharField(max_length=60, blank=True, null=True)
    apellido_usuario = models.CharField(max_length=60, blank=True, null=True)
    telefono_usuario = models.CharField(max_length=15, blank=True, null=True)
    email_usuario = models.EmailField(max_length=90, blank=True, null=True)
    rut_usuario = models.CharField(max_length=12, blank=True, null=True)
    
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    depto_casa = models.CharField(max_length=10, blank=True, null=True)
    nombre_receptor = models.CharField(max_length=60)
    apellido_receptor = models.CharField(max_length=60)
    rut_receptor = models.CharField(max_length=12)
    telefono_receptor = models.CharField(max_length=15)
    region = models.CharField(max_length=15)
    comuna = models.CharField(max_length=15)
    
    total_transferencia = models.DecimalField(max_digits=10, decimal_places=2)
    total_normal = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f'Pedido {self.id} - {self.email_usuario or "Sin usuario"}'

class ProductoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return f'{self.producto.nombre_producto} x {self.cantidad}'
