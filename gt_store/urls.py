from django.urls import path
from . import views


urlpatterns = [
        path('home/', views.index, name='home'),
        path('registro/', views.registro, name='registro'),
        path('pc/', views.general_pc, name='general_pc'),
        path('procesadores/', views.general_processors, name='general_processors'),
        path('placa_madre/', views.general_placa, name='general_placa'),
        path('placa_madre_amd/', views.general_placa_amd, name='general_placa'),
        path('placa_madre_intel/', views.general_placa_intel, name='general_placa'),
        path('ram/', views.general_ram, name='general_ram'),
        path('almacenamiento/', views.general_almacenamiento, name='general_almacenamiento'),
        path('fuente_de_poder/', views.general_fP, name='general_fP'),
        path('tarjeta_grafica/', views.general_gpu, name='general_gpu'),
        path('gabinete/', views.general_gabinete, name='general_gabinete'), 
        path('notebook/', views.general_notebooks, name='general_notebooks'),
        path('mouse/', views.general_mouse, name='general_mouse'),
        path('teclados/', views.general_keyboard, name='general_keyboard'),
        path('audifonos/', views.general_headset, name='general_headset'),
        path('audifonos_headset/', views.general_headset_headset, name='general_headset'),
        path('monitores/', views.general_monitor, name='general_monitor'),
        path('productos/<int:id_producto>/', views.detalle_producto, name='detalle_producto'),
        path('suge/', views.products, name='products'),


] 

