from django.shortcuts import render
from django.views.generic import View

class EmailView(View):
    t = 'email.html'
