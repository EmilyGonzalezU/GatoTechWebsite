# administrador/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='login'),
    path('listado de productos/', views.muestra, name='listado de productos'),
    path('product_edit/<str:id_producto>', views.product_edit, name='p_Edit'),
    path('producto_del/<str:id_producto>', views.producto_del, name='producto_del'),
    path('Agregar productos', views.product_add, name='product_add'),

]
