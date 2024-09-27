from .models import EducationalPrograms, KomponentEducationalPrograms
from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory


class EducationalProgramsForm(ModelForm):
    class Meta:
        model=EducationalPrograms
        fields='__all__'

class KomponentEducationalProgramsForm(ModelForm):
    class Meta:
        model=KomponentEducationalPrograms
        fields='__all__'
        widgets = {            
            'kredutu': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'semestr': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                )
        }


KomponentEducationalProgramsFormSet = inlineformset_factory(
    EducationalPrograms, KomponentEducationalPrograms, form=KomponentEducationalProgramsForm,
    extra=1, can_delete=True, can_delete_extra=True
)