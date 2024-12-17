from django.db import models
from group.models import Groups

# Create your models here.

class GrafikNavchannya(models.Model):

    grupa=models.ForeignKey(Groups,on_delete=models.PROTECT)
    teoretuchne_navchannya_1sm=models.CharField("Теоретичне навчання(1 семестр)", max_length=75, null=True, blank=True)
    praktuka_1sm=models.CharField("Практика(1 семестр)", max_length=75, null=True, blank=True)
    sesiya_1sm=models.CharField("Зимова сесія", max_length=75, null=True, blank=True)
    kanikylu_1sm=models.CharField("Канікули(1 семестр)", max_length=75, null=True, blank=True)
    teoretuchne_navchannya_2sm=models.CharField("Теоретичне навчання(2 семестр)", max_length=75, null=True, blank=True)
    praktuka_2sm=models.CharField("Практика(2 семестр)", max_length=75, null=True, blank=True)
    sesiya_2sm=models.CharField("Літня сесія", max_length=75, null=True, blank=True)
    kanikylu_2sm=models.CharField("Канікули(2 семестр)", max_length=75, null=True, blank=True)
    pidgotovkaKR=models.CharField("Підготовка КР", max_length=75, null=True, blank=True)
    ekzamenaciyna_komisiya=models.CharField("ЕК", max_length=75, null=True, blank=True)

    def __str__(self):
        return self.grupa.title
