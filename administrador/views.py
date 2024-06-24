# administrador/views.py

from django.shortcuts import render
from gt_store.models import Product, Pc, almacenamiento, Audifono, Procesador
from django.contrib.auth.decorators import login_required




@login_required
def muestra(request):
    request.session["usuario"] = "administrador"
    user = request.session["usuario"]
    context = {'usuario': user}
    return render(request, 'administrador/muestra.html', context)

def login(request):
    context={}
    return render(request, 'administrador/home.html', context)