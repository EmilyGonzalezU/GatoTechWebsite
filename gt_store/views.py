from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

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

# myapp/views.py

from django.shortcuts import render
from .models import Product

def general_gpu(request):
    productos = Product.objects.filter(categoria='pc')
    context = {"productos": productos}
    return render(request, 'gt_store/general_gpu.html', context)

def general_monitor(request):
    productos = Product.objects.filter(categoria='procesador')
    context = {"productos": productos}
    return render(request, 'gt_store/general_monitor.html', context)
