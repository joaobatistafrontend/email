from django.shortcuts import render
from django.views.generic import View

class EmailView(View):
    template_name = 'email.html'

    def get(self, request, *args, **kwargs):
        # Lógica para processar o GET request
        return render(request, self.template_name)