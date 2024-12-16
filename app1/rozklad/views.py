from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from .models import *
from control.models import Facultys
from .forms import RozkladForm

# Create your views here.
class  RozkladList ( ListView ): 
    model = Rozklad
    template_name = "rozklad/rozklad_list.html"
    context_object_name = "rozklads"


class RozkladUpdate(UpdateView):
    model = Rozklad
    template_name = "rozklad/rozklad_create_or_update.html"
    form_class= RozkladForm

class RozkladDelete(DeleteView):
    model = Rozklad
    success_url='/control/rozklad/'
    template_name = "rozklad/rozklad_delete.html"
    

def create(request):

    error=''
    if request.method=='POST':
        form=RozkladForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_rozklad')
        else:
            error='Форма не вірна'

    form=RozkladForm()

    data={
        'form':form,
        'error':error,
         
    }

    return render(request, "rozklad/rozklad_create_or_update.html", data)