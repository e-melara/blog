import datetime

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    TemplateView, CreateView
)

from .forms import SuscribersForm
from applications.entrada.models import Entry
from applications.home.models import Home


class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['portada'] = Entry.objects.entrada_en_portada()
        context['entradas'] = Entry.objects.entrada_home()
        context['recientes'] = Entry.objects.entradas_recientes()
        # cargado el home
        context['about'] = Home.objects.latest('created')
        context['form'] = SuscribersForm
        
        return context
    


class SuscripberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = reverse_lazy('home_app:home')
