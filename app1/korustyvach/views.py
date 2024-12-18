from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .models import *
from .forms import *



class KorustyvachList(ListView):
    model = User
    template_name = "korustyvach/korustyvach_list.html"
    context_object_name = "korustyvachs"


#class KorustyvachCreate(CreateView):
#    form_class = UserForm
#    template_name = "korustyvach/korustyvach_create_or_update.html"
#    success_url = reverse_lazy('korustyvach_list')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('korustyvach_list')
    else:
        form = UserForm()
    return render(request, 'korustyvach/korustyvach_create_or_update.html', {'form': form})
    


class KorustyvachUpdate(UpdateView):
    
    form_class = UserForm
    template_name = "korustyvach/korustyvach_create_or_update.html"
    success_url = reverse_lazy('korustyvach_list')

    

class KorustyvachDelete(DeleteView):
    model = User
    success_url='/control/korustyvach/'
    template_name = "korustyvach/korustyvach_delete.html"


def korustyvach_login(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('home')
        
    return render(request, 'korustyvach/login.html')


def korustyvach_logout(request):
    logout(request)
    return redirect('home')