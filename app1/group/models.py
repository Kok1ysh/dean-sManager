from django.db import models
from control.models import Facultys
from educational_programs.models import EducationalPrograms

# Create your models here.
class Groups(models.Model):
    title=models.CharField('Назва', max_length=75)
    titleFull=models.CharField('Повна назва', max_length=150)
    kurs=models.PositiveIntegerField(default=1)
    educational_programs=models.ForeignKey(EducationalPrograms,on_delete=models.PROTECT)
    faculty=models.ForeignKey(Facultys,on_delete=models.PROTECT)

    def __str__(self):
        return self.title