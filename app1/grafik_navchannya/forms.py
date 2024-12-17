from .models import GrafikNavchannya
from django import forms
from django.forms import ModelForm


class GrafikNavchannyaForm(ModelForm):
    class Meta:
        model=GrafikNavchannya
        fields='__all__'