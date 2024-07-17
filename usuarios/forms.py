from django import forms
from .models import PerfilUsuario, Direccion
from django.contrib.auth.hashers import make_password

class RegistroUsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-light',
            'id': 'pass',
            'required': 'required'
        })
    )

    class Meta:
        model = PerfilUsuario
        fields = ['nombre', 'apellido', 'email', 'telefono', 'rut', 'contrasena']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'nombre',
                'required': 'required'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'apellido',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-light',
                'id': 'email',
                'required': 'required'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'telefono',
                'required': 'required'
            }),
            'rut': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'rut',
                'required': 'required'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.contrasena = make_password(self.cleaned_data['contrasena'])
        if commit:
            user.save()
        return user

#Datos que se pueden modificar
class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['nombre', 'apellido', 'telefono']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'depto_casa', 'nombre_receptor', 'apellido_receptor', 'rut_receptor', 'telefono_receptor', 'region', 'comuna']
        widgets = {
            'calle': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'calle',
                'required': 'required'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
            'depto_casa': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
            'nombre_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
            'apellido_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
            'rut_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
            'telefono_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
            'region': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
            'comuna': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'required': 'required'
            }),
        }
#Datos completos
class DatosPersonalesForm2(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'nombre',
                'required': 'required'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'apellido',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-light',
                'id': 'email',
                'required': 'required'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'telefono',
                'required': 'required'
            })
        }