<<<<<<< HEAD
from django.shortcuts import render, redirect
from gt_store.models import Product

# Create your views here.
=======
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from gt_store.models import Product

>>>>>>> cambios
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

<<<<<<< HEAD
    def agregar(self, Product):
        id = str(Product.id_producto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": Product.id_producto,
                "imagen": Product.imagen.url,
                "nombre": Product.nombre_producto,
                "stock": Product.stock,
                "acumulado_transferencia": Product.precio_transferencia,
                "acumulado_normal": Product.precio_normal,
=======
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
>>>>>>> cambios
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
<<<<<<< HEAD
            self.carrito[id]["acumulado_transferencia"] += Product.precio_transferencia
            self.carrito[id]["acumulado_normal"] += Product.precio_normal
=======
            self.carrito[id]["acumulado_transferencia"] += producto.precio_transferencia
            self.carrito[id]["acumulado_normal"] += producto.precio_normal
>>>>>>> cambios

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

<<<<<<< HEAD
    def eliminar(self, Product):
        id = str(Product.id_producto)
=======
    def eliminar(self, producto):
        id = str(producto.id_producto)
>>>>>>> cambios
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

<<<<<<< HEAD
    def restar(self, Product):
        id = str(Product.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado_transferencia"] -= Product.precio_transferencia
            self.carrito[id]["acumulado_normal"] -= Product.precio_normal
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(Product)
=======
    def restar(self, producto):
        id = str(producto.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado_transferencia"] -= producto.precio_transferencia
            self.carrito[id]["acumulado_normal"] -= producto.precio_normal
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
>>>>>>> cambios
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

def tienda(request):
    productos = Product.objects.all()
    return render(request, "GatoTech/index.html", {'productos': productos})

def agregar_producto(request, id_producto):
    carrito = Carrito(request)
<<<<<<< HEAD
    producto = Product.objects.get(id_producto=id_producto)
    carrito.agregar(producto)
    return redirect("home")

def eliminar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Product.objects.get(id_producto=id_producto)
    carrito.eliminar(producto)
    return redirect("home")

def restar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Product.objects.get(id_producto=id_producto)
    carrito.restar(producto)
    return redirect("home")
=======
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
>>>>>>> cambios

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
<<<<<<< HEAD
    return redirect("home")
=======
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def carrito(request):
    return render(request, 'carrito/carrito.html')
>>>>>>> cambios
