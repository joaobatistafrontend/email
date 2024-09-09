from django import forms
from .models import Acompanhante

class AcompanhanteForm(forms.ModelForm):
    class Meta:
        model = Acompanhante
        fields = ['nome', 'email'] 