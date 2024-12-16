from .models import Rozklad
from django.forms import ModelForm, Select

class RozkladForm(ModelForm):
    class Meta:
        model=Rozklad
        fields='__all__'
        widgets={
            'ponedilok_1_para': Select(attrs={ 'class':'custom-select'}),
            'ponedilok_2_para': Select(attrs={ 'class':'custom-select'}),
            'ponedilok_3_para': Select(attrs={ 'class':'custom-select'}),
            'ponedilok_4_para': Select(attrs={ 'class':'custom-select'}),
            'ponedilok_5_para': Select(attrs={ 'class':'custom-select'}),
            'vivtorok_1_para': Select(attrs={ 'class':'custom-select'}),
            'vivtorok_2_para': Select(attrs={ 'class':'custom-select'}),
            'vivtorok_3_para': Select(attrs={ 'class':'custom-select'}),
            'vivtorok_4_para': Select(attrs={ 'class':'custom-select'}),
            'vivtorok_5_para': Select(attrs={ 'class':'custom-select'}),
            'sereda_1_para': Select(attrs={ 'class':'custom-select'}),
            'sereda_2_para': Select(attrs={ 'class':'custom-select'}),
            'sereda_3_para': Select(attrs={ 'class':'custom-select'}),
            'sereda_4_para': Select(attrs={ 'class':'custom-select'}),
            'sereda_5_para': Select(attrs={ 'class':'custom-select'}),
            'chetver_1_para': Select(attrs={ 'class':'custom-select'}),
            'chetver_2_para': Select(attrs={ 'class':'custom-select'}),
            'chetver_3_para': Select(attrs={ 'class':'custom-select'}),
            'chetver_4_para': Select(attrs={ 'class':'custom-select'}),
            'chetver_5_para': Select(attrs={ 'class':'custom-select'}),
            'pyatnytsya_1_para': Select(attrs={ 'class':'custom-select'}),
            'pyatnytsya_2_para': Select(attrs={ 'class':'custom-select'}),
            'pyatnytsya_3_para': Select(attrs={ 'class':'custom-select'}),
            'pyatnytsya_4_para': Select(attrs={ 'class':'custom-select'}),
            'pyatnytsya_5_para': Select(attrs={ 'class':'custom-select'}),
            'subota_1_para': Select(attrs={ 'class':'custom-select'}),
            'subota_2_para': Select(attrs={ 'class':'custom-select'}),
            'subota_3_para': Select(attrs={ 'class':'custom-select'}),
            'subota_4_para': Select(attrs={ 'class':'custom-select'}),
            'subota_5_para': Select(attrs={ 'class':'custom-select'}),
        }