from django.forms import *
from django import forms
from .models import *


class resultado_futbol_form(forms.ModelForm):
    
    class Meta:
        model = resultado_futbol
        fields = ['resultado','ganador']
    
    widgets = {
            
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
    }
    
    
    
    
    
class resultado_baseball_form(forms.ModelForm):
    
    class Meta:
        model = resultado_baseball
        fields = ['partido','resultado','ganador']
    
    widgets = {
            
            'partido': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
    }




class resultado_NBA_profecional_form(forms.ModelForm):
    
    class Meta:
        model = resultado_NBA_profecional
        fields = ['partido','resultado','ganador']
    
    widgets = {
            
            'partido': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
    }
    
    
    
    
    
class resultado_NBA_colegial_form(forms.ModelForm):
    
    class Meta:
        model = resultado_NBA_colegial
        fields = ['partido','resultado','ganador']
    
    widgets = {
            
            'partido': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
    }
    
    
    
    
    
    
class resultado_NLF_profecional_form(forms.ModelForm):
    
    class Meta:
        model = resultado_NLF_profecional
        fields = ['partido','resultado','ganador']
    
    widgets = {
            
            'partido': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
    }
    
    
    
    
    
class resultado_NLF_colegial_form(forms.ModelForm):
    
    class Meta:
        model = resultado_NLF_colegial
        fields = ['partido','resultado','ganador']
    
    widgets = {
            
            'partido': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
    }
    
    
    
    
    
    
class resultado_Hockey_form(forms.ModelForm):
    
    class Meta:
        model = resultado_Hockey
        fields = ['partido','resultado','ganador']
    
    widgets = {
            
            'partido': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
    }