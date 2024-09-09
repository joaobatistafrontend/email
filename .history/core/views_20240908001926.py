from django.shortcuts import render
from django.views.generic import View
from .form import AcompanhanteForm
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
        form = AcompanhanteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AcompanhanteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form, 'success': True})
        else:
            return render(request, self.template_name, {'form': form, 'errors': form.errors}) 