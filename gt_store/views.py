from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from itertools import chain
import random

from .models import Pc, Notebook, Procesador, Placa_madre, Tarjeta_video, almacenamiento, Fuente_poder, Ram, Gabinete
from .filters import ProcesadorFilter, PlacaMadreFilter, TarjetaVideoFilter, AlmacenamientoFilter, FuentePoderFilter, RamFilter, GabineteFilter

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
    #Notebook
    notebook = models.Notebook.objects.all()[:10]
    # Razer
    razer = models.Product.objects.filter(marca__iexact='RAZER')[:10]

    context = {
        "pcs_destacados": pcs_destacados,
        "potencia": potencia,
        "p_razer": razer,
        "notebooks": notebook,
    }
    return render(request, 'gt_store/index.html', context)

def general_pc(request):
    productos = models.Pc.objects.all()

    context = {"productos": productos}
                
    return render(request, 'gt_store/general_pc.html', context)

#Computation
def general_notebooks(request):
    notebooks = models.Notebook.objects.all()
    context = {"productos": notebooks}
    return render(request, 'gt_store/general_notebook.html', context)

def general_note_gamer(request):
    note_gamer = models.Notebook.objects.filter(tipo_notebook__iexact='notebook_gamer')
    context = {"productos":note_gamer}
    return render(request, 'gt_store/general_notebook.html', context)

def general_note_escritorio(request):
    note_escritorio = models.Notebook.objects.filter(tipo_notebook__iexact='notebook_oficina')
    context = {"productos":note_escritorio}
    return render(request, 'gt_store/general_notebook.html', context)

def general_pc_gamer(request):
    pc_gamer = models.Pc.objects.filter(tipo_pc__iexact='pc_gamer')
    context = {"productos":pc_gamer}
    return render(request, 'gt_store/general_pc.html', context)

def general_pc_escritorio(request):
    pc_escritorio = models.Pc.objects.filter(tipo_pc__iexact='pc_escritorio')
    context = {"productos": pc_escritorio}
    return render(request, 'gt_store/general_pc.html', context)


#Perifericos
def general_keyboard(request):
    productos = models.Teclado.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_teclado.html', context)

def general_mecanico(request):
    productos = models.Teclado.objects.filter(teclado_tipo__iexact='mecanico')
    context = {"productos": productos}
    return render(request, 'gt_store/general_teclado.html', context)

def general_membrana(request):
    productos = models.Teclado.objects.filter(teclado_tipo__iexact='membrana')
    context = {"productos": productos}
    return render(request, 'gt_store/general_teclado.html', context)


def general_mouse(request):
    productos = models.Mouse.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_mouse.html', context)

def general_mouse_optico(request):
    productos = models.Mouse.objects.filter(mouse_sensor__iexact='Optico')
    context = {"productos": productos}
    return render(request, 'gt_store/general_mouse.html', context)

def general_mouse_laser(request):
    productos = models.Mouse.objects.filter(mouse_sensor__iexact='Laser')
    context = {"productos": productos}
    return render(request, 'gt_store/general_mouse.html', context)

def general_headset(request):
    productos = models.Audifono.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_audifono.html', context)

def general_headset_headset(request):
    productos = models.Audifono.objects.filter(audifono_tipo_auricular__iexact='HEADSET')
    context = {"productos": productos}
    return render(request, 'gt_store/general_audifono.html', context)

def general_monitor(request):
    productos = models.Monitor.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_monitor.html', context)
#Components
def general_processors(request):
    productos = models.Procesador.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_procesador.html', context)

def general_proce_amd(request):
    productos = models.Procesador.objects.filter(marca__iexact='AMD')
    context = {"productos": productos}
    return render(request, 'gt_store/general_procesador.html', context)

def general_proce_intel(request):
    productos = models.Procesador.objects.filter(marca__iexact='INTEL')
    context = {"productos": productos}
    return render(request, 'gt_store/general_procesador.html', context)

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

def general_almacenamiento(request):
    productos = models.almacenamiento.objects.all()
    context = {"productos": productos}
    return render(request, 'gt_store/general_almacenamiento.html', context)

def general_ssd(request):
    productos = models.almacenamiento.objects.filter(tipo_almacenamiento__iexact='SSD')
    context = {"productos": productos}
    return render(request, 'gt_store/general_almacenamiento.html', context)

def general_hdd(request):
    productos = models.almacenamiento.objects.filter(tipo_almacenamiento__iexact='HDD')
    context = {"productos": productos}
    return render(request, 'gt_store/general_almacenamiento.html', context)

def general_nvme(request):
    productos = models.almacenamiento.objects.filter(tipo_almacenamiento__iexact='NVME')
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

def general_gpu_amd(request):
    productos = models.Tarjeta_video.objects.filter(marca__iexact='AMD')
    context = {"productos": productos}
    return render(request, 'gt_store/general_gpu.html', context)

def general_gpu_intel(request):
    productos = models.Tarjeta_video.objects.filter(marca__iexact='INTEL')
    context = {"productos": productos}
    return render(request, 'gt_store/general_gpu.html', context)

def general_gpu_nvidia(request):
    productos = models.Tarjeta_video.objects.filter(marca__iexact='NVIDIA')
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


#test detalle producto
def detalle_producto(request, id_producto):
    producto = get_object_or_404(models.Product, id_producto=id_producto)
    context = {"producto": producto}
    return render(request, 'gt_store/detalle_productos.html', context)

def products (request):
    producto = models.Product.objects.all()
    context = {"productos": producto}
    return render(request, 'gt_store/sugerencia.html', context)


def registro (request):
    return render(request, 'usuarios/registro.html')

#test filtro
def filtrar_mouse(request):
    queryset = Mouse.objects.all()
    mouse_filter = MouseFilter(request.GET, queryset=queryset)
    context = {
        'filter': mouse_filter,
        'productos': mouse_filter.qs
    }
    return render(request, 'gt_store/general_mouse.html', context)

def filtrar_teclado(request):
    queryset = Teclado.objects.all()
    teclado_filter = TecladoFilter(request.GET, queryset=queryset)
    context = {
        'filter': teclado_filter,
        'productos': teclado_filter.qs
    }
    return render(request, 'gt_store/general_teclado.html', context)

def filtrar_monitor(request):
    queryset = Monitor.objects.all()
    monitor_filter = MonitorFilter(request.GET, queryset=queryset)
    context = {
        'filter': monitor_filter,
        'productos': monitor_filter.qs
    }
    return render(request, 'gt_store/general_monitor.html', context)

def filtrar_audifonos(request):
    queryset = Audifono.objects.all()
    audifono_filter = AudifonoFilter(request.GET, queryset=queryset)
    context = {
        'filter': audifono_filter,
        'productos': audifono_filter.qs
    }
    return render(request, 'gt_store/general_audifono.html', context)

def filtrar_pcs(request):
    queryset = Pc.objects.all()
    pc_filter = PcFilter(request.GET, queryset=queryset)
    context = {
        'filter': pc_filter,
        'productos': pc_filter.qs
    }
    return render(request, 'gt_store/general_pc.html', context)

def filtrar_notebooks(request):
    queryset = Notebook.objects.all()
    notebook_filter = NotebookFilter(request.GET, queryset=queryset)
    context = {
        'filter': notebook_filter,
        'productos': notebook_filter.qs
    }
    return render(request, 'gt_store/general_notebook.html', context)

def filtrar_procesadores(request):
    queryset = Procesador.objects.all()
    filter = ProcesadorFilter(request.GET, queryset=queryset)
    context = {
        'filter': filter,
        'productos': filter.qs
    }
    return render(request, 'gt_store/general_procesador.html', context)

def filtrar_placas_madre(request):
    queryset = Placa_madre.objects.all()
    filter = PlacaMadreFilter(request.GET, queryset=queryset)
    context = {
        'filter': filter,
        'productos': filter.qs
    }
    return render(request, 'gt_store/general_placa.html', context)

def filtrar_tarjetas_video(request):
    queryset = Tarjeta_video.objects.all()
    filter = TarjetaVideoFilter(request.GET, queryset=queryset)
    context = {
        'filter': filter,
        'productos': filter.qs
    }
    return render(request, 'gt_store/general_gpu.html', context)

def filtrar_almacenamiento(request):
    queryset = almacenamiento.objects.all()
    filter = AlmacenamientoFilter(request.GET, queryset=queryset)
    context = {
        'filter': filter,
        'productos': filter.qs
    }
    return render(request, 'gt_store/general_almacenamiento.html', context)

def filtrar_fuente_poder(request):
    queryset = Fuente_poder.objects.all()
    filter = FuentePoderFilter(request.GET, queryset=queryset)
    context = {
        'filter': filter,
        'productos': filter.qs
    }
    return render(request, 'gt_store/general_fuente_poder.html', context)

def filtrar_ram(request):
    queryset = Ram.objects.all()
    filter = RamFilter(request.GET, queryset=queryset)
    context = {
        'filter': filter,
        'productos': filter.qs
    }
    return render(request, 'gt_store/general_ram.html', context)

def filtrar_gabinete(request):
    queryset = Gabinete.objects.all()
    filter = GabineteFilter(request.GET, queryset=queryset)
    context = {
        'filter': filter,
        'productos': filter.qs
    }
    return render(request, 'gt_store/general_gabinete.html', context)