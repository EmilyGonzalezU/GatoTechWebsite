from django import forms
from gt_store.models import models
class Pc_form(forms.ModelForm):
    class Meta:
        model = models.Pc
        fields = '__all__'