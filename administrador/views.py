# administrador/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from gt_store.models import Product, Pc, Notebook, Mouse, Teclado, Audifono, Procesador, Ram, Placa_madre, Tarjeta_video, Fuente_poder, almacenamiento, Gabinete, Monitor
from django.contrib.auth.decorators import login_required
from .forms import Pc_form, Notebook_form, Mouse_form, Teclado_form, Audifono_form, Procesador_form, Ram_form, Placa_form, Tarjeta_form, Fuente_form, Almacenamiento_form, Gabinete_form, Monitor_form




def home(request):
    context={}
    return render(request, 'administrador/home.html', context)

@login_required
def muestra(request):
    productos = Product.objects.all()
    context = {"productos": productos}
    return render(request, 'administrador/muestra.html', context)

FORM_MAP = {
    'pc': (Pc_form, Pc),
    'notebook': (Notebook_form, Notebook),
    'mouse': (Mouse_form, Mouse),
    'teclado': (Teclado_form, Teclado),
    'audifonos': (Audifono_form, Audifono),
    'procesador': (Procesador_form, Procesador),
    'ram': (Ram_form, Ram),
    'placa_madre': (Placa_form, Placa_madre),
    'tarjeta_video': (Tarjeta_form, Tarjeta_video),
    'fuente_poder': (Fuente_form, Fuente_poder),
    'almacenamiento': (Almacenamiento_form, almacenamiento),
    'gabinete': (Gabinete_form, Gabinete),
    'monitor': (Monitor_form, Monitor),
}

FORM_MAP2 = {
    'pc': (Pc_form),
    'notebook': (Notebook_form),
    'mouse': (Mouse_form),
    'teclado': (Teclado_form),
    'audifonos': (Audifono_form),
    'procesador': (Procesador_form),
    'ram': (Ram_form),
    'placa_madre': (Placa_form),
    'tarjeta_video': (Tarjeta_form),
    'fuente_poder': (Fuente_form),
    'almacenamiento': (Almacenamiento_form),
    'gabinete': (Gabinete_form),
    'monitor': (Monitor_form),
}

#Pone en plural los nombres de las categorias!! para que? es para proporcionar una representación más adecuada para listas o grupos de elementos en interfaces
CATEGORY_CHOICES = [(key, form.Meta.model._meta.verbose_name_plural.title()) for key, form in FORM_MAP2.items()]

def product_add(request):
    categoria = request.GET.get('categoria', 'pc')
    form_class = FORM_MAP2.get(categoria, Pc_form)

    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        form_class = FORM_MAP2.get(categoria, Pc_form)
        form = form_class(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'administrador/product_add.html', {
                'mensaje': f'{categoria.capitalize()} guardado con éxito',
                'form': form_class(),
                'selected_category': categoria,
                'categories': CATEGORY_CHOICES
            })
        else:
            return render(request, 'administrador/product_add.html', {
                'form': form,
                'selected_category': categoria,
                'categories': CATEGORY_CHOICES
            })
    else:
        form = form_class()

    return render(request, 'administrador/product_add.html', {
        'form': form,
        'selected_category': categoria,
        'categories': CATEGORY_CHOICES
    })

def product_edit(request, id_producto):
    producto = Product.objects.get(id_producto=id_producto)
    categoria = producto.categoria
    form_class, model_class = FORM_MAP.get(categoria, (Pc_form, Pc)) 

    producto_especifico = model_class.objects.get(id_producto=id_producto)

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=producto_especifico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito')
            return redirect('p_Edit', id_producto=id_producto)
        else:
            context = {'form': form, 'producto': producto_especifico}
    else:
        form = form_class(instance=producto_especifico)
        context = {'form': form, 'producto': producto_especifico}

    return render(request, 'administrador/product_edit.html', context)

def producto_del(request, id_producto):
    product = Product.objects.get(pk=id_producto)  
    product.delete()
    return redirect(to='listado de productos')
#Para ver pedidos realizados

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from carrito.models import Pedido, ProductoPedido

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_pedidos_view(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    print(f"Pedidos: {pedidos}")  # Debug: Imprimir pedidos

    pedidos_detalle = []
    for pedido in pedidos:
        productos = ProductoPedido.objects.filter(pedido=pedido)
        print(f"Pedido ID {pedido.id}, Productos: {productos}")  # Debug: Imprimir productos por pedido
        pedidos_detalle.append({
            'pedido': pedido,
            'productos': productos
        })

    context = {
        'pedidos_detalle': pedidos_detalle,
    }
    print(f"Contexto: {context}")  # Debug: Imprimir contexto
    return render(request, 'administrador/admin_compras.html', context)