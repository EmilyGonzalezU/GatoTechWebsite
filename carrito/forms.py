from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nombre_usuario', 'apellido_usuario', 'telefono_usuario', 'email_usuario', 'rut_usuario',
            'calle', 'numero', 'depto_casa', 'nombre_receptor', 'apellido_receptor', 'rut_receptor',
            'telefono_receptor', 'region', 'comuna'
        ]
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'nombre_usuario',
                'required': 'required'
            }),
            'apellido_usuario': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'apellido_usuario',
                'required': 'required'
            }),
            'telefono_usuario': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'telefono_usuario',
                'required': 'required'
            }),
            'email_usuario': forms.EmailInput(attrs={
                'class': 'form-control bg-light',
                'id': 'email_usuario',
                'required': 'required'
            }),
            'rut_usuario': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'rut_usuario',
                'required': 'required'
            }),
            'calle': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'calle',
                'required': 'required'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'numero',
                'required': 'required'
            }),
            'depto_casa': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'depto_casa',
            }),
            'nombre_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'nombre_receptor',
                'required': 'required'
            }),
            'apellido_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'apellido_receptor',
                'required': 'required'
            }),
            'rut_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'rut_receptor',
                'required': 'required'
            }),
            'telefono_receptor': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'telefono_receptor',
                'required': 'required'
            }),
            'region': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'region',
                'required': 'required'
            }),
            'comuna': forms.TextInput(attrs={
                'class': 'form-control bg-light',
                'id': 'comuna',
                'required': 'required'
            }),
        }