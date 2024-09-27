from django.db import models

# Create your models here.
class EducationalPrograms(models.Model):
    title=models.CharField('Назва',max_length=150)
    riven=models.CharField('Рівень',max_length=75)
    stupin=models.CharField('Ступінь',max_length=75)
    galuz=models.CharField('Галузь знань',max_length=75)
    specialnist=models.CharField('Спеціальність',max_length=75)
    specializaciya=models.CharField('Спеціалізація',max_length=75)
    osvKvalifikaciya=models.CharField('Освітня кваліфікація',max_length=150)
    profKvalifikaciya=models.CharField('Професійна кваліфікація',max_length=150)

    def __str__(self):
        return self.title
    
class FormaKontrolus(models.Model):
    title=models.CharField('Форма контролю',max_length=150)

    def __str__(self):
        return self.title

class KomponentEducationalPrograms(models.Model):
    kodND=models.CharField('Код н/д',max_length=32)
    title=models.CharField('Назва',max_length=150)
    kredutu=models.PositiveIntegerField(default=1)
    formaKontrolu=models.ForeignKey(FormaKontrolus,on_delete=models.PROTECT)
    semestr=models.PositiveIntegerField(default=1)
    educationalProgram=models.ForeignKey(EducationalPrograms,on_delete=models.PROTECT)

    def __str__(self):
        return self.title
