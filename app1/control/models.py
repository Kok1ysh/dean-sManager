from django.db import models

class Facultys (models.Model):
    title=models.CharField('Назва', max_length=50)
    adres=models.CharField('Адреса факультету', max_length=150)
    dean=models.CharField('Декан факультету', max_length=50)

    def __str__(self):
        return self.title