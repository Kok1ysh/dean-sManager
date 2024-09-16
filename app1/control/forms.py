from .models import Facultys, Kafedras
from django.forms import ModelForm


class FacultysForm(ModelForm):
    class Meta:
        model=Facultys
        fields=['title', 'adres', 'dean']


class KafedrasForm(ModelForm):
    class Meta:
        model=Kafedras
        fields=['titleKafedra', 'adresKafedra', 'managerKafedra','facultyKafedra']