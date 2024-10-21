from .models import Vukladach
from django import forms
from django.forms import ModelForm


class VukladachForm(ModelForm):
    class Meta:
        model=Vukladach
        fields='__all__'