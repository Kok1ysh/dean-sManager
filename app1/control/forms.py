from .models import Facultys, Kafedras
from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory


class FacultysForm(ModelForm):
    class Meta:
        model=Facultys
        fields=['title', 'adres', 'dean']


class KafedrasForm(ModelForm):
    class Meta:
        model=Kafedras
        fields=['titleKafedra', 'adresKafedra', 'managerKafedra','facultyKafedra']

