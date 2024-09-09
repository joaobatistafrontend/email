from django import forms
from .models import Acompanhante

class AcompanhanteForm(forms.ModelForm):
    class Meta:
        model = Acompanhante
        fields = ['nome', 'email'] 

        # Validação específica para o campo 'email'
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Verifica se já existe um registro com o mesmo e-mail
        if Acompanhante.objects.filter(email=email).exists():
            raise ValidationError("Esse email já está cadastrado.")
        
        return email