from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from gt_store.models import Product
from usuarios.forms import DatosPersonalesForm2
from usuarios.models import PerfilUsuario

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id_producto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id_producto,
                "imagen": producto.imagen.url,
                "nombre": producto.nombre_producto,
                "stock": producto.stock,
                "acumulado_transferencia": producto.precio_transferencia,
                "acumulado_normal": producto.precio_normal,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado_transferencia"] += producto.precio_transferencia
            self.carrito[id]["acumulado_normal"] += producto.precio_normal

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado_transferencia"] -= producto.precio_transferencia
            self.carrito[id]["acumulado_normal"] -= producto.precio_normal
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

def tienda(request):
    productos = Product.objects.all()
    return render(request, "GatoTech/index.html", {'productos': productos})

def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = get_object_or_404(Product, id_producto=id_producto)
    carrito.agregar(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eliminar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = get_object_or_404(Product, id_producto=id_producto)
    carrito.eliminar(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def restar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = get_object_or_404(Product, id_producto=id_producto)
    carrito.restar(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def carrito(request):
    return render(request, 'carrito/carrito.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required





def datos_usuario_compra(request):
    if 'user_id' in request.session:
        try:
            user = PerfilUsuario.objects.get(id=request.session['user_id'])
            form = DatosPersonalesForm2(instance=user)
        except PerfilUsuario.DoesNotExist:
            form = DatosPersonalesForm2()
    else:
        form = DatosPersonalesForm2()

    if request.method == 'POST':
        if 'user_id' in request.session:
            form = DatosPersonalesForm2(request.POST, instance=user)
        else:
            form = DatosPersonalesForm2(request.POST)
        
        if form.is_valid():
            return redirect('direccion')

    context = {
        'form': form,
    }
    return render(request, 'carrito/continuacion_compra.html', context)

def direccion(request):
    return render(request, 'carrito/agregar_direccion.html')
