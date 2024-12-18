from django.http import HttpResponse
from django.shortcuts import render
from control.models import Facultys
from group.models import Groups
from grafik_navchannya.models import GrafikNavchannya
from rozklad.models import Rozklad
from robochiy_navchalnuy_plan.models import ElementRNP
from django.db.models import Sum
from rozklad.models import Rozklad


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
    
    predmetu=ElementRNP.objects.filter(vukladach=request.user.vukladach)
    total_hours = predmetu.aggregate(Sum('Godun'))['Godun__sum'] or 0

    ponedilok_1_para = Rozklad.objects.filter(ponedilok_1_para__vukladach=request.user.vukladach).first()
    ponedilok_2_para = Rozklad.objects.filter(ponedilok_2_para__vukladach=request.user.vukladach).first()
    ponedilok_3_para = Rozklad.objects.filter(ponedilok_3_para__vukladach=request.user.vukladach).first()
    ponedilok_4_para = Rozklad.objects.filter(ponedilok_4_para__vukladach=request.user.vukladach).first()
    ponedilok_5_para = Rozklad.objects.filter(ponedilok_5_para__vukladach=request.user.vukladach).first()

    # Вівторок
    vivtorok_1_para = Rozklad.objects.filter(vivtorok_1_para__vukladach=request.user.vukladach).first()
    vivtorok_2_para = Rozklad.objects.filter(vivtorok_2_para__vukladach=request.user.vukladach).first()
    vivtorok_3_para = Rozklad.objects.filter(vivtorok_3_para__vukladach=request.user.vukladach).first()
    vivtorok_4_para = Rozklad.objects.filter(vivtorok_4_para__vukladach=request.user.vukladach).first()
    vivtorok_5_para = Rozklad.objects.filter(vivtorok_5_para__vukladach=request.user.vukladach).first()

    # Середа
    sereda_1_para = Rozklad.objects.filter(sereda_1_para__vukladach=request.user.vukladach).first()
    sereda_2_para = Rozklad.objects.filter(sereda_2_para__vukladach=request.user.vukladach).first()
    sereda_3_para = Rozklad.objects.filter(sereda_3_para__vukladach=request.user.vukladach).first()
    sereda_4_para = Rozklad.objects.filter(sereda_4_para__vukladach=request.user.vukladach).first()
    sereda_5_para = Rozklad.objects.filter(sereda_5_para__vukladach=request.user.vukladach).first()

    # Четвер
    chetver_1_para = Rozklad.objects.filter(chetver_1_para__vukladach=request.user.vukladach).first()
    chetver_2_para = Rozklad.objects.filter(chetver_2_para__vukladach=request.user.vukladach).first()
    chetver_3_para = Rozklad.objects.filter(chetver_3_para__vukladach=request.user.vukladach).first()
    chetver_4_para = Rozklad.objects.filter(chetver_4_para__vukladach=request.user.vukladach).first()
    chetver_5_para = Rozklad.objects.filter(chetver_5_para__vukladach=request.user.vukladach).first()

    # П'ятниця
    pyatnytsya_1_para = Rozklad.objects.filter(pyatnytsya_1_para__vukladach=request.user.vukladach).first()
    pyatnytsya_2_para = Rozklad.objects.filter(pyatnytsya_2_para__vukladach=request.user.vukladach).first()
    pyatnytsya_3_para = Rozklad.objects.filter(pyatnytsya_3_para__vukladach=request.user.vukladach).first()
    pyatnytsya_4_para = Rozklad.objects.filter(pyatnytsya_4_para__vukladach=request.user.vukladach).first()
    pyatnytsya_5_para = Rozklad.objects.filter(pyatnytsya_5_para__vukladach=request.user.vukladach).first()

    # Субота
    subota_1_para = Rozklad.objects.filter(subota_1_para__vukladach=request.user.vukladach).first()
    subota_2_para = Rozklad.objects.filter(subota_2_para__vukladach=request.user.vukladach).first()
    subota_3_para = Rozklad.objects.filter(subota_3_para__vukladach=request.user.vukladach).first()
    subota_4_para = Rozklad.objects.filter(subota_4_para__vukladach=request.user.vukladach).first()
    subota_5_para = Rozklad.objects.filter(subota_5_para__vukladach=request.user.vukladach).first()

    context = {
    'predmetu': predmetu,
    'total_hours': total_hours,
    'ponedilok_1_para': ponedilok_1_para,
    'ponedilok_2_para': ponedilok_2_para,
    'ponedilok_3_para': ponedilok_3_para,
    'ponedilok_4_para': ponedilok_4_para,
    'ponedilok_5_para': ponedilok_5_para,
    'vivtorok_1_para': vivtorok_1_para,
    'vivtorok_2_para': vivtorok_2_para,
    'vivtorok_3_para': vivtorok_3_para,
    'vivtorok_4_para': vivtorok_4_para,
    'vivtorok_5_para': vivtorok_5_para,
    'sereda_1_para': sereda_1_para,
    'sereda_2_para': sereda_2_para,
    'sereda_3_para': sereda_3_para,
    'sereda_4_para': sereda_4_para,
    'sereda_5_para': sereda_5_para,
    'chetver_1_para': chetver_1_para,
    'chetver_2_para': chetver_2_para,
    'chetver_3_para': chetver_3_para,
    'chetver_4_para': chetver_4_para,
    'chetver_5_para': chetver_5_para,
    'pyatnytsya_1_para': pyatnytsya_1_para,
    'pyatnytsya_2_para': pyatnytsya_2_para,
    'pyatnytsya_3_para': pyatnytsya_3_para,
    'pyatnytsya_4_para': pyatnytsya_4_para,
    'pyatnytsya_5_para': pyatnytsya_5_para,
    'subota_1_para': subota_1_para,
    'subota_2_para': subota_2_para,
    'subota_3_para': subota_3_para,
    'subota_4_para': subota_4_para,
    'subota_5_para': subota_5_para,
}
       
    return render(request,'main/profil.html', context)
