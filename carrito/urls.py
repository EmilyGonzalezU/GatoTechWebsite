
from django.urls import path
from . import views


urlpatterns = [
    path('agregar/<int:id_producto>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:id_producto>/', views.eliminar_producto, name="Del"),
    path('restar/<int:id_producto>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('carrito/', views.carrito, name="carrito"),
    

] 


