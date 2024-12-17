from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .models import *
from .forms import *



class GrafikNavchannyaList(ListView):
    model = GrafikNavchannya
    template_name = "grafik_navchannya/grafik_navchannya_list.html"
    context_object_name = "grafik_navchannyas"


class GrafikNavchannyaCreate(CreateView):
    model = GrafikNavchannya
    form_class = GrafikNavchannyaForm
    template_name = "grafik_navchannya/grafik_navchannya_create_or_update.html"
    success_url = reverse_lazy('grafik_navchannya_list')

    def form_valid(self, form):
        
        return super().form_valid(form)


class GrafikNavchannyaUpdate(UpdateView):
    model = GrafikNavchannya
    form_class = GrafikNavchannyaForm
    template_name = "grafik_navchannya/grafik_navchannya_create_or_update.html"
    success_url = reverse_lazy('grafik_navchannya_list')

    def form_valid(self, form):
        
        return super().form_valid(form)
    
class GrafikNavchannyaDelete(DeleteView):
    model = GrafikNavchannya
    success_url='/control/grafik-navchannya/'
    template_name = "grafik_navchannya/grafik_navchannya_delete.html"