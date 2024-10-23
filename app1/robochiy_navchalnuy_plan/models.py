from django.db import models
from educational_programs.models import EducationalPrograms, KomponentEducationalPrograms, FormaKontrolus
from group.models import Groups
from vukladach.models import Vukladach

class RobochiyNavchalnuyPlan(models.Model):
    educational_programs=models.ForeignKey(EducationalPrograms,on_delete=models.PROTECT)
    group=models.ForeignKey(Groups,on_delete=models.PROTECT)


    def __str__(self):
        return self.educational_programs.specialnist + " " + self.group.title
    

class ElementRNP(models.Model):    
    title=models.ForeignKey(KomponentEducationalPrograms,on_delete=models.PROTECT)
    vukladach=models.ForeignKey(Vukladach,on_delete=models.PROTECT)      
    Godun=models.PositiveIntegerField(default=0)
    kredutuECTS1sm=models.PositiveIntegerField(default=0)
    Godun1sm=models.PositiveIntegerField(default=0)
    lekcii1sm=models.PositiveIntegerField(default=0)
    praktuchni1sm=models.PositiveIntegerField(default=0)
    laboratorni1sm=models.PositiveIntegerField(default=0)
    samostiynaRobota1sm=models.PositiveIntegerField(default=0)
    formaKontrolu1sm=models.ForeignKey(FormaKontrolus,on_delete=models.PROTECT, related_name='elementrnp_forma1', 
        blank=True,  
        null=True)

    kredutuECTS2sm=models.PositiveIntegerField(default=0)
    Godun2sm=models.PositiveIntegerField(default=0)
    lekcii2sm=models.PositiveIntegerField(default=0)
    praktuchni2sm=models.PositiveIntegerField(default=0)
    laboratorni2sm=models.PositiveIntegerField(default=0)
    samostiynaRobota2sm=models.PositiveIntegerField(default=0)
    formaKontrolu2sm=models.ForeignKey(FormaKontrolus,on_delete=models.PROTECT, related_name='elementrnp_forma2', 
        blank=True,  
        null=True)

    robochiyNavchalnuyPlan=models.ForeignKey(RobochiyNavchalnuyPlan,on_delete=models.PROTECT)

    def __str__(self):
        return  str(self.title)

