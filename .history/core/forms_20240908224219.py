from django import forms
from django.core.exceptions import ValidationError
from .models import Acompanhante, Parlamentares

class AcompanhanteForm(forms.ModelForm):
    class Meta:
        model = Acompanhante
        fields = ['nome', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        parlamentares = self.cleaned_data.get('parlamentares')

        # Verifica se já existe um acompanhante com o mesmo email associado a este parlamentar
        if Acompanhante.objects.filter(email=email, parlamentares=parlamentares).exists():
            raise ValidationError("Este e-mail já está associado a este parlamentar.")
        return email
