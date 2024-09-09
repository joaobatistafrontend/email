from django.shortcuts import render
from django.views.generic import View
from .form import AcompanhanteForm
from .models import *



class IndexView(View):
    template_name = 'email.html'

class EmailView(View):
    template_name = 'email.html'

    def get(self, request):
        form = AcompanhanteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AcompanhanteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form, 'success': True})
        else:
            return render(request, self.template_name, {'form': form, 'errors': form.errors}) 