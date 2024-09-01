from django.forms import *
from django import forms
from .models import *


class equipo_futbol_form(forms.ModelForm):
    
    class Meta:
        model = equipos_futbol
        fields = ['nombre','logo']
    
    widgets = {
            
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            
    }
    
    
    
    
class equipo_baseball_form(forms.ModelForm):
    
    class Meta:
        model = equipos_baseball
        fields = ['nombre','logo']
    
    widgets = {
            
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
           
    }
    
    
    
class equipo_NBA_profecional_form(forms.ModelForm):
    
    class Meta:
        model = equipos_NBA_profecional
        fields = ['nombre','logo']
    
    widgets = {
            
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            
    }
    
    
    
class equipo_NBA_colegial_form(forms.ModelForm):
    
    class Meta:
        model = equipos_NBA_colegial
        fields = ['nombre','logo']
    
    widgets = {
            
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            
    }
    
    
    
    
    
class equipo_NLF_profecional_form(forms.ModelForm):
    
    class Meta:
        model = equipos_NLF_profecional
        fields = ['nombre','logo']
    
    widgets = {
            
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            
    }
    
    
    
    
    
class equipo_NLF_colegial_form(forms.ModelForm):
    
    class Meta:
        model = equipos_NLF_colegial
        fields = ['nombre','logo']
    
    widgets = {
            
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            
    }
    
    
    
    
    
    
class equipo_Hockey_form(forms.ModelForm):
    
    class Meta:
        model = equipos_hockey
        fields = ['nombre','logo']
    
    widgets = {
            
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            
    }