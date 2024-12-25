from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .models import *
from .forms import *



class GroupsList(ListView):
    model = Groups
    template_name = "group/group_list.html"
    context_object_name = "groups"


class GroupsCreate(CreateView):
    model = Groups
    form_class = GroupsForm
    template_name = "group/group_create_or_update.html"
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        
        return super().form_valid(form)


class GroupsUpdate(UpdateView):
    model = Groups
    form_class = GroupsForm
    template_name = "group/group_create_or_update.html"
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        
        return super().form_valid(form)


class GroupsDelete(DeleteView):
    model = Groups
    success_url='/control/group-create-or-update/'
    template_name = "group/group_delete.html"