from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('inicio sesion/', views.login_view, name='inicio'),
    path('cuenta usuarios/', views.login_usuario, name='login_usuario'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('', views.inicio, name='redireccion'),
    path('tipo_usuario/', views.tipo_usuario, name='tipo_usuario'),


] 

