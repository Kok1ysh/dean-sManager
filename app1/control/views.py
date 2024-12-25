from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .models import *
from .forms import *

def control_home(request):
    return render(request, 'control/control_home.html')


class  FacultysList ( ListView ): 
    model = Facultys
    template_name = "control/faculty_list.html"
    context_object_name = "facultys"



class FacultysCreate(CreateView):
    model = Facultys
    form_class = FacultysForm
    template_name = "control/facultys_create_or_update.html"
    success_url = reverse_lazy('facultys_list')

    def form_valid(self, form):
        
        return super().form_valid(form)


class FacultysUpdate(UpdateView):
    model = Facultys
    form_class = FacultysForm
    template_name = "control/facultys_create_or_update.html"
    success_url = reverse_lazy('facultys_list')

    def form_valid(self, form):
        
        return super().form_valid(form)
    

class  KafedrasList ( ListView ): 
    model = Kafedras
    template_name = "control/kafedras_list.html"
    context_object_name = "kafedras"



class KafedrasCreate(CreateView):
    model = Kafedras
    form_class = KafedrasForm
    template_name = "control/kafedras_create_or_update.html"
    success_url = reverse_lazy('kafedras_list')

    def form_valid(self, form):
        
        return super().form_valid(form)


class KafedrasUpdate(UpdateView):
    model = Kafedras
    form_class = KafedrasForm
    template_name = "control/kafedras_create_or_update.html"
    success_url = reverse_lazy('kafedras_list')

    def form_valid(self, form):
        
        return super().form_valid(form)
    
class FacultysDelete(DeleteView):
    model = Facultys
    success_url='/control/facultys-list'
    template_name = "control/faculty_delete.html"

class KafedrasDelete(DeleteView):
    model = Kafedras
    success_url='/control/kafedras-list'
    template_name = "control/kafedras_delete.html"

# def add_faculty(request):
#     error=''
#     if request.method=='POST':
#         form=FacultysForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('control_home')
#         else:
#             error='Форма не вірна'

#     form=FacultysForm()

#     data={
#         'form':form,
#         'error':error
#     }
#     return render(request, 'control/add_faculty.html',data)



# def add_kafedra(request):
#     error=''
#     if request.method=='POST':
#         form=KafedrasForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('control_home')
#         else:
#             error='Форма не вірна'

#     form=KafedrasForm()

#     data={
#         'form':form,
#         'error':error,
         
#     }

       

#     return render(request, 'control/add_kafedra.html',data)







