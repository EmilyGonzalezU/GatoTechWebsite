from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('inicio sesion/', views.login_view, name='inicio'),
    path('cuenta usuarios/', views.login_usuario, name='login_usuario'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('', views.inicio, name='redireccion'),
    path('personal/', views.datos_personales, name='datos_personales'),
    path('modificacion/<str:rut>/', views.editar_datos_personales, name='editar_datos_personales'),
    path('direcciones/agregar/', views.agregar_direccion, name='agregar_direccion'),
    path('direcciones/', views.lista_direcciones, name='lista_direcciones'),



] 

