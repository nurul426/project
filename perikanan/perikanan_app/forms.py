from django.forms import ModelForm
from django import forms
from .models import *

class FormLokasi(ModelForm):
    class Meta:
        model = Lokasi
        fields = '__all__'

        widgets = {
            'nama_TPI' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Tempat', 'required':'required'}),
            'g_lintang'    : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Lintang', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
            'g_bujur'   : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Bujur', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
            'gambar'       : forms.FileInput({'class':'form-control', 'required':'required'}),
        }


class FormProduksi(ModelForm):
    class Meta:
        model = Produksi
        fields = '__all__'

        widgets = {
            'nama_ikan'   : forms.TextInput({'class':'form-control', 'placeholder':'Nama Ikan', 'required':'required'}),
            'tahun1'   : forms.TextInput({'class':'form-control', 'placeholder':'2020', 'required':'required'}),
            'tahun2'   : forms.TextInput({'class':'form-control', 'placeholder':'2021', 'required':'required'}),
            'analisis'    : forms.Textarea({'class':'form-control',  'placeholder':'Deskripsi', 'required':'required'}),
        }