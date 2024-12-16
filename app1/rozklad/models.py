from django.db import models
from group.models import Groups
from robochiy_navchalnuy_plan.models import  ElementRNP
from control.models import Facultys
# Create your models here.
class Den(models.Model):
    title=models.CharField(max_length=75)

    def __str__(self):
        return self.title
    
class Para(models.Model):
    title=models.CharField(max_length=75)
    dzvinok=models.CharField(max_length=75)

    def __str__(self):
        return self.title
    

class Rozklad(models.Model):
    
    grupa=models.ForeignKey(Groups,on_delete=models.PROTECT)    
    facultet=models.ForeignKey(Facultys,on_delete=models.PROTECT)
    ponedilok_1_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="ponedilok_1")
    ponedilok_2_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="ponedilok_2")
    ponedilok_3_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="ponedilok_3")
    ponedilok_4_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="ponedilok_4")
    ponedilok_5_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="ponedilok_5")

    # Вівторок
    vivtorok_1_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="vivtorok_1")
    vivtorok_2_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="vivtorok_2")
    vivtorok_3_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="vivtorok_3")
    vivtorok_4_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="vivtorok_4")
    vivtorok_5_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="vivtorok_5")

    # Середа
    sereda_1_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="sereda_1")
    sereda_2_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="sereda_2")
    sereda_3_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="sereda_3")
    sereda_4_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="sereda_4")
    sereda_5_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="sereda_5")

    # Четвер
    chetver_1_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="chetver_1")
    chetver_2_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="chetver_2")
    chetver_3_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="chetver_3")
    chetver_4_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="chetver_4")
    chetver_5_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="chetver_5")

    # П'ятниця
    pyatnytsya_1_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="pyatnytsya_1")
    pyatnytsya_2_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="pyatnytsya_2")
    pyatnytsya_3_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="pyatnytsya_3")
    pyatnytsya_4_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="pyatnytsya_4")
    pyatnytsya_5_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="pyatnytsya_5")

    # Субота
    subota_1_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="subota_1")
    subota_2_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="subota_2")
    subota_3_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="subota_3")
    subota_4_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="subota_4")
    subota_5_para = models.ForeignKey(ElementRNP, on_delete=models.PROTECT, null=True, blank=True, related_name="subota_5")
    
    def __str__(self):
        return self.grupa.title
    
    def get_absolute_url(self):
        return f'/control/rozklad/'
    


    