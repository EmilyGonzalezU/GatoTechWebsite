# forms.py en la app 'app_usuarios'

from django import forms
from .models import PerfilUsuario

class RegistroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = PerfilUsuario
        fields = ['nombre', 'apellido', 'email', 'telefono', 'rut', 'password']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
