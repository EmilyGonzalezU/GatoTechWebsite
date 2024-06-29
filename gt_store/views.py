from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from itertools import chain
import random

# Create your views here.
def index(request):
     # PC Destacados
    pcs_destacados = models.Pc.objects.filter(tipo_pc__iexact='pc_gamer')[:10]
    
    # Potencia tu PC
    procesador_amd = models.Procesador.objects.filter(marca__iexact='AMD')[:2]
    procesador_intel = models.Procesador.objects.filter(marca__iexact='INTEL')[:2]
    placas = models.Placa_madre.objects.all()[:2]
    videos = models.Tarjeta_video.objects.all()[:4]
    
    potencia = list(chain(procesador_amd, procesador_intel, placas, videos))
    random.shuffle(potencia)
    
    # Razer
    razer = models.Product.objects.filter(marca__iexact='RAZER')[:10]

    context = {
        "pcs_destacados": pcs_destacados,
        "potencia": potencia,
        "p_razer": razer
    }
    return render(request, 'gt_store/index.html', context)

def general_pc(request):
    productos = models.Pc.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_pc.html', context)

#Computation
def general_notebooks(request):
    return render(request, 'gt_store/general_notebook.html')
#Periferics
def general_keyboard(request):
    return render(request, 'gt_store/general_teclado.html')

def general_mouse(request):
    return render(request, 'gt_store/general_mouse.html')

def general_headset(request):
    productos = models.Audifono.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_audifono.html', context)

def general_monitor(request):
    return render(request, 'gt_store/general_monitor.html')
#Components
def general_processors(request):
    productos = models.Procesador.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_procesador.html', context)

def general_placa(request):
    productos = models.Placa_madre.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_placa.html', context)

def general_almacenamiento(request):
    productos = models.almacenamiento.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_almacenamiento.html', context)
def general_fP(request):
    productos = models.Fuente_poder.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_fuente_poder.html', context)
def general_gpu(request):
    productos = models.Tarjeta_video.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_gpu.html', context)
def general_gabinete(request):
    productos = models.Gabinete.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_gabinete.html', context)
def general_ram(request):
    productos = models.Ram.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_ram.html', context)
def registro(request):
    return render(request, 'gt_store/registro.html')


def general_placa_amd(request):
    productos = models.Placa_madre.objects.filter(marca__iexact='AMD')
    context = {"productos": productos}
    return render(request, 'gt_store/general_placa.html', context)

def general_placa_intel(request):
    productos = models.Placa_madre.objects.filter(marca__iexact='INTEL')
    context = {"productos": productos}
    return render(request, 'gt_store/general_placa.html', context)

 
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


