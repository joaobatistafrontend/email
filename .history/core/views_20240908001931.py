from django.shortcuts import render
from django.views.generic import View
from .forms import AcompanhanteForm
from .models import *



class IndexView(View):
    template_name = 'index.html'
    parlamentares = Parlamentares
    def get(self, request):
        parlamentares = Parlamentares.objects.all()
        return render(request, self.template_name, {'parlamentares': parlamentares})


class EmailView(View):
    template_name = 'email.html'

    def get(self, request, pk):
        # Obtém o parlamentar com base no pk passado pela URL
        parlamentar = get_object_or_404(Parlamentares, pk=pk)
        form = AcompanhanteForm()
        return render(request, self.template_name, {'form': form, 'parlamentar': parlamentar})

    def post(self, request, pk):
        # Obtém o parlamentar com base no pk passado pela URL
        parlamentar = get_object_or_404(Parlamentares, pk=pk)
        form = AcompanhanteForm(request.POST)
        if form.is_valid():
            acompanhante = form.save(commit=False)
            # Associa o acompanhante ao parlamentar selecionado
            acompanhante.parlamentares = parlamentar
            acompanhante.save()
            return render(request, self.template_name, {'form': form, 'success': True, 'parlamentar': parlamentar})
        else:
            return render(request, self.template_name, {'form': form, 'errors': form.errors, 'parlamentar': parlamentar})
