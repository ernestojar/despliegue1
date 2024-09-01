from django.forms import *
from django import forms
from .models import *
from django.db.models import Q
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

resultado_validator = RegexValidator(
    regex=r'^\d+-\d+$',
    message="El formato debe ser un número entero, un guion y otro número entero (#-#)."
)



class futbol_form(forms.ModelForm):
    

    
    class Meta:
        model = futbol
        fields = ['equipo_local', 'equipo_visitante','fecha','A_ML_equip','A_ML_prob','A_SP_equip','A_SP_prob','A_SP_dif','A_Total_OU','A_Total_prob','A_Ud_equip','A_Ud_prob','A_SB_equip','A_SB_prob','A_MA','A_BB','A_total_punto',
                  'B_ML_equip','B_ML_prob','B_SP_equip','B_SP_prob','B_SP_dif','B_Total_OU','B_Total_prob','B_Ud_equip','B_Ud_prob','B_SB_equip','B_SB_prob','B_MA','B_BB','B_total_punto','A_MA_prob','B_MA_prob','C_MA_prob','D_MA_prob',
                  'C_ML_equip','C_ML_prob','C_SP_equip','C_SP_prob','C_SP_dif','C_Total_OU','C_Total_prob','C_Ud_equip','C_Ud_prob','C_SB_equip','C_SB_prob','C_MA','C_BB','C_total_punto','E_MA_prob','F_MA_prob','G_MA_prob','H_MA_prob',
                  'D_ML_equip','D_ML_prob','D_SP_equip','D_SP_prob','D_SP_dif','D_Total_OU','D_Total_prob','D_Ud_equip','D_Ud_prob','D_SB_equip','D_SB_prob','D_MA','D_BB','D_total_punto','I_MA_prob','J_MA_prob','A_BB_prob','B_BB_prob',
                  'E_ML_equip','E_ML_prob','E_SP_equip','E_SP_prob','E_SP_dif','E_Total_OU','E_Total_prob','E_Ud_equip','E_Ud_prob','E_SB_equip','E_SB_prob','E_MA','E_BB','E_total_punto','C_BB_prob','D_BB_prob','E_BB_prob','F_BB_prob',
                  'F_ML_equip','F_ML_prob','F_SP_equip','F_SP_prob','F_SP_dif','F_Total_OU','F_Total_prob','F_Ud_equip','F_Ud_prob','F_SB_equip','F_SB_prob','F_MA','F_BB','F_total_punto','G_BB_prob','H_BB_prob','I_BB_prob','J_BB_prob',
                  'G_ML_equip','G_ML_prob','G_SP_equip','G_SP_prob','G_SP_dif','G_Total_OU','G_Total_prob','G_Ud_equip','G_Ud_prob','G_SB_equip','G_SB_prob','G_MA','G_BB','G_total_punto',
                  'H_ML_equip','H_ML_prob','H_SP_equip','H_SP_prob','H_SP_dif','H_Total_OU','H_Total_prob','H_Ud_equip','H_Ud_prob','H_SB_equip','H_SB_prob','H_MA','H_BB','H_total_punto',
                  'I_ML_equip','I_ML_prob','I_SP_equip','I_SP_prob','I_SP_dif','I_Total_OU','I_Total_prob','I_Ud_equip','I_Ud_prob','I_SB_equip','I_SB_prob','I_MA','I_BB','I_total_punto',
                  'J_ML_equip','J_ML_prob','J_SP_equip','J_SP_prob','J_SP_dif','J_Total_OU','J_Total_prob','J_Ud_equip','J_Ud_prob','J_SB_equip','J_SB_prob','J_MA','J_BB','J_total_punto',
                  ]
        
        widgets = {
            
            'equipo_local': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'equipo_visitante': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control select-field', 'placeholder': '' }),
            'A_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visitante = cleaned_data.get('equipo_visitante')

       
        existing_partidos = futbol.objects.filter(
            Q(fecha=fecha) &
            ~Q(id=self.instance.id) &  
            (
                Q(equipo_local=equipo_local) | 
                Q(equipo_visitante=equipo_visitante) 
            )
        )

        if existing_partidos.exists():
            raise ValidationError("Ya existe un partido con el mismo equipo programado para esta fecha.")

       
        if equipo_local.nombre == equipo_visitante.nombre:
           raise ValidationError("El equipo local y el equipo visitante no pueden ser el mismo.")     

    
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        J_ML_equip = cleaned_data.get('J_ML_equip')
        
        A_SP_equip = cleaned_data.get('A_SP_equip')
        A_SP_prob = cleaned_data.get('A_SP_prob')
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        J_SP_prob = cleaned_data.get('J_SP_prob')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        A_Total_OU = cleaned_data.get('A_Total_OU')
        A_Total_prob = cleaned_data.get('A_Total_prob')
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_OU = cleaned_data.get('B_Total_OU')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_OU = cleaned_data.get('C_Total_OU')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_OU = cleaned_data.get('D_Total_OU')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_OU = cleaned_data.get('E_Total_OU')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_OU = cleaned_data.get('F_Total_OU')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_OU = cleaned_data.get('G_Total_OU')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        G_Total_punto = cleaned_data.get('G_total_punto')
        H_Total_OU = cleaned_data.get('H_Total_OU')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_OU = cleaned_data.get('I_Total_OU')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_OU = cleaned_data.get('J_Total_OU')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        J_Total_punto = cleaned_data.get('J_total_punto')
       
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')
        
        A_SB_equip = cleaned_data.get('A_SB_equip')
        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_equip = cleaned_data.get('J_SB_equip')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
        A_MA= cleaned_data.get('A_MA')
        B_MA= cleaned_data.get('B_MA')
        C_MA= cleaned_data.get('C_MA')
        D_MA= cleaned_data.get('D_MA')
        E_MA= cleaned_data.get('E_MA')
        F_MA= cleaned_data.get('F_MA')
        G_MA= cleaned_data.get('G_MA')
        H_MA= cleaned_data.get('H_MA')
        I_MA= cleaned_data.get('I_MA')
        J_MA= cleaned_data.get('J_MA')
        
        A_MA_prob= cleaned_data.get('A_MA_prob')
        B_MA_prob= cleaned_data.get('B_MA_prob')
        C_MA_prob= cleaned_data.get('C_MA_prob')
        D_MA_prob= cleaned_data.get('D_MA_prob')
        E_MA_prob= cleaned_data.get('E_MA_prob')
        F_MA_prob= cleaned_data.get('F_MA_prob')
        G_MA_prob= cleaned_data.get('G_MA_prob')
        H_MA_prob= cleaned_data.get('H_MA_prob')
        I_MA_prob= cleaned_data.get('I_MA_prob')
        J_MA_prob= cleaned_data.get('J_MA_prob')
        
        
        A_BB= cleaned_data.get('A_BB')
        B_BB= cleaned_data.get('B_BB')
        C_BB= cleaned_data.get('C_BB')
        D_BB= cleaned_data.get('D_BB')
        E_BB= cleaned_data.get('E_BB')
        F_BB= cleaned_data.get('F_BB')
        G_BB= cleaned_data.get('G_BB')
        H_BB= cleaned_data.get('H_BB')
        I_BB= cleaned_data.get('I_BB')
        J_BB= cleaned_data.get('J_BB')
         
        A_BB_prob= cleaned_data.get('A_BB_prob')
        B_BB_prob= cleaned_data.get('B_BB_prob')
        C_BB_prob= cleaned_data.get('C_BB_prob')
        D_BB_prob= cleaned_data.get('D_BB_prob')
        E_BB_prob= cleaned_data.get('E_BB_prob')
        F_BB_prob= cleaned_data.get('F_BB_prob')
        G_BB_prob= cleaned_data.get('G_BB_prob')
        H_BB_prob= cleaned_data.get('H_BB_prob')
        I_BB_prob= cleaned_data.get('I_BB_prob')
        J_BB_prob= cleaned_data.get('J_BB_prob')

        
        # Realiza la validación personalizada
        if A_ML_prob or A_ML_equip:
            if not (A_ML_equip and A_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if B_ML_prob or B_ML_equip:
            if not (B_ML_equip and B_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if C_ML_prob or C_ML_equip:
            if not (C_ML_equip and C_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if D_ML_prob or D_ML_equip:
            if not (D_ML_equip and D_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if E_ML_prob or E_ML_equip:
            if not (E_ML_equip and E_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if F_ML_prob or F_ML_equip:
            if not (F_ML_equip and F_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if G_ML_prob or G_ML_equip:
            if not (G_ML_equip and G_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if H_ML_prob or H_ML_equip:
            if not (H_ML_equip and H_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if I_ML_prob or I_ML_equip:
            if not (I_ML_equip and I_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if J_ML_prob or J_ML_equip:
            if not (J_ML_equip and J_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        
        if A_SP_equip or A_SP_prob or A_SP_dif :
            if not (A_SP_equip and A_SP_prob and A_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if B_SP_equip or B_SP_prob or B_SP_dif :
            if not (B_SP_equip and B_SP_prob and B_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if C_SP_equip or C_SP_prob or C_SP_dif :
            if not (C_SP_equip and C_SP_prob and C_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if D_SP_equip or D_SP_prob or D_SP_dif :
            if not (D_SP_equip and D_SP_prob and D_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if E_SP_equip or E_SP_prob or E_SP_dif :
            if not (E_SP_equip and E_SP_prob and E_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if F_SP_equip or F_SP_prob or F_SP_dif :
            if not (F_SP_equip and F_SP_prob and F_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if G_SP_equip or G_SP_prob or G_SP_dif :
            if not (G_SP_equip and G_SP_prob and G_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if H_SP_equip or H_SP_prob or H_SP_dif :
            if not (H_SP_equip and H_SP_prob and H_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if I_SP_equip or I_SP_prob or I_SP_dif :
            if not (I_SP_equip and I_SP_prob and I_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if J_SP_equip or J_SP_prob or J_SP_dif :
            if not (J_SP_equip and J_SP_prob and J_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
  
       
        if A_Total_OU or A_Total_prob or A_Total_punto :
            if not (A_Total_OU and A_Total_prob and A_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if B_Total_OU or B_Total_prob or B_Total_punto :
            if not (B_Total_OU and B_Total_prob and B_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if C_Total_OU or C_Total_prob or C_Total_punto :
            if not (C_Total_OU and C_Total_prob and C_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if D_Total_OU or D_Total_prob or D_Total_punto :
            if not (D_Total_OU and D_Total_prob and D_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if E_Total_OU or E_Total_prob or E_Total_punto :
            if not (E_Total_OU and E_Total_prob and E_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if F_Total_OU or F_Total_prob or F_Total_punto :
            if not (F_Total_OU and F_Total_prob and F_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if G_Total_OU or G_Total_prob or G_Total_punto :
            if not (G_Total_OU and G_Total_prob and G_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if H_Total_OU or H_Total_prob or H_Total_punto :
            if not (H_Total_OU and H_Total_prob and H_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if I_Total_OU or I_Total_prob or I_Total_punto :
            if not (I_Total_OU and I_Total_prob and I_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if J_Total_OU or J_Total_prob or J_Total_punto :
            if not (J_Total_OU and J_Total_prob and J_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
      
        if A_Ud_equip or A_Ud_prob:
            if not (A_Ud_equip and A_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if B_Ud_equip or B_Ud_prob:
            if not (B_Ud_equip and B_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if C_Ud_equip or C_Ud_prob:
            if not (C_Ud_equip and C_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if D_Ud_equip or D_Ud_prob:
            if not (D_Ud_equip and D_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if E_Ud_equip or E_Ud_prob:
            if not (E_Ud_equip and E_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if F_Ud_equip or F_Ud_prob:
            if not (F_Ud_equip and F_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if G_Ud_equip or G_Ud_prob:
            if not (G_Ud_equip and G_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if H_Ud_equip or H_Ud_prob:
            if not (H_Ud_equip and H_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if I_Ud_equip or I_Ud_prob:
            if not (I_Ud_equip and I_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if J_Ud_equip or J_Ud_prob:
            if not (J_Ud_equip and J_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
       
        if A_SB_equip or A_SB_prob:
            if not (A_SB_equip and A_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if B_SB_equip or B_SB_prob:
            if not (B_SB_equip and B_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if C_SB_equip or C_SB_prob:
            if not (C_SB_equip and C_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if D_SB_equip or D_SB_prob:
            if not (D_SB_equip and D_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if E_SB_equip or E_SB_prob:
            if not (E_SB_equip and E_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if F_SB_equip or F_SB_prob:
            if not (F_SB_equip and F_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if G_SB_equip or G_SB_prob:
            if not (G_SB_equip and G_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if H_SB_equip or H_SB_prob:
            if not (H_SB_equip and H_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if I_SB_equip or I_SB_prob:
            if not (I_SB_equip and I_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if J_SB_equip or J_SB_prob:
            if not (J_SB_equip and J_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
       
        if A_MA or A_MA_prob:
            if not (A_MA and A_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if B_MA or B_MA_prob:
            if not (B_MA and B_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if C_MA or C_MA_prob:
            if not (C_MA and C_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if D_MA or D_MA_prob:
            if not (D_MA and D_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if E_MA or E_MA_prob:
            if not (E_MA and E_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if F_MA or F_MA_prob:
            if not (F_MA and F_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if G_MA or G_MA_prob:
            if not (G_MA and G_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if H_MA or H_MA_prob:
            if not (H_MA and H_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if I_MA or I_MA_prob:
            if not (I_MA and I_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if J_MA or J_MA_prob:
            if not (J_MA and J_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ") 
   
        
        if A_BB or A_BB_prob:
            if not (A_BB and A_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if B_BB or B_BB_prob:
            if not (B_BB and B_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if C_BB or C_BB_prob:
            if not (C_BB and C_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if D_BB or D_BB_prob:
            if not (D_BB and D_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if E_BB or E_BB_prob:
            if not (E_BB and E_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if F_BB or F_BB_prob:
            if not (F_BB and F_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if G_BB or G_BB_prob:
            if not (G_BB and G_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if H_BB or H_BB_prob:
            if not (H_BB and H_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if I_BB or I_BB_prob:
            if not (I_BB and I_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if J_BB or J_BB_prob:
            if not (J_BB and J_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        
       
       
       
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        
        A_SP_prob = cleaned_data.get('A_SP_prob')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        J_SP_prob = cleaned_data.get('J_SP_prob')

        A_Total_prob = cleaned_data.get('A_Total_prob')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')

        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
       
        if A_ML_prob and (A_ML_prob < 1 or A_ML_prob > 99):
            raise ValidationError({"A_ML_prob": "El valor de probabilidad debe estar entre 1 y 99."})
        if B_ML_prob and (B_ML_prob < 0 or B_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_ML_prob and (C_ML_prob < 0 or C_ML_prob > 99):
            raise ValidationError({"C_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_ML_prob and (D_ML_prob < 0 or D_ML_prob > 99):
            raise ValidationError({"D_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_ML_prob and (E_ML_prob < 0 or E_ML_prob > 99):
            raise ValidationError({"E_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_ML_prob and (F_ML_prob < 0 or F_ML_prob > 99):
            raise ValidationError({"F_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_ML_prob and (G_ML_prob < 0 or G_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_ML_prob and (H_ML_prob < 0 or H_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_ML_prob and (I_ML_prob < 0 or I_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_ML_prob and (J_ML_prob < 0 or J_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})


        if A_SP_prob and (A_SP_prob < 0 or A_SP_prob > 99):
            raise ValidationError({"A_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SP_prob and (B_SP_prob < 0 or B_SP_prob > 99):
            raise ValidationError({"B_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SP_prob and (C_SP_prob < 0 or C_SP_prob > 99):
            raise ValidationError({"C_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SP_prob and (D_SP_prob < 0 or D_SP_prob > 99):
            raise ValidationError({"D_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SP_prob and (E_SP_prob < 0 or E_SP_prob > 99):
            raise ValidationError({"E_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SP_prob and (F_SP_prob < 0 or F_SP_prob > 99):
            raise ValidationError({"F_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SP_prob and (G_SP_prob < 0 or G_SP_prob > 99):
            raise ValidationError({"G_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SP_prob and (H_SP_prob < 0 or H_SP_prob > 99):
            raise ValidationError({"H_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SP_prob and (I_SP_prob < 0 or I_SP_prob > 99):
            raise ValidationError({"I_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SP_prob and (J_SP_prob < 0 or J_SP_prob > 99):
            raise ValidationError({"J_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Total_prob and (A_Total_prob < 0 or A_Total_prob > 99):
            raise ValidationError({"A_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Total_prob and (B_Total_prob < 0 or B_Total_prob > 99):
            raise ValidationError({"B_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Total_prob and (C_Total_prob < 0 or C_Total_prob > 99):
            raise ValidationError({"C_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Total_prob and (D_Total_prob < 0 or D_Total_prob > 99):
            raise ValidationError({"D_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Total_prob and (E_Total_prob < 0 or E_Total_prob > 99):
            raise ValidationError({"E_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Total_prob and (F_Total_prob < 0 or F_Total_prob > 99):
            raise ValidationError({"F_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Total_prob and (G_Total_prob < 0 or G_Total_prob > 99):
            raise ValidationError({"G_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Total_prob and (H_Total_prob < 0 or H_Total_prob > 99):
            raise ValidationError({"H_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Total_prob and (I_Total_prob < 0 or I_Total_prob > 99):
            raise ValidationError({"I_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Total_prob and (J_Total_prob < 0 or J_Total_prob > 99):
            raise ValidationError({"J_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Ud_prob and (A_Ud_prob < 0 or A_Ud_prob > 99):
            raise ValidationError({"A_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Ud_prob and (B_Ud_prob < 0 or B_Ud_prob > 99):
            raise ValidationError({"B_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Ud_prob and (C_Ud_prob < 0 or C_Ud_prob > 99):
            raise ValidationError({"C_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Ud_prob and (D_Ud_prob < 0 or D_Ud_prob > 99):
            raise ValidationError({"D_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Ud_prob and (E_Ud_prob < 0 or E_Ud_prob > 99):
            raise ValidationError({"E_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Ud_prob and (F_Ud_prob < 0 or F_Ud_prob > 99):
            raise ValidationError({"F_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Ud_prob and (G_Ud_prob < 0 or G_Ud_prob > 99):
            raise ValidationError({"G_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Ud_prob and (H_Ud_prob < 0 or H_Ud_prob > 99):
            raise ValidationError({"H_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Ud_prob and (I_Ud_prob < 0 or I_Ud_prob > 99):
            raise ValidationError({"I_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Ud_prob and (J_Ud_prob < 0 or J_Ud_prob > 99):
            raise ValidationError({"J_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_SB_prob and (A_SB_prob < 0 or A_SB_prob > 99):
            raise ValidationError({"A_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SB_prob and (B_SB_prob < 0 or B_SB_prob > 99):
            raise ValidationError({"B_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SB_prob and (C_SB_prob < 0 or C_SB_prob > 99):
            raise ValidationError({"C_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SB_prob and (D_SB_prob < 0 or D_SB_prob > 99):
            raise ValidationError({"D_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SB_prob and (E_SB_prob < 0 or E_SB_prob > 99):
            raise ValidationError({"E_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SB_prob and (F_SB_prob < 0 or F_SB_prob > 99):
            raise ValidationError({"F_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SB_prob and (G_SB_prob < 0 or G_SB_prob > 99):
            raise ValidationError({"G_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SB_prob and (H_SB_prob < 0 or H_SB_prob > 99):
            raise ValidationError({"H_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SB_prob and (I_SB_prob < 0 or I_SB_prob > 99):
            raise ValidationError({"I_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SB_prob and (J_SB_prob < 0 or J_SB_prob > 99):
            raise ValidationError({"J_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
          
        if A_MA_prob and (A_MA_prob < 0 or A_MA_prob > 99):
            raise ValidationError({"A_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_MA_prob and (B_MA_prob < 0 or B_MA_prob > 99):
            raise ValidationError({"B_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if C_MA_prob and (C_MA_prob < 0 or C_MA_prob > 99):
            raise ValidationError({"C_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if D_MA_prob and (D_MA_prob < 0 or D_MA_prob > 99):
            raise ValidationError({"D_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if E_MA_prob and (E_MA_prob < 0 or E_MA_prob > 99):
            raise ValidationError({"E_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_MA_prob and (F_MA_prob < 0 or F_MA_prob > 99):
            raise ValidationError({"F_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_MA_prob and (G_MA_prob < 0 or G_MA_prob > 99):
            raise ValidationError({"G_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_MA_prob and (H_MA_prob < 0 or H_MA_prob > 99):
            raise ValidationError({"H_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_MA_prob and (I_MA_prob < 0 or I_MA_prob > 99):
            raise ValidationError({"I_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_MA_prob and (J_MA_prob < 0 or J_MA_prob > 99):
            raise ValidationError({"J_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        if A_BB_prob and (A_BB_prob < 0 or A_BB_prob > 99):
            raise ValidationError({"A_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_BB_prob and (B_BB_prob < 0 or B_BB_prob > 99):
            raise ValidationError({"B_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_BB_prob and (C_BB_prob < 0 or C_BB_prob > 99):
            raise ValidationError({"C_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_BB_prob and (D_BB_prob < 0 or D_BB_prob > 99):
            raise ValidationError({"D_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_BB_prob and (E_BB_prob < 0 or E_BB_prob > 99):
            raise ValidationError({"E_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_BB_prob and (F_BB_prob < 0 or F_BB_prob > 99):
            raise ValidationError({"F_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_BB_prob and (G_BB_prob < 0 or G_BB_prob > 99):
            raise ValidationError({"G_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_BB_prob and (H_BB_prob < 0 or H_BB_prob > 99):
            raise ValidationError({"H_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_BB_prob and (I_BB_prob < 0 or I_BB_prob > 99):
            raise ValidationError({"I_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_BB_prob and (J_BB_prob < 0 or J_BB_prob > 99):
            raise ValidationError({"J_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_equip = cleaned_data.get('J_ML_equip')

        A_SP_equip = cleaned_data.get('A_SP_equip')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
       
        A_SB_equip = cleaned_data.get('A_SB_equip')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        J_SB_equip = cleaned_data.get('J_SB_equip')
       
        A_MA = cleaned_data.get('A_MA')
        B_MA = cleaned_data.get('B_MA')
        C_MA = cleaned_data.get('C_MA')
        D_MA = cleaned_data.get('D_MA')
        E_MA = cleaned_data.get('E_MA')
        F_MA = cleaned_data.get('F_MA')
        G_MA = cleaned_data.get('G_MA')
        H_MA = cleaned_data.get('H_MA')
        I_MA = cleaned_data.get('I_MA')
        J_MA = cleaned_data.get('J_MA')

        A_BB = cleaned_data.get('A_BB')
        B_BB = cleaned_data.get('B_BB')
        C_BB = cleaned_data.get('C_BB')
        D_BB = cleaned_data.get('D_BB')
        E_BB = cleaned_data.get('E_BB')
        F_BB = cleaned_data.get('F_BB')
        G_BB = cleaned_data.get('G_BB')
        H_BB = cleaned_data.get('H_BB')
        I_BB = cleaned_data.get('I_BB')
        J_BB = cleaned_data.get('J_BB')
        
        
              
        # Validación para ganador
        if A_ML_equip and (A_ML_equip != equipo_local and A_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})
        if B_ML_equip and (B_ML_equip != equipo_local and B_ML_equip != equipo_visitante):
            raise ValidationError({"B_ML_equip": "Debes elegir un equipo válido."})
        if C_ML_equip and (C_ML_equip != equipo_local and C_ML_equip != equipo_visitante):
            raise ValidationError({"C_ML_equip": "Debes elegir un equipo válido."})
        if D_ML_equip and (D_ML_equip != equipo_local and D_ML_equip != equipo_visitante):
            raise ValidationError({"D_ML_equip": "Debes elegir un equipo válido."})
        if E_ML_equip and (E_ML_equip != equipo_local and E_ML_equip != equipo_visitante):
            raise ValidationError({"E_ML_equip": "Debes elegir un equipo válido."})
        if F_ML_equip and (F_ML_equip != equipo_local and F_ML_equip != equipo_visitante):
            raise ValidationError({"F_ML_equip": "Debes elegir un equipo válido."})
        if G_ML_equip and (G_ML_equip != equipo_local and G_ML_equip != equipo_visitante):
            raise ValidationError({"G_ML_equip": "Debes elegir un equipo válido."})
        if H_ML_equip and (H_ML_equip != equipo_local and H_ML_equip != equipo_visitante):
            raise ValidationError({"H_ML_equip": "Debes elegir un equipo válido."})
        if I_ML_equip and (I_ML_equip != equipo_local and I_ML_equip != equipo_visitante):
            raise ValidationError({"I_ML_equip": "Debes elegir un equipo válido."})
        if J_ML_equip and (J_ML_equip != equipo_local and J_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})

        if A_SP_equip and (A_SP_equip != equipo_local and A_SP_equip != equipo_visitante):
            raise ValidationError({"A_SP_equip": "Debes elegir un equipo válido."})
        if B_SP_equip and (B_SP_equip != equipo_local and B_SP_equip != equipo_visitante):
            raise ValidationError({"B_SP_equip": "Debes elegir un equipo válido."})
        if C_SP_equip and (C_SP_equip != equipo_local and C_SP_equip != equipo_visitante):
            raise ValidationError({"C_SP_equip": "Debes elegir un equipo válido."})
        if D_SP_equip and (D_SP_equip != equipo_local and D_SP_equip != equipo_visitante):
            raise ValidationError({"D_SP_equip": "Debes elegir un equipo válido."})
        if E_SP_equip and (E_SP_equip != equipo_local and E_SP_equip != equipo_visitante):
            raise ValidationError({"E_SP_equip": "Debes elegir un equipo válido."})
        if F_SP_equip and (F_SP_equip != equipo_local and F_SP_equip != equipo_visitante):
            raise ValidationError({"F_SP_equip": "Debes elegir un equipo válido."})
        if G_SP_equip and (G_SP_equip != equipo_local and G_SP_equip != equipo_visitante):
            raise ValidationError({"G_SP_equip": "Debes elegir un equipo válido."})
        if H_SP_equip and (H_SP_equip != equipo_local and H_SP_equip != equipo_visitante):
            raise ValidationError({"H_SP_equip": "Debes elegir un equipo válido."})
        if I_SP_equip and (I_SP_equip != equipo_local and I_SP_equip != equipo_visitante):
            raise ValidationError({"I_SP_equip": "Debes elegir un equipo válido."})
        if J_SP_equip and (J_SP_equip != equipo_local and J_SP_equip != equipo_visitante):
            raise ValidationError({"J_SP_equip": "Debes elegir un equipo válido."})
        
        if A_Ud_equip and (A_Ud_equip != equipo_local and A_Ud_equip != equipo_visitante):
            raise ValidationError({"A_Ud_equip": "Debes elegir un equipo válido."})
        if B_Ud_equip and (B_Ud_equip != equipo_local and B_Ud_equip != equipo_visitante):
            raise ValidationError({"B_Ud_equip": "Debes elegir un equipo válido."})
        if C_Ud_equip and (C_Ud_equip != equipo_local and C_Ud_equip != equipo_visitante):
            raise ValidationError({"C_Ud_equip": "Debes elegir un equipo válido."})
        if D_Ud_equip and (D_Ud_equip != equipo_local and D_Ud_equip != equipo_visitante):
            raise ValidationError({"D_Ud_equip": "Debes elegir un equipo válido."})
        if E_Ud_equip and (E_Ud_equip != equipo_local and E_Ud_equip != equipo_visitante):
            raise ValidationError({"E_Ud_equip": "Debes elegir un equipo válido."})
        if F_Ud_equip and (F_Ud_equip != equipo_local and F_Ud_equip != equipo_visitante):
            raise ValidationError({"F_Ud_equip": "Debes elegir un equipo válido."})
        if G_Ud_equip and (G_Ud_equip != equipo_local and G_Ud_equip != equipo_visitante):
            raise ValidationError({"G_Ud_equip": "Debes elegir un equipo válido."})
        if H_Ud_equip and (H_Ud_equip != equipo_local and H_Ud_equip != equipo_visitante):
            raise ValidationError({"H_Ud_equip": "Debes elegir un equipo válido."})
        if I_Ud_equip and (I_Ud_equip != equipo_local and I_Ud_equip != equipo_visitante):
            raise ValidationError({"I_Ud_equip": "Debes elegir un equipo válido."})
        if J_Ud_equip and (J_Ud_equip != equipo_local and J_Ud_equip != equipo_visitante):
            raise ValidationError({"J_Ud_equip": "Debes elegir un equipo válido."})
        
        if A_SB_equip and (A_SB_equip != equipo_local and A_SB_equip != equipo_visitante):
            raise ValidationError({"A_SB_equip": "Debes elegir un equipo válido."})
        if B_SB_equip and (B_SB_equip != equipo_local and B_SB_equip != equipo_visitante):
            raise ValidationError({"B_SB_equip": "Debes elegir un equipo válido."})
        if C_SB_equip and (C_SB_equip != equipo_local and C_SB_equip != equipo_visitante):
            raise ValidationError({"C_SB_equip": "Debes elegir un equipo válido."})
        if D_SB_equip and (D_SB_equip != equipo_local and D_SB_equip != equipo_visitante):
            raise ValidationError({"D_SB_equip": "Debes elegir un equipo válido."})
        if E_SB_equip and (E_SB_equip != equipo_local and E_SB_equip != equipo_visitante):
            raise ValidationError({"E_SB_equip": "Debes elegir un equipo válido."})
        if F_SB_equip and (F_SB_equip != equipo_local and F_SB_equip != equipo_visitante):
            raise ValidationError({"F_SB_equip": "Debes elegir un equipo válido."})
        if G_SB_equip and (G_SB_equip != equipo_local and G_SB_equip != equipo_visitante):
            raise ValidationError({"G_SB_equip": "Debes elegir un equipo válido."})
        if H_SB_equip and (H_SB_equip != equipo_local and H_SB_equip != equipo_visitante):
            raise ValidationError({"H_SB_equip": "Debes elegir un equipo válido."})
        if I_SB_equip and (I_SB_equip != equipo_local and I_SB_equip != equipo_visitante):
            raise ValidationError({"I_SB_equip": "Debes elegir un equipo válido."})
        if J_SB_equip and (J_SB_equip != equipo_local and J_SB_equip != equipo_visitante):
            raise ValidationError({"J_SB_equip": "Debes elegir un equipo válido."})
        
        if A_MA and (A_MA != equipo_local and A_MA != equipo_visitante):
            raise ValidationError({"A_MA": "Debes elegir un equipo válido."})
        if B_MA and (B_MA != equipo_local and B_MA != equipo_visitante):
            raise ValidationError({"B_MA": "Debes elegir un equipo válido."})
        if C_MA and (C_MA != equipo_local and C_MA != equipo_visitante):
            raise ValidationError({"C_MA": "Debes elegir un equipo válido."})
        if D_MA and (D_MA != equipo_local and D_MA != equipo_visitante):
            raise ValidationError({"D_MA": "Debes elegir un equipo válido."})
        if E_MA and (E_MA != equipo_local and E_MA != equipo_visitante):
            raise ValidationError({"E_MA": "Debes elegir un equipo válido."})
        if F_MA and (F_MA != equipo_local and F_MA != equipo_visitante):
            raise ValidationError({"F_MA": "Debes elegir un equipo válido."})
        if G_MA and (G_MA != equipo_local and G_MA != equipo_visitante):
            raise ValidationError({"G_MA": "Debes elegir un equipo válido."})
        if H_MA and (H_MA != equipo_local and H_MA != equipo_visitante):
            raise ValidationError({"H_MA": "Debes elegir un equipo válido."})
        if I_MA and (I_MA != equipo_local and I_MA != equipo_visitante):
            raise ValidationError({"I_MA": "Debes elegir un equipo válido."})
        if J_MA and (J_MA != equipo_local and J_MA != equipo_visitante):
            raise ValidationError({"J_MA": "Debes elegir un equipo válido."})
        
        if A_BB and (A_BB != equipo_local and A_BB != equipo_visitante):
            raise ValidationError({"A_BB": "Debes elegir un equipo válido."})
        if B_BB and (B_BB != equipo_local and B_BB != equipo_visitante):
            raise ValidationError({"B_BB": "Debes elegir un equipo válido."})
        if C_BB and (C_BB != equipo_local and C_BB != equipo_visitante):
            raise ValidationError({"C_BB": "Debes elegir un equipo válido."})
        if D_BB and (D_BB != equipo_local and D_BB != equipo_visitante):
            raise ValidationError({"D_BB": "Debes elegir un equipo válido."})
        if E_BB and (E_BB != equipo_local and E_BB != equipo_visitante):
            raise ValidationError({"E_BB": "Debes elegir un equipo válido."})
        if F_BB and (F_BB != equipo_local and F_BB != equipo_visitante):
            raise ValidationError({"F_BB": "Debes elegir un equipo válido."})
        if G_BB and (G_BB != equipo_local and G_BB != equipo_visitante):
            raise ValidationError({"G_BB": "Debes elegir un equipo válido."})
        if H_BB and (H_BB != equipo_local and H_BB != equipo_visitante):
            raise ValidationError({"H_BB": "Debes elegir un equipo válido."})
        if I_BB and (I_BB != equipo_local and I_BB != equipo_visitante):
            raise ValidationError({"I_BB": "Debes elegir un equipo válido."})
        if J_BB and (J_BB != equipo_local and J_BB != equipo_visitante):
            raise ValidationError({"J_BB": "Debes elegir un equipo válido."})
         

        
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_punto = cleaned_data.get('G_total_punto')     
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_punto = cleaned_data.get('J_total_punto')
        
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        
        if A_Total_punto and (A_Total_punto < 0 ):
            raise ValidationError({"A_Total_punto": "Introdusca un valor válido."})
        if B_Total_punto and (B_Total_punto < 0 ):
            raise ValidationError({"B_Total_punto": "Introdusca un valor válido."})
        if C_Total_punto and (C_Total_punto < 0 ):
            raise ValidationError({"C_Total_punto": "Introdusca un valor válido."})
        if D_Total_punto and (D_Total_punto < 0 ):
            raise ValidationError({"D_Total_punto": "Introdusca un valor válido."})
        if E_Total_punto and (E_Total_punto < 0 ):
            raise ValidationError({"E_Total_punto": "Introdusca un valor válido."})
        if F_Total_punto and (F_Total_punto < 0 ):
            raise ValidationError({"F_Total_punto": "Introdusca un valor válido."})
        if G_Total_punto and (G_Total_punto < 0 ):
            raise ValidationError({"G_Total_punto": "Introdusca un valor válido."})
        if H_Total_punto and (H_Total_punto < 0 ):
            raise ValidationError({"H_Total_punto": "Introdusca un valor válido."})
        if I_Total_punto and (I_Total_punto < 0 ):
            raise ValidationError({"I_Total_punto": "Introdusca un valor válido."})
        if J_Total_punto and (J_Total_punto < 0 ):
            raise ValidationError({"J_Total_punto": "Introdusca un valor válido."})
        
        if A_SP_dif and (A_SP_dif < 0 ):
            raise ValidationError({"A_SP_dif": "Introdusca un valor válido."})
        if B_SP_dif and (B_SP_dif < 0 ):
            raise ValidationError({"B_SP_dif": "Introdusca un valor válido."})
        if C_SP_dif and (C_SP_dif < 0 ):
            raise ValidationError({"C_SP_dif": "Introdusca un valor válido."})
        if D_SP_dif and (D_SP_dif < 0 ):
            raise ValidationError({"D_SP_dif": "Introdusca un valor válido."})
        if E_SP_dif and (E_SP_dif < 0 ):
            raise ValidationError({"E_SP_dif": "Introdusca un valor válido."})
        if F_SP_dif and (F_SP_dif < 0 ):
            raise ValidationError({"F_SP_dif": "Introdusca un valor válido."})
        if G_SP_dif and (G_SP_dif < 0 ):
            raise ValidationError({"G_SP_dif": "Introdusca un valor válido."})
        if H_SP_dif and (H_SP_dif < 0 ):
            raise ValidationError({"H_SP_dif": "Introdusca un valor válido."})
        if I_SP_dif and (I_SP_dif < 0 ):
            raise ValidationError({"I_SP_dif": "Introdusca un valor válido."})
        if J_SP_dif and (J_SP_dif < 0 ):
            raise ValidationError({"J_SP_dif": "Introdusca un valor válido."})
        
        return cleaned_data
    
    
    
        
class baseball_form(forms.ModelForm):
    

    
    class Meta:
        model = Baseball
        fields = ['equipo_local', 'equipo_visitante','fecha','A_ML_equip','A_ML_prob','A_SP_equip','A_SP_prob','A_SP_dif','A_Total_OU','A_Total_prob','A_Ud_equip','A_Ud_prob','A_SB_equip','A_SB_prob','A_MA','A_BB','A_total_punto',
                  'B_ML_equip','B_ML_prob','B_SP_equip','B_SP_prob','B_SP_dif','B_Total_OU','B_Total_prob','B_Ud_equip','B_Ud_prob','B_SB_equip','B_SB_prob','B_MA','B_BB','B_total_punto','A_MA_prob','B_MA_prob','C_MA_prob','D_MA_prob',
                  'C_ML_equip','C_ML_prob','C_SP_equip','C_SP_prob','C_SP_dif','C_Total_OU','C_Total_prob','C_Ud_equip','C_Ud_prob','C_SB_equip','C_SB_prob','C_MA','C_BB','C_total_punto','E_MA_prob','F_MA_prob','G_MA_prob','H_MA_prob',
                  'D_ML_equip','D_ML_prob','D_SP_equip','D_SP_prob','D_SP_dif','D_Total_OU','D_Total_prob','D_Ud_equip','D_Ud_prob','D_SB_equip','D_SB_prob','D_MA','D_BB','D_total_punto','I_MA_prob','J_MA_prob','A_BB_prob','B_BB_prob',
                  'E_ML_equip','E_ML_prob','E_SP_equip','E_SP_prob','E_SP_dif','E_Total_OU','E_Total_prob','E_Ud_equip','E_Ud_prob','E_SB_equip','E_SB_prob','E_MA','E_BB','E_total_punto','C_BB_prob','D_BB_prob','E_BB_prob','F_BB_prob',
                  'F_ML_equip','F_ML_prob','F_SP_equip','F_SP_prob','F_SP_dif','F_Total_OU','F_Total_prob','F_Ud_equip','F_Ud_prob','F_SB_equip','F_SB_prob','F_MA','F_BB','F_total_punto','G_BB_prob','H_BB_prob','I_BB_prob','J_BB_prob',
                  'G_ML_equip','G_ML_prob','G_SP_equip','G_SP_prob','G_SP_dif','G_Total_OU','G_Total_prob','G_Ud_equip','G_Ud_prob','G_SB_equip','G_SB_prob','G_MA','G_BB','G_total_punto',
                  'H_ML_equip','H_ML_prob','H_SP_equip','H_SP_prob','H_SP_dif','H_Total_OU','H_Total_prob','H_Ud_equip','H_Ud_prob','H_SB_equip','H_SB_prob','H_MA','H_BB','H_total_punto',
                  'I_ML_equip','I_ML_prob','I_SP_equip','I_SP_prob','I_SP_dif','I_Total_OU','I_Total_prob','I_Ud_equip','I_Ud_prob','I_SB_equip','I_SB_prob','I_MA','I_BB','I_total_punto',
                  'J_ML_equip','J_ML_prob','J_SP_equip','J_SP_prob','J_SP_dif','J_Total_OU','J_Total_prob','J_Ud_equip','J_Ud_prob','J_SB_equip','J_SB_prob','J_MA','J_BB','J_total_punto',
                  ]
        
        widgets = {
            
            'equipo_local': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'equipo_visitante': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control select-field', 'placeholder': '' }),
            'A_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visitante = cleaned_data.get('equipo_visitante')

       
        existing_partidos = Baseball.objects.filter(
            Q(fecha=fecha) &
            ~Q(id=self.instance.id) &  
            (
                Q(equipo_local=equipo_local) | 
                Q(equipo_visitante=equipo_visitante) 
            )
        )

        if existing_partidos.exists():
            raise ValidationError("Ya existe un partido con el mismo equipo programado para esta fecha.")

       
        if equipo_local.nombre == equipo_visitante.nombre:
           raise ValidationError("El equipo local y el equipo visitante no pueden ser el mismo.")     

    
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        J_ML_equip = cleaned_data.get('J_ML_equip')
        
        A_SP_equip = cleaned_data.get('A_SP_equip')
        A_SP_prob = cleaned_data.get('A_SP_prob')
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        J_SP_prob = cleaned_data.get('J_SP_prob')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        A_Total_OU = cleaned_data.get('A_Total_OU')
        A_Total_prob = cleaned_data.get('A_Total_prob')
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_OU = cleaned_data.get('B_Total_OU')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_OU = cleaned_data.get('C_Total_OU')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_OU = cleaned_data.get('D_Total_OU')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_OU = cleaned_data.get('E_Total_OU')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_OU = cleaned_data.get('F_Total_OU')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_OU = cleaned_data.get('G_Total_OU')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        G_Total_punto = cleaned_data.get('G_total_punto')
        H_Total_OU = cleaned_data.get('H_Total_OU')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_OU = cleaned_data.get('I_Total_OU')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_OU = cleaned_data.get('J_Total_OU')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        J_Total_punto = cleaned_data.get('J_total_punto')
       
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')
        
        A_SB_equip = cleaned_data.get('A_SB_equip')
        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_equip = cleaned_data.get('J_SB_equip')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
        A_MA= cleaned_data.get('A_MA')
        B_MA= cleaned_data.get('B_MA')
        C_MA= cleaned_data.get('C_MA')
        D_MA= cleaned_data.get('D_MA')
        E_MA= cleaned_data.get('E_MA')
        F_MA= cleaned_data.get('F_MA')
        G_MA= cleaned_data.get('G_MA')
        H_MA= cleaned_data.get('H_MA')
        I_MA= cleaned_data.get('I_MA')
        J_MA= cleaned_data.get('J_MA')
        
        A_MA_prob= cleaned_data.get('A_MA_prob')
        B_MA_prob= cleaned_data.get('B_MA_prob')
        C_MA_prob= cleaned_data.get('C_MA_prob')
        D_MA_prob= cleaned_data.get('D_MA_prob')
        E_MA_prob= cleaned_data.get('E_MA_prob')
        F_MA_prob= cleaned_data.get('F_MA_prob')
        G_MA_prob= cleaned_data.get('G_MA_prob')
        H_MA_prob= cleaned_data.get('H_MA_prob')
        I_MA_prob= cleaned_data.get('I_MA_prob')
        J_MA_prob= cleaned_data.get('J_MA_prob')
        
        
        A_BB= cleaned_data.get('A_BB')
        B_BB= cleaned_data.get('B_BB')
        C_BB= cleaned_data.get('C_BB')
        D_BB= cleaned_data.get('D_BB')
        E_BB= cleaned_data.get('E_BB')
        F_BB= cleaned_data.get('F_BB')
        G_BB= cleaned_data.get('G_BB')
        H_BB= cleaned_data.get('H_BB')
        I_BB= cleaned_data.get('I_BB')
        J_BB= cleaned_data.get('J_BB')
         
        A_BB_prob= cleaned_data.get('A_BB_prob')
        B_BB_prob= cleaned_data.get('B_BB_prob')
        C_BB_prob= cleaned_data.get('C_BB_prob')
        D_BB_prob= cleaned_data.get('D_BB_prob')
        E_BB_prob= cleaned_data.get('E_BB_prob')
        F_BB_prob= cleaned_data.get('F_BB_prob')
        G_BB_prob= cleaned_data.get('G_BB_prob')
        H_BB_prob= cleaned_data.get('H_BB_prob')
        I_BB_prob= cleaned_data.get('I_BB_prob')
        J_BB_prob= cleaned_data.get('J_BB_prob')

        
        # Realiza la validación personalizada
        if A_ML_prob or A_ML_equip:
            if not (A_ML_equip and A_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if B_ML_prob or B_ML_equip:
            if not (B_ML_equip and B_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if C_ML_prob or C_ML_equip:
            if not (C_ML_equip and C_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if D_ML_prob or D_ML_equip:
            if not (D_ML_equip and D_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if E_ML_prob or E_ML_equip:
            if not (E_ML_equip and E_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if F_ML_prob or F_ML_equip:
            if not (F_ML_equip and F_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if G_ML_prob or G_ML_equip:
            if not (G_ML_equip and G_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if H_ML_prob or H_ML_equip:
            if not (H_ML_equip and H_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if I_ML_prob or I_ML_equip:
            if not (I_ML_equip and I_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if J_ML_prob or J_ML_equip:
            if not (J_ML_equip and J_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        
        if A_SP_equip or A_SP_prob or A_SP_dif :
            if not (A_SP_equip and A_SP_prob and A_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if B_SP_equip or B_SP_prob or B_SP_dif :
            if not (B_SP_equip and B_SP_prob and B_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if C_SP_equip or C_SP_prob or C_SP_dif :
            if not (C_SP_equip and C_SP_prob and C_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if D_SP_equip or D_SP_prob or D_SP_dif :
            if not (D_SP_equip and D_SP_prob and D_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if E_SP_equip or E_SP_prob or E_SP_dif :
            if not (E_SP_equip and E_SP_prob and E_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if F_SP_equip or F_SP_prob or F_SP_dif :
            if not (F_SP_equip and F_SP_prob and F_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if G_SP_equip or G_SP_prob or G_SP_dif :
            if not (G_SP_equip and G_SP_prob and G_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if H_SP_equip or H_SP_prob or H_SP_dif :
            if not (H_SP_equip and H_SP_prob and H_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if I_SP_equip or I_SP_prob or I_SP_dif :
            if not (I_SP_equip and I_SP_prob and I_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if J_SP_equip or J_SP_prob or J_SP_dif :
            if not (J_SP_equip and J_SP_prob and J_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
  
       
        if A_Total_OU or A_Total_prob or A_Total_punto :
            if not (A_Total_OU and A_Total_prob and A_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if B_Total_OU or B_Total_prob or B_Total_punto :
            if not (B_Total_OU and B_Total_prob and B_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if C_Total_OU or C_Total_prob or C_Total_punto :
            if not (C_Total_OU and C_Total_prob and C_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if D_Total_OU or D_Total_prob or D_Total_punto :
            if not (D_Total_OU and D_Total_prob and D_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if E_Total_OU or E_Total_prob or E_Total_punto :
            if not (E_Total_OU and E_Total_prob and E_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if F_Total_OU or F_Total_prob or F_Total_punto :
            if not (F_Total_OU and F_Total_prob and F_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if G_Total_OU or G_Total_prob or G_Total_punto :
            if not (G_Total_OU and G_Total_prob and G_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if H_Total_OU or H_Total_prob or H_Total_punto :
            if not (H_Total_OU and H_Total_prob and H_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if I_Total_OU or I_Total_prob or I_Total_punto :
            if not (I_Total_OU and I_Total_prob and I_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if J_Total_OU or J_Total_prob or J_Total_punto :
            if not (J_Total_OU and J_Total_prob and J_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
      
        if A_Ud_equip or A_Ud_prob:
            if not (A_Ud_equip and A_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if B_Ud_equip or B_Ud_prob:
            if not (B_Ud_equip and B_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if C_Ud_equip or C_Ud_prob:
            if not (C_Ud_equip and C_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if D_Ud_equip or D_Ud_prob:
            if not (D_Ud_equip and D_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if E_Ud_equip or E_Ud_prob:
            if not (E_Ud_equip and E_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if F_Ud_equip or F_Ud_prob:
            if not (F_Ud_equip and F_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if G_Ud_equip or G_Ud_prob:
            if not (G_Ud_equip and G_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if H_Ud_equip or H_Ud_prob:
            if not (H_Ud_equip and H_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if I_Ud_equip or I_Ud_prob:
            if not (I_Ud_equip and I_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if J_Ud_equip or J_Ud_prob:
            if not (J_Ud_equip and J_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
       
        if A_SB_equip or A_SB_prob:
            if not (A_SB_equip and A_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if B_SB_equip or B_SB_prob:
            if not (B_SB_equip and B_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if C_SB_equip or C_SB_prob:
            if not (C_SB_equip and C_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if D_SB_equip or D_SB_prob:
            if not (D_SB_equip and D_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if E_SB_equip or E_SB_prob:
            if not (E_SB_equip and E_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if F_SB_equip or F_SB_prob:
            if not (F_SB_equip and F_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if G_SB_equip or G_SB_prob:
            if not (G_SB_equip and G_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if H_SB_equip or H_SB_prob:
            if not (H_SB_equip and H_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if I_SB_equip or I_SB_prob:
            if not (I_SB_equip and I_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if J_SB_equip or J_SB_prob:
            if not (J_SB_equip and J_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
       
        if A_MA or A_MA_prob:
            if not (A_MA and A_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if B_MA or B_MA_prob:
            if not (B_MA and B_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if C_MA or C_MA_prob:
            if not (C_MA and C_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if D_MA or D_MA_prob:
            if not (D_MA and D_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if E_MA or E_MA_prob:
            if not (E_MA and E_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if F_MA or F_MA_prob:
            if not (F_MA and F_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if G_MA or G_MA_prob:
            if not (G_MA and G_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if H_MA or H_MA_prob:
            if not (H_MA and H_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if I_MA or I_MA_prob:
            if not (I_MA and I_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if J_MA or J_MA_prob:
            if not (J_MA and J_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ") 
   
        
        if A_BB or A_BB_prob:
            if not (A_BB and A_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if B_BB or B_BB_prob:
            if not (B_BB and B_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if C_BB or C_BB_prob:
            if not (C_BB and C_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if D_BB or D_BB_prob:
            if not (D_BB and D_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if E_BB or E_BB_prob:
            if not (E_BB and E_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if F_BB or F_BB_prob:
            if not (F_BB and F_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if G_BB or G_BB_prob:
            if not (G_BB and G_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if H_BB or H_BB_prob:
            if not (H_BB and H_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if I_BB or I_BB_prob:
            if not (I_BB and I_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if J_BB or J_BB_prob:
            if not (J_BB and J_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        
       
       
       
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        
        A_SP_prob = cleaned_data.get('A_SP_prob')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        J_SP_prob = cleaned_data.get('J_SP_prob')

        A_Total_prob = cleaned_data.get('A_Total_prob')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')

        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
       
        if A_ML_prob and (A_ML_prob < 1 or A_ML_prob > 99):
            raise ValidationError({"A_ML_prob": "El valor de probabilidad debe estar entre 1 y 99."})
        if B_ML_prob and (B_ML_prob < 0 or B_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_ML_prob and (C_ML_prob < 0 or C_ML_prob > 99):
            raise ValidationError({"C_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_ML_prob and (D_ML_prob < 0 or D_ML_prob > 99):
            raise ValidationError({"D_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_ML_prob and (E_ML_prob < 0 or E_ML_prob > 99):
            raise ValidationError({"E_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_ML_prob and (F_ML_prob < 0 or F_ML_prob > 99):
            raise ValidationError({"F_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_ML_prob and (G_ML_prob < 0 or G_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_ML_prob and (H_ML_prob < 0 or H_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_ML_prob and (I_ML_prob < 0 or I_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_ML_prob and (J_ML_prob < 0 or J_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})


        if A_SP_prob and (A_SP_prob < 0 or A_SP_prob > 99):
            raise ValidationError({"A_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SP_prob and (B_SP_prob < 0 or B_SP_prob > 99):
            raise ValidationError({"B_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SP_prob and (C_SP_prob < 0 or C_SP_prob > 99):
            raise ValidationError({"C_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SP_prob and (D_SP_prob < 0 or D_SP_prob > 99):
            raise ValidationError({"D_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SP_prob and (E_SP_prob < 0 or E_SP_prob > 99):
            raise ValidationError({"E_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SP_prob and (F_SP_prob < 0 or F_SP_prob > 99):
            raise ValidationError({"F_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SP_prob and (G_SP_prob < 0 or G_SP_prob > 99):
            raise ValidationError({"G_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SP_prob and (H_SP_prob < 0 or H_SP_prob > 99):
            raise ValidationError({"H_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SP_prob and (I_SP_prob < 0 or I_SP_prob > 99):
            raise ValidationError({"I_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SP_prob and (J_SP_prob < 0 or J_SP_prob > 99):
            raise ValidationError({"J_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Total_prob and (A_Total_prob < 0 or A_Total_prob > 99):
            raise ValidationError({"A_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Total_prob and (B_Total_prob < 0 or B_Total_prob > 99):
            raise ValidationError({"B_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Total_prob and (C_Total_prob < 0 or C_Total_prob > 99):
            raise ValidationError({"C_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Total_prob and (D_Total_prob < 0 or D_Total_prob > 99):
            raise ValidationError({"D_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Total_prob and (E_Total_prob < 0 or E_Total_prob > 99):
            raise ValidationError({"E_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Total_prob and (F_Total_prob < 0 or F_Total_prob > 99):
            raise ValidationError({"F_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Total_prob and (G_Total_prob < 0 or G_Total_prob > 99):
            raise ValidationError({"G_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Total_prob and (H_Total_prob < 0 or H_Total_prob > 99):
            raise ValidationError({"H_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Total_prob and (I_Total_prob < 0 or I_Total_prob > 99):
            raise ValidationError({"I_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Total_prob and (J_Total_prob < 0 or J_Total_prob > 99):
            raise ValidationError({"J_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Ud_prob and (A_Ud_prob < 0 or A_Ud_prob > 99):
            raise ValidationError({"A_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Ud_prob and (B_Ud_prob < 0 or B_Ud_prob > 99):
            raise ValidationError({"B_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Ud_prob and (C_Ud_prob < 0 or C_Ud_prob > 99):
            raise ValidationError({"C_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Ud_prob and (D_Ud_prob < 0 or D_Ud_prob > 99):
            raise ValidationError({"D_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Ud_prob and (E_Ud_prob < 0 or E_Ud_prob > 99):
            raise ValidationError({"E_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Ud_prob and (F_Ud_prob < 0 or F_Ud_prob > 99):
            raise ValidationError({"F_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Ud_prob and (G_Ud_prob < 0 or G_Ud_prob > 99):
            raise ValidationError({"G_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Ud_prob and (H_Ud_prob < 0 or H_Ud_prob > 99):
            raise ValidationError({"H_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Ud_prob and (I_Ud_prob < 0 or I_Ud_prob > 99):
            raise ValidationError({"I_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Ud_prob and (J_Ud_prob < 0 or J_Ud_prob > 99):
            raise ValidationError({"J_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_SB_prob and (A_SB_prob < 0 or A_SB_prob > 99):
            raise ValidationError({"A_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SB_prob and (B_SB_prob < 0 or B_SB_prob > 99):
            raise ValidationError({"B_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SB_prob and (C_SB_prob < 0 or C_SB_prob > 99):
            raise ValidationError({"C_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SB_prob and (D_SB_prob < 0 or D_SB_prob > 99):
            raise ValidationError({"D_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SB_prob and (E_SB_prob < 0 or E_SB_prob > 99):
            raise ValidationError({"E_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SB_prob and (F_SB_prob < 0 or F_SB_prob > 99):
            raise ValidationError({"F_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SB_prob and (G_SB_prob < 0 or G_SB_prob > 99):
            raise ValidationError({"G_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SB_prob and (H_SB_prob < 0 or H_SB_prob > 99):
            raise ValidationError({"H_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SB_prob and (I_SB_prob < 0 or I_SB_prob > 99):
            raise ValidationError({"I_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SB_prob and (J_SB_prob < 0 or J_SB_prob > 99):
            raise ValidationError({"J_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
          
        if A_MA_prob and (A_MA_prob < 0 or A_MA_prob > 99):
            raise ValidationError({"A_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_MA_prob and (B_MA_prob < 0 or B_MA_prob > 99):
            raise ValidationError({"B_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if C_MA_prob and (C_MA_prob < 0 or C_MA_prob > 99):
            raise ValidationError({"C_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if D_MA_prob and (D_MA_prob < 0 or D_MA_prob > 99):
            raise ValidationError({"D_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if E_MA_prob and (E_MA_prob < 0 or E_MA_prob > 99):
            raise ValidationError({"E_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_MA_prob and (F_MA_prob < 0 or F_MA_prob > 99):
            raise ValidationError({"F_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_MA_prob and (G_MA_prob < 0 or G_MA_prob > 99):
            raise ValidationError({"G_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_MA_prob and (H_MA_prob < 0 or H_MA_prob > 99):
            raise ValidationError({"H_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_MA_prob and (I_MA_prob < 0 or I_MA_prob > 99):
            raise ValidationError({"I_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_MA_prob and (J_MA_prob < 0 or J_MA_prob > 99):
            raise ValidationError({"J_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        if A_BB_prob and (A_BB_prob < 0 or A_BB_prob > 99):
            raise ValidationError({"A_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_BB_prob and (B_BB_prob < 0 or B_BB_prob > 99):
            raise ValidationError({"B_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_BB_prob and (C_BB_prob < 0 or C_BB_prob > 99):
            raise ValidationError({"C_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_BB_prob and (D_BB_prob < 0 or D_BB_prob > 99):
            raise ValidationError({"D_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_BB_prob and (E_BB_prob < 0 or E_BB_prob > 99):
            raise ValidationError({"E_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_BB_prob and (F_BB_prob < 0 or F_BB_prob > 99):
            raise ValidationError({"F_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_BB_prob and (G_BB_prob < 0 or G_BB_prob > 99):
            raise ValidationError({"G_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_BB_prob and (H_BB_prob < 0 or H_BB_prob > 99):
            raise ValidationError({"H_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_BB_prob and (I_BB_prob < 0 or I_BB_prob > 99):
            raise ValidationError({"I_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_BB_prob and (J_BB_prob < 0 or J_BB_prob > 99):
            raise ValidationError({"J_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_equip = cleaned_data.get('J_ML_equip')

        A_SP_equip = cleaned_data.get('A_SP_equip')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
       
        A_SB_equip = cleaned_data.get('A_SB_equip')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        J_SB_equip = cleaned_data.get('J_SB_equip')
       
        A_MA = cleaned_data.get('A_MA')
        B_MA = cleaned_data.get('B_MA')
        C_MA = cleaned_data.get('C_MA')
        D_MA = cleaned_data.get('D_MA')
        E_MA = cleaned_data.get('E_MA')
        F_MA = cleaned_data.get('F_MA')
        G_MA = cleaned_data.get('G_MA')
        H_MA = cleaned_data.get('H_MA')
        I_MA = cleaned_data.get('I_MA')
        J_MA = cleaned_data.get('J_MA')

        A_BB = cleaned_data.get('A_BB')
        B_BB = cleaned_data.get('B_BB')
        C_BB = cleaned_data.get('C_BB')
        D_BB = cleaned_data.get('D_BB')
        E_BB = cleaned_data.get('E_BB')
        F_BB = cleaned_data.get('F_BB')
        G_BB = cleaned_data.get('G_BB')
        H_BB = cleaned_data.get('H_BB')
        I_BB = cleaned_data.get('I_BB')
        J_BB = cleaned_data.get('J_BB')
        
        
              
        # Validación para ganador
        if A_ML_equip and (A_ML_equip != equipo_local and A_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})
        if B_ML_equip and (B_ML_equip != equipo_local and B_ML_equip != equipo_visitante):
            raise ValidationError({"B_ML_equip": "Debes elegir un equipo válido."})
        if C_ML_equip and (C_ML_equip != equipo_local and C_ML_equip != equipo_visitante):
            raise ValidationError({"C_ML_equip": "Debes elegir un equipo válido."})
        if D_ML_equip and (D_ML_equip != equipo_local and D_ML_equip != equipo_visitante):
            raise ValidationError({"D_ML_equip": "Debes elegir un equipo válido."})
        if E_ML_equip and (E_ML_equip != equipo_local and E_ML_equip != equipo_visitante):
            raise ValidationError({"E_ML_equip": "Debes elegir un equipo válido."})
        if F_ML_equip and (F_ML_equip != equipo_local and F_ML_equip != equipo_visitante):
            raise ValidationError({"F_ML_equip": "Debes elegir un equipo válido."})
        if G_ML_equip and (G_ML_equip != equipo_local and G_ML_equip != equipo_visitante):
            raise ValidationError({"G_ML_equip": "Debes elegir un equipo válido."})
        if H_ML_equip and (H_ML_equip != equipo_local and H_ML_equip != equipo_visitante):
            raise ValidationError({"H_ML_equip": "Debes elegir un equipo válido."})
        if I_ML_equip and (I_ML_equip != equipo_local and I_ML_equip != equipo_visitante):
            raise ValidationError({"I_ML_equip": "Debes elegir un equipo válido."})
        if J_ML_equip and (J_ML_equip != equipo_local and J_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})

        if A_SP_equip and (A_SP_equip != equipo_local and A_SP_equip != equipo_visitante):
            raise ValidationError({"A_SP_equip": "Debes elegir un equipo válido."})
        if B_SP_equip and (B_SP_equip != equipo_local and B_SP_equip != equipo_visitante):
            raise ValidationError({"B_SP_equip": "Debes elegir un equipo válido."})
        if C_SP_equip and (C_SP_equip != equipo_local and C_SP_equip != equipo_visitante):
            raise ValidationError({"C_SP_equip": "Debes elegir un equipo válido."})
        if D_SP_equip and (D_SP_equip != equipo_local and D_SP_equip != equipo_visitante):
            raise ValidationError({"D_SP_equip": "Debes elegir un equipo válido."})
        if E_SP_equip and (E_SP_equip != equipo_local and E_SP_equip != equipo_visitante):
            raise ValidationError({"E_SP_equip": "Debes elegir un equipo válido."})
        if F_SP_equip and (F_SP_equip != equipo_local and F_SP_equip != equipo_visitante):
            raise ValidationError({"F_SP_equip": "Debes elegir un equipo válido."})
        if G_SP_equip and (G_SP_equip != equipo_local and G_SP_equip != equipo_visitante):
            raise ValidationError({"G_SP_equip": "Debes elegir un equipo válido."})
        if H_SP_equip and (H_SP_equip != equipo_local and H_SP_equip != equipo_visitante):
            raise ValidationError({"H_SP_equip": "Debes elegir un equipo válido."})
        if I_SP_equip and (I_SP_equip != equipo_local and I_SP_equip != equipo_visitante):
            raise ValidationError({"I_SP_equip": "Debes elegir un equipo válido."})
        if J_SP_equip and (J_SP_equip != equipo_local and J_SP_equip != equipo_visitante):
            raise ValidationError({"J_SP_equip": "Debes elegir un equipo válido."})
        
        if A_Ud_equip and (A_Ud_equip != equipo_local and A_Ud_equip != equipo_visitante):
            raise ValidationError({"A_Ud_equip": "Debes elegir un equipo válido."})
        if B_Ud_equip and (B_Ud_equip != equipo_local and B_Ud_equip != equipo_visitante):
            raise ValidationError({"B_Ud_equip": "Debes elegir un equipo válido."})
        if C_Ud_equip and (C_Ud_equip != equipo_local and C_Ud_equip != equipo_visitante):
            raise ValidationError({"C_Ud_equip": "Debes elegir un equipo válido."})
        if D_Ud_equip and (D_Ud_equip != equipo_local and D_Ud_equip != equipo_visitante):
            raise ValidationError({"D_Ud_equip": "Debes elegir un equipo válido."})
        if E_Ud_equip and (E_Ud_equip != equipo_local and E_Ud_equip != equipo_visitante):
            raise ValidationError({"E_Ud_equip": "Debes elegir un equipo válido."})
        if F_Ud_equip and (F_Ud_equip != equipo_local and F_Ud_equip != equipo_visitante):
            raise ValidationError({"F_Ud_equip": "Debes elegir un equipo válido."})
        if G_Ud_equip and (G_Ud_equip != equipo_local and G_Ud_equip != equipo_visitante):
            raise ValidationError({"G_Ud_equip": "Debes elegir un equipo válido."})
        if H_Ud_equip and (H_Ud_equip != equipo_local and H_Ud_equip != equipo_visitante):
            raise ValidationError({"H_Ud_equip": "Debes elegir un equipo válido."})
        if I_Ud_equip and (I_Ud_equip != equipo_local and I_Ud_equip != equipo_visitante):
            raise ValidationError({"I_Ud_equip": "Debes elegir un equipo válido."})
        if J_Ud_equip and (J_Ud_equip != equipo_local and J_Ud_equip != equipo_visitante):
            raise ValidationError({"J_Ud_equip": "Debes elegir un equipo válido."})
        
        if A_SB_equip and (A_SB_equip != equipo_local and A_SB_equip != equipo_visitante):
            raise ValidationError({"A_SB_equip": "Debes elegir un equipo válido."})
        if B_SB_equip and (B_SB_equip != equipo_local and B_SB_equip != equipo_visitante):
            raise ValidationError({"B_SB_equip": "Debes elegir un equipo válido."})
        if C_SB_equip and (C_SB_equip != equipo_local and C_SB_equip != equipo_visitante):
            raise ValidationError({"C_SB_equip": "Debes elegir un equipo válido."})
        if D_SB_equip and (D_SB_equip != equipo_local and D_SB_equip != equipo_visitante):
            raise ValidationError({"D_SB_equip": "Debes elegir un equipo válido."})
        if E_SB_equip and (E_SB_equip != equipo_local and E_SB_equip != equipo_visitante):
            raise ValidationError({"E_SB_equip": "Debes elegir un equipo válido."})
        if F_SB_equip and (F_SB_equip != equipo_local and F_SB_equip != equipo_visitante):
            raise ValidationError({"F_SB_equip": "Debes elegir un equipo válido."})
        if G_SB_equip and (G_SB_equip != equipo_local and G_SB_equip != equipo_visitante):
            raise ValidationError({"G_SB_equip": "Debes elegir un equipo válido."})
        if H_SB_equip and (H_SB_equip != equipo_local and H_SB_equip != equipo_visitante):
            raise ValidationError({"H_SB_equip": "Debes elegir un equipo válido."})
        if I_SB_equip and (I_SB_equip != equipo_local and I_SB_equip != equipo_visitante):
            raise ValidationError({"I_SB_equip": "Debes elegir un equipo válido."})
        if J_SB_equip and (J_SB_equip != equipo_local and J_SB_equip != equipo_visitante):
            raise ValidationError({"J_SB_equip": "Debes elegir un equipo válido."})
        
        if A_MA and (A_MA != equipo_local and A_MA != equipo_visitante):
            raise ValidationError({"A_MA": "Debes elegir un equipo válido."})
        if B_MA and (B_MA != equipo_local and B_MA != equipo_visitante):
            raise ValidationError({"B_MA": "Debes elegir un equipo válido."})
        if C_MA and (C_MA != equipo_local and C_MA != equipo_visitante):
            raise ValidationError({"C_MA": "Debes elegir un equipo válido."})
        if D_MA and (D_MA != equipo_local and D_MA != equipo_visitante):
            raise ValidationError({"D_MA": "Debes elegir un equipo válido."})
        if E_MA and (E_MA != equipo_local and E_MA != equipo_visitante):
            raise ValidationError({"E_MA": "Debes elegir un equipo válido."})
        if F_MA and (F_MA != equipo_local and F_MA != equipo_visitante):
            raise ValidationError({"F_MA": "Debes elegir un equipo válido."})
        if G_MA and (G_MA != equipo_local and G_MA != equipo_visitante):
            raise ValidationError({"G_MA": "Debes elegir un equipo válido."})
        if H_MA and (H_MA != equipo_local and H_MA != equipo_visitante):
            raise ValidationError({"H_MA": "Debes elegir un equipo válido."})
        if I_MA and (I_MA != equipo_local and I_MA != equipo_visitante):
            raise ValidationError({"I_MA": "Debes elegir un equipo válido."})
        if J_MA and (J_MA != equipo_local and J_MA != equipo_visitante):
            raise ValidationError({"J_MA": "Debes elegir un equipo válido."})
        
        if A_BB and (A_BB != equipo_local and A_BB != equipo_visitante):
            raise ValidationError({"A_BB": "Debes elegir un equipo válido."})
        if B_BB and (B_BB != equipo_local and B_BB != equipo_visitante):
            raise ValidationError({"B_BB": "Debes elegir un equipo válido."})
        if C_BB and (C_BB != equipo_local and C_BB != equipo_visitante):
            raise ValidationError({"C_BB": "Debes elegir un equipo válido."})
        if D_BB and (D_BB != equipo_local and D_BB != equipo_visitante):
            raise ValidationError({"D_BB": "Debes elegir un equipo válido."})
        if E_BB and (E_BB != equipo_local and E_BB != equipo_visitante):
            raise ValidationError({"E_BB": "Debes elegir un equipo válido."})
        if F_BB and (F_BB != equipo_local and F_BB != equipo_visitante):
            raise ValidationError({"F_BB": "Debes elegir un equipo válido."})
        if G_BB and (G_BB != equipo_local and G_BB != equipo_visitante):
            raise ValidationError({"G_BB": "Debes elegir un equipo válido."})
        if H_BB and (H_BB != equipo_local and H_BB != equipo_visitante):
            raise ValidationError({"H_BB": "Debes elegir un equipo válido."})
        if I_BB and (I_BB != equipo_local and I_BB != equipo_visitante):
            raise ValidationError({"I_BB": "Debes elegir un equipo válido."})
        if J_BB and (J_BB != equipo_local and J_BB != equipo_visitante):
            raise ValidationError({"J_BB": "Debes elegir un equipo válido."})
         

        
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_punto = cleaned_data.get('G_total_punto')     
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_punto = cleaned_data.get('J_total_punto')
        
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        
        if A_Total_punto and (A_Total_punto < 0 ):
            raise ValidationError({"A_Total_punto": "Introdusca un valor válido."})
        if B_Total_punto and (B_Total_punto < 0 ):
            raise ValidationError({"B_Total_punto": "Introdusca un valor válido."})
        if C_Total_punto and (C_Total_punto < 0 ):
            raise ValidationError({"C_Total_punto": "Introdusca un valor válido."})
        if D_Total_punto and (D_Total_punto < 0 ):
            raise ValidationError({"D_Total_punto": "Introdusca un valor válido."})
        if E_Total_punto and (E_Total_punto < 0 ):
            raise ValidationError({"E_Total_punto": "Introdusca un valor válido."})
        if F_Total_punto and (F_Total_punto < 0 ):
            raise ValidationError({"F_Total_punto": "Introdusca un valor válido."})
        if G_Total_punto and (G_Total_punto < 0 ):
            raise ValidationError({"G_Total_punto": "Introdusca un valor válido."})
        if H_Total_punto and (H_Total_punto < 0 ):
            raise ValidationError({"H_Total_punto": "Introdusca un valor válido."})
        if I_Total_punto and (I_Total_punto < 0 ):
            raise ValidationError({"I_Total_punto": "Introdusca un valor válido."})
        if J_Total_punto and (J_Total_punto < 0 ):
            raise ValidationError({"J_Total_punto": "Introdusca un valor válido."})
        
        if A_SP_dif and (A_SP_dif < 0 ):
            raise ValidationError({"A_SP_dif": "Introdusca un valor válido."})
        if B_SP_dif and (B_SP_dif < 0 ):
            raise ValidationError({"B_SP_dif": "Introdusca un valor válido."})
        if C_SP_dif and (C_SP_dif < 0 ):
            raise ValidationError({"C_SP_dif": "Introdusca un valor válido."})
        if D_SP_dif and (D_SP_dif < 0 ):
            raise ValidationError({"D_SP_dif": "Introdusca un valor válido."})
        if E_SP_dif and (E_SP_dif < 0 ):
            raise ValidationError({"E_SP_dif": "Introdusca un valor válido."})
        if F_SP_dif and (F_SP_dif < 0 ):
            raise ValidationError({"F_SP_dif": "Introdusca un valor válido."})
        if G_SP_dif and (G_SP_dif < 0 ):
            raise ValidationError({"G_SP_dif": "Introdusca un valor válido."})
        if H_SP_dif and (H_SP_dif < 0 ):
            raise ValidationError({"H_SP_dif": "Introdusca un valor válido."})
        if I_SP_dif and (I_SP_dif < 0 ):
            raise ValidationError({"I_SP_dif": "Introdusca un valor válido."})
        if J_SP_dif and (J_SP_dif < 0 ):
            raise ValidationError({"J_SP_dif": "Introdusca un valor válido."})
        
        return cleaned_data
    


class NBA_Profecional_form(forms.ModelForm):
    

    
    class Meta:
        model = NBA_Profecional
        fields = ['equipo_local', 'equipo_visitante','fecha','A_ML_equip','A_ML_prob','A_SP_equip','A_SP_prob','A_SP_dif','A_Total_OU','A_Total_prob','A_Ud_equip','A_Ud_prob','A_SB_equip','A_SB_prob','A_MA','A_BB','A_total_punto',
                  'B_ML_equip','B_ML_prob','B_SP_equip','B_SP_prob','B_SP_dif','B_Total_OU','B_Total_prob','B_Ud_equip','B_Ud_prob','B_SB_equip','B_SB_prob','B_MA','B_BB','B_total_punto','A_MA_prob','B_MA_prob','C_MA_prob','D_MA_prob',
                  'C_ML_equip','C_ML_prob','C_SP_equip','C_SP_prob','C_SP_dif','C_Total_OU','C_Total_prob','C_Ud_equip','C_Ud_prob','C_SB_equip','C_SB_prob','C_MA','C_BB','C_total_punto','E_MA_prob','F_MA_prob','G_MA_prob','H_MA_prob',
                  'D_ML_equip','D_ML_prob','D_SP_equip','D_SP_prob','D_SP_dif','D_Total_OU','D_Total_prob','D_Ud_equip','D_Ud_prob','D_SB_equip','D_SB_prob','D_MA','D_BB','D_total_punto','I_MA_prob','J_MA_prob','A_BB_prob','B_BB_prob',
                  'E_ML_equip','E_ML_prob','E_SP_equip','E_SP_prob','E_SP_dif','E_Total_OU','E_Total_prob','E_Ud_equip','E_Ud_prob','E_SB_equip','E_SB_prob','E_MA','E_BB','E_total_punto','C_BB_prob','D_BB_prob','E_BB_prob','F_BB_prob',
                  'F_ML_equip','F_ML_prob','F_SP_equip','F_SP_prob','F_SP_dif','F_Total_OU','F_Total_prob','F_Ud_equip','F_Ud_prob','F_SB_equip','F_SB_prob','F_MA','F_BB','F_total_punto','G_BB_prob','H_BB_prob','I_BB_prob','J_BB_prob',
                  'G_ML_equip','G_ML_prob','G_SP_equip','G_SP_prob','G_SP_dif','G_Total_OU','G_Total_prob','G_Ud_equip','G_Ud_prob','G_SB_equip','G_SB_prob','G_MA','G_BB','G_total_punto',
                  'H_ML_equip','H_ML_prob','H_SP_equip','H_SP_prob','H_SP_dif','H_Total_OU','H_Total_prob','H_Ud_equip','H_Ud_prob','H_SB_equip','H_SB_prob','H_MA','H_BB','H_total_punto',
                  'I_ML_equip','I_ML_prob','I_SP_equip','I_SP_prob','I_SP_dif','I_Total_OU','I_Total_prob','I_Ud_equip','I_Ud_prob','I_SB_equip','I_SB_prob','I_MA','I_BB','I_total_punto',
                  'J_ML_equip','J_ML_prob','J_SP_equip','J_SP_prob','J_SP_dif','J_Total_OU','J_Total_prob','J_Ud_equip','J_Ud_prob','J_SB_equip','J_SB_prob','J_MA','J_BB','J_total_punto',
                  ]
        
        widgets = {
            
            'equipo_local': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'equipo_visitante': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control select-field', 'placeholder': '' }),
            'A_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visitante = cleaned_data.get('equipo_visitante')

       
        existing_partidos = NBA_Profecional.objects.filter(
            Q(fecha=fecha) &
            ~Q(id=self.instance.id) &  
            (
                Q(equipo_local=equipo_local) | 
                Q(equipo_visitante=equipo_visitante) 
            )
        )

        if existing_partidos.exists():
            raise ValidationError("Ya existe un partido con el mismo equipo programado para esta fecha.")

       
        if equipo_local.nombre == equipo_visitante.nombre:
           raise ValidationError("El equipo local y el equipo visitante no pueden ser el mismo.")     

    
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        J_ML_equip = cleaned_data.get('J_ML_equip')
        
        A_SP_equip = cleaned_data.get('A_SP_equip')
        A_SP_prob = cleaned_data.get('A_SP_prob')
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        J_SP_prob = cleaned_data.get('J_SP_prob')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        A_Total_OU = cleaned_data.get('A_Total_OU')
        A_Total_prob = cleaned_data.get('A_Total_prob')
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_OU = cleaned_data.get('B_Total_OU')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_OU = cleaned_data.get('C_Total_OU')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_OU = cleaned_data.get('D_Total_OU')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_OU = cleaned_data.get('E_Total_OU')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_OU = cleaned_data.get('F_Total_OU')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_OU = cleaned_data.get('G_Total_OU')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        G_Total_punto = cleaned_data.get('G_total_punto')
        H_Total_OU = cleaned_data.get('H_Total_OU')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_OU = cleaned_data.get('I_Total_OU')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_OU = cleaned_data.get('J_Total_OU')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        J_Total_punto = cleaned_data.get('J_total_punto')
       
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')
        
        A_SB_equip = cleaned_data.get('A_SB_equip')
        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_equip = cleaned_data.get('J_SB_equip')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
        A_MA= cleaned_data.get('A_MA')
        B_MA= cleaned_data.get('B_MA')
        C_MA= cleaned_data.get('C_MA')
        D_MA= cleaned_data.get('D_MA')
        E_MA= cleaned_data.get('E_MA')
        F_MA= cleaned_data.get('F_MA')
        G_MA= cleaned_data.get('G_MA')
        H_MA= cleaned_data.get('H_MA')
        I_MA= cleaned_data.get('I_MA')
        J_MA= cleaned_data.get('J_MA')
        
        A_MA_prob= cleaned_data.get('A_MA_prob')
        B_MA_prob= cleaned_data.get('B_MA_prob')
        C_MA_prob= cleaned_data.get('C_MA_prob')
        D_MA_prob= cleaned_data.get('D_MA_prob')
        E_MA_prob= cleaned_data.get('E_MA_prob')
        F_MA_prob= cleaned_data.get('F_MA_prob')
        G_MA_prob= cleaned_data.get('G_MA_prob')
        H_MA_prob= cleaned_data.get('H_MA_prob')
        I_MA_prob= cleaned_data.get('I_MA_prob')
        J_MA_prob= cleaned_data.get('J_MA_prob')
        
        
        A_BB= cleaned_data.get('A_BB')
        B_BB= cleaned_data.get('B_BB')
        C_BB= cleaned_data.get('C_BB')
        D_BB= cleaned_data.get('D_BB')
        E_BB= cleaned_data.get('E_BB')
        F_BB= cleaned_data.get('F_BB')
        G_BB= cleaned_data.get('G_BB')
        H_BB= cleaned_data.get('H_BB')
        I_BB= cleaned_data.get('I_BB')
        J_BB= cleaned_data.get('J_BB')
         
        A_BB_prob= cleaned_data.get('A_BB_prob')
        B_BB_prob= cleaned_data.get('B_BB_prob')
        C_BB_prob= cleaned_data.get('C_BB_prob')
        D_BB_prob= cleaned_data.get('D_BB_prob')
        E_BB_prob= cleaned_data.get('E_BB_prob')
        F_BB_prob= cleaned_data.get('F_BB_prob')
        G_BB_prob= cleaned_data.get('G_BB_prob')
        H_BB_prob= cleaned_data.get('H_BB_prob')
        I_BB_prob= cleaned_data.get('I_BB_prob')
        J_BB_prob= cleaned_data.get('J_BB_prob')

        
        # Realiza la validación personalizada
        if A_ML_prob or A_ML_equip:
            if not (A_ML_equip and A_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if B_ML_prob or B_ML_equip:
            if not (B_ML_equip and B_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if C_ML_prob or C_ML_equip:
            if not (C_ML_equip and C_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if D_ML_prob or D_ML_equip:
            if not (D_ML_equip and D_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if E_ML_prob or E_ML_equip:
            if not (E_ML_equip and E_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if F_ML_prob or F_ML_equip:
            if not (F_ML_equip and F_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if G_ML_prob or G_ML_equip:
            if not (G_ML_equip and G_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if H_ML_prob or H_ML_equip:
            if not (H_ML_equip and H_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if I_ML_prob or I_ML_equip:
            if not (I_ML_equip and I_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if J_ML_prob or J_ML_equip:
            if not (J_ML_equip and J_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        
        if A_SP_equip or A_SP_prob or A_SP_dif :
            if not (A_SP_equip and A_SP_prob and A_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if B_SP_equip or B_SP_prob or B_SP_dif :
            if not (B_SP_equip and B_SP_prob and B_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if C_SP_equip or C_SP_prob or C_SP_dif :
            if not (C_SP_equip and C_SP_prob and C_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if D_SP_equip or D_SP_prob or D_SP_dif :
            if not (D_SP_equip and D_SP_prob and D_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if E_SP_equip or E_SP_prob or E_SP_dif :
            if not (E_SP_equip and E_SP_prob and E_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if F_SP_equip or F_SP_prob or F_SP_dif :
            if not (F_SP_equip and F_SP_prob and F_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if G_SP_equip or G_SP_prob or G_SP_dif :
            if not (G_SP_equip and G_SP_prob and G_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if H_SP_equip or H_SP_prob or H_SP_dif :
            if not (H_SP_equip and H_SP_prob and H_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if I_SP_equip or I_SP_prob or I_SP_dif :
            if not (I_SP_equip and I_SP_prob and I_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if J_SP_equip or J_SP_prob or J_SP_dif :
            if not (J_SP_equip and J_SP_prob and J_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
  
       
        if A_Total_OU or A_Total_prob or A_Total_punto :
            if not (A_Total_OU and A_Total_prob and A_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if B_Total_OU or B_Total_prob or B_Total_punto :
            if not (B_Total_OU and B_Total_prob and B_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if C_Total_OU or C_Total_prob or C_Total_punto :
            if not (C_Total_OU and C_Total_prob and C_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if D_Total_OU or D_Total_prob or D_Total_punto :
            if not (D_Total_OU and D_Total_prob and D_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if E_Total_OU or E_Total_prob or E_Total_punto :
            if not (E_Total_OU and E_Total_prob and E_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if F_Total_OU or F_Total_prob or F_Total_punto :
            if not (F_Total_OU and F_Total_prob and F_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if G_Total_OU or G_Total_prob or G_Total_punto :
            if not (G_Total_OU and G_Total_prob and G_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if H_Total_OU or H_Total_prob or H_Total_punto :
            if not (H_Total_OU and H_Total_prob and H_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if I_Total_OU or I_Total_prob or I_Total_punto :
            if not (I_Total_OU and I_Total_prob and I_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if J_Total_OU or J_Total_prob or J_Total_punto :
            if not (J_Total_OU and J_Total_prob and J_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
      
        if A_Ud_equip or A_Ud_prob:
            if not (A_Ud_equip and A_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if B_Ud_equip or B_Ud_prob:
            if not (B_Ud_equip and B_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if C_Ud_equip or C_Ud_prob:
            if not (C_Ud_equip and C_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if D_Ud_equip or D_Ud_prob:
            if not (D_Ud_equip and D_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if E_Ud_equip or E_Ud_prob:
            if not (E_Ud_equip and E_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if F_Ud_equip or F_Ud_prob:
            if not (F_Ud_equip and F_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if G_Ud_equip or G_Ud_prob:
            if not (G_Ud_equip and G_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if H_Ud_equip or H_Ud_prob:
            if not (H_Ud_equip and H_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if I_Ud_equip or I_Ud_prob:
            if not (I_Ud_equip and I_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if J_Ud_equip or J_Ud_prob:
            if not (J_Ud_equip and J_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
       
        if A_SB_equip or A_SB_prob:
            if not (A_SB_equip and A_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if B_SB_equip or B_SB_prob:
            if not (B_SB_equip and B_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if C_SB_equip or C_SB_prob:
            if not (C_SB_equip and C_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if D_SB_equip or D_SB_prob:
            if not (D_SB_equip and D_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if E_SB_equip or E_SB_prob:
            if not (E_SB_equip and E_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if F_SB_equip or F_SB_prob:
            if not (F_SB_equip and F_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if G_SB_equip or G_SB_prob:
            if not (G_SB_equip and G_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if H_SB_equip or H_SB_prob:
            if not (H_SB_equip and H_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if I_SB_equip or I_SB_prob:
            if not (I_SB_equip and I_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if J_SB_equip or J_SB_prob:
            if not (J_SB_equip and J_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
       
        if A_MA or A_MA_prob:
            if not (A_MA and A_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if B_MA or B_MA_prob:
            if not (B_MA and B_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if C_MA or C_MA_prob:
            if not (C_MA and C_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if D_MA or D_MA_prob:
            if not (D_MA and D_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if E_MA or E_MA_prob:
            if not (E_MA and E_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if F_MA or F_MA_prob:
            if not (F_MA and F_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if G_MA or G_MA_prob:
            if not (G_MA and G_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if H_MA or H_MA_prob:
            if not (H_MA and H_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if I_MA or I_MA_prob:
            if not (I_MA and I_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if J_MA or J_MA_prob:
            if not (J_MA and J_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ") 
   
        
        if A_BB or A_BB_prob:
            if not (A_BB and A_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if B_BB or B_BB_prob:
            if not (B_BB and B_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if C_BB or C_BB_prob:
            if not (C_BB and C_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if D_BB or D_BB_prob:
            if not (D_BB and D_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if E_BB or E_BB_prob:
            if not (E_BB and E_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if F_BB or F_BB_prob:
            if not (F_BB and F_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if G_BB or G_BB_prob:
            if not (G_BB and G_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if H_BB or H_BB_prob:
            if not (H_BB and H_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if I_BB or I_BB_prob:
            if not (I_BB and I_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if J_BB or J_BB_prob:
            if not (J_BB and J_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        
       
       
       
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        
        A_SP_prob = cleaned_data.get('A_SP_prob')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        J_SP_prob = cleaned_data.get('J_SP_prob')

        A_Total_prob = cleaned_data.get('A_Total_prob')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')

        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
       
        if A_ML_prob and (A_ML_prob < 1 or A_ML_prob > 99):
            raise ValidationError({"A_ML_prob": "El valor de probabilidad debe estar entre 1 y 99."})
        if B_ML_prob and (B_ML_prob < 0 or B_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_ML_prob and (C_ML_prob < 0 or C_ML_prob > 99):
            raise ValidationError({"C_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_ML_prob and (D_ML_prob < 0 or D_ML_prob > 99):
            raise ValidationError({"D_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_ML_prob and (E_ML_prob < 0 or E_ML_prob > 99):
            raise ValidationError({"E_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_ML_prob and (F_ML_prob < 0 or F_ML_prob > 99):
            raise ValidationError({"F_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_ML_prob and (G_ML_prob < 0 or G_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_ML_prob and (H_ML_prob < 0 or H_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_ML_prob and (I_ML_prob < 0 or I_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_ML_prob and (J_ML_prob < 0 or J_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})


        if A_SP_prob and (A_SP_prob < 0 or A_SP_prob > 99):
            raise ValidationError({"A_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SP_prob and (B_SP_prob < 0 or B_SP_prob > 99):
            raise ValidationError({"B_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SP_prob and (C_SP_prob < 0 or C_SP_prob > 99):
            raise ValidationError({"C_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SP_prob and (D_SP_prob < 0 or D_SP_prob > 99):
            raise ValidationError({"D_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SP_prob and (E_SP_prob < 0 or E_SP_prob > 99):
            raise ValidationError({"E_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SP_prob and (F_SP_prob < 0 or F_SP_prob > 99):
            raise ValidationError({"F_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SP_prob and (G_SP_prob < 0 or G_SP_prob > 99):
            raise ValidationError({"G_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SP_prob and (H_SP_prob < 0 or H_SP_prob > 99):
            raise ValidationError({"H_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SP_prob and (I_SP_prob < 0 or I_SP_prob > 99):
            raise ValidationError({"I_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SP_prob and (J_SP_prob < 0 or J_SP_prob > 99):
            raise ValidationError({"J_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Total_prob and (A_Total_prob < 0 or A_Total_prob > 99):
            raise ValidationError({"A_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Total_prob and (B_Total_prob < 0 or B_Total_prob > 99):
            raise ValidationError({"B_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Total_prob and (C_Total_prob < 0 or C_Total_prob > 99):
            raise ValidationError({"C_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Total_prob and (D_Total_prob < 0 or D_Total_prob > 99):
            raise ValidationError({"D_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Total_prob and (E_Total_prob < 0 or E_Total_prob > 99):
            raise ValidationError({"E_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Total_prob and (F_Total_prob < 0 or F_Total_prob > 99):
            raise ValidationError({"F_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Total_prob and (G_Total_prob < 0 or G_Total_prob > 99):
            raise ValidationError({"G_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Total_prob and (H_Total_prob < 0 or H_Total_prob > 99):
            raise ValidationError({"H_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Total_prob and (I_Total_prob < 0 or I_Total_prob > 99):
            raise ValidationError({"I_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Total_prob and (J_Total_prob < 0 or J_Total_prob > 99):
            raise ValidationError({"J_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Ud_prob and (A_Ud_prob < 0 or A_Ud_prob > 99):
            raise ValidationError({"A_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Ud_prob and (B_Ud_prob < 0 or B_Ud_prob > 99):
            raise ValidationError({"B_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Ud_prob and (C_Ud_prob < 0 or C_Ud_prob > 99):
            raise ValidationError({"C_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Ud_prob and (D_Ud_prob < 0 or D_Ud_prob > 99):
            raise ValidationError({"D_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Ud_prob and (E_Ud_prob < 0 or E_Ud_prob > 99):
            raise ValidationError({"E_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Ud_prob and (F_Ud_prob < 0 or F_Ud_prob > 99):
            raise ValidationError({"F_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Ud_prob and (G_Ud_prob < 0 or G_Ud_prob > 99):
            raise ValidationError({"G_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Ud_prob and (H_Ud_prob < 0 or H_Ud_prob > 99):
            raise ValidationError({"H_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Ud_prob and (I_Ud_prob < 0 or I_Ud_prob > 99):
            raise ValidationError({"I_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Ud_prob and (J_Ud_prob < 0 or J_Ud_prob > 99):
            raise ValidationError({"J_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_SB_prob and (A_SB_prob < 0 or A_SB_prob > 99):
            raise ValidationError({"A_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SB_prob and (B_SB_prob < 0 or B_SB_prob > 99):
            raise ValidationError({"B_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SB_prob and (C_SB_prob < 0 or C_SB_prob > 99):
            raise ValidationError({"C_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SB_prob and (D_SB_prob < 0 or D_SB_prob > 99):
            raise ValidationError({"D_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SB_prob and (E_SB_prob < 0 or E_SB_prob > 99):
            raise ValidationError({"E_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SB_prob and (F_SB_prob < 0 or F_SB_prob > 99):
            raise ValidationError({"F_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SB_prob and (G_SB_prob < 0 or G_SB_prob > 99):
            raise ValidationError({"G_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SB_prob and (H_SB_prob < 0 or H_SB_prob > 99):
            raise ValidationError({"H_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SB_prob and (I_SB_prob < 0 or I_SB_prob > 99):
            raise ValidationError({"I_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SB_prob and (J_SB_prob < 0 or J_SB_prob > 99):
            raise ValidationError({"J_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
          
        if A_MA_prob and (A_MA_prob < 0 or A_MA_prob > 99):
            raise ValidationError({"A_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_MA_prob and (B_MA_prob < 0 or B_MA_prob > 99):
            raise ValidationError({"B_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if C_MA_prob and (C_MA_prob < 0 or C_MA_prob > 99):
            raise ValidationError({"C_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if D_MA_prob and (D_MA_prob < 0 or D_MA_prob > 99):
            raise ValidationError({"D_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if E_MA_prob and (E_MA_prob < 0 or E_MA_prob > 99):
            raise ValidationError({"E_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_MA_prob and (F_MA_prob < 0 or F_MA_prob > 99):
            raise ValidationError({"F_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_MA_prob and (G_MA_prob < 0 or G_MA_prob > 99):
            raise ValidationError({"G_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_MA_prob and (H_MA_prob < 0 or H_MA_prob > 99):
            raise ValidationError({"H_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_MA_prob and (I_MA_prob < 0 or I_MA_prob > 99):
            raise ValidationError({"I_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_MA_prob and (J_MA_prob < 0 or J_MA_prob > 99):
            raise ValidationError({"J_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        if A_BB_prob and (A_BB_prob < 0 or A_BB_prob > 99):
            raise ValidationError({"A_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_BB_prob and (B_BB_prob < 0 or B_BB_prob > 99):
            raise ValidationError({"B_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_BB_prob and (C_BB_prob < 0 or C_BB_prob > 99):
            raise ValidationError({"C_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_BB_prob and (D_BB_prob < 0 or D_BB_prob > 99):
            raise ValidationError({"D_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_BB_prob and (E_BB_prob < 0 or E_BB_prob > 99):
            raise ValidationError({"E_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_BB_prob and (F_BB_prob < 0 or F_BB_prob > 99):
            raise ValidationError({"F_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_BB_prob and (G_BB_prob < 0 or G_BB_prob > 99):
            raise ValidationError({"G_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_BB_prob and (H_BB_prob < 0 or H_BB_prob > 99):
            raise ValidationError({"H_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_BB_prob and (I_BB_prob < 0 or I_BB_prob > 99):
            raise ValidationError({"I_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_BB_prob and (J_BB_prob < 0 or J_BB_prob > 99):
            raise ValidationError({"J_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_equip = cleaned_data.get('J_ML_equip')

        A_SP_equip = cleaned_data.get('A_SP_equip')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
       
        A_SB_equip = cleaned_data.get('A_SB_equip')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        J_SB_equip = cleaned_data.get('J_SB_equip')
       
        A_MA = cleaned_data.get('A_MA')
        B_MA = cleaned_data.get('B_MA')
        C_MA = cleaned_data.get('C_MA')
        D_MA = cleaned_data.get('D_MA')
        E_MA = cleaned_data.get('E_MA')
        F_MA = cleaned_data.get('F_MA')
        G_MA = cleaned_data.get('G_MA')
        H_MA = cleaned_data.get('H_MA')
        I_MA = cleaned_data.get('I_MA')
        J_MA = cleaned_data.get('J_MA')

        A_BB = cleaned_data.get('A_BB')
        B_BB = cleaned_data.get('B_BB')
        C_BB = cleaned_data.get('C_BB')
        D_BB = cleaned_data.get('D_BB')
        E_BB = cleaned_data.get('E_BB')
        F_BB = cleaned_data.get('F_BB')
        G_BB = cleaned_data.get('G_BB')
        H_BB = cleaned_data.get('H_BB')
        I_BB = cleaned_data.get('I_BB')
        J_BB = cleaned_data.get('J_BB')
        
        
              
        # Validación para ganador
        if A_ML_equip and (A_ML_equip != equipo_local and A_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})
        if B_ML_equip and (B_ML_equip != equipo_local and B_ML_equip != equipo_visitante):
            raise ValidationError({"B_ML_equip": "Debes elegir un equipo válido."})
        if C_ML_equip and (C_ML_equip != equipo_local and C_ML_equip != equipo_visitante):
            raise ValidationError({"C_ML_equip": "Debes elegir un equipo válido."})
        if D_ML_equip and (D_ML_equip != equipo_local and D_ML_equip != equipo_visitante):
            raise ValidationError({"D_ML_equip": "Debes elegir un equipo válido."})
        if E_ML_equip and (E_ML_equip != equipo_local and E_ML_equip != equipo_visitante):
            raise ValidationError({"E_ML_equip": "Debes elegir un equipo válido."})
        if F_ML_equip and (F_ML_equip != equipo_local and F_ML_equip != equipo_visitante):
            raise ValidationError({"F_ML_equip": "Debes elegir un equipo válido."})
        if G_ML_equip and (G_ML_equip != equipo_local and G_ML_equip != equipo_visitante):
            raise ValidationError({"G_ML_equip": "Debes elegir un equipo válido."})
        if H_ML_equip and (H_ML_equip != equipo_local and H_ML_equip != equipo_visitante):
            raise ValidationError({"H_ML_equip": "Debes elegir un equipo válido."})
        if I_ML_equip and (I_ML_equip != equipo_local and I_ML_equip != equipo_visitante):
            raise ValidationError({"I_ML_equip": "Debes elegir un equipo válido."})
        if J_ML_equip and (J_ML_equip != equipo_local and J_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})

        if A_SP_equip and (A_SP_equip != equipo_local and A_SP_equip != equipo_visitante):
            raise ValidationError({"A_SP_equip": "Debes elegir un equipo válido."})
        if B_SP_equip and (B_SP_equip != equipo_local and B_SP_equip != equipo_visitante):
            raise ValidationError({"B_SP_equip": "Debes elegir un equipo válido."})
        if C_SP_equip and (C_SP_equip != equipo_local and C_SP_equip != equipo_visitante):
            raise ValidationError({"C_SP_equip": "Debes elegir un equipo válido."})
        if D_SP_equip and (D_SP_equip != equipo_local and D_SP_equip != equipo_visitante):
            raise ValidationError({"D_SP_equip": "Debes elegir un equipo válido."})
        if E_SP_equip and (E_SP_equip != equipo_local and E_SP_equip != equipo_visitante):
            raise ValidationError({"E_SP_equip": "Debes elegir un equipo válido."})
        if F_SP_equip and (F_SP_equip != equipo_local and F_SP_equip != equipo_visitante):
            raise ValidationError({"F_SP_equip": "Debes elegir un equipo válido."})
        if G_SP_equip and (G_SP_equip != equipo_local and G_SP_equip != equipo_visitante):
            raise ValidationError({"G_SP_equip": "Debes elegir un equipo válido."})
        if H_SP_equip and (H_SP_equip != equipo_local and H_SP_equip != equipo_visitante):
            raise ValidationError({"H_SP_equip": "Debes elegir un equipo válido."})
        if I_SP_equip and (I_SP_equip != equipo_local and I_SP_equip != equipo_visitante):
            raise ValidationError({"I_SP_equip": "Debes elegir un equipo válido."})
        if J_SP_equip and (J_SP_equip != equipo_local and J_SP_equip != equipo_visitante):
            raise ValidationError({"J_SP_equip": "Debes elegir un equipo válido."})
        
        if A_Ud_equip and (A_Ud_equip != equipo_local and A_Ud_equip != equipo_visitante):
            raise ValidationError({"A_Ud_equip": "Debes elegir un equipo válido."})
        if B_Ud_equip and (B_Ud_equip != equipo_local and B_Ud_equip != equipo_visitante):
            raise ValidationError({"B_Ud_equip": "Debes elegir un equipo válido."})
        if C_Ud_equip and (C_Ud_equip != equipo_local and C_Ud_equip != equipo_visitante):
            raise ValidationError({"C_Ud_equip": "Debes elegir un equipo válido."})
        if D_Ud_equip and (D_Ud_equip != equipo_local and D_Ud_equip != equipo_visitante):
            raise ValidationError({"D_Ud_equip": "Debes elegir un equipo válido."})
        if E_Ud_equip and (E_Ud_equip != equipo_local and E_Ud_equip != equipo_visitante):
            raise ValidationError({"E_Ud_equip": "Debes elegir un equipo válido."})
        if F_Ud_equip and (F_Ud_equip != equipo_local and F_Ud_equip != equipo_visitante):
            raise ValidationError({"F_Ud_equip": "Debes elegir un equipo válido."})
        if G_Ud_equip and (G_Ud_equip != equipo_local and G_Ud_equip != equipo_visitante):
            raise ValidationError({"G_Ud_equip": "Debes elegir un equipo válido."})
        if H_Ud_equip and (H_Ud_equip != equipo_local and H_Ud_equip != equipo_visitante):
            raise ValidationError({"H_Ud_equip": "Debes elegir un equipo válido."})
        if I_Ud_equip and (I_Ud_equip != equipo_local and I_Ud_equip != equipo_visitante):
            raise ValidationError({"I_Ud_equip": "Debes elegir un equipo válido."})
        if J_Ud_equip and (J_Ud_equip != equipo_local and J_Ud_equip != equipo_visitante):
            raise ValidationError({"J_Ud_equip": "Debes elegir un equipo válido."})
        
        if A_SB_equip and (A_SB_equip != equipo_local and A_SB_equip != equipo_visitante):
            raise ValidationError({"A_SB_equip": "Debes elegir un equipo válido."})
        if B_SB_equip and (B_SB_equip != equipo_local and B_SB_equip != equipo_visitante):
            raise ValidationError({"B_SB_equip": "Debes elegir un equipo válido."})
        if C_SB_equip and (C_SB_equip != equipo_local and C_SB_equip != equipo_visitante):
            raise ValidationError({"C_SB_equip": "Debes elegir un equipo válido."})
        if D_SB_equip and (D_SB_equip != equipo_local and D_SB_equip != equipo_visitante):
            raise ValidationError({"D_SB_equip": "Debes elegir un equipo válido."})
        if E_SB_equip and (E_SB_equip != equipo_local and E_SB_equip != equipo_visitante):
            raise ValidationError({"E_SB_equip": "Debes elegir un equipo válido."})
        if F_SB_equip and (F_SB_equip != equipo_local and F_SB_equip != equipo_visitante):
            raise ValidationError({"F_SB_equip": "Debes elegir un equipo válido."})
        if G_SB_equip and (G_SB_equip != equipo_local and G_SB_equip != equipo_visitante):
            raise ValidationError({"G_SB_equip": "Debes elegir un equipo válido."})
        if H_SB_equip and (H_SB_equip != equipo_local and H_SB_equip != equipo_visitante):
            raise ValidationError({"H_SB_equip": "Debes elegir un equipo válido."})
        if I_SB_equip and (I_SB_equip != equipo_local and I_SB_equip != equipo_visitante):
            raise ValidationError({"I_SB_equip": "Debes elegir un equipo válido."})
        if J_SB_equip and (J_SB_equip != equipo_local and J_SB_equip != equipo_visitante):
            raise ValidationError({"J_SB_equip": "Debes elegir un equipo válido."})
        
        if A_MA and (A_MA != equipo_local and A_MA != equipo_visitante):
            raise ValidationError({"A_MA": "Debes elegir un equipo válido."})
        if B_MA and (B_MA != equipo_local and B_MA != equipo_visitante):
            raise ValidationError({"B_MA": "Debes elegir un equipo válido."})
        if C_MA and (C_MA != equipo_local and C_MA != equipo_visitante):
            raise ValidationError({"C_MA": "Debes elegir un equipo válido."})
        if D_MA and (D_MA != equipo_local and D_MA != equipo_visitante):
            raise ValidationError({"D_MA": "Debes elegir un equipo válido."})
        if E_MA and (E_MA != equipo_local and E_MA != equipo_visitante):
            raise ValidationError({"E_MA": "Debes elegir un equipo válido."})
        if F_MA and (F_MA != equipo_local and F_MA != equipo_visitante):
            raise ValidationError({"F_MA": "Debes elegir un equipo válido."})
        if G_MA and (G_MA != equipo_local and G_MA != equipo_visitante):
            raise ValidationError({"G_MA": "Debes elegir un equipo válido."})
        if H_MA and (H_MA != equipo_local and H_MA != equipo_visitante):
            raise ValidationError({"H_MA": "Debes elegir un equipo válido."})
        if I_MA and (I_MA != equipo_local and I_MA != equipo_visitante):
            raise ValidationError({"I_MA": "Debes elegir un equipo válido."})
        if J_MA and (J_MA != equipo_local and J_MA != equipo_visitante):
            raise ValidationError({"J_MA": "Debes elegir un equipo válido."})
        
        if A_BB and (A_BB != equipo_local and A_BB != equipo_visitante):
            raise ValidationError({"A_BB": "Debes elegir un equipo válido."})
        if B_BB and (B_BB != equipo_local and B_BB != equipo_visitante):
            raise ValidationError({"B_BB": "Debes elegir un equipo válido."})
        if C_BB and (C_BB != equipo_local and C_BB != equipo_visitante):
            raise ValidationError({"C_BB": "Debes elegir un equipo válido."})
        if D_BB and (D_BB != equipo_local and D_BB != equipo_visitante):
            raise ValidationError({"D_BB": "Debes elegir un equipo válido."})
        if E_BB and (E_BB != equipo_local and E_BB != equipo_visitante):
            raise ValidationError({"E_BB": "Debes elegir un equipo válido."})
        if F_BB and (F_BB != equipo_local and F_BB != equipo_visitante):
            raise ValidationError({"F_BB": "Debes elegir un equipo válido."})
        if G_BB and (G_BB != equipo_local and G_BB != equipo_visitante):
            raise ValidationError({"G_BB": "Debes elegir un equipo válido."})
        if H_BB and (H_BB != equipo_local and H_BB != equipo_visitante):
            raise ValidationError({"H_BB": "Debes elegir un equipo válido."})
        if I_BB and (I_BB != equipo_local and I_BB != equipo_visitante):
            raise ValidationError({"I_BB": "Debes elegir un equipo válido."})
        if J_BB and (J_BB != equipo_local and J_BB != equipo_visitante):
            raise ValidationError({"J_BB": "Debes elegir un equipo válido."})
         

        
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_punto = cleaned_data.get('G_total_punto')     
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_punto = cleaned_data.get('J_total_punto')
        
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        
        if A_Total_punto and (A_Total_punto < 0 ):
            raise ValidationError({"A_Total_punto": "Introdusca un valor válido."})
        if B_Total_punto and (B_Total_punto < 0 ):
            raise ValidationError({"B_Total_punto": "Introdusca un valor válido."})
        if C_Total_punto and (C_Total_punto < 0 ):
            raise ValidationError({"C_Total_punto": "Introdusca un valor válido."})
        if D_Total_punto and (D_Total_punto < 0 ):
            raise ValidationError({"D_Total_punto": "Introdusca un valor válido."})
        if E_Total_punto and (E_Total_punto < 0 ):
            raise ValidationError({"E_Total_punto": "Introdusca un valor válido."})
        if F_Total_punto and (F_Total_punto < 0 ):
            raise ValidationError({"F_Total_punto": "Introdusca un valor válido."})
        if G_Total_punto and (G_Total_punto < 0 ):
            raise ValidationError({"G_Total_punto": "Introdusca un valor válido."})
        if H_Total_punto and (H_Total_punto < 0 ):
            raise ValidationError({"H_Total_punto": "Introdusca un valor válido."})
        if I_Total_punto and (I_Total_punto < 0 ):
            raise ValidationError({"I_Total_punto": "Introdusca un valor válido."})
        if J_Total_punto and (J_Total_punto < 0 ):
            raise ValidationError({"J_Total_punto": "Introdusca un valor válido."})
        
        if A_SP_dif and (A_SP_dif < 0 ):
            raise ValidationError({"A_SP_dif": "Introdusca un valor válido."})
        if B_SP_dif and (B_SP_dif < 0 ):
            raise ValidationError({"B_SP_dif": "Introdusca un valor válido."})
        if C_SP_dif and (C_SP_dif < 0 ):
            raise ValidationError({"C_SP_dif": "Introdusca un valor válido."})
        if D_SP_dif and (D_SP_dif < 0 ):
            raise ValidationError({"D_SP_dif": "Introdusca un valor válido."})
        if E_SP_dif and (E_SP_dif < 0 ):
            raise ValidationError({"E_SP_dif": "Introdusca un valor válido."})
        if F_SP_dif and (F_SP_dif < 0 ):
            raise ValidationError({"F_SP_dif": "Introdusca un valor válido."})
        if G_SP_dif and (G_SP_dif < 0 ):
            raise ValidationError({"G_SP_dif": "Introdusca un valor válido."})
        if H_SP_dif and (H_SP_dif < 0 ):
            raise ValidationError({"H_SP_dif": "Introdusca un valor válido."})
        if I_SP_dif and (I_SP_dif < 0 ):
            raise ValidationError({"I_SP_dif": "Introdusca un valor válido."})
        if J_SP_dif and (J_SP_dif < 0 ):
            raise ValidationError({"J_SP_dif": "Introdusca un valor válido."})
        
        return cleaned_data
    


        
class NBA_Colegial_form(forms.ModelForm):
    
    equipo_local = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    equipo_visitante = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    B_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    C_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    D_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    E_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    F_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    G_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    H_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    I_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    J_ML_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_SP_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_Ud_equip = forms.ModelChoiceField( queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_SB_equip = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_MA = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_BB = forms.ModelChoiceField(queryset=equipos_NBA_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    
    
    
    class Meta:
        model = NBA_Colegial
        fields = ['equipo_local', 'equipo_visitante','fecha','A_ML_equip','A_ML_prob','A_SP_equip','A_SP_prob','A_SP_dif','A_Total_OU','A_Total_prob','A_Ud_equip','A_Ud_prob','A_SB_equip','A_SB_prob','A_MA','A_BB','A_total_punto',
                  'B_ML_equip','B_ML_prob','B_SP_equip','B_SP_prob','B_SP_dif','B_Total_OU','B_Total_prob','B_Ud_equip','B_Ud_prob','B_SB_equip','B_SB_prob','B_MA','B_BB','B_total_punto','A_MA_prob','B_MA_prob','C_MA_prob','D_MA_prob',
                  'C_ML_equip','C_ML_prob','C_SP_equip','C_SP_prob','C_SP_dif','C_Total_OU','C_Total_prob','C_Ud_equip','C_Ud_prob','C_SB_equip','C_SB_prob','C_MA','C_BB','C_total_punto','E_MA_prob','F_MA_prob','G_MA_prob','H_MA_prob',
                  'D_ML_equip','D_ML_prob','D_SP_equip','D_SP_prob','D_SP_dif','D_Total_OU','D_Total_prob','D_Ud_equip','D_Ud_prob','D_SB_equip','D_SB_prob','D_MA','D_BB','D_total_punto','I_MA_prob','J_MA_prob','A_BB_prob','B_BB_prob',
                  'E_ML_equip','E_ML_prob','E_SP_equip','E_SP_prob','E_SP_dif','E_Total_OU','E_Total_prob','E_Ud_equip','E_Ud_prob','E_SB_equip','E_SB_prob','E_MA','E_BB','E_total_punto','C_BB_prob','D_BB_prob','E_BB_prob','F_BB_prob',
                  'F_ML_equip','F_ML_prob','F_SP_equip','F_SP_prob','F_SP_dif','F_Total_OU','F_Total_prob','F_Ud_equip','F_Ud_prob','F_SB_equip','F_SB_prob','F_MA','F_BB','F_total_punto','G_BB_prob','H_BB_prob','I_BB_prob','J_BB_prob',
                  'G_ML_equip','G_ML_prob','G_SP_equip','G_SP_prob','G_SP_dif','G_Total_OU','G_Total_prob','G_Ud_equip','G_Ud_prob','G_SB_equip','G_SB_prob','G_MA','G_BB','G_total_punto',
                  'H_ML_equip','H_ML_prob','H_SP_equip','H_SP_prob','H_SP_dif','H_Total_OU','H_Total_prob','H_Ud_equip','H_Ud_prob','H_SB_equip','H_SB_prob','H_MA','H_BB','H_total_punto',
                  'I_ML_equip','I_ML_prob','I_SP_equip','I_SP_prob','I_SP_dif','I_Total_OU','I_Total_prob','I_Ud_equip','I_Ud_prob','I_SB_equip','I_SB_prob','I_MA','I_BB','I_total_punto',
                  'J_ML_equip','J_ML_prob','J_SP_equip','J_SP_prob','J_SP_dif','J_Total_OU','J_Total_prob','J_Ud_equip','J_Ud_prob','J_SB_equip','J_SB_prob','J_MA','J_BB','J_total_punto',
                  ]
        
        widgets = {
            
            'equipo_local': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'equipo_visitante': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control select-field', 'placeholder': '' }),
            'A_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visitante = cleaned_data.get('equipo_visitante')

       
        existing_partidos = NBA_Colegial.objects.filter(
            Q(fecha=fecha) &
            ~Q(id=self.instance.id) &  
            (
                Q(equipo_local=equipo_local) | 
                Q(equipo_visitante=equipo_visitante) 
            )
        )

        if existing_partidos.exists():
            raise ValidationError("Ya existe un partido con el mismo equipo programado para esta fecha.")

       
        if equipo_local.nombre == equipo_visitante.nombre:
           raise ValidationError("El equipo local y el equipo visitante no pueden ser el mismo.")     

    
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        J_ML_equip = cleaned_data.get('J_ML_equip')
        
        A_SP_equip = cleaned_data.get('A_SP_equip')
        A_SP_prob = cleaned_data.get('A_SP_prob')
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        J_SP_prob = cleaned_data.get('J_SP_prob')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        A_Total_OU = cleaned_data.get('A_Total_OU')
        A_Total_prob = cleaned_data.get('A_Total_prob')
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_OU = cleaned_data.get('B_Total_OU')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_OU = cleaned_data.get('C_Total_OU')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_OU = cleaned_data.get('D_Total_OU')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_OU = cleaned_data.get('E_Total_OU')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_OU = cleaned_data.get('F_Total_OU')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_OU = cleaned_data.get('G_Total_OU')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        G_Total_punto = cleaned_data.get('G_total_punto')
        H_Total_OU = cleaned_data.get('H_Total_OU')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_OU = cleaned_data.get('I_Total_OU')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_OU = cleaned_data.get('J_Total_OU')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        J_Total_punto = cleaned_data.get('J_total_punto')
       
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')
        
        A_SB_equip = cleaned_data.get('A_SB_equip')
        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_equip = cleaned_data.get('J_SB_equip')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
        A_MA= cleaned_data.get('A_MA')
        B_MA= cleaned_data.get('B_MA')
        C_MA= cleaned_data.get('C_MA')
        D_MA= cleaned_data.get('D_MA')
        E_MA= cleaned_data.get('E_MA')
        F_MA= cleaned_data.get('F_MA')
        G_MA= cleaned_data.get('G_MA')
        H_MA= cleaned_data.get('H_MA')
        I_MA= cleaned_data.get('I_MA')
        J_MA= cleaned_data.get('J_MA')
        
        A_MA_prob= cleaned_data.get('A_MA_prob')
        B_MA_prob= cleaned_data.get('B_MA_prob')
        C_MA_prob= cleaned_data.get('C_MA_prob')
        D_MA_prob= cleaned_data.get('D_MA_prob')
        E_MA_prob= cleaned_data.get('E_MA_prob')
        F_MA_prob= cleaned_data.get('F_MA_prob')
        G_MA_prob= cleaned_data.get('G_MA_prob')
        H_MA_prob= cleaned_data.get('H_MA_prob')
        I_MA_prob= cleaned_data.get('I_MA_prob')
        J_MA_prob= cleaned_data.get('J_MA_prob')
        
        
        A_BB= cleaned_data.get('A_BB')
        B_BB= cleaned_data.get('B_BB')
        C_BB= cleaned_data.get('C_BB')
        D_BB= cleaned_data.get('D_BB')
        E_BB= cleaned_data.get('E_BB')
        F_BB= cleaned_data.get('F_BB')
        G_BB= cleaned_data.get('G_BB')
        H_BB= cleaned_data.get('H_BB')
        I_BB= cleaned_data.get('I_BB')
        J_BB= cleaned_data.get('J_BB')
         
        A_BB_prob= cleaned_data.get('A_BB_prob')
        B_BB_prob= cleaned_data.get('B_BB_prob')
        C_BB_prob= cleaned_data.get('C_BB_prob')
        D_BB_prob= cleaned_data.get('D_BB_prob')
        E_BB_prob= cleaned_data.get('E_BB_prob')
        F_BB_prob= cleaned_data.get('F_BB_prob')
        G_BB_prob= cleaned_data.get('G_BB_prob')
        H_BB_prob= cleaned_data.get('H_BB_prob')
        I_BB_prob= cleaned_data.get('I_BB_prob')
        J_BB_prob= cleaned_data.get('J_BB_prob')

        
        # Realiza la validación personalizada
        if A_ML_prob or A_ML_equip:
            if not (A_ML_equip and A_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if B_ML_prob or B_ML_equip:
            if not (B_ML_equip and B_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if C_ML_prob or C_ML_equip:
            if not (C_ML_equip and C_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if D_ML_prob or D_ML_equip:
            if not (D_ML_equip and D_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if E_ML_prob or E_ML_equip:
            if not (E_ML_equip and E_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if F_ML_prob or F_ML_equip:
            if not (F_ML_equip and F_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if G_ML_prob or G_ML_equip:
            if not (G_ML_equip and G_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if H_ML_prob or H_ML_equip:
            if not (H_ML_equip and H_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if I_ML_prob or I_ML_equip:
            if not (I_ML_equip and I_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if J_ML_prob or J_ML_equip:
            if not (J_ML_equip and J_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        
        if A_SP_equip or A_SP_prob or A_SP_dif :
            if not (A_SP_equip and A_SP_prob and A_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if B_SP_equip or B_SP_prob or B_SP_dif :
            if not (B_SP_equip and B_SP_prob and B_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if C_SP_equip or C_SP_prob or C_SP_dif :
            if not (C_SP_equip and C_SP_prob and C_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if D_SP_equip or D_SP_prob or D_SP_dif :
            if not (D_SP_equip and D_SP_prob and D_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if E_SP_equip or E_SP_prob or E_SP_dif :
            if not (E_SP_equip and E_SP_prob and E_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if F_SP_equip or F_SP_prob or F_SP_dif :
            if not (F_SP_equip and F_SP_prob and F_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if G_SP_equip or G_SP_prob or G_SP_dif :
            if not (G_SP_equip and G_SP_prob and G_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if H_SP_equip or H_SP_prob or H_SP_dif :
            if not (H_SP_equip and H_SP_prob and H_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if I_SP_equip or I_SP_prob or I_SP_dif :
            if not (I_SP_equip and I_SP_prob and I_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if J_SP_equip or J_SP_prob or J_SP_dif :
            if not (J_SP_equip and J_SP_prob and J_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
  
       
        if A_Total_OU or A_Total_prob or A_Total_punto :
            if not (A_Total_OU and A_Total_prob and A_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if B_Total_OU or B_Total_prob or B_Total_punto :
            if not (B_Total_OU and B_Total_prob and B_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if C_Total_OU or C_Total_prob or C_Total_punto :
            if not (C_Total_OU and C_Total_prob and C_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if D_Total_OU or D_Total_prob or D_Total_punto :
            if not (D_Total_OU and D_Total_prob and D_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if E_Total_OU or E_Total_prob or E_Total_punto :
            if not (E_Total_OU and E_Total_prob and E_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if F_Total_OU or F_Total_prob or F_Total_punto :
            if not (F_Total_OU and F_Total_prob and F_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if G_Total_OU or G_Total_prob or G_Total_punto :
            if not (G_Total_OU and G_Total_prob and G_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if H_Total_OU or H_Total_prob or H_Total_punto :
            if not (H_Total_OU and H_Total_prob and H_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if I_Total_OU or I_Total_prob or I_Total_punto :
            if not (I_Total_OU and I_Total_prob and I_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if J_Total_OU or J_Total_prob or J_Total_punto :
            if not (J_Total_OU and J_Total_prob and J_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
      
        if A_Ud_equip or A_Ud_prob:
            if not (A_Ud_equip and A_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if B_Ud_equip or B_Ud_prob:
            if not (B_Ud_equip and B_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if C_Ud_equip or C_Ud_prob:
            if not (C_Ud_equip and C_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if D_Ud_equip or D_Ud_prob:
            if not (D_Ud_equip and D_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if E_Ud_equip or E_Ud_prob:
            if not (E_Ud_equip and E_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if F_Ud_equip or F_Ud_prob:
            if not (F_Ud_equip and F_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if G_Ud_equip or G_Ud_prob:
            if not (G_Ud_equip and G_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if H_Ud_equip or H_Ud_prob:
            if not (H_Ud_equip and H_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if I_Ud_equip or I_Ud_prob:
            if not (I_Ud_equip and I_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if J_Ud_equip or J_Ud_prob:
            if not (J_Ud_equip and J_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
       
        if A_SB_equip or A_SB_prob:
            if not (A_SB_equip and A_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if B_SB_equip or B_SB_prob:
            if not (B_SB_equip and B_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if C_SB_equip or C_SB_prob:
            if not (C_SB_equip and C_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if D_SB_equip or D_SB_prob:
            if not (D_SB_equip and D_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if E_SB_equip or E_SB_prob:
            if not (E_SB_equip and E_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if F_SB_equip or F_SB_prob:
            if not (F_SB_equip and F_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if G_SB_equip or G_SB_prob:
            if not (G_SB_equip and G_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if H_SB_equip or H_SB_prob:
            if not (H_SB_equip and H_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if I_SB_equip or I_SB_prob:
            if not (I_SB_equip and I_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if J_SB_equip or J_SB_prob:
            if not (J_SB_equip and J_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
       
        if A_MA or A_MA_prob:
            if not (A_MA and A_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if B_MA or B_MA_prob:
            if not (B_MA and B_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if C_MA or C_MA_prob:
            if not (C_MA and C_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if D_MA or D_MA_prob:
            if not (D_MA and D_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if E_MA or E_MA_prob:
            if not (E_MA and E_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if F_MA or F_MA_prob:
            if not (F_MA and F_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if G_MA or G_MA_prob:
            if not (G_MA and G_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if H_MA or H_MA_prob:
            if not (H_MA and H_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if I_MA or I_MA_prob:
            if not (I_MA and I_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if J_MA or J_MA_prob:
            if not (J_MA and J_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ") 
   
        
        if A_BB or A_BB_prob:
            if not (A_BB and A_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if B_BB or B_BB_prob:
            if not (B_BB and B_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if C_BB or C_BB_prob:
            if not (C_BB and C_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if D_BB or D_BB_prob:
            if not (D_BB and D_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if E_BB or E_BB_prob:
            if not (E_BB and E_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if F_BB or F_BB_prob:
            if not (F_BB and F_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if G_BB or G_BB_prob:
            if not (G_BB and G_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if H_BB or H_BB_prob:
            if not (H_BB and H_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if I_BB or I_BB_prob:
            if not (I_BB and I_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if J_BB or J_BB_prob:
            if not (J_BB and J_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        
       
       
       
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        
        A_SP_prob = cleaned_data.get('A_SP_prob')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        J_SP_prob = cleaned_data.get('J_SP_prob')

        A_Total_prob = cleaned_data.get('A_Total_prob')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')

        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
       
        if A_ML_prob and (A_ML_prob < 1 or A_ML_prob > 99):
            raise ValidationError({"A_ML_prob": "El valor de probabilidad debe estar entre 1 y 99."})
        if B_ML_prob and (B_ML_prob < 0 or B_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_ML_prob and (C_ML_prob < 0 or C_ML_prob > 99):
            raise ValidationError({"C_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_ML_prob and (D_ML_prob < 0 or D_ML_prob > 99):
            raise ValidationError({"D_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_ML_prob and (E_ML_prob < 0 or E_ML_prob > 99):
            raise ValidationError({"E_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_ML_prob and (F_ML_prob < 0 or F_ML_prob > 99):
            raise ValidationError({"F_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_ML_prob and (G_ML_prob < 0 or G_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_ML_prob and (H_ML_prob < 0 or H_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_ML_prob and (I_ML_prob < 0 or I_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_ML_prob and (J_ML_prob < 0 or J_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})


        if A_SP_prob and (A_SP_prob < 0 or A_SP_prob > 99):
            raise ValidationError({"A_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SP_prob and (B_SP_prob < 0 or B_SP_prob > 99):
            raise ValidationError({"B_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SP_prob and (C_SP_prob < 0 or C_SP_prob > 99):
            raise ValidationError({"C_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SP_prob and (D_SP_prob < 0 or D_SP_prob > 99):
            raise ValidationError({"D_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SP_prob and (E_SP_prob < 0 or E_SP_prob > 99):
            raise ValidationError({"E_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SP_prob and (F_SP_prob < 0 or F_SP_prob > 99):
            raise ValidationError({"F_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SP_prob and (G_SP_prob < 0 or G_SP_prob > 99):
            raise ValidationError({"G_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SP_prob and (H_SP_prob < 0 or H_SP_prob > 99):
            raise ValidationError({"H_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SP_prob and (I_SP_prob < 0 or I_SP_prob > 99):
            raise ValidationError({"I_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SP_prob and (J_SP_prob < 0 or J_SP_prob > 99):
            raise ValidationError({"J_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Total_prob and (A_Total_prob < 0 or A_Total_prob > 99):
            raise ValidationError({"A_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Total_prob and (B_Total_prob < 0 or B_Total_prob > 99):
            raise ValidationError({"B_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Total_prob and (C_Total_prob < 0 or C_Total_prob > 99):
            raise ValidationError({"C_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Total_prob and (D_Total_prob < 0 or D_Total_prob > 99):
            raise ValidationError({"D_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Total_prob and (E_Total_prob < 0 or E_Total_prob > 99):
            raise ValidationError({"E_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Total_prob and (F_Total_prob < 0 or F_Total_prob > 99):
            raise ValidationError({"F_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Total_prob and (G_Total_prob < 0 or G_Total_prob > 99):
            raise ValidationError({"G_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Total_prob and (H_Total_prob < 0 or H_Total_prob > 99):
            raise ValidationError({"H_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Total_prob and (I_Total_prob < 0 or I_Total_prob > 99):
            raise ValidationError({"I_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Total_prob and (J_Total_prob < 0 or J_Total_prob > 99):
            raise ValidationError({"J_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Ud_prob and (A_Ud_prob < 0 or A_Ud_prob > 99):
            raise ValidationError({"A_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Ud_prob and (B_Ud_prob < 0 or B_Ud_prob > 99):
            raise ValidationError({"B_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Ud_prob and (C_Ud_prob < 0 or C_Ud_prob > 99):
            raise ValidationError({"C_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Ud_prob and (D_Ud_prob < 0 or D_Ud_prob > 99):
            raise ValidationError({"D_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Ud_prob and (E_Ud_prob < 0 or E_Ud_prob > 99):
            raise ValidationError({"E_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Ud_prob and (F_Ud_prob < 0 or F_Ud_prob > 99):
            raise ValidationError({"F_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Ud_prob and (G_Ud_prob < 0 or G_Ud_prob > 99):
            raise ValidationError({"G_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Ud_prob and (H_Ud_prob < 0 or H_Ud_prob > 99):
            raise ValidationError({"H_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Ud_prob and (I_Ud_prob < 0 or I_Ud_prob > 99):
            raise ValidationError({"I_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Ud_prob and (J_Ud_prob < 0 or J_Ud_prob > 99):
            raise ValidationError({"J_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_SB_prob and (A_SB_prob < 0 or A_SB_prob > 99):
            raise ValidationError({"A_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SB_prob and (B_SB_prob < 0 or B_SB_prob > 99):
            raise ValidationError({"B_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SB_prob and (C_SB_prob < 0 or C_SB_prob > 99):
            raise ValidationError({"C_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SB_prob and (D_SB_prob < 0 or D_SB_prob > 99):
            raise ValidationError({"D_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SB_prob and (E_SB_prob < 0 or E_SB_prob > 99):
            raise ValidationError({"E_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SB_prob and (F_SB_prob < 0 or F_SB_prob > 99):
            raise ValidationError({"F_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SB_prob and (G_SB_prob < 0 or G_SB_prob > 99):
            raise ValidationError({"G_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SB_prob and (H_SB_prob < 0 or H_SB_prob > 99):
            raise ValidationError({"H_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SB_prob and (I_SB_prob < 0 or I_SB_prob > 99):
            raise ValidationError({"I_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SB_prob and (J_SB_prob < 0 or J_SB_prob > 99):
            raise ValidationError({"J_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
          
        if A_MA_prob and (A_MA_prob < 0 or A_MA_prob > 99):
            raise ValidationError({"A_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_MA_prob and (B_MA_prob < 0 or B_MA_prob > 99):
            raise ValidationError({"B_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if C_MA_prob and (C_MA_prob < 0 or C_MA_prob > 99):
            raise ValidationError({"C_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if D_MA_prob and (D_MA_prob < 0 or D_MA_prob > 99):
            raise ValidationError({"D_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if E_MA_prob and (E_MA_prob < 0 or E_MA_prob > 99):
            raise ValidationError({"E_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_MA_prob and (F_MA_prob < 0 or F_MA_prob > 99):
            raise ValidationError({"F_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_MA_prob and (G_MA_prob < 0 or G_MA_prob > 99):
            raise ValidationError({"G_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_MA_prob and (H_MA_prob < 0 or H_MA_prob > 99):
            raise ValidationError({"H_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_MA_prob and (I_MA_prob < 0 or I_MA_prob > 99):
            raise ValidationError({"I_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_MA_prob and (J_MA_prob < 0 or J_MA_prob > 99):
            raise ValidationError({"J_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        if A_BB_prob and (A_BB_prob < 0 or A_BB_prob > 99):
            raise ValidationError({"A_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_BB_prob and (B_BB_prob < 0 or B_BB_prob > 99):
            raise ValidationError({"B_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_BB_prob and (C_BB_prob < 0 or C_BB_prob > 99):
            raise ValidationError({"C_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_BB_prob and (D_BB_prob < 0 or D_BB_prob > 99):
            raise ValidationError({"D_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_BB_prob and (E_BB_prob < 0 or E_BB_prob > 99):
            raise ValidationError({"E_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_BB_prob and (F_BB_prob < 0 or F_BB_prob > 99):
            raise ValidationError({"F_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_BB_prob and (G_BB_prob < 0 or G_BB_prob > 99):
            raise ValidationError({"G_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_BB_prob and (H_BB_prob < 0 or H_BB_prob > 99):
            raise ValidationError({"H_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_BB_prob and (I_BB_prob < 0 or I_BB_prob > 99):
            raise ValidationError({"I_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_BB_prob and (J_BB_prob < 0 or J_BB_prob > 99):
            raise ValidationError({"J_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_equip = cleaned_data.get('J_ML_equip')

        A_SP_equip = cleaned_data.get('A_SP_equip')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
       
        A_SB_equip = cleaned_data.get('A_SB_equip')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        J_SB_equip = cleaned_data.get('J_SB_equip')
       
        A_MA = cleaned_data.get('A_MA')
        B_MA = cleaned_data.get('B_MA')
        C_MA = cleaned_data.get('C_MA')
        D_MA = cleaned_data.get('D_MA')
        E_MA = cleaned_data.get('E_MA')
        F_MA = cleaned_data.get('F_MA')
        G_MA = cleaned_data.get('G_MA')
        H_MA = cleaned_data.get('H_MA')
        I_MA = cleaned_data.get('I_MA')
        J_MA = cleaned_data.get('J_MA')

        A_BB = cleaned_data.get('A_BB')
        B_BB = cleaned_data.get('B_BB')
        C_BB = cleaned_data.get('C_BB')
        D_BB = cleaned_data.get('D_BB')
        E_BB = cleaned_data.get('E_BB')
        F_BB = cleaned_data.get('F_BB')
        G_BB = cleaned_data.get('G_BB')
        H_BB = cleaned_data.get('H_BB')
        I_BB = cleaned_data.get('I_BB')
        J_BB = cleaned_data.get('J_BB')
        
        
              
        # Validación para ganador
        if A_ML_equip and (A_ML_equip != equipo_local and A_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})
        if B_ML_equip and (B_ML_equip != equipo_local and B_ML_equip != equipo_visitante):
            raise ValidationError({"B_ML_equip": "Debes elegir un equipo válido."})
        if C_ML_equip and (C_ML_equip != equipo_local and C_ML_equip != equipo_visitante):
            raise ValidationError({"C_ML_equip": "Debes elegir un equipo válido."})
        if D_ML_equip and (D_ML_equip != equipo_local and D_ML_equip != equipo_visitante):
            raise ValidationError({"D_ML_equip": "Debes elegir un equipo válido."})
        if E_ML_equip and (E_ML_equip != equipo_local and E_ML_equip != equipo_visitante):
            raise ValidationError({"E_ML_equip": "Debes elegir un equipo válido."})
        if F_ML_equip and (F_ML_equip != equipo_local and F_ML_equip != equipo_visitante):
            raise ValidationError({"F_ML_equip": "Debes elegir un equipo válido."})
        if G_ML_equip and (G_ML_equip != equipo_local and G_ML_equip != equipo_visitante):
            raise ValidationError({"G_ML_equip": "Debes elegir un equipo válido."})
        if H_ML_equip and (H_ML_equip != equipo_local and H_ML_equip != equipo_visitante):
            raise ValidationError({"H_ML_equip": "Debes elegir un equipo válido."})
        if I_ML_equip and (I_ML_equip != equipo_local and I_ML_equip != equipo_visitante):
            raise ValidationError({"I_ML_equip": "Debes elegir un equipo válido."})
        if J_ML_equip and (J_ML_equip != equipo_local and J_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})

        if A_SP_equip and (A_SP_equip != equipo_local and A_SP_equip != equipo_visitante):
            raise ValidationError({"A_SP_equip": "Debes elegir un equipo válido."})
        if B_SP_equip and (B_SP_equip != equipo_local and B_SP_equip != equipo_visitante):
            raise ValidationError({"B_SP_equip": "Debes elegir un equipo válido."})
        if C_SP_equip and (C_SP_equip != equipo_local and C_SP_equip != equipo_visitante):
            raise ValidationError({"C_SP_equip": "Debes elegir un equipo válido."})
        if D_SP_equip and (D_SP_equip != equipo_local and D_SP_equip != equipo_visitante):
            raise ValidationError({"D_SP_equip": "Debes elegir un equipo válido."})
        if E_SP_equip and (E_SP_equip != equipo_local and E_SP_equip != equipo_visitante):
            raise ValidationError({"E_SP_equip": "Debes elegir un equipo válido."})
        if F_SP_equip and (F_SP_equip != equipo_local and F_SP_equip != equipo_visitante):
            raise ValidationError({"F_SP_equip": "Debes elegir un equipo válido."})
        if G_SP_equip and (G_SP_equip != equipo_local and G_SP_equip != equipo_visitante):
            raise ValidationError({"G_SP_equip": "Debes elegir un equipo válido."})
        if H_SP_equip and (H_SP_equip != equipo_local and H_SP_equip != equipo_visitante):
            raise ValidationError({"H_SP_equip": "Debes elegir un equipo válido."})
        if I_SP_equip and (I_SP_equip != equipo_local and I_SP_equip != equipo_visitante):
            raise ValidationError({"I_SP_equip": "Debes elegir un equipo válido."})
        if J_SP_equip and (J_SP_equip != equipo_local and J_SP_equip != equipo_visitante):
            raise ValidationError({"J_SP_equip": "Debes elegir un equipo válido."})
        
        if A_Ud_equip and (A_Ud_equip != equipo_local and A_Ud_equip != equipo_visitante):
            raise ValidationError({"A_Ud_equip": "Debes elegir un equipo válido."})
        if B_Ud_equip and (B_Ud_equip != equipo_local and B_Ud_equip != equipo_visitante):
            raise ValidationError({"B_Ud_equip": "Debes elegir un equipo válido."})
        if C_Ud_equip and (C_Ud_equip != equipo_local and C_Ud_equip != equipo_visitante):
            raise ValidationError({"C_Ud_equip": "Debes elegir un equipo válido."})
        if D_Ud_equip and (D_Ud_equip != equipo_local and D_Ud_equip != equipo_visitante):
            raise ValidationError({"D_Ud_equip": "Debes elegir un equipo válido."})
        if E_Ud_equip and (E_Ud_equip != equipo_local and E_Ud_equip != equipo_visitante):
            raise ValidationError({"E_Ud_equip": "Debes elegir un equipo válido."})
        if F_Ud_equip and (F_Ud_equip != equipo_local and F_Ud_equip != equipo_visitante):
            raise ValidationError({"F_Ud_equip": "Debes elegir un equipo válido."})
        if G_Ud_equip and (G_Ud_equip != equipo_local and G_Ud_equip != equipo_visitante):
            raise ValidationError({"G_Ud_equip": "Debes elegir un equipo válido."})
        if H_Ud_equip and (H_Ud_equip != equipo_local and H_Ud_equip != equipo_visitante):
            raise ValidationError({"H_Ud_equip": "Debes elegir un equipo válido."})
        if I_Ud_equip and (I_Ud_equip != equipo_local and I_Ud_equip != equipo_visitante):
            raise ValidationError({"I_Ud_equip": "Debes elegir un equipo válido."})
        if J_Ud_equip and (J_Ud_equip != equipo_local and J_Ud_equip != equipo_visitante):
            raise ValidationError({"J_Ud_equip": "Debes elegir un equipo válido."})
        
        if A_SB_equip and (A_SB_equip != equipo_local and A_SB_equip != equipo_visitante):
            raise ValidationError({"A_SB_equip": "Debes elegir un equipo válido."})
        if B_SB_equip and (B_SB_equip != equipo_local and B_SB_equip != equipo_visitante):
            raise ValidationError({"B_SB_equip": "Debes elegir un equipo válido."})
        if C_SB_equip and (C_SB_equip != equipo_local and C_SB_equip != equipo_visitante):
            raise ValidationError({"C_SB_equip": "Debes elegir un equipo válido."})
        if D_SB_equip and (D_SB_equip != equipo_local and D_SB_equip != equipo_visitante):
            raise ValidationError({"D_SB_equip": "Debes elegir un equipo válido."})
        if E_SB_equip and (E_SB_equip != equipo_local and E_SB_equip != equipo_visitante):
            raise ValidationError({"E_SB_equip": "Debes elegir un equipo válido."})
        if F_SB_equip and (F_SB_equip != equipo_local and F_SB_equip != equipo_visitante):
            raise ValidationError({"F_SB_equip": "Debes elegir un equipo válido."})
        if G_SB_equip and (G_SB_equip != equipo_local and G_SB_equip != equipo_visitante):
            raise ValidationError({"G_SB_equip": "Debes elegir un equipo válido."})
        if H_SB_equip and (H_SB_equip != equipo_local and H_SB_equip != equipo_visitante):
            raise ValidationError({"H_SB_equip": "Debes elegir un equipo válido."})
        if I_SB_equip and (I_SB_equip != equipo_local and I_SB_equip != equipo_visitante):
            raise ValidationError({"I_SB_equip": "Debes elegir un equipo válido."})
        if J_SB_equip and (J_SB_equip != equipo_local and J_SB_equip != equipo_visitante):
            raise ValidationError({"J_SB_equip": "Debes elegir un equipo válido."})
        
        if A_MA and (A_MA != equipo_local and A_MA != equipo_visitante):
            raise ValidationError({"A_MA": "Debes elegir un equipo válido."})
        if B_MA and (B_MA != equipo_local and B_MA != equipo_visitante):
            raise ValidationError({"B_MA": "Debes elegir un equipo válido."})
        if C_MA and (C_MA != equipo_local and C_MA != equipo_visitante):
            raise ValidationError({"C_MA": "Debes elegir un equipo válido."})
        if D_MA and (D_MA != equipo_local and D_MA != equipo_visitante):
            raise ValidationError({"D_MA": "Debes elegir un equipo válido."})
        if E_MA and (E_MA != equipo_local and E_MA != equipo_visitante):
            raise ValidationError({"E_MA": "Debes elegir un equipo válido."})
        if F_MA and (F_MA != equipo_local and F_MA != equipo_visitante):
            raise ValidationError({"F_MA": "Debes elegir un equipo válido."})
        if G_MA and (G_MA != equipo_local and G_MA != equipo_visitante):
            raise ValidationError({"G_MA": "Debes elegir un equipo válido."})
        if H_MA and (H_MA != equipo_local and H_MA != equipo_visitante):
            raise ValidationError({"H_MA": "Debes elegir un equipo válido."})
        if I_MA and (I_MA != equipo_local and I_MA != equipo_visitante):
            raise ValidationError({"I_MA": "Debes elegir un equipo válido."})
        if J_MA and (J_MA != equipo_local and J_MA != equipo_visitante):
            raise ValidationError({"J_MA": "Debes elegir un equipo válido."})
        
        if A_BB and (A_BB != equipo_local and A_BB != equipo_visitante):
            raise ValidationError({"A_BB": "Debes elegir un equipo válido."})
        if B_BB and (B_BB != equipo_local and B_BB != equipo_visitante):
            raise ValidationError({"B_BB": "Debes elegir un equipo válido."})
        if C_BB and (C_BB != equipo_local and C_BB != equipo_visitante):
            raise ValidationError({"C_BB": "Debes elegir un equipo válido."})
        if D_BB and (D_BB != equipo_local and D_BB != equipo_visitante):
            raise ValidationError({"D_BB": "Debes elegir un equipo válido."})
        if E_BB and (E_BB != equipo_local and E_BB != equipo_visitante):
            raise ValidationError({"E_BB": "Debes elegir un equipo válido."})
        if F_BB and (F_BB != equipo_local and F_BB != equipo_visitante):
            raise ValidationError({"F_BB": "Debes elegir un equipo válido."})
        if G_BB and (G_BB != equipo_local and G_BB != equipo_visitante):
            raise ValidationError({"G_BB": "Debes elegir un equipo válido."})
        if H_BB and (H_BB != equipo_local and H_BB != equipo_visitante):
            raise ValidationError({"H_BB": "Debes elegir un equipo válido."})
        if I_BB and (I_BB != equipo_local and I_BB != equipo_visitante):
            raise ValidationError({"I_BB": "Debes elegir un equipo válido."})
        if J_BB and (J_BB != equipo_local and J_BB != equipo_visitante):
            raise ValidationError({"J_BB": "Debes elegir un equipo válido."})
         

        
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_punto = cleaned_data.get('G_total_punto')     
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_punto = cleaned_data.get('J_total_punto')
        
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        
        if A_Total_punto and (A_Total_punto < 0 ):
            raise ValidationError({"A_Total_punto": "Introdusca un valor válido."})
        if B_Total_punto and (B_Total_punto < 0 ):
            raise ValidationError({"B_Total_punto": "Introdusca un valor válido."})
        if C_Total_punto and (C_Total_punto < 0 ):
            raise ValidationError({"C_Total_punto": "Introdusca un valor válido."})
        if D_Total_punto and (D_Total_punto < 0 ):
            raise ValidationError({"D_Total_punto": "Introdusca un valor válido."})
        if E_Total_punto and (E_Total_punto < 0 ):
            raise ValidationError({"E_Total_punto": "Introdusca un valor válido."})
        if F_Total_punto and (F_Total_punto < 0 ):
            raise ValidationError({"F_Total_punto": "Introdusca un valor válido."})
        if G_Total_punto and (G_Total_punto < 0 ):
            raise ValidationError({"G_Total_punto": "Introdusca un valor válido."})
        if H_Total_punto and (H_Total_punto < 0 ):
            raise ValidationError({"H_Total_punto": "Introdusca un valor válido."})
        if I_Total_punto and (I_Total_punto < 0 ):
            raise ValidationError({"I_Total_punto": "Introdusca un valor válido."})
        if J_Total_punto and (J_Total_punto < 0 ):
            raise ValidationError({"J_Total_punto": "Introdusca un valor válido."})
        
        if A_SP_dif and (A_SP_dif < 0 ):
            raise ValidationError({"A_SP_dif": "Introdusca un valor válido."})
        if B_SP_dif and (B_SP_dif < 0 ):
            raise ValidationError({"B_SP_dif": "Introdusca un valor válido."})
        if C_SP_dif and (C_SP_dif < 0 ):
            raise ValidationError({"C_SP_dif": "Introdusca un valor válido."})
        if D_SP_dif and (D_SP_dif < 0 ):
            raise ValidationError({"D_SP_dif": "Introdusca un valor válido."})
        if E_SP_dif and (E_SP_dif < 0 ):
            raise ValidationError({"E_SP_dif": "Introdusca un valor válido."})
        if F_SP_dif and (F_SP_dif < 0 ):
            raise ValidationError({"F_SP_dif": "Introdusca un valor válido."})
        if G_SP_dif and (G_SP_dif < 0 ):
            raise ValidationError({"G_SP_dif": "Introdusca un valor válido."})
        if H_SP_dif and (H_SP_dif < 0 ):
            raise ValidationError({"H_SP_dif": "Introdusca un valor válido."})
        if I_SP_dif and (I_SP_dif < 0 ):
            raise ValidationError({"I_SP_dif": "Introdusca un valor válido."})
        if J_SP_dif and (J_SP_dif < 0 ):
            raise ValidationError({"J_SP_dif": "Introdusca un valor válido."})
        
        return cleaned_data
    

        
        
class NLF_Profecional_form(forms.ModelForm):
    

    
    class Meta:
        model = NLF_Profecional
        fields = ['equipo_local', 'equipo_visitante','fecha','A_ML_equip','A_ML_prob','A_SP_equip','A_SP_prob','A_SP_dif','A_Total_OU','A_Total_prob','A_Ud_equip','A_Ud_prob','A_SB_equip','A_SB_prob','A_MA','A_BB','A_total_punto',
                  'B_ML_equip','B_ML_prob','B_SP_equip','B_SP_prob','B_SP_dif','B_Total_OU','B_Total_prob','B_Ud_equip','B_Ud_prob','B_SB_equip','B_SB_prob','B_MA','B_BB','B_total_punto','A_MA_prob','B_MA_prob','C_MA_prob','D_MA_prob',
                  'C_ML_equip','C_ML_prob','C_SP_equip','C_SP_prob','C_SP_dif','C_Total_OU','C_Total_prob','C_Ud_equip','C_Ud_prob','C_SB_equip','C_SB_prob','C_MA','C_BB','C_total_punto','E_MA_prob','F_MA_prob','G_MA_prob','H_MA_prob',
                  'D_ML_equip','D_ML_prob','D_SP_equip','D_SP_prob','D_SP_dif','D_Total_OU','D_Total_prob','D_Ud_equip','D_Ud_prob','D_SB_equip','D_SB_prob','D_MA','D_BB','D_total_punto','I_MA_prob','J_MA_prob','A_BB_prob','B_BB_prob',
                  'E_ML_equip','E_ML_prob','E_SP_equip','E_SP_prob','E_SP_dif','E_Total_OU','E_Total_prob','E_Ud_equip','E_Ud_prob','E_SB_equip','E_SB_prob','E_MA','E_BB','E_total_punto','C_BB_prob','D_BB_prob','E_BB_prob','F_BB_prob',
                  'F_ML_equip','F_ML_prob','F_SP_equip','F_SP_prob','F_SP_dif','F_Total_OU','F_Total_prob','F_Ud_equip','F_Ud_prob','F_SB_equip','F_SB_prob','F_MA','F_BB','F_total_punto','G_BB_prob','H_BB_prob','I_BB_prob','J_BB_prob',
                  'G_ML_equip','G_ML_prob','G_SP_equip','G_SP_prob','G_SP_dif','G_Total_OU','G_Total_prob','G_Ud_equip','G_Ud_prob','G_SB_equip','G_SB_prob','G_MA','G_BB','G_total_punto',
                  'H_ML_equip','H_ML_prob','H_SP_equip','H_SP_prob','H_SP_dif','H_Total_OU','H_Total_prob','H_Ud_equip','H_Ud_prob','H_SB_equip','H_SB_prob','H_MA','H_BB','H_total_punto',
                  'I_ML_equip','I_ML_prob','I_SP_equip','I_SP_prob','I_SP_dif','I_Total_OU','I_Total_prob','I_Ud_equip','I_Ud_prob','I_SB_equip','I_SB_prob','I_MA','I_BB','I_total_punto',
                  'J_ML_equip','J_ML_prob','J_SP_equip','J_SP_prob','J_SP_dif','J_Total_OU','J_Total_prob','J_Ud_equip','J_Ud_prob','J_SB_equip','J_SB_prob','J_MA','J_BB','J_total_punto',
                  ]
        
        widgets = {
            
            'equipo_local': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'equipo_visitante': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control select-field', 'placeholder': '' }),
            'A_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visitante = cleaned_data.get('equipo_visitante')

       
        existing_partidos = NLF_Profecional.objects.filter(
            Q(fecha=fecha) &
            ~Q(id=self.instance.id) &  
            (
                Q(equipo_local=equipo_local) | 
                Q(equipo_visitante=equipo_visitante) 
            )
        )

        if existing_partidos.exists():
            raise ValidationError("Ya existe un partido con el mismo equipo programado para esta fecha.")

       
        if equipo_local.nombre == equipo_visitante.nombre:
           raise ValidationError("El equipo local y el equipo visitante no pueden ser el mismo.")     

    
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        J_ML_equip = cleaned_data.get('J_ML_equip')
        
        A_SP_equip = cleaned_data.get('A_SP_equip')
        A_SP_prob = cleaned_data.get('A_SP_prob')
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        J_SP_prob = cleaned_data.get('J_SP_prob')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        A_Total_OU = cleaned_data.get('A_Total_OU')
        A_Total_prob = cleaned_data.get('A_Total_prob')
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_OU = cleaned_data.get('B_Total_OU')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_OU = cleaned_data.get('C_Total_OU')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_OU = cleaned_data.get('D_Total_OU')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_OU = cleaned_data.get('E_Total_OU')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_OU = cleaned_data.get('F_Total_OU')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_OU = cleaned_data.get('G_Total_OU')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        G_Total_punto = cleaned_data.get('G_total_punto')
        H_Total_OU = cleaned_data.get('H_Total_OU')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_OU = cleaned_data.get('I_Total_OU')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_OU = cleaned_data.get('J_Total_OU')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        J_Total_punto = cleaned_data.get('J_total_punto')
       
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')
        
        A_SB_equip = cleaned_data.get('A_SB_equip')
        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_equip = cleaned_data.get('J_SB_equip')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
        A_MA= cleaned_data.get('A_MA')
        B_MA= cleaned_data.get('B_MA')
        C_MA= cleaned_data.get('C_MA')
        D_MA= cleaned_data.get('D_MA')
        E_MA= cleaned_data.get('E_MA')
        F_MA= cleaned_data.get('F_MA')
        G_MA= cleaned_data.get('G_MA')
        H_MA= cleaned_data.get('H_MA')
        I_MA= cleaned_data.get('I_MA')
        J_MA= cleaned_data.get('J_MA')
        
        A_MA_prob= cleaned_data.get('A_MA_prob')
        B_MA_prob= cleaned_data.get('B_MA_prob')
        C_MA_prob= cleaned_data.get('C_MA_prob')
        D_MA_prob= cleaned_data.get('D_MA_prob')
        E_MA_prob= cleaned_data.get('E_MA_prob')
        F_MA_prob= cleaned_data.get('F_MA_prob')
        G_MA_prob= cleaned_data.get('G_MA_prob')
        H_MA_prob= cleaned_data.get('H_MA_prob')
        I_MA_prob= cleaned_data.get('I_MA_prob')
        J_MA_prob= cleaned_data.get('J_MA_prob')
        
        
        A_BB= cleaned_data.get('A_BB')
        B_BB= cleaned_data.get('B_BB')
        C_BB= cleaned_data.get('C_BB')
        D_BB= cleaned_data.get('D_BB')
        E_BB= cleaned_data.get('E_BB')
        F_BB= cleaned_data.get('F_BB')
        G_BB= cleaned_data.get('G_BB')
        H_BB= cleaned_data.get('H_BB')
        I_BB= cleaned_data.get('I_BB')
        J_BB= cleaned_data.get('J_BB')
         
        A_BB_prob= cleaned_data.get('A_BB_prob')
        B_BB_prob= cleaned_data.get('B_BB_prob')
        C_BB_prob= cleaned_data.get('C_BB_prob')
        D_BB_prob= cleaned_data.get('D_BB_prob')
        E_BB_prob= cleaned_data.get('E_BB_prob')
        F_BB_prob= cleaned_data.get('F_BB_prob')
        G_BB_prob= cleaned_data.get('G_BB_prob')
        H_BB_prob= cleaned_data.get('H_BB_prob')
        I_BB_prob= cleaned_data.get('I_BB_prob')
        J_BB_prob= cleaned_data.get('J_BB_prob')

        
        # Realiza la validación personalizada
        if A_ML_prob or A_ML_equip:
            if not (A_ML_equip and A_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if B_ML_prob or B_ML_equip:
            if not (B_ML_equip and B_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if C_ML_prob or C_ML_equip:
            if not (C_ML_equip and C_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if D_ML_prob or D_ML_equip:
            if not (D_ML_equip and D_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if E_ML_prob or E_ML_equip:
            if not (E_ML_equip and E_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if F_ML_prob or F_ML_equip:
            if not (F_ML_equip and F_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if G_ML_prob or G_ML_equip:
            if not (G_ML_equip and G_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if H_ML_prob or H_ML_equip:
            if not (H_ML_equip and H_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if I_ML_prob or I_ML_equip:
            if not (I_ML_equip and I_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if J_ML_prob or J_ML_equip:
            if not (J_ML_equip and J_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        
        if A_SP_equip or A_SP_prob or A_SP_dif :
            if not (A_SP_equip and A_SP_prob and A_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if B_SP_equip or B_SP_prob or B_SP_dif :
            if not (B_SP_equip and B_SP_prob and B_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if C_SP_equip or C_SP_prob or C_SP_dif :
            if not (C_SP_equip and C_SP_prob and C_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if D_SP_equip or D_SP_prob or D_SP_dif :
            if not (D_SP_equip and D_SP_prob and D_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if E_SP_equip or E_SP_prob or E_SP_dif :
            if not (E_SP_equip and E_SP_prob and E_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if F_SP_equip or F_SP_prob or F_SP_dif :
            if not (F_SP_equip and F_SP_prob and F_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if G_SP_equip or G_SP_prob or G_SP_dif :
            if not (G_SP_equip and G_SP_prob and G_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if H_SP_equip or H_SP_prob or H_SP_dif :
            if not (H_SP_equip and H_SP_prob and H_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if I_SP_equip or I_SP_prob or I_SP_dif :
            if not (I_SP_equip and I_SP_prob and I_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if J_SP_equip or J_SP_prob or J_SP_dif :
            if not (J_SP_equip and J_SP_prob and J_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
  
       
        if A_Total_OU or A_Total_prob or A_Total_punto :
            if not (A_Total_OU and A_Total_prob and A_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if B_Total_OU or B_Total_prob or B_Total_punto :
            if not (B_Total_OU and B_Total_prob and B_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if C_Total_OU or C_Total_prob or C_Total_punto :
            if not (C_Total_OU and C_Total_prob and C_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if D_Total_OU or D_Total_prob or D_Total_punto :
            if not (D_Total_OU and D_Total_prob and D_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if E_Total_OU or E_Total_prob or E_Total_punto :
            if not (E_Total_OU and E_Total_prob and E_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if F_Total_OU or F_Total_prob or F_Total_punto :
            if not (F_Total_OU and F_Total_prob and F_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if G_Total_OU or G_Total_prob or G_Total_punto :
            if not (G_Total_OU and G_Total_prob and G_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if H_Total_OU or H_Total_prob or H_Total_punto :
            if not (H_Total_OU and H_Total_prob and H_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if I_Total_OU or I_Total_prob or I_Total_punto :
            if not (I_Total_OU and I_Total_prob and I_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if J_Total_OU or J_Total_prob or J_Total_punto :
            if not (J_Total_OU and J_Total_prob and J_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
      
        if A_Ud_equip or A_Ud_prob:
            if not (A_Ud_equip and A_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if B_Ud_equip or B_Ud_prob:
            if not (B_Ud_equip and B_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if C_Ud_equip or C_Ud_prob:
            if not (C_Ud_equip and C_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if D_Ud_equip or D_Ud_prob:
            if not (D_Ud_equip and D_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if E_Ud_equip or E_Ud_prob:
            if not (E_Ud_equip and E_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if F_Ud_equip or F_Ud_prob:
            if not (F_Ud_equip and F_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if G_Ud_equip or G_Ud_prob:
            if not (G_Ud_equip and G_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if H_Ud_equip or H_Ud_prob:
            if not (H_Ud_equip and H_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if I_Ud_equip or I_Ud_prob:
            if not (I_Ud_equip and I_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if J_Ud_equip or J_Ud_prob:
            if not (J_Ud_equip and J_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
       
        if A_SB_equip or A_SB_prob:
            if not (A_SB_equip and A_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if B_SB_equip or B_SB_prob:
            if not (B_SB_equip and B_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if C_SB_equip or C_SB_prob:
            if not (C_SB_equip and C_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if D_SB_equip or D_SB_prob:
            if not (D_SB_equip and D_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if E_SB_equip or E_SB_prob:
            if not (E_SB_equip and E_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if F_SB_equip or F_SB_prob:
            if not (F_SB_equip and F_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if G_SB_equip or G_SB_prob:
            if not (G_SB_equip and G_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if H_SB_equip or H_SB_prob:
            if not (H_SB_equip and H_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if I_SB_equip or I_SB_prob:
            if not (I_SB_equip and I_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if J_SB_equip or J_SB_prob:
            if not (J_SB_equip and J_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
       
        if A_MA or A_MA_prob:
            if not (A_MA and A_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if B_MA or B_MA_prob:
            if not (B_MA and B_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if C_MA or C_MA_prob:
            if not (C_MA and C_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if D_MA or D_MA_prob:
            if not (D_MA and D_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if E_MA or E_MA_prob:
            if not (E_MA and E_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if F_MA or F_MA_prob:
            if not (F_MA and F_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if G_MA or G_MA_prob:
            if not (G_MA and G_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if H_MA or H_MA_prob:
            if not (H_MA and H_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if I_MA or I_MA_prob:
            if not (I_MA and I_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if J_MA or J_MA_prob:
            if not (J_MA and J_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ") 
   
        
        if A_BB or A_BB_prob:
            if not (A_BB and A_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if B_BB or B_BB_prob:
            if not (B_BB and B_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if C_BB or C_BB_prob:
            if not (C_BB and C_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if D_BB or D_BB_prob:
            if not (D_BB and D_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if E_BB or E_BB_prob:
            if not (E_BB and E_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if F_BB or F_BB_prob:
            if not (F_BB and F_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if G_BB or G_BB_prob:
            if not (G_BB and G_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if H_BB or H_BB_prob:
            if not (H_BB and H_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if I_BB or I_BB_prob:
            if not (I_BB and I_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if J_BB or J_BB_prob:
            if not (J_BB and J_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        
       
       
       
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        
        A_SP_prob = cleaned_data.get('A_SP_prob')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        J_SP_prob = cleaned_data.get('J_SP_prob')

        A_Total_prob = cleaned_data.get('A_Total_prob')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')

        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
       
        if A_ML_prob and (A_ML_prob < 1 or A_ML_prob > 99):
            raise ValidationError({"A_ML_prob": "El valor de probabilidad debe estar entre 1 y 99."})
        if B_ML_prob and (B_ML_prob < 0 or B_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_ML_prob and (C_ML_prob < 0 or C_ML_prob > 99):
            raise ValidationError({"C_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_ML_prob and (D_ML_prob < 0 or D_ML_prob > 99):
            raise ValidationError({"D_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_ML_prob and (E_ML_prob < 0 or E_ML_prob > 99):
            raise ValidationError({"E_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_ML_prob and (F_ML_prob < 0 or F_ML_prob > 99):
            raise ValidationError({"F_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_ML_prob and (G_ML_prob < 0 or G_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_ML_prob and (H_ML_prob < 0 or H_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_ML_prob and (I_ML_prob < 0 or I_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_ML_prob and (J_ML_prob < 0 or J_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})


        if A_SP_prob and (A_SP_prob < 0 or A_SP_prob > 99):
            raise ValidationError({"A_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SP_prob and (B_SP_prob < 0 or B_SP_prob > 99):
            raise ValidationError({"B_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SP_prob and (C_SP_prob < 0 or C_SP_prob > 99):
            raise ValidationError({"C_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SP_prob and (D_SP_prob < 0 or D_SP_prob > 99):
            raise ValidationError({"D_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SP_prob and (E_SP_prob < 0 or E_SP_prob > 99):
            raise ValidationError({"E_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SP_prob and (F_SP_prob < 0 or F_SP_prob > 99):
            raise ValidationError({"F_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SP_prob and (G_SP_prob < 0 or G_SP_prob > 99):
            raise ValidationError({"G_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SP_prob and (H_SP_prob < 0 or H_SP_prob > 99):
            raise ValidationError({"H_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SP_prob and (I_SP_prob < 0 or I_SP_prob > 99):
            raise ValidationError({"I_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SP_prob and (J_SP_prob < 0 or J_SP_prob > 99):
            raise ValidationError({"J_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Total_prob and (A_Total_prob < 0 or A_Total_prob > 99):
            raise ValidationError({"A_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Total_prob and (B_Total_prob < 0 or B_Total_prob > 99):
            raise ValidationError({"B_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Total_prob and (C_Total_prob < 0 or C_Total_prob > 99):
            raise ValidationError({"C_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Total_prob and (D_Total_prob < 0 or D_Total_prob > 99):
            raise ValidationError({"D_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Total_prob and (E_Total_prob < 0 or E_Total_prob > 99):
            raise ValidationError({"E_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Total_prob and (F_Total_prob < 0 or F_Total_prob > 99):
            raise ValidationError({"F_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Total_prob and (G_Total_prob < 0 or G_Total_prob > 99):
            raise ValidationError({"G_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Total_prob and (H_Total_prob < 0 or H_Total_prob > 99):
            raise ValidationError({"H_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Total_prob and (I_Total_prob < 0 or I_Total_prob > 99):
            raise ValidationError({"I_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Total_prob and (J_Total_prob < 0 or J_Total_prob > 99):
            raise ValidationError({"J_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Ud_prob and (A_Ud_prob < 0 or A_Ud_prob > 99):
            raise ValidationError({"A_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Ud_prob and (B_Ud_prob < 0 or B_Ud_prob > 99):
            raise ValidationError({"B_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Ud_prob and (C_Ud_prob < 0 or C_Ud_prob > 99):
            raise ValidationError({"C_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Ud_prob and (D_Ud_prob < 0 or D_Ud_prob > 99):
            raise ValidationError({"D_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Ud_prob and (E_Ud_prob < 0 or E_Ud_prob > 99):
            raise ValidationError({"E_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Ud_prob and (F_Ud_prob < 0 or F_Ud_prob > 99):
            raise ValidationError({"F_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Ud_prob and (G_Ud_prob < 0 or G_Ud_prob > 99):
            raise ValidationError({"G_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Ud_prob and (H_Ud_prob < 0 or H_Ud_prob > 99):
            raise ValidationError({"H_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Ud_prob and (I_Ud_prob < 0 or I_Ud_prob > 99):
            raise ValidationError({"I_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Ud_prob and (J_Ud_prob < 0 or J_Ud_prob > 99):
            raise ValidationError({"J_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_SB_prob and (A_SB_prob < 0 or A_SB_prob > 99):
            raise ValidationError({"A_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SB_prob and (B_SB_prob < 0 or B_SB_prob > 99):
            raise ValidationError({"B_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SB_prob and (C_SB_prob < 0 or C_SB_prob > 99):
            raise ValidationError({"C_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SB_prob and (D_SB_prob < 0 or D_SB_prob > 99):
            raise ValidationError({"D_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SB_prob and (E_SB_prob < 0 or E_SB_prob > 99):
            raise ValidationError({"E_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SB_prob and (F_SB_prob < 0 or F_SB_prob > 99):
            raise ValidationError({"F_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SB_prob and (G_SB_prob < 0 or G_SB_prob > 99):
            raise ValidationError({"G_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SB_prob and (H_SB_prob < 0 or H_SB_prob > 99):
            raise ValidationError({"H_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SB_prob and (I_SB_prob < 0 or I_SB_prob > 99):
            raise ValidationError({"I_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SB_prob and (J_SB_prob < 0 or J_SB_prob > 99):
            raise ValidationError({"J_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
          
        if A_MA_prob and (A_MA_prob < 0 or A_MA_prob > 99):
            raise ValidationError({"A_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_MA_prob and (B_MA_prob < 0 or B_MA_prob > 99):
            raise ValidationError({"B_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if C_MA_prob and (C_MA_prob < 0 or C_MA_prob > 99):
            raise ValidationError({"C_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if D_MA_prob and (D_MA_prob < 0 or D_MA_prob > 99):
            raise ValidationError({"D_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if E_MA_prob and (E_MA_prob < 0 or E_MA_prob > 99):
            raise ValidationError({"E_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_MA_prob and (F_MA_prob < 0 or F_MA_prob > 99):
            raise ValidationError({"F_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_MA_prob and (G_MA_prob < 0 or G_MA_prob > 99):
            raise ValidationError({"G_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_MA_prob and (H_MA_prob < 0 or H_MA_prob > 99):
            raise ValidationError({"H_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_MA_prob and (I_MA_prob < 0 or I_MA_prob > 99):
            raise ValidationError({"I_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_MA_prob and (J_MA_prob < 0 or J_MA_prob > 99):
            raise ValidationError({"J_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        if A_BB_prob and (A_BB_prob < 0 or A_BB_prob > 99):
            raise ValidationError({"A_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_BB_prob and (B_BB_prob < 0 or B_BB_prob > 99):
            raise ValidationError({"B_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_BB_prob and (C_BB_prob < 0 or C_BB_prob > 99):
            raise ValidationError({"C_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_BB_prob and (D_BB_prob < 0 or D_BB_prob > 99):
            raise ValidationError({"D_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_BB_prob and (E_BB_prob < 0 or E_BB_prob > 99):
            raise ValidationError({"E_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_BB_prob and (F_BB_prob < 0 or F_BB_prob > 99):
            raise ValidationError({"F_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_BB_prob and (G_BB_prob < 0 or G_BB_prob > 99):
            raise ValidationError({"G_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_BB_prob and (H_BB_prob < 0 or H_BB_prob > 99):
            raise ValidationError({"H_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_BB_prob and (I_BB_prob < 0 or I_BB_prob > 99):
            raise ValidationError({"I_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_BB_prob and (J_BB_prob < 0 or J_BB_prob > 99):
            raise ValidationError({"J_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_equip = cleaned_data.get('J_ML_equip')

        A_SP_equip = cleaned_data.get('A_SP_equip')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
       
        A_SB_equip = cleaned_data.get('A_SB_equip')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        J_SB_equip = cleaned_data.get('J_SB_equip')
       
        A_MA = cleaned_data.get('A_MA')
        B_MA = cleaned_data.get('B_MA')
        C_MA = cleaned_data.get('C_MA')
        D_MA = cleaned_data.get('D_MA')
        E_MA = cleaned_data.get('E_MA')
        F_MA = cleaned_data.get('F_MA')
        G_MA = cleaned_data.get('G_MA')
        H_MA = cleaned_data.get('H_MA')
        I_MA = cleaned_data.get('I_MA')
        J_MA = cleaned_data.get('J_MA')

        A_BB = cleaned_data.get('A_BB')
        B_BB = cleaned_data.get('B_BB')
        C_BB = cleaned_data.get('C_BB')
        D_BB = cleaned_data.get('D_BB')
        E_BB = cleaned_data.get('E_BB')
        F_BB = cleaned_data.get('F_BB')
        G_BB = cleaned_data.get('G_BB')
        H_BB = cleaned_data.get('H_BB')
        I_BB = cleaned_data.get('I_BB')
        J_BB = cleaned_data.get('J_BB')
        
        
              
        # Validación para ganador
        if A_ML_equip and (A_ML_equip != equipo_local and A_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})
        if B_ML_equip and (B_ML_equip != equipo_local and B_ML_equip != equipo_visitante):
            raise ValidationError({"B_ML_equip": "Debes elegir un equipo válido."})
        if C_ML_equip and (C_ML_equip != equipo_local and C_ML_equip != equipo_visitante):
            raise ValidationError({"C_ML_equip": "Debes elegir un equipo válido."})
        if D_ML_equip and (D_ML_equip != equipo_local and D_ML_equip != equipo_visitante):
            raise ValidationError({"D_ML_equip": "Debes elegir un equipo válido."})
        if E_ML_equip and (E_ML_equip != equipo_local and E_ML_equip != equipo_visitante):
            raise ValidationError({"E_ML_equip": "Debes elegir un equipo válido."})
        if F_ML_equip and (F_ML_equip != equipo_local and F_ML_equip != equipo_visitante):
            raise ValidationError({"F_ML_equip": "Debes elegir un equipo válido."})
        if G_ML_equip and (G_ML_equip != equipo_local and G_ML_equip != equipo_visitante):
            raise ValidationError({"G_ML_equip": "Debes elegir un equipo válido."})
        if H_ML_equip and (H_ML_equip != equipo_local and H_ML_equip != equipo_visitante):
            raise ValidationError({"H_ML_equip": "Debes elegir un equipo válido."})
        if I_ML_equip and (I_ML_equip != equipo_local and I_ML_equip != equipo_visitante):
            raise ValidationError({"I_ML_equip": "Debes elegir un equipo válido."})
        if J_ML_equip and (J_ML_equip != equipo_local and J_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})

        if A_SP_equip and (A_SP_equip != equipo_local and A_SP_equip != equipo_visitante):
            raise ValidationError({"A_SP_equip": "Debes elegir un equipo válido."})
        if B_SP_equip and (B_SP_equip != equipo_local and B_SP_equip != equipo_visitante):
            raise ValidationError({"B_SP_equip": "Debes elegir un equipo válido."})
        if C_SP_equip and (C_SP_equip != equipo_local and C_SP_equip != equipo_visitante):
            raise ValidationError({"C_SP_equip": "Debes elegir un equipo válido."})
        if D_SP_equip and (D_SP_equip != equipo_local and D_SP_equip != equipo_visitante):
            raise ValidationError({"D_SP_equip": "Debes elegir un equipo válido."})
        if E_SP_equip and (E_SP_equip != equipo_local and E_SP_equip != equipo_visitante):
            raise ValidationError({"E_SP_equip": "Debes elegir un equipo válido."})
        if F_SP_equip and (F_SP_equip != equipo_local and F_SP_equip != equipo_visitante):
            raise ValidationError({"F_SP_equip": "Debes elegir un equipo válido."})
        if G_SP_equip and (G_SP_equip != equipo_local and G_SP_equip != equipo_visitante):
            raise ValidationError({"G_SP_equip": "Debes elegir un equipo válido."})
        if H_SP_equip and (H_SP_equip != equipo_local and H_SP_equip != equipo_visitante):
            raise ValidationError({"H_SP_equip": "Debes elegir un equipo válido."})
        if I_SP_equip and (I_SP_equip != equipo_local and I_SP_equip != equipo_visitante):
            raise ValidationError({"I_SP_equip": "Debes elegir un equipo válido."})
        if J_SP_equip and (J_SP_equip != equipo_local and J_SP_equip != equipo_visitante):
            raise ValidationError({"J_SP_equip": "Debes elegir un equipo válido."})
        
        if A_Ud_equip and (A_Ud_equip != equipo_local and A_Ud_equip != equipo_visitante):
            raise ValidationError({"A_Ud_equip": "Debes elegir un equipo válido."})
        if B_Ud_equip and (B_Ud_equip != equipo_local and B_Ud_equip != equipo_visitante):
            raise ValidationError({"B_Ud_equip": "Debes elegir un equipo válido."})
        if C_Ud_equip and (C_Ud_equip != equipo_local and C_Ud_equip != equipo_visitante):
            raise ValidationError({"C_Ud_equip": "Debes elegir un equipo válido."})
        if D_Ud_equip and (D_Ud_equip != equipo_local and D_Ud_equip != equipo_visitante):
            raise ValidationError({"D_Ud_equip": "Debes elegir un equipo válido."})
        if E_Ud_equip and (E_Ud_equip != equipo_local and E_Ud_equip != equipo_visitante):
            raise ValidationError({"E_Ud_equip": "Debes elegir un equipo válido."})
        if F_Ud_equip and (F_Ud_equip != equipo_local and F_Ud_equip != equipo_visitante):
            raise ValidationError({"F_Ud_equip": "Debes elegir un equipo válido."})
        if G_Ud_equip and (G_Ud_equip != equipo_local and G_Ud_equip != equipo_visitante):
            raise ValidationError({"G_Ud_equip": "Debes elegir un equipo válido."})
        if H_Ud_equip and (H_Ud_equip != equipo_local and H_Ud_equip != equipo_visitante):
            raise ValidationError({"H_Ud_equip": "Debes elegir un equipo válido."})
        if I_Ud_equip and (I_Ud_equip != equipo_local and I_Ud_equip != equipo_visitante):
            raise ValidationError({"I_Ud_equip": "Debes elegir un equipo válido."})
        if J_Ud_equip and (J_Ud_equip != equipo_local and J_Ud_equip != equipo_visitante):
            raise ValidationError({"J_Ud_equip": "Debes elegir un equipo válido."})
        
        if A_SB_equip and (A_SB_equip != equipo_local and A_SB_equip != equipo_visitante):
            raise ValidationError({"A_SB_equip": "Debes elegir un equipo válido."})
        if B_SB_equip and (B_SB_equip != equipo_local and B_SB_equip != equipo_visitante):
            raise ValidationError({"B_SB_equip": "Debes elegir un equipo válido."})
        if C_SB_equip and (C_SB_equip != equipo_local and C_SB_equip != equipo_visitante):
            raise ValidationError({"C_SB_equip": "Debes elegir un equipo válido."})
        if D_SB_equip and (D_SB_equip != equipo_local and D_SB_equip != equipo_visitante):
            raise ValidationError({"D_SB_equip": "Debes elegir un equipo válido."})
        if E_SB_equip and (E_SB_equip != equipo_local and E_SB_equip != equipo_visitante):
            raise ValidationError({"E_SB_equip": "Debes elegir un equipo válido."})
        if F_SB_equip and (F_SB_equip != equipo_local and F_SB_equip != equipo_visitante):
            raise ValidationError({"F_SB_equip": "Debes elegir un equipo válido."})
        if G_SB_equip and (G_SB_equip != equipo_local and G_SB_equip != equipo_visitante):
            raise ValidationError({"G_SB_equip": "Debes elegir un equipo válido."})
        if H_SB_equip and (H_SB_equip != equipo_local and H_SB_equip != equipo_visitante):
            raise ValidationError({"H_SB_equip": "Debes elegir un equipo válido."})
        if I_SB_equip and (I_SB_equip != equipo_local and I_SB_equip != equipo_visitante):
            raise ValidationError({"I_SB_equip": "Debes elegir un equipo válido."})
        if J_SB_equip and (J_SB_equip != equipo_local and J_SB_equip != equipo_visitante):
            raise ValidationError({"J_SB_equip": "Debes elegir un equipo válido."})
        
        if A_MA and (A_MA != equipo_local and A_MA != equipo_visitante):
            raise ValidationError({"A_MA": "Debes elegir un equipo válido."})
        if B_MA and (B_MA != equipo_local and B_MA != equipo_visitante):
            raise ValidationError({"B_MA": "Debes elegir un equipo válido."})
        if C_MA and (C_MA != equipo_local and C_MA != equipo_visitante):
            raise ValidationError({"C_MA": "Debes elegir un equipo válido."})
        if D_MA and (D_MA != equipo_local and D_MA != equipo_visitante):
            raise ValidationError({"D_MA": "Debes elegir un equipo válido."})
        if E_MA and (E_MA != equipo_local and E_MA != equipo_visitante):
            raise ValidationError({"E_MA": "Debes elegir un equipo válido."})
        if F_MA and (F_MA != equipo_local and F_MA != equipo_visitante):
            raise ValidationError({"F_MA": "Debes elegir un equipo válido."})
        if G_MA and (G_MA != equipo_local and G_MA != equipo_visitante):
            raise ValidationError({"G_MA": "Debes elegir un equipo válido."})
        if H_MA and (H_MA != equipo_local and H_MA != equipo_visitante):
            raise ValidationError({"H_MA": "Debes elegir un equipo válido."})
        if I_MA and (I_MA != equipo_local and I_MA != equipo_visitante):
            raise ValidationError({"I_MA": "Debes elegir un equipo válido."})
        if J_MA and (J_MA != equipo_local and J_MA != equipo_visitante):
            raise ValidationError({"J_MA": "Debes elegir un equipo válido."})
        
        if A_BB and (A_BB != equipo_local and A_BB != equipo_visitante):
            raise ValidationError({"A_BB": "Debes elegir un equipo válido."})
        if B_BB and (B_BB != equipo_local and B_BB != equipo_visitante):
            raise ValidationError({"B_BB": "Debes elegir un equipo válido."})
        if C_BB and (C_BB != equipo_local and C_BB != equipo_visitante):
            raise ValidationError({"C_BB": "Debes elegir un equipo válido."})
        if D_BB and (D_BB != equipo_local and D_BB != equipo_visitante):
            raise ValidationError({"D_BB": "Debes elegir un equipo válido."})
        if E_BB and (E_BB != equipo_local and E_BB != equipo_visitante):
            raise ValidationError({"E_BB": "Debes elegir un equipo válido."})
        if F_BB and (F_BB != equipo_local and F_BB != equipo_visitante):
            raise ValidationError({"F_BB": "Debes elegir un equipo válido."})
        if G_BB and (G_BB != equipo_local and G_BB != equipo_visitante):
            raise ValidationError({"G_BB": "Debes elegir un equipo válido."})
        if H_BB and (H_BB != equipo_local and H_BB != equipo_visitante):
            raise ValidationError({"H_BB": "Debes elegir un equipo válido."})
        if I_BB and (I_BB != equipo_local and I_BB != equipo_visitante):
            raise ValidationError({"I_BB": "Debes elegir un equipo válido."})
        if J_BB and (J_BB != equipo_local and J_BB != equipo_visitante):
            raise ValidationError({"J_BB": "Debes elegir un equipo válido."})
         

        
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_punto = cleaned_data.get('G_total_punto')     
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_punto = cleaned_data.get('J_total_punto')
        
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        
        if A_Total_punto and (A_Total_punto < 0 ):
            raise ValidationError({"A_Total_punto": "Introdusca un valor válido."})
        if B_Total_punto and (B_Total_punto < 0 ):
            raise ValidationError({"B_Total_punto": "Introdusca un valor válido."})
        if C_Total_punto and (C_Total_punto < 0 ):
            raise ValidationError({"C_Total_punto": "Introdusca un valor válido."})
        if D_Total_punto and (D_Total_punto < 0 ):
            raise ValidationError({"D_Total_punto": "Introdusca un valor válido."})
        if E_Total_punto and (E_Total_punto < 0 ):
            raise ValidationError({"E_Total_punto": "Introdusca un valor válido."})
        if F_Total_punto and (F_Total_punto < 0 ):
            raise ValidationError({"F_Total_punto": "Introdusca un valor válido."})
        if G_Total_punto and (G_Total_punto < 0 ):
            raise ValidationError({"G_Total_punto": "Introdusca un valor válido."})
        if H_Total_punto and (H_Total_punto < 0 ):
            raise ValidationError({"H_Total_punto": "Introdusca un valor válido."})
        if I_Total_punto and (I_Total_punto < 0 ):
            raise ValidationError({"I_Total_punto": "Introdusca un valor válido."})
        if J_Total_punto and (J_Total_punto < 0 ):
            raise ValidationError({"J_Total_punto": "Introdusca un valor válido."})
        
        if A_SP_dif and (A_SP_dif < 0 ):
            raise ValidationError({"A_SP_dif": "Introdusca un valor válido."})
        if B_SP_dif and (B_SP_dif < 0 ):
            raise ValidationError({"B_SP_dif": "Introdusca un valor válido."})
        if C_SP_dif and (C_SP_dif < 0 ):
            raise ValidationError({"C_SP_dif": "Introdusca un valor válido."})
        if D_SP_dif and (D_SP_dif < 0 ):
            raise ValidationError({"D_SP_dif": "Introdusca un valor válido."})
        if E_SP_dif and (E_SP_dif < 0 ):
            raise ValidationError({"E_SP_dif": "Introdusca un valor válido."})
        if F_SP_dif and (F_SP_dif < 0 ):
            raise ValidationError({"F_SP_dif": "Introdusca un valor válido."})
        if G_SP_dif and (G_SP_dif < 0 ):
            raise ValidationError({"G_SP_dif": "Introdusca un valor válido."})
        if H_SP_dif and (H_SP_dif < 0 ):
            raise ValidationError({"H_SP_dif": "Introdusca un valor válido."})
        if I_SP_dif and (I_SP_dif < 0 ):
            raise ValidationError({"I_SP_dif": "Introdusca un valor válido."})
        if J_SP_dif and (J_SP_dif < 0 ):
            raise ValidationError({"J_SP_dif": "Introdusca un valor válido."})
        
        return cleaned_data
    
        
        
        
        
        
class NLF_Colegial_form(forms.ModelForm):
    
    equipo_local = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    equipo_visitante = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    A_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    B_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    B_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    C_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    C_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    D_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    D_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    E_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    E_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    F_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    F_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    G_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    G_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    H_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    H_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    I_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    I_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    J_ML_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),  widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_SP_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_Ud_equip = forms.ModelChoiceField( queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_SB_equip = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_MA = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    J_BB = forms.ModelChoiceField(queryset=equipos_NLF_colegial.objects.all().order_by('nombre'),   widget=forms.Select(attrs={'class':'form-control', 'placeholder': '' }),required=False)
    
    
    class Meta:
        model = NLF_Colegial
        fields = ['equipo_local', 'equipo_visitante','fecha','A_ML_equip','A_ML_prob','A_SP_equip','A_SP_prob','A_SP_dif','A_Total_OU','A_Total_prob','A_Ud_equip','A_Ud_prob','A_SB_equip','A_SB_prob','A_MA','A_BB','A_total_punto',
                  'B_ML_equip','B_ML_prob','B_SP_equip','B_SP_prob','B_SP_dif','B_Total_OU','B_Total_prob','B_Ud_equip','B_Ud_prob','B_SB_equip','B_SB_prob','B_MA','B_BB','B_total_punto','A_MA_prob','B_MA_prob','C_MA_prob','D_MA_prob',
                  'C_ML_equip','C_ML_prob','C_SP_equip','C_SP_prob','C_SP_dif','C_Total_OU','C_Total_prob','C_Ud_equip','C_Ud_prob','C_SB_equip','C_SB_prob','C_MA','C_BB','C_total_punto','E_MA_prob','F_MA_prob','G_MA_prob','H_MA_prob',
                  'D_ML_equip','D_ML_prob','D_SP_equip','D_SP_prob','D_SP_dif','D_Total_OU','D_Total_prob','D_Ud_equip','D_Ud_prob','D_SB_equip','D_SB_prob','D_MA','D_BB','D_total_punto','I_MA_prob','J_MA_prob','A_BB_prob','B_BB_prob',
                  'E_ML_equip','E_ML_prob','E_SP_equip','E_SP_prob','E_SP_dif','E_Total_OU','E_Total_prob','E_Ud_equip','E_Ud_prob','E_SB_equip','E_SB_prob','E_MA','E_BB','E_total_punto','C_BB_prob','D_BB_prob','E_BB_prob','F_BB_prob',
                  'F_ML_equip','F_ML_prob','F_SP_equip','F_SP_prob','F_SP_dif','F_Total_OU','F_Total_prob','F_Ud_equip','F_Ud_prob','F_SB_equip','F_SB_prob','F_MA','F_BB','F_total_punto','G_BB_prob','H_BB_prob','I_BB_prob','J_BB_prob',
                  'G_ML_equip','G_ML_prob','G_SP_equip','G_SP_prob','G_SP_dif','G_Total_OU','G_Total_prob','G_Ud_equip','G_Ud_prob','G_SB_equip','G_SB_prob','G_MA','G_BB','G_total_punto',
                  'H_ML_equip','H_ML_prob','H_SP_equip','H_SP_prob','H_SP_dif','H_Total_OU','H_Total_prob','H_Ud_equip','H_Ud_prob','H_SB_equip','H_SB_prob','H_MA','H_BB','H_total_punto',
                  'I_ML_equip','I_ML_prob','I_SP_equip','I_SP_prob','I_SP_dif','I_Total_OU','I_Total_prob','I_Ud_equip','I_Ud_prob','I_SB_equip','I_SB_prob','I_MA','I_BB','I_total_punto',
                  'J_ML_equip','J_ML_prob','J_SP_equip','J_SP_prob','J_SP_dif','J_Total_OU','J_Total_prob','J_Ud_equip','J_Ud_prob','J_SB_equip','J_SB_prob','J_MA','J_BB','J_total_punto',
                  ]
        
        widgets = {
            
            'equipo_local': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'equipo_visitante': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control select-field', 'placeholder': '' }),
            'A_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visitante = cleaned_data.get('equipo_visitante')

       
        existing_partidos = NLF_Colegial.objects.filter(
            Q(fecha=fecha) &
            ~Q(id=self.instance.id) &  
            (
                Q(equipo_local=equipo_local) | 
                Q(equipo_visitante=equipo_visitante) 
            )
        )

        if existing_partidos.exists():
            raise ValidationError("Ya existe un partido con el mismo equipo programado para esta fecha.")

       
        if equipo_local.nombre == equipo_visitante.nombre:
           raise ValidationError("El equipo local y el equipo visitante no pueden ser el mismo.")     

    
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        J_ML_equip = cleaned_data.get('J_ML_equip')
        
        A_SP_equip = cleaned_data.get('A_SP_equip')
        A_SP_prob = cleaned_data.get('A_SP_prob')
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        J_SP_prob = cleaned_data.get('J_SP_prob')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        A_Total_OU = cleaned_data.get('A_Total_OU')
        A_Total_prob = cleaned_data.get('A_Total_prob')
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_OU = cleaned_data.get('B_Total_OU')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_OU = cleaned_data.get('C_Total_OU')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_OU = cleaned_data.get('D_Total_OU')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_OU = cleaned_data.get('E_Total_OU')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_OU = cleaned_data.get('F_Total_OU')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_OU = cleaned_data.get('G_Total_OU')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        G_Total_punto = cleaned_data.get('G_total_punto')
        H_Total_OU = cleaned_data.get('H_Total_OU')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_OU = cleaned_data.get('I_Total_OU')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_OU = cleaned_data.get('J_Total_OU')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        J_Total_punto = cleaned_data.get('J_total_punto')
       
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')
        
        A_SB_equip = cleaned_data.get('A_SB_equip')
        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_equip = cleaned_data.get('J_SB_equip')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
        A_MA= cleaned_data.get('A_MA')
        B_MA= cleaned_data.get('B_MA')
        C_MA= cleaned_data.get('C_MA')
        D_MA= cleaned_data.get('D_MA')
        E_MA= cleaned_data.get('E_MA')
        F_MA= cleaned_data.get('F_MA')
        G_MA= cleaned_data.get('G_MA')
        H_MA= cleaned_data.get('H_MA')
        I_MA= cleaned_data.get('I_MA')
        J_MA= cleaned_data.get('J_MA')
        
        A_MA_prob= cleaned_data.get('A_MA_prob')
        B_MA_prob= cleaned_data.get('B_MA_prob')
        C_MA_prob= cleaned_data.get('C_MA_prob')
        D_MA_prob= cleaned_data.get('D_MA_prob')
        E_MA_prob= cleaned_data.get('E_MA_prob')
        F_MA_prob= cleaned_data.get('F_MA_prob')
        G_MA_prob= cleaned_data.get('G_MA_prob')
        H_MA_prob= cleaned_data.get('H_MA_prob')
        I_MA_prob= cleaned_data.get('I_MA_prob')
        J_MA_prob= cleaned_data.get('J_MA_prob')
        
        
        A_BB= cleaned_data.get('A_BB')
        B_BB= cleaned_data.get('B_BB')
        C_BB= cleaned_data.get('C_BB')
        D_BB= cleaned_data.get('D_BB')
        E_BB= cleaned_data.get('E_BB')
        F_BB= cleaned_data.get('F_BB')
        G_BB= cleaned_data.get('G_BB')
        H_BB= cleaned_data.get('H_BB')
        I_BB= cleaned_data.get('I_BB')
        J_BB= cleaned_data.get('J_BB')
         
        A_BB_prob= cleaned_data.get('A_BB_prob')
        B_BB_prob= cleaned_data.get('B_BB_prob')
        C_BB_prob= cleaned_data.get('C_BB_prob')
        D_BB_prob= cleaned_data.get('D_BB_prob')
        E_BB_prob= cleaned_data.get('E_BB_prob')
        F_BB_prob= cleaned_data.get('F_BB_prob')
        G_BB_prob= cleaned_data.get('G_BB_prob')
        H_BB_prob= cleaned_data.get('H_BB_prob')
        I_BB_prob= cleaned_data.get('I_BB_prob')
        J_BB_prob= cleaned_data.get('J_BB_prob')

        
        # Realiza la validación personalizada
        if A_ML_prob or A_ML_equip:
            if not (A_ML_equip and A_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if B_ML_prob or B_ML_equip:
            if not (B_ML_equip and B_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if C_ML_prob or C_ML_equip:
            if not (C_ML_equip and C_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if D_ML_prob or D_ML_equip:
            if not (D_ML_equip and D_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if E_ML_prob or E_ML_equip:
            if not (E_ML_equip and E_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if F_ML_prob or F_ML_equip:
            if not (F_ML_equip and F_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if G_ML_prob or G_ML_equip:
            if not (G_ML_equip and G_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if H_ML_prob or H_ML_equip:
            if not (H_ML_equip and H_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if I_ML_prob or I_ML_equip:
            if not (I_ML_equip and I_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if J_ML_prob or J_ML_equip:
            if not (J_ML_equip and J_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        
        if A_SP_equip or A_SP_prob or A_SP_dif :
            if not (A_SP_equip and A_SP_prob and A_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if B_SP_equip or B_SP_prob or B_SP_dif :
            if not (B_SP_equip and B_SP_prob and B_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if C_SP_equip or C_SP_prob or C_SP_dif :
            if not (C_SP_equip and C_SP_prob and C_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if D_SP_equip or D_SP_prob or D_SP_dif :
            if not (D_SP_equip and D_SP_prob and D_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if E_SP_equip or E_SP_prob or E_SP_dif :
            if not (E_SP_equip and E_SP_prob and E_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if F_SP_equip or F_SP_prob or F_SP_dif :
            if not (F_SP_equip and F_SP_prob and F_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if G_SP_equip or G_SP_prob or G_SP_dif :
            if not (G_SP_equip and G_SP_prob and G_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if H_SP_equip or H_SP_prob or H_SP_dif :
            if not (H_SP_equip and H_SP_prob and H_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if I_SP_equip or I_SP_prob or I_SP_dif :
            if not (I_SP_equip and I_SP_prob and I_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if J_SP_equip or J_SP_prob or J_SP_dif :
            if not (J_SP_equip and J_SP_prob and J_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
  
       
        if A_Total_OU or A_Total_prob or A_Total_punto :
            if not (A_Total_OU and A_Total_prob and A_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if B_Total_OU or B_Total_prob or B_Total_punto :
            if not (B_Total_OU and B_Total_prob and B_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if C_Total_OU or C_Total_prob or C_Total_punto :
            if not (C_Total_OU and C_Total_prob and C_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if D_Total_OU or D_Total_prob or D_Total_punto :
            if not (D_Total_OU and D_Total_prob and D_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if E_Total_OU or E_Total_prob or E_Total_punto :
            if not (E_Total_OU and E_Total_prob and E_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if F_Total_OU or F_Total_prob or F_Total_punto :
            if not (F_Total_OU and F_Total_prob and F_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if G_Total_OU or G_Total_prob or G_Total_punto :
            if not (G_Total_OU and G_Total_prob and G_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if H_Total_OU or H_Total_prob or H_Total_punto :
            if not (H_Total_OU and H_Total_prob and H_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if I_Total_OU or I_Total_prob or I_Total_punto :
            if not (I_Total_OU and I_Total_prob and I_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if J_Total_OU or J_Total_prob or J_Total_punto :
            if not (J_Total_OU and J_Total_prob and J_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
      
        if A_Ud_equip or A_Ud_prob:
            if not (A_Ud_equip and A_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if B_Ud_equip or B_Ud_prob:
            if not (B_Ud_equip and B_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if C_Ud_equip or C_Ud_prob:
            if not (C_Ud_equip and C_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if D_Ud_equip or D_Ud_prob:
            if not (D_Ud_equip and D_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if E_Ud_equip or E_Ud_prob:
            if not (E_Ud_equip and E_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if F_Ud_equip or F_Ud_prob:
            if not (F_Ud_equip and F_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if G_Ud_equip or G_Ud_prob:
            if not (G_Ud_equip and G_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if H_Ud_equip or H_Ud_prob:
            if not (H_Ud_equip and H_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if I_Ud_equip or I_Ud_prob:
            if not (I_Ud_equip and I_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if J_Ud_equip or J_Ud_prob:
            if not (J_Ud_equip and J_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
       
        if A_SB_equip or A_SB_prob:
            if not (A_SB_equip and A_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if B_SB_equip or B_SB_prob:
            if not (B_SB_equip and B_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if C_SB_equip or C_SB_prob:
            if not (C_SB_equip and C_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if D_SB_equip or D_SB_prob:
            if not (D_SB_equip and D_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if E_SB_equip or E_SB_prob:
            if not (E_SB_equip and E_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if F_SB_equip or F_SB_prob:
            if not (F_SB_equip and F_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if G_SB_equip or G_SB_prob:
            if not (G_SB_equip and G_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if H_SB_equip or H_SB_prob:
            if not (H_SB_equip and H_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if I_SB_equip or I_SB_prob:
            if not (I_SB_equip and I_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if J_SB_equip or J_SB_prob:
            if not (J_SB_equip and J_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
       
        if A_MA or A_MA_prob:
            if not (A_MA and A_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if B_MA or B_MA_prob:
            if not (B_MA and B_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if C_MA or C_MA_prob:
            if not (C_MA and C_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if D_MA or D_MA_prob:
            if not (D_MA and D_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if E_MA or E_MA_prob:
            if not (E_MA and E_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if F_MA or F_MA_prob:
            if not (F_MA and F_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if G_MA or G_MA_prob:
            if not (G_MA and G_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if H_MA or H_MA_prob:
            if not (H_MA and H_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if I_MA or I_MA_prob:
            if not (I_MA and I_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if J_MA or J_MA_prob:
            if not (J_MA and J_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ") 
   
        
        if A_BB or A_BB_prob:
            if not (A_BB and A_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if B_BB or B_BB_prob:
            if not (B_BB and B_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if C_BB or C_BB_prob:
            if not (C_BB and C_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if D_BB or D_BB_prob:
            if not (D_BB and D_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if E_BB or E_BB_prob:
            if not (E_BB and E_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if F_BB or F_BB_prob:
            if not (F_BB and F_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if G_BB or G_BB_prob:
            if not (G_BB and G_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if H_BB or H_BB_prob:
            if not (H_BB and H_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if I_BB or I_BB_prob:
            if not (I_BB and I_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if J_BB or J_BB_prob:
            if not (J_BB and J_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        
       
       
       
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        
        A_SP_prob = cleaned_data.get('A_SP_prob')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        J_SP_prob = cleaned_data.get('J_SP_prob')

        A_Total_prob = cleaned_data.get('A_Total_prob')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')

        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
       
        if A_ML_prob and (A_ML_prob < 1 or A_ML_prob > 99):
            raise ValidationError({"A_ML_prob": "El valor de probabilidad debe estar entre 1 y 99."})
        if B_ML_prob and (B_ML_prob < 0 or B_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_ML_prob and (C_ML_prob < 0 or C_ML_prob > 99):
            raise ValidationError({"C_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_ML_prob and (D_ML_prob < 0 or D_ML_prob > 99):
            raise ValidationError({"D_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_ML_prob and (E_ML_prob < 0 or E_ML_prob > 99):
            raise ValidationError({"E_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_ML_prob and (F_ML_prob < 0 or F_ML_prob > 99):
            raise ValidationError({"F_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_ML_prob and (G_ML_prob < 0 or G_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_ML_prob and (H_ML_prob < 0 or H_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_ML_prob and (I_ML_prob < 0 or I_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_ML_prob and (J_ML_prob < 0 or J_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})


        if A_SP_prob and (A_SP_prob < 0 or A_SP_prob > 99):
            raise ValidationError({"A_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SP_prob and (B_SP_prob < 0 or B_SP_prob > 99):
            raise ValidationError({"B_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SP_prob and (C_SP_prob < 0 or C_SP_prob > 99):
            raise ValidationError({"C_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SP_prob and (D_SP_prob < 0 or D_SP_prob > 99):
            raise ValidationError({"D_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SP_prob and (E_SP_prob < 0 or E_SP_prob > 99):
            raise ValidationError({"E_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SP_prob and (F_SP_prob < 0 or F_SP_prob > 99):
            raise ValidationError({"F_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SP_prob and (G_SP_prob < 0 or G_SP_prob > 99):
            raise ValidationError({"G_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SP_prob and (H_SP_prob < 0 or H_SP_prob > 99):
            raise ValidationError({"H_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SP_prob and (I_SP_prob < 0 or I_SP_prob > 99):
            raise ValidationError({"I_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SP_prob and (J_SP_prob < 0 or J_SP_prob > 99):
            raise ValidationError({"J_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Total_prob and (A_Total_prob < 0 or A_Total_prob > 99):
            raise ValidationError({"A_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Total_prob and (B_Total_prob < 0 or B_Total_prob > 99):
            raise ValidationError({"B_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Total_prob and (C_Total_prob < 0 or C_Total_prob > 99):
            raise ValidationError({"C_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Total_prob and (D_Total_prob < 0 or D_Total_prob > 99):
            raise ValidationError({"D_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Total_prob and (E_Total_prob < 0 or E_Total_prob > 99):
            raise ValidationError({"E_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Total_prob and (F_Total_prob < 0 or F_Total_prob > 99):
            raise ValidationError({"F_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Total_prob and (G_Total_prob < 0 or G_Total_prob > 99):
            raise ValidationError({"G_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Total_prob and (H_Total_prob < 0 or H_Total_prob > 99):
            raise ValidationError({"H_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Total_prob and (I_Total_prob < 0 or I_Total_prob > 99):
            raise ValidationError({"I_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Total_prob and (J_Total_prob < 0 or J_Total_prob > 99):
            raise ValidationError({"J_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Ud_prob and (A_Ud_prob < 0 or A_Ud_prob > 99):
            raise ValidationError({"A_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Ud_prob and (B_Ud_prob < 0 or B_Ud_prob > 99):
            raise ValidationError({"B_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Ud_prob and (C_Ud_prob < 0 or C_Ud_prob > 99):
            raise ValidationError({"C_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Ud_prob and (D_Ud_prob < 0 or D_Ud_prob > 99):
            raise ValidationError({"D_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Ud_prob and (E_Ud_prob < 0 or E_Ud_prob > 99):
            raise ValidationError({"E_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Ud_prob and (F_Ud_prob < 0 or F_Ud_prob > 99):
            raise ValidationError({"F_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Ud_prob and (G_Ud_prob < 0 or G_Ud_prob > 99):
            raise ValidationError({"G_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Ud_prob and (H_Ud_prob < 0 or H_Ud_prob > 99):
            raise ValidationError({"H_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Ud_prob and (I_Ud_prob < 0 or I_Ud_prob > 99):
            raise ValidationError({"I_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Ud_prob and (J_Ud_prob < 0 or J_Ud_prob > 99):
            raise ValidationError({"J_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_SB_prob and (A_SB_prob < 0 or A_SB_prob > 99):
            raise ValidationError({"A_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SB_prob and (B_SB_prob < 0 or B_SB_prob > 99):
            raise ValidationError({"B_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SB_prob and (C_SB_prob < 0 or C_SB_prob > 99):
            raise ValidationError({"C_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SB_prob and (D_SB_prob < 0 or D_SB_prob > 99):
            raise ValidationError({"D_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SB_prob and (E_SB_prob < 0 or E_SB_prob > 99):
            raise ValidationError({"E_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SB_prob and (F_SB_prob < 0 or F_SB_prob > 99):
            raise ValidationError({"F_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SB_prob and (G_SB_prob < 0 or G_SB_prob > 99):
            raise ValidationError({"G_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SB_prob and (H_SB_prob < 0 or H_SB_prob > 99):
            raise ValidationError({"H_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SB_prob and (I_SB_prob < 0 or I_SB_prob > 99):
            raise ValidationError({"I_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SB_prob and (J_SB_prob < 0 or J_SB_prob > 99):
            raise ValidationError({"J_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
          
        if A_MA_prob and (A_MA_prob < 0 or A_MA_prob > 99):
            raise ValidationError({"A_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_MA_prob and (B_MA_prob < 0 or B_MA_prob > 99):
            raise ValidationError({"B_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if C_MA_prob and (C_MA_prob < 0 or C_MA_prob > 99):
            raise ValidationError({"C_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if D_MA_prob and (D_MA_prob < 0 or D_MA_prob > 99):
            raise ValidationError({"D_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if E_MA_prob and (E_MA_prob < 0 or E_MA_prob > 99):
            raise ValidationError({"E_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_MA_prob and (F_MA_prob < 0 or F_MA_prob > 99):
            raise ValidationError({"F_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_MA_prob and (G_MA_prob < 0 or G_MA_prob > 99):
            raise ValidationError({"G_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_MA_prob and (H_MA_prob < 0 or H_MA_prob > 99):
            raise ValidationError({"H_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_MA_prob and (I_MA_prob < 0 or I_MA_prob > 99):
            raise ValidationError({"I_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_MA_prob and (J_MA_prob < 0 or J_MA_prob > 99):
            raise ValidationError({"J_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        if A_BB_prob and (A_BB_prob < 0 or A_BB_prob > 99):
            raise ValidationError({"A_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_BB_prob and (B_BB_prob < 0 or B_BB_prob > 99):
            raise ValidationError({"B_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_BB_prob and (C_BB_prob < 0 or C_BB_prob > 99):
            raise ValidationError({"C_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_BB_prob and (D_BB_prob < 0 or D_BB_prob > 99):
            raise ValidationError({"D_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_BB_prob and (E_BB_prob < 0 or E_BB_prob > 99):
            raise ValidationError({"E_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_BB_prob and (F_BB_prob < 0 or F_BB_prob > 99):
            raise ValidationError({"F_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_BB_prob and (G_BB_prob < 0 or G_BB_prob > 99):
            raise ValidationError({"G_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_BB_prob and (H_BB_prob < 0 or H_BB_prob > 99):
            raise ValidationError({"H_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_BB_prob and (I_BB_prob < 0 or I_BB_prob > 99):
            raise ValidationError({"I_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_BB_prob and (J_BB_prob < 0 or J_BB_prob > 99):
            raise ValidationError({"J_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_equip = cleaned_data.get('J_ML_equip')

        A_SP_equip = cleaned_data.get('A_SP_equip')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
       
        A_SB_equip = cleaned_data.get('A_SB_equip')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        J_SB_equip = cleaned_data.get('J_SB_equip')
       
        A_MA = cleaned_data.get('A_MA')
        B_MA = cleaned_data.get('B_MA')
        C_MA = cleaned_data.get('C_MA')
        D_MA = cleaned_data.get('D_MA')
        E_MA = cleaned_data.get('E_MA')
        F_MA = cleaned_data.get('F_MA')
        G_MA = cleaned_data.get('G_MA')
        H_MA = cleaned_data.get('H_MA')
        I_MA = cleaned_data.get('I_MA')
        J_MA = cleaned_data.get('J_MA')

        A_BB = cleaned_data.get('A_BB')
        B_BB = cleaned_data.get('B_BB')
        C_BB = cleaned_data.get('C_BB')
        D_BB = cleaned_data.get('D_BB')
        E_BB = cleaned_data.get('E_BB')
        F_BB = cleaned_data.get('F_BB')
        G_BB = cleaned_data.get('G_BB')
        H_BB = cleaned_data.get('H_BB')
        I_BB = cleaned_data.get('I_BB')
        J_BB = cleaned_data.get('J_BB')
        
        
              
        # Validación para ganador
        if A_ML_equip and (A_ML_equip != equipo_local and A_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})
        if B_ML_equip and (B_ML_equip != equipo_local and B_ML_equip != equipo_visitante):
            raise ValidationError({"B_ML_equip": "Debes elegir un equipo válido."})
        if C_ML_equip and (C_ML_equip != equipo_local and C_ML_equip != equipo_visitante):
            raise ValidationError({"C_ML_equip": "Debes elegir un equipo válido."})
        if D_ML_equip and (D_ML_equip != equipo_local and D_ML_equip != equipo_visitante):
            raise ValidationError({"D_ML_equip": "Debes elegir un equipo válido."})
        if E_ML_equip and (E_ML_equip != equipo_local and E_ML_equip != equipo_visitante):
            raise ValidationError({"E_ML_equip": "Debes elegir un equipo válido."})
        if F_ML_equip and (F_ML_equip != equipo_local and F_ML_equip != equipo_visitante):
            raise ValidationError({"F_ML_equip": "Debes elegir un equipo válido."})
        if G_ML_equip and (G_ML_equip != equipo_local and G_ML_equip != equipo_visitante):
            raise ValidationError({"G_ML_equip": "Debes elegir un equipo válido."})
        if H_ML_equip and (H_ML_equip != equipo_local and H_ML_equip != equipo_visitante):
            raise ValidationError({"H_ML_equip": "Debes elegir un equipo válido."})
        if I_ML_equip and (I_ML_equip != equipo_local and I_ML_equip != equipo_visitante):
            raise ValidationError({"I_ML_equip": "Debes elegir un equipo válido."})
        if J_ML_equip and (J_ML_equip != equipo_local and J_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})

        if A_SP_equip and (A_SP_equip != equipo_local and A_SP_equip != equipo_visitante):
            raise ValidationError({"A_SP_equip": "Debes elegir un equipo válido."})
        if B_SP_equip and (B_SP_equip != equipo_local and B_SP_equip != equipo_visitante):
            raise ValidationError({"B_SP_equip": "Debes elegir un equipo válido."})
        if C_SP_equip and (C_SP_equip != equipo_local and C_SP_equip != equipo_visitante):
            raise ValidationError({"C_SP_equip": "Debes elegir un equipo válido."})
        if D_SP_equip and (D_SP_equip != equipo_local and D_SP_equip != equipo_visitante):
            raise ValidationError({"D_SP_equip": "Debes elegir un equipo válido."})
        if E_SP_equip and (E_SP_equip != equipo_local and E_SP_equip != equipo_visitante):
            raise ValidationError({"E_SP_equip": "Debes elegir un equipo válido."})
        if F_SP_equip and (F_SP_equip != equipo_local and F_SP_equip != equipo_visitante):
            raise ValidationError({"F_SP_equip": "Debes elegir un equipo válido."})
        if G_SP_equip and (G_SP_equip != equipo_local and G_SP_equip != equipo_visitante):
            raise ValidationError({"G_SP_equip": "Debes elegir un equipo válido."})
        if H_SP_equip and (H_SP_equip != equipo_local and H_SP_equip != equipo_visitante):
            raise ValidationError({"H_SP_equip": "Debes elegir un equipo válido."})
        if I_SP_equip and (I_SP_equip != equipo_local and I_SP_equip != equipo_visitante):
            raise ValidationError({"I_SP_equip": "Debes elegir un equipo válido."})
        if J_SP_equip and (J_SP_equip != equipo_local and J_SP_equip != equipo_visitante):
            raise ValidationError({"J_SP_equip": "Debes elegir un equipo válido."})
        
        if A_Ud_equip and (A_Ud_equip != equipo_local and A_Ud_equip != equipo_visitante):
            raise ValidationError({"A_Ud_equip": "Debes elegir un equipo válido."})
        if B_Ud_equip and (B_Ud_equip != equipo_local and B_Ud_equip != equipo_visitante):
            raise ValidationError({"B_Ud_equip": "Debes elegir un equipo válido."})
        if C_Ud_equip and (C_Ud_equip != equipo_local and C_Ud_equip != equipo_visitante):
            raise ValidationError({"C_Ud_equip": "Debes elegir un equipo válido."})
        if D_Ud_equip and (D_Ud_equip != equipo_local and D_Ud_equip != equipo_visitante):
            raise ValidationError({"D_Ud_equip": "Debes elegir un equipo válido."})
        if E_Ud_equip and (E_Ud_equip != equipo_local and E_Ud_equip != equipo_visitante):
            raise ValidationError({"E_Ud_equip": "Debes elegir un equipo válido."})
        if F_Ud_equip and (F_Ud_equip != equipo_local and F_Ud_equip != equipo_visitante):
            raise ValidationError({"F_Ud_equip": "Debes elegir un equipo válido."})
        if G_Ud_equip and (G_Ud_equip != equipo_local and G_Ud_equip != equipo_visitante):
            raise ValidationError({"G_Ud_equip": "Debes elegir un equipo válido."})
        if H_Ud_equip and (H_Ud_equip != equipo_local and H_Ud_equip != equipo_visitante):
            raise ValidationError({"H_Ud_equip": "Debes elegir un equipo válido."})
        if I_Ud_equip and (I_Ud_equip != equipo_local and I_Ud_equip != equipo_visitante):
            raise ValidationError({"I_Ud_equip": "Debes elegir un equipo válido."})
        if J_Ud_equip and (J_Ud_equip != equipo_local and J_Ud_equip != equipo_visitante):
            raise ValidationError({"J_Ud_equip": "Debes elegir un equipo válido."})
        
        if A_SB_equip and (A_SB_equip != equipo_local and A_SB_equip != equipo_visitante):
            raise ValidationError({"A_SB_equip": "Debes elegir un equipo válido."})
        if B_SB_equip and (B_SB_equip != equipo_local and B_SB_equip != equipo_visitante):
            raise ValidationError({"B_SB_equip": "Debes elegir un equipo válido."})
        if C_SB_equip and (C_SB_equip != equipo_local and C_SB_equip != equipo_visitante):
            raise ValidationError({"C_SB_equip": "Debes elegir un equipo válido."})
        if D_SB_equip and (D_SB_equip != equipo_local and D_SB_equip != equipo_visitante):
            raise ValidationError({"D_SB_equip": "Debes elegir un equipo válido."})
        if E_SB_equip and (E_SB_equip != equipo_local and E_SB_equip != equipo_visitante):
            raise ValidationError({"E_SB_equip": "Debes elegir un equipo válido."})
        if F_SB_equip and (F_SB_equip != equipo_local and F_SB_equip != equipo_visitante):
            raise ValidationError({"F_SB_equip": "Debes elegir un equipo válido."})
        if G_SB_equip and (G_SB_equip != equipo_local and G_SB_equip != equipo_visitante):
            raise ValidationError({"G_SB_equip": "Debes elegir un equipo válido."})
        if H_SB_equip and (H_SB_equip != equipo_local and H_SB_equip != equipo_visitante):
            raise ValidationError({"H_SB_equip": "Debes elegir un equipo válido."})
        if I_SB_equip and (I_SB_equip != equipo_local and I_SB_equip != equipo_visitante):
            raise ValidationError({"I_SB_equip": "Debes elegir un equipo válido."})
        if J_SB_equip and (J_SB_equip != equipo_local and J_SB_equip != equipo_visitante):
            raise ValidationError({"J_SB_equip": "Debes elegir un equipo válido."})
        
        if A_MA and (A_MA != equipo_local and A_MA != equipo_visitante):
            raise ValidationError({"A_MA": "Debes elegir un equipo válido."})
        if B_MA and (B_MA != equipo_local and B_MA != equipo_visitante):
            raise ValidationError({"B_MA": "Debes elegir un equipo válido."})
        if C_MA and (C_MA != equipo_local and C_MA != equipo_visitante):
            raise ValidationError({"C_MA": "Debes elegir un equipo válido."})
        if D_MA and (D_MA != equipo_local and D_MA != equipo_visitante):
            raise ValidationError({"D_MA": "Debes elegir un equipo válido."})
        if E_MA and (E_MA != equipo_local and E_MA != equipo_visitante):
            raise ValidationError({"E_MA": "Debes elegir un equipo válido."})
        if F_MA and (F_MA != equipo_local and F_MA != equipo_visitante):
            raise ValidationError({"F_MA": "Debes elegir un equipo válido."})
        if G_MA and (G_MA != equipo_local and G_MA != equipo_visitante):
            raise ValidationError({"G_MA": "Debes elegir un equipo válido."})
        if H_MA and (H_MA != equipo_local and H_MA != equipo_visitante):
            raise ValidationError({"H_MA": "Debes elegir un equipo válido."})
        if I_MA and (I_MA != equipo_local and I_MA != equipo_visitante):
            raise ValidationError({"I_MA": "Debes elegir un equipo válido."})
        if J_MA and (J_MA != equipo_local and J_MA != equipo_visitante):
            raise ValidationError({"J_MA": "Debes elegir un equipo válido."})
        
        if A_BB and (A_BB != equipo_local and A_BB != equipo_visitante):
            raise ValidationError({"A_BB": "Debes elegir un equipo válido."})
        if B_BB and (B_BB != equipo_local and B_BB != equipo_visitante):
            raise ValidationError({"B_BB": "Debes elegir un equipo válido."})
        if C_BB and (C_BB != equipo_local and C_BB != equipo_visitante):
            raise ValidationError({"C_BB": "Debes elegir un equipo válido."})
        if D_BB and (D_BB != equipo_local and D_BB != equipo_visitante):
            raise ValidationError({"D_BB": "Debes elegir un equipo válido."})
        if E_BB and (E_BB != equipo_local and E_BB != equipo_visitante):
            raise ValidationError({"E_BB": "Debes elegir un equipo válido."})
        if F_BB and (F_BB != equipo_local and F_BB != equipo_visitante):
            raise ValidationError({"F_BB": "Debes elegir un equipo válido."})
        if G_BB and (G_BB != equipo_local and G_BB != equipo_visitante):
            raise ValidationError({"G_BB": "Debes elegir un equipo válido."})
        if H_BB and (H_BB != equipo_local and H_BB != equipo_visitante):
            raise ValidationError({"H_BB": "Debes elegir un equipo válido."})
        if I_BB and (I_BB != equipo_local and I_BB != equipo_visitante):
            raise ValidationError({"I_BB": "Debes elegir un equipo válido."})
        if J_BB and (J_BB != equipo_local and J_BB != equipo_visitante):
            raise ValidationError({"J_BB": "Debes elegir un equipo válido."})
         

        
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_punto = cleaned_data.get('G_total_punto')     
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_punto = cleaned_data.get('J_total_punto')
        
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        
        if A_Total_punto and (A_Total_punto < 0 ):
            raise ValidationError({"A_Total_punto": "Introdusca un valor válido."})
        if B_Total_punto and (B_Total_punto < 0 ):
            raise ValidationError({"B_Total_punto": "Introdusca un valor válido."})
        if C_Total_punto and (C_Total_punto < 0 ):
            raise ValidationError({"C_Total_punto": "Introdusca un valor válido."})
        if D_Total_punto and (D_Total_punto < 0 ):
            raise ValidationError({"D_Total_punto": "Introdusca un valor válido."})
        if E_Total_punto and (E_Total_punto < 0 ):
            raise ValidationError({"E_Total_punto": "Introdusca un valor válido."})
        if F_Total_punto and (F_Total_punto < 0 ):
            raise ValidationError({"F_Total_punto": "Introdusca un valor válido."})
        if G_Total_punto and (G_Total_punto < 0 ):
            raise ValidationError({"G_Total_punto": "Introdusca un valor válido."})
        if H_Total_punto and (H_Total_punto < 0 ):
            raise ValidationError({"H_Total_punto": "Introdusca un valor válido."})
        if I_Total_punto and (I_Total_punto < 0 ):
            raise ValidationError({"I_Total_punto": "Introdusca un valor válido."})
        if J_Total_punto and (J_Total_punto < 0 ):
            raise ValidationError({"J_Total_punto": "Introdusca un valor válido."})
        
        if A_SP_dif and (A_SP_dif < 0 ):
            raise ValidationError({"A_SP_dif": "Introdusca un valor válido."})
        if B_SP_dif and (B_SP_dif < 0 ):
            raise ValidationError({"B_SP_dif": "Introdusca un valor válido."})
        if C_SP_dif and (C_SP_dif < 0 ):
            raise ValidationError({"C_SP_dif": "Introdusca un valor válido."})
        if D_SP_dif and (D_SP_dif < 0 ):
            raise ValidationError({"D_SP_dif": "Introdusca un valor válido."})
        if E_SP_dif and (E_SP_dif < 0 ):
            raise ValidationError({"E_SP_dif": "Introdusca un valor válido."})
        if F_SP_dif and (F_SP_dif < 0 ):
            raise ValidationError({"F_SP_dif": "Introdusca un valor válido."})
        if G_SP_dif and (G_SP_dif < 0 ):
            raise ValidationError({"G_SP_dif": "Introdusca un valor válido."})
        if H_SP_dif and (H_SP_dif < 0 ):
            raise ValidationError({"H_SP_dif": "Introdusca un valor válido."})
        if I_SP_dif and (I_SP_dif < 0 ):
            raise ValidationError({"I_SP_dif": "Introdusca un valor válido."})
        if J_SP_dif and (J_SP_dif < 0 ):
            raise ValidationError({"J_SP_dif": "Introdusca un valor válido."})
        
        return cleaned_data
    
        
        
        
class Hockey_form(forms.ModelForm):
    

    
    class Meta:
        model = Hockey
        fields = ['equipo_local', 'equipo_visitante','fecha','A_ML_equip','A_ML_prob','A_SP_equip','A_SP_prob','A_SP_dif','A_Total_OU','A_Total_prob','A_Ud_equip','A_Ud_prob','A_SB_equip','A_SB_prob','A_MA','A_BB','A_total_punto',
                  'B_ML_equip','B_ML_prob','B_SP_equip','B_SP_prob','B_SP_dif','B_Total_OU','B_Total_prob','B_Ud_equip','B_Ud_prob','B_SB_equip','B_SB_prob','B_MA','B_BB','B_total_punto','A_MA_prob','B_MA_prob','C_MA_prob','D_MA_prob',
                  'C_ML_equip','C_ML_prob','C_SP_equip','C_SP_prob','C_SP_dif','C_Total_OU','C_Total_prob','C_Ud_equip','C_Ud_prob','C_SB_equip','C_SB_prob','C_MA','C_BB','C_total_punto','E_MA_prob','F_MA_prob','G_MA_prob','H_MA_prob',
                  'D_ML_equip','D_ML_prob','D_SP_equip','D_SP_prob','D_SP_dif','D_Total_OU','D_Total_prob','D_Ud_equip','D_Ud_prob','D_SB_equip','D_SB_prob','D_MA','D_BB','D_total_punto','I_MA_prob','J_MA_prob','A_BB_prob','B_BB_prob',
                  'E_ML_equip','E_ML_prob','E_SP_equip','E_SP_prob','E_SP_dif','E_Total_OU','E_Total_prob','E_Ud_equip','E_Ud_prob','E_SB_equip','E_SB_prob','E_MA','E_BB','E_total_punto','C_BB_prob','D_BB_prob','E_BB_prob','F_BB_prob',
                  'F_ML_equip','F_ML_prob','F_SP_equip','F_SP_prob','F_SP_dif','F_Total_OU','F_Total_prob','F_Ud_equip','F_Ud_prob','F_SB_equip','F_SB_prob','F_MA','F_BB','F_total_punto','G_BB_prob','H_BB_prob','I_BB_prob','J_BB_prob',
                  'G_ML_equip','G_ML_prob','G_SP_equip','G_SP_prob','G_SP_dif','G_Total_OU','G_Total_prob','G_Ud_equip','G_Ud_prob','G_SB_equip','G_SB_prob','G_MA','G_BB','G_total_punto',
                  'H_ML_equip','H_ML_prob','H_SP_equip','H_SP_prob','H_SP_dif','H_Total_OU','H_Total_prob','H_Ud_equip','H_Ud_prob','H_SB_equip','H_SB_prob','H_MA','H_BB','H_total_punto',
                  'I_ML_equip','I_ML_prob','I_SP_equip','I_SP_prob','I_SP_dif','I_Total_OU','I_Total_prob','I_Ud_equip','I_Ud_prob','I_SB_equip','I_SB_prob','I_MA','I_BB','I_total_punto',
                  'J_ML_equip','J_ML_prob','J_SP_equip','J_SP_prob','J_SP_dif','J_Total_OU','J_Total_prob','J_Ud_equip','J_Ud_prob','J_SB_equip','J_SB_prob','J_MA','J_BB','J_total_punto',
                  ]
        
        widgets = {
            
            'equipo_local': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'equipo_visitante': forms.Select(attrs={'class':'form-control ', 'placeholder': '' }),
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control select-field', 'placeholder': '' }),
            'A_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'F_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB': forms.TextInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_ML_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SP_dif': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_OU': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Total_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_total_punto': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_Ud_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_equip': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_SB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
            'A_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_MA_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'A_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'B_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'C_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'D_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'E_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'F_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'G_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'H_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'I_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
            'J_BB_prob': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '' }),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visitante = cleaned_data.get('equipo_visitante')

       
        existing_partidos = Hockey.objects.filter(
            Q(fecha=fecha) &
            ~Q(id=self.instance.id) &  
            (
                Q(equipo_local=equipo_local) | 
                Q(equipo_visitante=equipo_visitante) 
            )
        )

        if existing_partidos.exists():
            raise ValidationError("Ya existe un partido con el mismo equipo programado para esta fecha.")

       
        if equipo_local.nombre == equipo_visitante.nombre:
           raise ValidationError("El equipo local y el equipo visitante no pueden ser el mismo.")     

    
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        J_ML_equip = cleaned_data.get('J_ML_equip')
        
        A_SP_equip = cleaned_data.get('A_SP_equip')
        A_SP_prob = cleaned_data.get('A_SP_prob')
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        J_SP_prob = cleaned_data.get('J_SP_prob')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        A_Total_OU = cleaned_data.get('A_Total_OU')
        A_Total_prob = cleaned_data.get('A_Total_prob')
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_OU = cleaned_data.get('B_Total_OU')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_OU = cleaned_data.get('C_Total_OU')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_OU = cleaned_data.get('D_Total_OU')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_OU = cleaned_data.get('E_Total_OU')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_OU = cleaned_data.get('F_Total_OU')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_OU = cleaned_data.get('G_Total_OU')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        G_Total_punto = cleaned_data.get('G_total_punto')
        H_Total_OU = cleaned_data.get('H_Total_OU')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_OU = cleaned_data.get('I_Total_OU')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_OU = cleaned_data.get('J_Total_OU')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        J_Total_punto = cleaned_data.get('J_total_punto')
       
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')
        
        A_SB_equip = cleaned_data.get('A_SB_equip')
        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_equip = cleaned_data.get('J_SB_equip')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
        A_MA= cleaned_data.get('A_MA')
        B_MA= cleaned_data.get('B_MA')
        C_MA= cleaned_data.get('C_MA')
        D_MA= cleaned_data.get('D_MA')
        E_MA= cleaned_data.get('E_MA')
        F_MA= cleaned_data.get('F_MA')
        G_MA= cleaned_data.get('G_MA')
        H_MA= cleaned_data.get('H_MA')
        I_MA= cleaned_data.get('I_MA')
        J_MA= cleaned_data.get('J_MA')
        
        A_MA_prob= cleaned_data.get('A_MA_prob')
        B_MA_prob= cleaned_data.get('B_MA_prob')
        C_MA_prob= cleaned_data.get('C_MA_prob')
        D_MA_prob= cleaned_data.get('D_MA_prob')
        E_MA_prob= cleaned_data.get('E_MA_prob')
        F_MA_prob= cleaned_data.get('F_MA_prob')
        G_MA_prob= cleaned_data.get('G_MA_prob')
        H_MA_prob= cleaned_data.get('H_MA_prob')
        I_MA_prob= cleaned_data.get('I_MA_prob')
        J_MA_prob= cleaned_data.get('J_MA_prob')
        
        
        A_BB= cleaned_data.get('A_BB')
        B_BB= cleaned_data.get('B_BB')
        C_BB= cleaned_data.get('C_BB')
        D_BB= cleaned_data.get('D_BB')
        E_BB= cleaned_data.get('E_BB')
        F_BB= cleaned_data.get('F_BB')
        G_BB= cleaned_data.get('G_BB')
        H_BB= cleaned_data.get('H_BB')
        I_BB= cleaned_data.get('I_BB')
        J_BB= cleaned_data.get('J_BB')
         
        A_BB_prob= cleaned_data.get('A_BB_prob')
        B_BB_prob= cleaned_data.get('B_BB_prob')
        C_BB_prob= cleaned_data.get('C_BB_prob')
        D_BB_prob= cleaned_data.get('D_BB_prob')
        E_BB_prob= cleaned_data.get('E_BB_prob')
        F_BB_prob= cleaned_data.get('F_BB_prob')
        G_BB_prob= cleaned_data.get('G_BB_prob')
        H_BB_prob= cleaned_data.get('H_BB_prob')
        I_BB_prob= cleaned_data.get('I_BB_prob')
        J_BB_prob= cleaned_data.get('J_BB_prob')

        
        # Realiza la validación personalizada
        if A_ML_prob or A_ML_equip:
            if not (A_ML_equip and A_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if B_ML_prob or B_ML_equip:
            if not (B_ML_equip and B_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if C_ML_prob or C_ML_equip:
            if not (C_ML_equip and C_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if D_ML_prob or D_ML_equip:
            if not (D_ML_equip and D_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if E_ML_prob or E_ML_equip:
            if not (E_ML_equip and E_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if F_ML_prob or F_ML_equip:
            if not (F_ML_equip and F_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if G_ML_prob or G_ML_equip:
            if not (G_ML_equip and G_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if H_ML_prob or H_ML_equip:
            if not (H_ML_equip and H_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if I_ML_prob or I_ML_equip:
            if not (I_ML_equip and I_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        if J_ML_prob or J_ML_equip:
            if not (J_ML_equip and J_ML_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de moneline en un mismo sitema se debe rellenar el otro. ")    
        
        if A_SP_equip or A_SP_prob or A_SP_dif :
            if not (A_SP_equip and A_SP_prob and A_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if B_SP_equip or B_SP_prob or B_SP_dif :
            if not (B_SP_equip and B_SP_prob and B_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if C_SP_equip or C_SP_prob or C_SP_dif :
            if not (C_SP_equip and C_SP_prob and C_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if D_SP_equip or D_SP_prob or D_SP_dif :
            if not (D_SP_equip and D_SP_prob and D_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if E_SP_equip or E_SP_prob or E_SP_dif :
            if not (E_SP_equip and E_SP_prob and E_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if F_SP_equip or F_SP_prob or F_SP_dif :
            if not (F_SP_equip and F_SP_prob and F_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if G_SP_equip or G_SP_prob or G_SP_dif :
            if not (G_SP_equip and G_SP_prob and G_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if H_SP_equip or H_SP_prob or H_SP_dif :
            if not (H_SP_equip and H_SP_prob and H_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if I_SP_equip or I_SP_prob or I_SP_dif :
            if not (I_SP_equip and I_SP_prob and I_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
        if J_SP_equip or J_SP_prob or J_SP_dif :
            if not (J_SP_equip and J_SP_prob and J_SP_dif):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Spread en un mismo sitema se debe rellenar los otros otro. ")    
  
       
        if A_Total_OU or A_Total_prob or A_Total_punto :
            if not (A_Total_OU and A_Total_prob and A_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if B_Total_OU or B_Total_prob or B_Total_punto :
            if not (B_Total_OU and B_Total_prob and B_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if C_Total_OU or C_Total_prob or C_Total_punto :
            if not (C_Total_OU and C_Total_prob and C_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if D_Total_OU or D_Total_prob or D_Total_punto :
            if not (D_Total_OU and D_Total_prob and D_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if E_Total_OU or E_Total_prob or E_Total_punto :
            if not (E_Total_OU and E_Total_prob and E_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if F_Total_OU or F_Total_prob or F_Total_punto :
            if not (F_Total_OU and F_Total_prob and F_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if G_Total_OU or G_Total_prob or G_Total_punto :
            if not (G_Total_OU and G_Total_prob and G_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if H_Total_OU or H_Total_prob or H_Total_punto :
            if not (H_Total_OU and H_Total_prob and H_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if I_Total_OU or I_Total_prob or I_Total_punto :
            if not (I_Total_OU and I_Total_prob and I_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
        if J_Total_OU or J_Total_prob or J_Total_punto :
            if not (J_Total_OU and J_Total_prob and J_Total_punto):
                raise forms.ValidationError("Si se introduce al menos uno de los campos de Total en un mismo sitema se debe rellenar los otros. ")    
      
        if A_Ud_equip or A_Ud_prob:
            if not (A_Ud_equip and A_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if B_Ud_equip or B_Ud_prob:
            if not (B_Ud_equip and B_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if C_Ud_equip or C_Ud_prob:
            if not (C_Ud_equip and C_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if D_Ud_equip or D_Ud_prob:
            if not (D_Ud_equip and D_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if E_Ud_equip or E_Ud_prob:
            if not (E_Ud_equip and E_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if F_Ud_equip or F_Ud_prob:
            if not (F_Ud_equip and F_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if G_Ud_equip or G_Ud_prob:
            if not (G_Ud_equip and G_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if H_Ud_equip or H_Ud_prob:
            if not (H_Ud_equip and H_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if I_Ud_equip or I_Ud_prob:
            if not (I_Ud_equip and I_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
        if J_Ud_equip or J_Ud_prob:
            if not (J_Ud_equip and J_Ud_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Underdogs en un mismo sitema se debe rellenar el otro. ")    
       
        if A_SB_equip or A_SB_prob:
            if not (A_SB_equip and A_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if B_SB_equip or B_SB_prob:
            if not (B_SB_equip and B_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if C_SB_equip or C_SB_prob:
            if not (C_SB_equip and C_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if D_SB_equip or D_SB_prob:
            if not (D_SB_equip and D_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if E_SB_equip or E_SB_prob:
            if not (E_SB_equip and E_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if F_SB_equip or F_SB_prob:
            if not (F_SB_equip and F_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if G_SB_equip or G_SB_prob:
            if not (G_SB_equip and G_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if H_SB_equip or H_SB_prob:
            if not (H_SB_equip and H_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if I_SB_equip or I_SB_prob:
            if not (I_SB_equip and I_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
        if J_SB_equip or J_SB_prob:
            if not (J_SB_equip and J_SB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Sharp Bettor en un mismo sitema se debe rellenar el otro. ")    
       
        if A_MA or A_MA_prob:
            if not (A_MA and A_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if B_MA or B_MA_prob:
            if not (B_MA and B_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if C_MA or C_MA_prob:
            if not (C_MA and C_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if D_MA or D_MA_prob:
            if not (D_MA and D_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if E_MA or E_MA_prob:
            if not (E_MA and E_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if F_MA or F_MA_prob:
            if not (F_MA and F_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if G_MA or G_MA_prob:
            if not (G_MA and G_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if H_MA or H_MA_prob:
            if not (H_MA and H_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if I_MA or I_MA_prob:
            if not (I_MA and I_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ")
        if J_MA or J_MA_prob:
            if not (J_MA and J_MA_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Money Adventage en un mismo sitema se debe rellenar el otro. ") 
   
        
        if A_BB or A_BB_prob:
            if not (A_BB and A_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if B_BB or B_BB_prob:
            if not (B_BB and B_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if C_BB or C_BB_prob:
            if not (C_BB and C_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if D_BB or D_BB_prob:
            if not (D_BB and D_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if E_BB or E_BB_prob:
            if not (E_BB and E_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if F_BB or F_BB_prob:
            if not (F_BB and F_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if G_BB or G_BB_prob:
            if not (G_BB and G_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if H_BB or H_BB_prob:
            if not (H_BB and H_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if I_BB or I_BB_prob:
            if not (I_BB and I_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        if J_BB or J_BB_prob:
            if not (J_BB and J_BB_prob ):
                raise forms.ValidationError("Si se introduce uno de los campos de Best Bets en un mismo sitema se debe rellenar el otro. ")
        
       
       
       
        A_ML_prob = cleaned_data.get('A_ML_prob')
        B_ML_prob = cleaned_data.get('B_ML_prob')
        C_ML_prob = cleaned_data.get('C_ML_prob')
        D_ML_prob = cleaned_data.get('D_ML_prob')
        E_ML_prob = cleaned_data.get('E_ML_prob')
        F_ML_prob = cleaned_data.get('F_ML_prob')
        G_ML_prob = cleaned_data.get('G_ML_prob')
        H_ML_prob = cleaned_data.get('H_ML_prob')
        I_ML_prob = cleaned_data.get('I_ML_prob')
        J_ML_prob = cleaned_data.get('J_ML_prob')
        
        A_SP_prob = cleaned_data.get('A_SP_prob')
        B_SP_prob = cleaned_data.get('B_SP_prob')
        C_SP_prob = cleaned_data.get('C_SP_prob')
        D_SP_prob = cleaned_data.get('D_SP_prob')
        E_SP_prob = cleaned_data.get('E_SP_prob')
        F_SP_prob = cleaned_data.get('F_SP_prob')
        G_SP_prob = cleaned_data.get('G_SP_prob')
        H_SP_prob = cleaned_data.get('H_SP_prob')
        I_SP_prob = cleaned_data.get('I_SP_prob')
        J_SP_prob = cleaned_data.get('J_SP_prob')

        A_Total_prob = cleaned_data.get('A_Total_prob')
        B_Total_prob = cleaned_data.get('B_Total_prob')
        C_Total_prob = cleaned_data.get('C_Total_prob')
        D_Total_prob = cleaned_data.get('D_Total_prob')
        E_Total_prob = cleaned_data.get('E_Total_prob')
        F_Total_prob = cleaned_data.get('F_Total_prob')
        G_Total_prob = cleaned_data.get('G_Total_prob')
        H_Total_prob = cleaned_data.get('H_Total_prob')
        I_Total_prob = cleaned_data.get('I_Total_prob')
        J_Total_prob = cleaned_data.get('J_Total_prob')
        
        A_Ud_prob = cleaned_data.get('A_Ud_prob')
        B_Ud_prob = cleaned_data.get('B_Ud_prob')
        C_Ud_prob = cleaned_data.get('C_Ud_prob')
        D_Ud_prob = cleaned_data.get('D_Ud_prob')
        E_Ud_prob = cleaned_data.get('E_Ud_prob')
        F_Ud_prob = cleaned_data.get('F_Ud_prob')
        G_Ud_prob = cleaned_data.get('G_Ud_prob')
        H_Ud_prob = cleaned_data.get('H_Ud_prob')
        I_Ud_prob = cleaned_data.get('I_Ud_prob')
        J_Ud_prob = cleaned_data.get('J_Ud_prob')

        A_SB_prob = cleaned_data.get('A_SB_prob')
        B_SB_prob = cleaned_data.get('B_SB_prob')
        C_SB_prob = cleaned_data.get('C_SB_prob')
        D_SB_prob = cleaned_data.get('D_SB_prob')
        E_SB_prob = cleaned_data.get('E_SB_prob')
        F_SB_prob = cleaned_data.get('F_SB_prob')
        G_SB_prob = cleaned_data.get('G_SB_prob')
        H_SB_prob = cleaned_data.get('H_SB_prob')
        I_SB_prob = cleaned_data.get('I_SB_prob')
        J_SB_prob = cleaned_data.get('J_SB_prob')
        
        
       
        if A_ML_prob and (A_ML_prob < 1 or A_ML_prob > 99):
            raise ValidationError({"A_ML_prob": "El valor de probabilidad debe estar entre 1 y 99."})
        if B_ML_prob and (B_ML_prob < 0 or B_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_ML_prob and (C_ML_prob < 0 or C_ML_prob > 99):
            raise ValidationError({"C_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_ML_prob and (D_ML_prob < 0 or D_ML_prob > 99):
            raise ValidationError({"D_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_ML_prob and (E_ML_prob < 0 or E_ML_prob > 99):
            raise ValidationError({"E_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_ML_prob and (F_ML_prob < 0 or F_ML_prob > 99):
            raise ValidationError({"F_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_ML_prob and (G_ML_prob < 0 or G_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_ML_prob and (H_ML_prob < 0 or H_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_ML_prob and (I_ML_prob < 0 or I_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_ML_prob and (J_ML_prob < 0 or J_ML_prob > 99):
            raise ValidationError({"B_ML_prob": "El valor de probabilidad total debe estar entre 1 y 99."})


        if A_SP_prob and (A_SP_prob < 0 or A_SP_prob > 99):
            raise ValidationError({"A_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SP_prob and (B_SP_prob < 0 or B_SP_prob > 99):
            raise ValidationError({"B_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SP_prob and (C_SP_prob < 0 or C_SP_prob > 99):
            raise ValidationError({"C_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SP_prob and (D_SP_prob < 0 or D_SP_prob > 99):
            raise ValidationError({"D_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SP_prob and (E_SP_prob < 0 or E_SP_prob > 99):
            raise ValidationError({"E_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SP_prob and (F_SP_prob < 0 or F_SP_prob > 99):
            raise ValidationError({"F_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SP_prob and (G_SP_prob < 0 or G_SP_prob > 99):
            raise ValidationError({"G_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SP_prob and (H_SP_prob < 0 or H_SP_prob > 99):
            raise ValidationError({"H_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SP_prob and (I_SP_prob < 0 or I_SP_prob > 99):
            raise ValidationError({"I_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SP_prob and (J_SP_prob < 0 or J_SP_prob > 99):
            raise ValidationError({"J_SP_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Total_prob and (A_Total_prob < 0 or A_Total_prob > 99):
            raise ValidationError({"A_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Total_prob and (B_Total_prob < 0 or B_Total_prob > 99):
            raise ValidationError({"B_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Total_prob and (C_Total_prob < 0 or C_Total_prob > 99):
            raise ValidationError({"C_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Total_prob and (D_Total_prob < 0 or D_Total_prob > 99):
            raise ValidationError({"D_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Total_prob and (E_Total_prob < 0 or E_Total_prob > 99):
            raise ValidationError({"E_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Total_prob and (F_Total_prob < 0 or F_Total_prob > 99):
            raise ValidationError({"F_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Total_prob and (G_Total_prob < 0 or G_Total_prob > 99):
            raise ValidationError({"G_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Total_prob and (H_Total_prob < 0 or H_Total_prob > 99):
            raise ValidationError({"H_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Total_prob and (I_Total_prob < 0 or I_Total_prob > 99):
            raise ValidationError({"I_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Total_prob and (J_Total_prob < 0 or J_Total_prob > 99):
            raise ValidationError({"J_Total_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_Ud_prob and (A_Ud_prob < 0 or A_Ud_prob > 99):
            raise ValidationError({"A_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_Ud_prob and (B_Ud_prob < 0 or B_Ud_prob > 99):
            raise ValidationError({"B_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_Ud_prob and (C_Ud_prob < 0 or C_Ud_prob > 99):
            raise ValidationError({"C_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_Ud_prob and (D_Ud_prob < 0 or D_Ud_prob > 99):
            raise ValidationError({"D_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_Ud_prob and (E_Ud_prob < 0 or E_Ud_prob > 99):
            raise ValidationError({"E_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_Ud_prob and (F_Ud_prob < 0 or F_Ud_prob > 99):
            raise ValidationError({"F_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_Ud_prob and (G_Ud_prob < 0 or G_Ud_prob > 99):
            raise ValidationError({"G_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_Ud_prob and (H_Ud_prob < 0 or H_Ud_prob > 99):
            raise ValidationError({"H_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_Ud_prob and (I_Ud_prob < 0 or I_Ud_prob > 99):
            raise ValidationError({"I_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_Ud_prob and (J_Ud_prob < 0 or J_Ud_prob > 99):
            raise ValidationError({"J_Ud_prob": "El valor de probabilidad total debe estar entre 1 y 99."})

        if A_SB_prob and (A_SB_prob < 0 or A_SB_prob > 99):
            raise ValidationError({"A_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_SB_prob and (B_SB_prob < 0 or B_SB_prob > 99):
            raise ValidationError({"B_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_SB_prob and (C_SB_prob < 0 or C_SB_prob > 99):
            raise ValidationError({"C_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_SB_prob and (D_SB_prob < 0 or D_SB_prob > 99):
            raise ValidationError({"D_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_SB_prob and (E_SB_prob < 0 or E_SB_prob > 99):
            raise ValidationError({"E_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_SB_prob and (F_SB_prob < 0 or F_SB_prob > 99):
            raise ValidationError({"F_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_SB_prob and (G_SB_prob < 0 or G_SB_prob > 99):
            raise ValidationError({"G_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_SB_prob and (H_SB_prob < 0 or H_SB_prob > 99):
            raise ValidationError({"H_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_SB_prob and (I_SB_prob < 0 or I_SB_prob > 99):
            raise ValidationError({"I_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_SB_prob and (J_SB_prob < 0 or J_SB_prob > 99):
            raise ValidationError({"J_SB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
          
        if A_MA_prob and (A_MA_prob < 0 or A_MA_prob > 99):
            raise ValidationError({"A_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_MA_prob and (B_MA_prob < 0 or B_MA_prob > 99):
            raise ValidationError({"B_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if C_MA_prob and (C_MA_prob < 0 or C_MA_prob > 99):
            raise ValidationError({"C_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if D_MA_prob and (D_MA_prob < 0 or D_MA_prob > 99):
            raise ValidationError({"D_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})  
        if E_MA_prob and (E_MA_prob < 0 or E_MA_prob > 99):
            raise ValidationError({"E_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_MA_prob and (F_MA_prob < 0 or F_MA_prob > 99):
            raise ValidationError({"F_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_MA_prob and (G_MA_prob < 0 or G_MA_prob > 99):
            raise ValidationError({"G_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_MA_prob and (H_MA_prob < 0 or H_MA_prob > 99):
            raise ValidationError({"H_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_MA_prob and (I_MA_prob < 0 or I_MA_prob > 99):
            raise ValidationError({"I_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_MA_prob and (J_MA_prob < 0 or J_MA_prob > 99):
            raise ValidationError({"J_MA_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        if A_BB_prob and (A_BB_prob < 0 or A_BB_prob > 99):
            raise ValidationError({"A_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if B_BB_prob and (B_BB_prob < 0 or B_BB_prob > 99):
            raise ValidationError({"B_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if C_BB_prob and (C_BB_prob < 0 or C_BB_prob > 99):
            raise ValidationError({"C_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if D_BB_prob and (D_BB_prob < 0 or D_BB_prob > 99):
            raise ValidationError({"D_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if E_BB_prob and (E_BB_prob < 0 or E_BB_prob > 99):
            raise ValidationError({"E_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if F_BB_prob and (F_BB_prob < 0 or F_BB_prob > 99):
            raise ValidationError({"F_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if G_BB_prob and (G_BB_prob < 0 or G_BB_prob > 99):
            raise ValidationError({"G_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if H_BB_prob and (H_BB_prob < 0 or H_BB_prob > 99):
            raise ValidationError({"H_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if I_BB_prob and (I_BB_prob < 0 or I_BB_prob > 99):
            raise ValidationError({"I_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        if J_BB_prob and (J_BB_prob < 0 or J_BB_prob > 99):
            raise ValidationError({"J_BB_prob": "El valor de probabilidad total debe estar entre 1 y 99."})
        
        
        A_ML_equip = cleaned_data.get('A_ML_equip')
        B_ML_equip = cleaned_data.get('B_ML_equip')
        C_ML_equip = cleaned_data.get('C_ML_equip')
        D_ML_equip = cleaned_data.get('D_ML_equip')
        E_ML_equip = cleaned_data.get('E_ML_equip')
        F_ML_equip = cleaned_data.get('F_ML_equip')
        G_ML_equip = cleaned_data.get('G_ML_equip')
        H_ML_equip = cleaned_data.get('H_ML_equip')
        I_ML_equip = cleaned_data.get('I_ML_equip')
        J_ML_equip = cleaned_data.get('J_ML_equip')

        A_SP_equip = cleaned_data.get('A_SP_equip')
        B_SP_equip = cleaned_data.get('B_SP_equip')
        C_SP_equip = cleaned_data.get('C_SP_equip')
        D_SP_equip = cleaned_data.get('D_SP_equip')
        E_SP_equip = cleaned_data.get('E_SP_equip')
        F_SP_equip = cleaned_data.get('F_SP_equip')
        G_SP_equip = cleaned_data.get('G_SP_equip')
        H_SP_equip = cleaned_data.get('H_SP_equip')
        I_SP_equip = cleaned_data.get('I_SP_equip')
        J_SP_equip = cleaned_data.get('J_SP_equip')
        
        A_Ud_equip = cleaned_data.get('A_Ud_equip')
        B_Ud_equip = cleaned_data.get('B_Ud_equip')
        C_Ud_equip = cleaned_data.get('C_Ud_equip')
        D_Ud_equip = cleaned_data.get('D_Ud_equip')
        E_Ud_equip = cleaned_data.get('E_Ud_equip')
        F_Ud_equip = cleaned_data.get('F_Ud_equip')
        G_Ud_equip = cleaned_data.get('G_Ud_equip')
        H_Ud_equip = cleaned_data.get('H_Ud_equip')
        I_Ud_equip = cleaned_data.get('I_Ud_equip')
        J_Ud_equip = cleaned_data.get('J_Ud_equip')
       
        A_SB_equip = cleaned_data.get('A_SB_equip')
        B_SB_equip = cleaned_data.get('B_SB_equip')
        C_SB_equip = cleaned_data.get('C_SB_equip')
        D_SB_equip = cleaned_data.get('D_SB_equip')
        E_SB_equip = cleaned_data.get('E_SB_equip')
        F_SB_equip = cleaned_data.get('F_SB_equip')
        G_SB_equip = cleaned_data.get('G_SB_equip')
        H_SB_equip = cleaned_data.get('H_SB_equip')
        I_SB_equip = cleaned_data.get('I_SB_equip')
        J_SB_equip = cleaned_data.get('J_SB_equip')
       
        A_MA = cleaned_data.get('A_MA')
        B_MA = cleaned_data.get('B_MA')
        C_MA = cleaned_data.get('C_MA')
        D_MA = cleaned_data.get('D_MA')
        E_MA = cleaned_data.get('E_MA')
        F_MA = cleaned_data.get('F_MA')
        G_MA = cleaned_data.get('G_MA')
        H_MA = cleaned_data.get('H_MA')
        I_MA = cleaned_data.get('I_MA')
        J_MA = cleaned_data.get('J_MA')

        A_BB = cleaned_data.get('A_BB')
        B_BB = cleaned_data.get('B_BB')
        C_BB = cleaned_data.get('C_BB')
        D_BB = cleaned_data.get('D_BB')
        E_BB = cleaned_data.get('E_BB')
        F_BB = cleaned_data.get('F_BB')
        G_BB = cleaned_data.get('G_BB')
        H_BB = cleaned_data.get('H_BB')
        I_BB = cleaned_data.get('I_BB')
        J_BB = cleaned_data.get('J_BB')
        
        
              
        # Validación para ganador
        if A_ML_equip and (A_ML_equip != equipo_local and A_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})
        if B_ML_equip and (B_ML_equip != equipo_local and B_ML_equip != equipo_visitante):
            raise ValidationError({"B_ML_equip": "Debes elegir un equipo válido."})
        if C_ML_equip and (C_ML_equip != equipo_local and C_ML_equip != equipo_visitante):
            raise ValidationError({"C_ML_equip": "Debes elegir un equipo válido."})
        if D_ML_equip and (D_ML_equip != equipo_local and D_ML_equip != equipo_visitante):
            raise ValidationError({"D_ML_equip": "Debes elegir un equipo válido."})
        if E_ML_equip and (E_ML_equip != equipo_local and E_ML_equip != equipo_visitante):
            raise ValidationError({"E_ML_equip": "Debes elegir un equipo válido."})
        if F_ML_equip and (F_ML_equip != equipo_local and F_ML_equip != equipo_visitante):
            raise ValidationError({"F_ML_equip": "Debes elegir un equipo válido."})
        if G_ML_equip and (G_ML_equip != equipo_local and G_ML_equip != equipo_visitante):
            raise ValidationError({"G_ML_equip": "Debes elegir un equipo válido."})
        if H_ML_equip and (H_ML_equip != equipo_local and H_ML_equip != equipo_visitante):
            raise ValidationError({"H_ML_equip": "Debes elegir un equipo válido."})
        if I_ML_equip and (I_ML_equip != equipo_local and I_ML_equip != equipo_visitante):
            raise ValidationError({"I_ML_equip": "Debes elegir un equipo válido."})
        if J_ML_equip and (J_ML_equip != equipo_local and J_ML_equip != equipo_visitante):
            raise ValidationError({"A_ML_equip": "Debes elegir un equipo válido."})

        if A_SP_equip and (A_SP_equip != equipo_local and A_SP_equip != equipo_visitante):
            raise ValidationError({"A_SP_equip": "Debes elegir un equipo válido."})
        if B_SP_equip and (B_SP_equip != equipo_local and B_SP_equip != equipo_visitante):
            raise ValidationError({"B_SP_equip": "Debes elegir un equipo válido."})
        if C_SP_equip and (C_SP_equip != equipo_local and C_SP_equip != equipo_visitante):
            raise ValidationError({"C_SP_equip": "Debes elegir un equipo válido."})
        if D_SP_equip and (D_SP_equip != equipo_local and D_SP_equip != equipo_visitante):
            raise ValidationError({"D_SP_equip": "Debes elegir un equipo válido."})
        if E_SP_equip and (E_SP_equip != equipo_local and E_SP_equip != equipo_visitante):
            raise ValidationError({"E_SP_equip": "Debes elegir un equipo válido."})
        if F_SP_equip and (F_SP_equip != equipo_local and F_SP_equip != equipo_visitante):
            raise ValidationError({"F_SP_equip": "Debes elegir un equipo válido."})
        if G_SP_equip and (G_SP_equip != equipo_local and G_SP_equip != equipo_visitante):
            raise ValidationError({"G_SP_equip": "Debes elegir un equipo válido."})
        if H_SP_equip and (H_SP_equip != equipo_local and H_SP_equip != equipo_visitante):
            raise ValidationError({"H_SP_equip": "Debes elegir un equipo válido."})
        if I_SP_equip and (I_SP_equip != equipo_local and I_SP_equip != equipo_visitante):
            raise ValidationError({"I_SP_equip": "Debes elegir un equipo válido."})
        if J_SP_equip and (J_SP_equip != equipo_local and J_SP_equip != equipo_visitante):
            raise ValidationError({"J_SP_equip": "Debes elegir un equipo válido."})
        
        if A_Ud_equip and (A_Ud_equip != equipo_local and A_Ud_equip != equipo_visitante):
            raise ValidationError({"A_Ud_equip": "Debes elegir un equipo válido."})
        if B_Ud_equip and (B_Ud_equip != equipo_local and B_Ud_equip != equipo_visitante):
            raise ValidationError({"B_Ud_equip": "Debes elegir un equipo válido."})
        if C_Ud_equip and (C_Ud_equip != equipo_local and C_Ud_equip != equipo_visitante):
            raise ValidationError({"C_Ud_equip": "Debes elegir un equipo válido."})
        if D_Ud_equip and (D_Ud_equip != equipo_local and D_Ud_equip != equipo_visitante):
            raise ValidationError({"D_Ud_equip": "Debes elegir un equipo válido."})
        if E_Ud_equip and (E_Ud_equip != equipo_local and E_Ud_equip != equipo_visitante):
            raise ValidationError({"E_Ud_equip": "Debes elegir un equipo válido."})
        if F_Ud_equip and (F_Ud_equip != equipo_local and F_Ud_equip != equipo_visitante):
            raise ValidationError({"F_Ud_equip": "Debes elegir un equipo válido."})
        if G_Ud_equip and (G_Ud_equip != equipo_local and G_Ud_equip != equipo_visitante):
            raise ValidationError({"G_Ud_equip": "Debes elegir un equipo válido."})
        if H_Ud_equip and (H_Ud_equip != equipo_local and H_Ud_equip != equipo_visitante):
            raise ValidationError({"H_Ud_equip": "Debes elegir un equipo válido."})
        if I_Ud_equip and (I_Ud_equip != equipo_local and I_Ud_equip != equipo_visitante):
            raise ValidationError({"I_Ud_equip": "Debes elegir un equipo válido."})
        if J_Ud_equip and (J_Ud_equip != equipo_local and J_Ud_equip != equipo_visitante):
            raise ValidationError({"J_Ud_equip": "Debes elegir un equipo válido."})
        
        if A_SB_equip and (A_SB_equip != equipo_local and A_SB_equip != equipo_visitante):
            raise ValidationError({"A_SB_equip": "Debes elegir un equipo válido."})
        if B_SB_equip and (B_SB_equip != equipo_local and B_SB_equip != equipo_visitante):
            raise ValidationError({"B_SB_equip": "Debes elegir un equipo válido."})
        if C_SB_equip and (C_SB_equip != equipo_local and C_SB_equip != equipo_visitante):
            raise ValidationError({"C_SB_equip": "Debes elegir un equipo válido."})
        if D_SB_equip and (D_SB_equip != equipo_local and D_SB_equip != equipo_visitante):
            raise ValidationError({"D_SB_equip": "Debes elegir un equipo válido."})
        if E_SB_equip and (E_SB_equip != equipo_local and E_SB_equip != equipo_visitante):
            raise ValidationError({"E_SB_equip": "Debes elegir un equipo válido."})
        if F_SB_equip and (F_SB_equip != equipo_local and F_SB_equip != equipo_visitante):
            raise ValidationError({"F_SB_equip": "Debes elegir un equipo válido."})
        if G_SB_equip and (G_SB_equip != equipo_local and G_SB_equip != equipo_visitante):
            raise ValidationError({"G_SB_equip": "Debes elegir un equipo válido."})
        if H_SB_equip and (H_SB_equip != equipo_local and H_SB_equip != equipo_visitante):
            raise ValidationError({"H_SB_equip": "Debes elegir un equipo válido."})
        if I_SB_equip and (I_SB_equip != equipo_local and I_SB_equip != equipo_visitante):
            raise ValidationError({"I_SB_equip": "Debes elegir un equipo válido."})
        if J_SB_equip and (J_SB_equip != equipo_local and J_SB_equip != equipo_visitante):
            raise ValidationError({"J_SB_equip": "Debes elegir un equipo válido."})
        
        if A_MA and (A_MA != equipo_local and A_MA != equipo_visitante):
            raise ValidationError({"A_MA": "Debes elegir un equipo válido."})
        if B_MA and (B_MA != equipo_local and B_MA != equipo_visitante):
            raise ValidationError({"B_MA": "Debes elegir un equipo válido."})
        if C_MA and (C_MA != equipo_local and C_MA != equipo_visitante):
            raise ValidationError({"C_MA": "Debes elegir un equipo válido."})
        if D_MA and (D_MA != equipo_local and D_MA != equipo_visitante):
            raise ValidationError({"D_MA": "Debes elegir un equipo válido."})
        if E_MA and (E_MA != equipo_local and E_MA != equipo_visitante):
            raise ValidationError({"E_MA": "Debes elegir un equipo válido."})
        if F_MA and (F_MA != equipo_local and F_MA != equipo_visitante):
            raise ValidationError({"F_MA": "Debes elegir un equipo válido."})
        if G_MA and (G_MA != equipo_local and G_MA != equipo_visitante):
            raise ValidationError({"G_MA": "Debes elegir un equipo válido."})
        if H_MA and (H_MA != equipo_local and H_MA != equipo_visitante):
            raise ValidationError({"H_MA": "Debes elegir un equipo válido."})
        if I_MA and (I_MA != equipo_local and I_MA != equipo_visitante):
            raise ValidationError({"I_MA": "Debes elegir un equipo válido."})
        if J_MA and (J_MA != equipo_local and J_MA != equipo_visitante):
            raise ValidationError({"J_MA": "Debes elegir un equipo válido."})
        
        if A_BB and (A_BB != equipo_local and A_BB != equipo_visitante):
            raise ValidationError({"A_BB": "Debes elegir un equipo válido."})
        if B_BB and (B_BB != equipo_local and B_BB != equipo_visitante):
            raise ValidationError({"B_BB": "Debes elegir un equipo válido."})
        if C_BB and (C_BB != equipo_local and C_BB != equipo_visitante):
            raise ValidationError({"C_BB": "Debes elegir un equipo válido."})
        if D_BB and (D_BB != equipo_local and D_BB != equipo_visitante):
            raise ValidationError({"D_BB": "Debes elegir un equipo válido."})
        if E_BB and (E_BB != equipo_local and E_BB != equipo_visitante):
            raise ValidationError({"E_BB": "Debes elegir un equipo válido."})
        if F_BB and (F_BB != equipo_local and F_BB != equipo_visitante):
            raise ValidationError({"F_BB": "Debes elegir un equipo válido."})
        if G_BB and (G_BB != equipo_local and G_BB != equipo_visitante):
            raise ValidationError({"G_BB": "Debes elegir un equipo válido."})
        if H_BB and (H_BB != equipo_local and H_BB != equipo_visitante):
            raise ValidationError({"H_BB": "Debes elegir un equipo válido."})
        if I_BB and (I_BB != equipo_local and I_BB != equipo_visitante):
            raise ValidationError({"I_BB": "Debes elegir un equipo válido."})
        if J_BB and (J_BB != equipo_local and J_BB != equipo_visitante):
            raise ValidationError({"J_BB": "Debes elegir un equipo válido."})
         

        
        A_Total_punto = cleaned_data.get('A_total_punto')
        B_Total_punto = cleaned_data.get('B_total_punto')
        C_Total_punto = cleaned_data.get('C_total_punto')
        D_Total_punto = cleaned_data.get('D_total_punto')
        E_Total_punto = cleaned_data.get('E_total_punto')
        F_Total_punto = cleaned_data.get('F_total_punto')
        G_Total_punto = cleaned_data.get('G_total_punto')     
        H_Total_punto = cleaned_data.get('H_total_punto')
        I_Total_punto = cleaned_data.get('I_total_punto')
        J_Total_punto = cleaned_data.get('J_total_punto')
        
        A_SP_dif = cleaned_data.get('A_SP_dif')
        B_SP_dif = cleaned_data.get('B_SP_dif')
        C_SP_dif = cleaned_data.get('C_SP_dif')
        D_SP_dif = cleaned_data.get('D_SP_dif')
        E_SP_dif = cleaned_data.get('E_SP_dif')
        F_SP_dif = cleaned_data.get('F_SP_dif')
        G_SP_dif = cleaned_data.get('G_SP_dif')
        H_SP_dif = cleaned_data.get('H_SP_dif')
        I_SP_dif = cleaned_data.get('I_SP_dif')
        J_SP_dif = cleaned_data.get('J_SP_dif')
        
        
        if A_Total_punto and (A_Total_punto < 0 ):
            raise ValidationError({"A_Total_punto": "Introdusca un valor válido."})
        if B_Total_punto and (B_Total_punto < 0 ):
            raise ValidationError({"B_Total_punto": "Introdusca un valor válido."})
        if C_Total_punto and (C_Total_punto < 0 ):
            raise ValidationError({"C_Total_punto": "Introdusca un valor válido."})
        if D_Total_punto and (D_Total_punto < 0 ):
            raise ValidationError({"D_Total_punto": "Introdusca un valor válido."})
        if E_Total_punto and (E_Total_punto < 0 ):
            raise ValidationError({"E_Total_punto": "Introdusca un valor válido."})
        if F_Total_punto and (F_Total_punto < 0 ):
            raise ValidationError({"F_Total_punto": "Introdusca un valor válido."})
        if G_Total_punto and (G_Total_punto < 0 ):
            raise ValidationError({"G_Total_punto": "Introdusca un valor válido."})
        if H_Total_punto and (H_Total_punto < 0 ):
            raise ValidationError({"H_Total_punto": "Introdusca un valor válido."})
        if I_Total_punto and (I_Total_punto < 0 ):
            raise ValidationError({"I_Total_punto": "Introdusca un valor válido."})
        if J_Total_punto and (J_Total_punto < 0 ):
            raise ValidationError({"J_Total_punto": "Introdusca un valor válido."})
        
        if A_SP_dif and (A_SP_dif < 0 ):
            raise ValidationError({"A_SP_dif": "Introdusca un valor válido."})
        if B_SP_dif and (B_SP_dif < 0 ):
            raise ValidationError({"B_SP_dif": "Introdusca un valor válido."})
        if C_SP_dif and (C_SP_dif < 0 ):
            raise ValidationError({"C_SP_dif": "Introdusca un valor válido."})
        if D_SP_dif and (D_SP_dif < 0 ):
            raise ValidationError({"D_SP_dif": "Introdusca un valor válido."})
        if E_SP_dif and (E_SP_dif < 0 ):
            raise ValidationError({"E_SP_dif": "Introdusca un valor válido."})
        if F_SP_dif and (F_SP_dif < 0 ):
            raise ValidationError({"F_SP_dif": "Introdusca un valor válido."})
        if G_SP_dif and (G_SP_dif < 0 ):
            raise ValidationError({"G_SP_dif": "Introdusca un valor válido."})
        if H_SP_dif and (H_SP_dif < 0 ):
            raise ValidationError({"H_SP_dif": "Introdusca un valor válido."})
        if I_SP_dif and (I_SP_dif < 0 ):
            raise ValidationError({"I_SP_dif": "Introdusca un valor válido."})
        if J_SP_dif and (J_SP_dif < 0 ):
            raise ValidationError({"J_SP_dif": "Introdusca un valor válido."})
        
        return cleaned_data
    
    
    
    
    

class resultado_futbol_form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    class Meta:
        model = futbol
        fields = ['resultado', 'ganador']
        widgets = {
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
        }

    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data 
    
    
    
    
    
class resultado_NBA_Profecional_form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    class Meta:
        model = NBA_Profecional
        fields = ['resultado', 'ganador']
        widgets = {
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
        }

    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data 
    

class resultado_NBA_Colegial_form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    class Meta:
        model = NBA_Colegial
        fields = ['resultado', 'ganador']
        widgets = {
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
        }

    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data 
    
    
    
    
class resultado_baseball_form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    class Meta:
        model = Baseball
        fields = ['resultado', 'ganador']
        widgets = {
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
        }

    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data    
    
    
    
class resultado_NLF_Profecional_form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    class Meta:
        model = NLF_Profecional
        fields = ['resultado', 'ganador']
        widgets = {
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
        }

    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data   
    
    
    
    
class resultado_NLF_Colegial_form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    class Meta:
        model = NLF_Colegial
        fields = ['resultado', 'ganador']
        widgets = {
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
        }

    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data   
    
    
    
    
    
    
class resultado_Hockey_form(forms.ModelForm):
    resultado = forms.CharField(validators=[resultado_validator])
    class Meta:
        model = Hockey
        fields = ['resultado', 'ganador']
        widgets = {
            'resultado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#-#' }),
            'ganador': forms.Select(attrs={'class':'form-control', 'placeholder': '' }),
        }

    def clean(self):
        cleaned_data = super().clean()
        resultado = cleaned_data.get('resultado')
        ganador = cleaned_data.get('ganador')

        # Verificar si el resultado es un empate
        if resultado:
            partes = resultado.split('-')
            if len(partes) == 2 and partes[0] == partes[1]:
                if ganador != 'Empate':
                    self.add_error('ganador', 'Para un empate, el ganador debe ser "Empate".')
            else:
                if ganador == 'Empate':
                    self.add_error('ganador', 'No se puede seleccionar "Empate" si el resultado no es un empate.')

        return cleaned_data   
    
    
    
    


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=254)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
