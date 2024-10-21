from django.db import models
from control.models import Facultys, Kafedras

class Vukladach(models.Model):
    imya=models.CharField("Ім'я", max_length=75)
    prizvusche=models.CharField("Прізвище", max_length=75)
    poBatkovi=models.CharField("По батькові", max_length=75)
    posada=models.CharField("Посада", max_length=175)
    naukovaStupin=models.CharField("Наукова ступінь", max_length=75)
    vcheneZvannya=models.CharField("Вчене звання", max_length=75)
    facultet=models.ForeignKey(Facultys,on_delete=models.PROTECT)
    kafedra=models.ForeignKey(Kafedras,on_delete=models.PROTECT)

    def __str__(self):
        return self.prizvusche + ' ' + self.imya
