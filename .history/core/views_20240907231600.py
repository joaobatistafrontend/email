from django.shortcuts import render
from django.views.generic import View

class EmailV(View):
    template_name = 'email.html'
