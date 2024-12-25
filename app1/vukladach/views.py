from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .models import *
from .forms import *



class VukladachList(ListView):
    model = Vukladach
    template_name = "vukladach/vukladach_list.html"
    context_object_name = "vukladachs"


class VukladachCreate(CreateView):
    model = Vukladach
    form_class = VukladachForm
    template_name = "vukladach/vukladach_create_or_update.html"
    success_url = reverse_lazy('vukladach_list')

    def form_valid(self, form):
        
        return super().form_valid(form)


class VukladachUpdate(UpdateView):
    model = Vukladach
    form_class = VukladachForm
    template_name = "vukladach/vukladach_create_or_update.html"
    success_url = reverse_lazy('vukladach_list')

    def form_valid(self, form):
        
        return super().form_valid(form)

class VukladachDelete(DeleteView):
    model = Vukladach
    success_url='/control/vukladach/'
    template_name = "vukladach/vukladach_delete.html"