from .models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):

    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model=User
        fields=['first_name','last_name','username','password', 'is_admin', 'is_vukladach', 'vukladach']
        labels = {            
            'first_name': "Ім'я",
            'last_name': "Призвіще",
            'is_admin': "Є адміном",
            'is_vukladach': "Є викладачем", 
            'vukladach': "Викладач",
        }
        widgets = {            
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

   