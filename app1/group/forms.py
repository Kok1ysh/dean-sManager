from .models import Groups
from django import forms
from django.forms import ModelForm


class GroupsForm(ModelForm):
    class Meta:
        model=Groups
        fields='__all__'