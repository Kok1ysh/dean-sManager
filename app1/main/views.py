from django.http import HttpResponse
from django.shortcuts import render
from control.models import Facultys



def index(request):
    facultys=Facultys.objects.all()   
    return render(request,'main/home.html',{'facultys':facultys})

def profil(request):
       
    return render(request,'main/profil.html')
