from django.shortcuts import render

def control_home(request):
    return render(request, 'control/control_home.html')
