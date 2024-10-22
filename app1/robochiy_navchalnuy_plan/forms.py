from .models import RobochiyNavchalnuyPlan, ElementRNP
from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory


class RobochiyNavchalnuyPlanForm(ModelForm):
    class Meta:
        model=RobochiyNavchalnuyPlan
        fields='__all__'

class ElementRNPForm(ModelForm):
    class Meta:
        model=ElementRNP
        fields='__all__'
       


ElementRNPFormSet = inlineformset_factory(
    RobochiyNavchalnuyPlan, ElementRNP, form=ElementRNPForm,
    extra=1, can_delete=True, can_delete_extra=True
)