# views.py en la app 'app_usuarios'

from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm  

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_exito')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})
