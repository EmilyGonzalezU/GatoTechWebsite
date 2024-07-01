from django.shortcuts import render, redirect
from gt_store.models import Product

# Create your views here.
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
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado_transferencia"] += Product.precio_transferencia
            self.carrito[id]["acumulado_normal"] += Product.precio_normal

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, Product):
        id = str(Product.id_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, Product):
        id = str(Product.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado_transferencia"] -= Product.precio_transferencia
            self.carrito[id]["acumulado_normal"] -= Product.precio_normal
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(Product)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

def tienda(request):
    productos = Product.objects.all()
    return render(request, "GatoTech/index.html", {'productos': productos})

def agregar_producto(request, id_producto):
    carrito = Carrito(request)
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

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("home")
