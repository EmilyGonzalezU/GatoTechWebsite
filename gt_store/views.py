from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def index(request):
    return render(request, 'gt_store/index.html')

def general_pc(request):
    return render(request, 'gt_store/general_pc.html')

#Computation
def general_notebooks(request):
    return render(request, 'gt_store/general_notebook.html')
#Periferics
def general_keyboard(request):
    return render(request, 'gt_store/general_teclado.html')

def general_mouse(request):
    return render(request, 'gt_store/general_mouse.html')

def general_headset(request):
    return render(request, 'gt_store/general_audifono.html')

def general_monitor(request):
    return render(request, 'gt_store/general_monitor.html')
#Components
def general_processors(request):
    return render(request, 'gt_store/general_procesador.html')

def general_placa(request):
    return render(request, 'gt_store/general_placa.html')

def general_almacenamiento(request):
    return render(request, 'gt_store/general_almacenamiento.html')

def general_fP(request):
    return render(request, 'gt_store/general_fuente_poder.html')

def general_gpu(request):
    return render(request, 'gt_store/general_gpu.html')

def general_gabinete(request):
    return render(request, 'gt_store/general_gabinete.html')

def general_ram(request):
    return render(request, 'gt_store/general_ram.html')

def registro(request):
    return render(request, 'gt_store/registro.html')

#Vistas con BD}
#COMPUTACION
def general_pc(request):
    productos = models.Pc.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_pc.html', context)

def general_placa(request):
    productos = models.Placa_madre.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_placa.html', context)

def general_placa_amd(request):
    productos = models.Placa_madre.objects.filter(marca__iexact='AMD')
    context = {"productos": productos}
    return render(request, 'gt_store/general_placa.html', context)

def general_placa_intel(request):
    productos = models.Placa_madre.objects.filter(marca__iexact='INTEL')
    context = {"productos": productos}
    return render(request, 'gt_store/general_placa.html', context)

#COMPONENTES
def general_almacenamiento(request):
    productos = models.almacenamiento.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_almacenamiento.html', context)

def general_fP(request):
    productos = models.Fuente_poder.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_fuente_poder.html', context)

def general_gabinete(request):
    productos = models.Gabinete.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_gabinete.html', context)

#PERIFERICOS
def general_headset(request):
    productos = models.Audifono.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_audifono.html', context)

def general_headset_headset(request):
    productos = models.Audifono.objects.filter(audifono_tipo_auricular__iexact='HEADSET')
    context = {"productos": productos}
    return render(request, 'gt_store/general_audifono.html', context)

#test detalle producto
def detalle_producto(request, id_producto):
    producto = get_object_or_404(models.Product, id_producto=id_producto)
    context = {"producto": producto}
    return render(request, 'gt_store/detalle_productos.html', context)

def products (request):
    producto = models.Product.objects.all()
    context = {"productos": producto}
    return render(request, 'gt_store/sugerencia.html', context)
