from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

class Home(ListView):
    template_name = 'home.html'
