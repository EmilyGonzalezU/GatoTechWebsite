from django.contrib import admin
from .models import Pedido, ProductoPedido

# Register your models here.
admin.site.register(Pedido)
admin.site.register(ProductoPedido)
