from django.contrib import admin
from django.contrib import admin
from .models import Product
from .forms import ProductoForm

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm

    class Media:
        js = ('gt_store/js/categorias.js',)

admin.site.register(Product, ProductoAdmin)