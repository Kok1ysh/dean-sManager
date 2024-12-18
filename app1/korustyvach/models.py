from django.db import models
from django.contrib.auth.models import AbstractUser
from vukladach.models import Vukladach

# Create your models here.

class User(AbstractUser):

    is_vukladach = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    vukladach=models.ForeignKey(Vukladach,on_delete=models.PROTECT, null=True, blank=True)