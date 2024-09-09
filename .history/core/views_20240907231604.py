from django.shortcuts import render
from django.views.generic import View

class EmailView(View):
    template_name = 'email.html'
