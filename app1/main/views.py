from django.http import HttpResponse
from django.shortcuts import render
from control.models import Facultys
from group.models import Groups
from grafik_navchannya.models import GrafikNavchannya
from rozklad.models import Rozklad
from robochiy_navchalnuy_plan.models import ElementRNP


def index(request):
    facultys=Facultys.objects.all() 
    context = {'facultys':facultys}
    return render(request,'main/home.html', context)

def groups(request):
    faculty = request.GET.get('faculty')
    groups = Groups.objects.filter(faculty=faculty)
    context = {'groups': groups}
    return render(request, 'main/groups.html', context)

def predmet(request):
    grupa = request.GET.get('group')
    predmet = Rozklad.objects.filter(grupa=grupa).first()
    grafik = GrafikNavchannya.objects.filter(grupa=grupa).first()
    plan=ElementRNP.objects.filter(robochiyNavchalnuyPlan__group=grupa)
    print(predmet)
    context = {'predmet': predmet,
               'grafik': grafik,
               'plan': plan}

    return render(request, 'main/predmet.html', context)

def profil(request):
       
    return render(request,'main/profil.html')
