from django.shortcuts import render, redirect
from .models import Facultys
from .forms import FacultysForm, KafedrasForm

def control_home(request):
    return render(request, 'control/control_home.html')

def add_faculty(request):
    error=''
    if request.method=='POST':
        form=FacultysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control_home')
        else:
            error='Форма не вірна'

    form=FacultysForm()

    data={
        'form':form,
        'error':error
    }
    return render(request, 'control/add_faculty.html',data)



def add_kafedra(request):
    error=''
    if request.method=='POST':
        form=KafedrasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control_home')
        else:
            error='Форма не вірна'

    form=KafedrasForm()

    data={
        'form':form,
        'error':error,
        'facultys':Facultys.objects.all() 
    }

       

    return render(request, 'control/add_kafedra.html',data)
