from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .forms import AcompanhanteForm
from .models import *



class IndexView(View):
    template_name = 'index.html'
    parlamentares = Parlamentares
    def get(self, request):
        parlamentares = Parlamentares.objects.all()
        return render(request, self.template_name, {'parlamentares': parlamentares})

from .models import Parlamentares, Acompanhante

class EmailView(View):
    template_name = 'email.html'

    def get(self, request, pk):
        # Obtém o parlamentar com base no pk
        parlamentar = get_object_or_404(Parlamentares, pk=pk)
        form = AcompanhanteForm(parlamentar=parlamentar)
        return render(request, self.template_name, {'form': form, 'parlamentar': parlamentar})

    def post(self, request, pk):
        # Obtém o parlamentar com base no pk
        parlamentar = get_object_or_404(Parlamentares, pk=pk)
        form = AcompanhanteForm(request.POST, parlamentar=parlamentar)
        
        if form.is_valid():
            # Associa o acompanhante ao parlamentar e salva
            acompanhante = form.save(commit=False)
            acompanhante.parlamentares = parlamentar
            acompanhante.save()
            return render(request, self.template_name, {'form': form, 'success': True, 'parlamentar': parlamentar})
        else:
            return render(request, self.template_name, {'form': form, 'errors': form.errors, 'parlamentar': parlamentar})


# class EmailView(View):
#     template_name = 'email.html'

#     def get(self, request, pk):
#         # Obtém o parlamentar com base no pk passado pela URL
#         parlamentar = get_object_or_404(Parlamentares, pk=pk)
#         form = AcompanhanteForm()
#         return render(request, self.template_name, {'form': form, 'parlamentar': parlamentar})

#     def post(self, request, pk):
#         # Obtém o parlamentar com base no pk passado pela URL
#         parlamentar = get_object_or_404(Parlamentares, pk=pk)
#         form = AcompanhanteForm(request.POST)
#         if form.is_valid():
#             acompanhante = form.save(commit=False)
#             # Associa o acompanhante ao parlamentar selecionado
#             acompanhante.parlamentare = parlamentar
#             acompanhante.save()
#             return render(request, self.template_name, {'form': form, 'success': True, 'parlamentar': parlamentar})
#         else:
#             return render(request, self.template_name, {'form': form, 'errors': form.errors, 'parlamentar': parlamentar})