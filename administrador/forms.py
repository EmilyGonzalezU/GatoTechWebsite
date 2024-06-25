from django import forms
from gt_store.models import Pc, almacenamiento, Notebook, Procesador, Placa_madre, Ram, Tarjeta_video, Fuente_poder, Gabinete, Mouse, Teclado, Audifono,Monitor


class Pc_form(forms.ModelForm):
    class Meta:
        model = Pc
        fields = '__all__'

class Almacenamiento_form(forms.ModelForm):
    class Meta:
        model = almacenamiento
        fields = '__all__'

class Notebook_form(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = '__all__'

class Procesador_form(forms.ModelForm):
    class Meta:
        model =  Procesador
        fields = '__all__'

class Placa_form(forms.ModelForm):
    class Meta:
        model =  Placa_madre
        fields = '__all__'

class Ram_form(forms.ModelForm):
    class Meta:
        model =  Ram
        fields = '__all__'

class Tarjeta_form(forms.ModelForm):
    class Meta:
        model =  Tarjeta_video
        fields = '__all__'

class Fuente_form(forms.ModelForm):
    class Meta:
        model =  Fuente_poder
        fields = '__all__'

class Almacenamiento_form(forms.ModelForm):
    class Meta:
        model =  almacenamiento
        fields = '__all__'

class Gabinete_form(forms.ModelForm):
    class Meta:
        model =  Gabinete
        fields = '__all__'

class Mouse_form(forms.ModelForm):
    class Meta:
        model =  Mouse
        fields = '__all__'

class Teclado_form(forms.ModelForm):
    class Meta:
        model =  Teclado
        fields = '__all__'

class Audifono_form(forms.ModelForm):
    class Meta:
        model =  Audifono
        fields = '__all__'

class Monitor_form(forms.ModelForm):
    class Meta:
        model =  Monitor
        fields = '__all__'