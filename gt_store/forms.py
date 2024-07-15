from django import forms
from . import models

class Product_form(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'

class Pc_form(forms.ModelForm):
    class Meta:
        model = models.Pc
        fields = '__all__'

class Notebook_form(forms.ModelForm):
    class Meta:
        model = models.Notebook
        fields = '__all__'

class Procesador_form(forms.ModelForm):
    class Meta:
        model = models.Procesador
        fields = '__all__'

class Placa_form(forms.ModelForm):
    class Meta:
        model = models.Placa_madre
        fields = '__all__'

class Ram_form(forms.ModelForm):
    class Meta:
        model = models.Ram
        fields = '__all__'

class Tarjeta_form(forms.ModelForm):
    class Meta:
        model = models.Tarjeta_video
        fields = '__all__'

class Fuente_form(forms.ModelForm):
    class Meta:
        model = models.Fuente_poder
        fields = '__all__'

class Almacenamiento_form(forms.ModelForm):
    class Meta:
        model = models.almacenamiento
        fields = '__all__'

class Gabinete_form(forms.ModelForm):
    class Meta:
        model = models.Gabinete
        fields = '__all__'

class Mouse_form(forms.ModelForm):
    class Meta:
        model = models.Mouse
        fields = '__all__'

class Teclado_form(forms.ModelForm):
    class Meta:
        model = models.Teclado
        fields = '__all__'

class Audifono_form(forms.ModelForm):
    class Meta:
        model = models.Audifono
        fields = '__all__'

class Monitor_form(forms.ModelForm):
    class Meta:
        model = models.Monitor
        fields = '__all__'