from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm  
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import PerfilUsuario, Direccion
from django.views.decorators.csrf import csrf_exempt
from .forms import DatosPersonalesForm, DireccionForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def inicio(request):
    if not request.session.get('user_nombre'):
        return redirect('inicio')  
    return render(request, 'usuarios/usuario.html')

@csrf_exempt
def login_view(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombre = request.POST.get('nombre')
        form_source = request.POST.get('form_source')

        if not email:
            context['email_error'] = "Ingrese su e-mail."
        elif not ("@" in email and "." in email):
            context['email_error'] = "Ingrese un e-mail válido."
        else:
            try:
                user = PerfilUsuario.objects.get(email=email)
                if check_password(password, user.contrasena):
                    request.session['user_id'] = user.id
                    request.session['user_nombre'] = user.nombre
                    request.session['user_apellido'] = user.apellido
                    request.session['user_telefono'] = user.telefono
                    request.session['user_email'] = user.email
                    request.session['user_rut'] = user.rut
                    return redirect('home')
                else:
                    context['password_error'] = "Contraseña incorrecta."
            except PerfilUsuario.DoesNotExist:
                context['email_error'] = "El email no existe."

        if not password or len(password) < 8:
            context['password_error'] = "Ingrese su contraseña (mínimo 8 caracteres)."

        if form_source == 'modal':
            context['modal_errors'] = True

    return render(request, 'usuarios/inicioSesion.html', context)


def login_usuario (request):
    return render(request, 'usuarios/usuario.html')

from django.contrib.auth import logout

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio') 

#Cuenta usuario

def datos_personales(request):
    if 'user_id' not in request.session:
        return redirect('login_usuario')

    try:
        user = PerfilUsuario.objects.get(id=request.session['user_id'])
    except PerfilUsuario.DoesNotExist:
        return redirect('login_usuario')

    context = {
        'user': user,
    }
    return render(request, 'usuarios/personal.html', context)

def editar_datos_personales(request, rut):
    persona = PerfilUsuario.objects.get(rut=rut)

    if request.method == 'POST':
        form = DatosPersonalesForm(data=request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos actualizados con éxito')
            return redirect('datos_personales')  
        form = DatosPersonalesForm(instance=persona)

    context = {
        'form': form,
        'datos': persona,
    }
    return render(request, 'usuarios/personal_edit.html', context)

#Direcciones
def agregar_direccion(request):
    if 'user_id' not in request.session:
        return redirect('login_usuario')  

    if request.method == 'POST':
        form = DireccionForm(request.POST)
        if form.is_valid():
            direccion = form.save(commit=False)
            user = PerfilUsuario.objects.get(id=request.session['user_id'])
            direccion.perfil_usuario = user
            direccion.save()
            return redirect('lista_direcciones')
    else:
        form = DireccionForm()
    return render(request, 'usuarios/direcciones_add.html', {'form': form})

def lista_direcciones(request):
    if 'user_id' not in request.session:
        return redirect('login_usuario')
    user = PerfilUsuario.objects.get(id=request.session['user_id'])
    direcciones = Direccion.objects.filter(perfil_usuario=user)
    return render(request, 'usuarios/direcciones.html', {'direcciones': direcciones})


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
#??