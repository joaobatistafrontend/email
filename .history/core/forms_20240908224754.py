from django import forms
from django.core.exceptions import ValidationError
from .models import Acompanhante, Parlamentares

class AcompanhanteForm(forms.ModelForm):
    class Meta:
        model = Acompanhante
        fields = ['nome', 'email']

    def __init__(self, *args, **kwargs):
        # O parlamentar é passado para o formulário via argumento
        self.parlamentar = kwargs.pop('parlamentar', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Verifica se o acompanhante já existe para este parlamentar com o mesmo email
        if Acompanhante.objects.filter(email=email, parlamentares=self.parlamentar).exists():
            raise ValidationError("Este e-mail já está cadastrado para este parlamentar.")
        
        return email

# from django import forms
# from .models import Acompanhante
# from django.core.exceptions import ValidationError
    
# class AcompanhanteForm(forms.ModelForm):
#     class Meta:
#         model = Acompanhante
#         fields = ['nome', 'email'] 

#         # Validação específica para o campo 'email'
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
        
#         # Verifica se já existe um registro com o mesmo e-mail
#         if Acompanhante.objects.filter(email=email).exists():
#             raise ValidationError("Esse email já está cadastrado.")
        
#         return email