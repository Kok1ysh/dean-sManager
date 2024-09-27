from django.db import models

class Facultys (models.Model):
    title=models.CharField('Назва', max_length=50)
    adres=models.CharField('Адреса факультету', max_length=150)
    dean=models.CharField('Декан факультету', max_length=50)

    def __str__(self):
        return self.title
    

class Kafedras(models.Model):
    titleKafedra=models.CharField('Назва', max_length=75)
    adresKafedra=models.CharField('Адреса кафедри', max_length=150)
    managerKafedra=models.CharField('Завідувач кафедри', max_length=50)
    facultyKafedra=models.ForeignKey(Facultys,on_delete=models.PROTECT)

    def __str__(self):
        return self.titleKafedra
    

