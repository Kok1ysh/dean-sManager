from .models import Facultys
from django.forms import ModelForm


class FacultysForm(ModelForm):
    class Meta:
        model=Facultys
        fields=['title', 'adres', 'dean']