from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): #Definiendo la vista home
    template_name = 'home.html'