from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('home/', views.index, name='home'),
        path('pc/', views.general_pc, name='general_pc'),
        path('procesadores/', views.general_processors, name='general_processors'),
        path('placa_madre/', views.general_placa, name='general_placa'),
        path('ram/', views.general_ram, name='general_ram'),
        path('almacenamiento/', views.general_almacenamiento, name='general_almacenamiento'),
        path('fuente_de_poder/', views.general_fP, name='general_fP'),
        path('tarjeta_grafica/', views.general_gpu, name='general_gpu'),
        path('gabinete/', views.general_gabinete, name='general_gabinete'), 
        path('notebook/', views.general_notebooks, name='general_notebooks'),
        path('mouse/', views.general_mouse, name='general_mouse'),
        path('teclados/', views.general_keyboard, name='general_keyboard'),
        path('audifonos/', views.general_headset, name='general_headset'),
        path('monitores/', views.general_monitor, name='general_monitor'),
        
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)