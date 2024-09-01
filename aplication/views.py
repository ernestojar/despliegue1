from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms  import  *
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required
def index(request):
    return render(request,"index.html")

def logout(request):
    logout(request)
    return redirect('/')

@login_required
def Futbol_def (request):
    return render(request,"Futbol/futbol.html")

@login_required
def Baseball_def (request):
    return render(request,"Baseball/baseball.html")

@login_required
def NBA_profecional_def (request):
    return render(request,"NBA_Profecional/NBA_profecional.html")

@login_required
def NBA_colegial_def (request):
    return render(request,"NBA_Colegial/NBA_colegial.html")

@login_required
def NLF_profecional_def (request):
    return render(request,"NLF_Profecional/NLF_profecional.html")

@login_required
def NLF_colegial_def (request):
    return render(request,"NLF_Colegial/NLF_colegial.html")

@login_required
def Hockey_def (request):
    return render(request,"Hockey/hockey.html")



# Futbol

def Crear_Futbol(request):
    if request.method == 'POST':
        formulario = futbol_form(request.POST)
        if formulario.is_valid():
            formulario.clean()
            objeto_creado = formulario.save()
            
          
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = futbol.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = futbol.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = futbol.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = futbol.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'Futbol/informes.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,  'formulario':formulario, 'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })
       
        else:
            return render(request, 'Futbol/crear_futbol.html', {'formulario': formulario})
    else:
        formulario = futbol_form()
        return render(request, 'Futbol/crear_futbol.html', {'formulario': formulario})

def Modificar_Futbol(request, id):
    f = futbol.objects.get(id=id)
    formulario =  futbol_form (request.POST or None, request.FILES or None, instance=f)
    if formulario.is_valid():
        formulario.save()
        return redirect('listar_futbol')
    return render(request, 'Futbol/modificar_futbol.html', {'formulario': formulario})

def Listar_Futbol(request):
    futbols =futbol.objects.all().order_by('fecha')
    return render(request, 'Futbol/listar_futbol.html', {'lista':futbols} )

def Eliminar_Futbol(request, id):
    f = get_object_or_404(futbol, id=id)
    f.delete()
    return redirect('listar_futbol')

def Buscar_futbol(request):
    resultados = []
    if request.method == 'POST':
        termino_busqueda = request.POST.get('searchbar')
        
        if termino_busqueda:
            # Construye condiciones para buscar en el nombre del equipo local o visitante
            condiciones = (
                Q(equipo_local__nombre__icontains=termino_busqueda) |
                Q(equipo_visitante__nombre__icontains=termino_busqueda)
            )
            
            # Filtra los resultados basándose en las condiciones construidas
            resultados = futbol.objects.filter(condiciones)
        

        return render(request, 'Futbol/resultados.html', {'resultados': resultados})
    return render(request, 'Futbol/listar_futbol.html')

def Resultado_Futbol(request, id):
    f = futbol.objects.get(id=id)
    
    equipo_local = f.equipo_local.nombre
    equipo_visitante = f.equipo_visitante.nombre
    opciones_ganador = [ equipo_local,equipo_visitante,'Empate' ]
    
    if request.method == 'POST':
        form = resultado_futbol_form(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return redirect('listar_futbol')
    else:
        form = resultado_futbol_form( instance=f)

    return render(request, 'Futbol/resultado_futbol.html', {'form': form,'opciones_ganador': opciones_ganador})

def Informe_Resultado(request, id):
            objeto_creado = futbol.objects.get(id=id)
    
    
   
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = futbol.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = futbol.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = futbol.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = futbol.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'Futbol/informe_lista.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })

def extraer_valores_de_resultado(partido):
    valores_entre_hashes = partido.resultado.strip('#').split('-')
    
    valor_izquierdo = int(valores_entre_hashes[0]) if valores_entre_hashes[0].isdigit() else None
    valor_derecho = int(valores_entre_hashes[1]) if len(valores_entre_hashes) > 1 and valores_entre_hashes[1].isdigit() else None
   
    valor_izquierdo_variable = valor_izquierdo
    valor_derecho_variable = valor_derecho
    
    return valor_izquierdo_variable, valor_derecho_variable

def Resultados_Sistemas(request):
    
    partidos_filtrados = futbol.objects.exclude(ganador__isnull=True).exclude(resultado__isnull=True)
    partidos = partidos_filtrados.order_by('-fecha')[:20]
    
    
    #Sistema A
    
    ganador=''
    cont_A_ML=0
    cont_A_SP=0
    cont_A_Ud=0
    cont_A_SB=0
    cont_A_MA=0
    cont_A_BB=0
    cont_A_Total=0
    A_cont=0
    A_cont1=0
    A_cont2=0
    A_cont3=0
    A_cont4=0
    A_cont5=0
    A_cont6=0
    sum=0
    res=0
    valor_izquierdo=0
    valor_derecho=0
    A_prom=0
    A_prom1=0
    A_prom2=0
    A_prom3=0
    A_prom4=0 
    A_prom5=0
    A_prom6=0
    
    for valor in partidos: 
        
        ganador=valor.ganador
        
        valor_izquierdo, valor_derecho = extraer_valores_de_resultado(valor)
        sum= valor_izquierdo+valor_derecho
        
        if valor.A_ML_equip is not None:
           A_cont+=1
           if ganador==valor.A_ML_equip.nombre:
              cont_A_ML+=1 
              
              
        if valor.A_Ud_equip is not None:
           A_cont1+=1      
           if ganador==valor.A_Ud_equip.nombre:
              cont_A_Ud+=1
              
              
        if valor.A_SB_equip is not None: 
           A_cont2+=1      
           if ganador==valor.A_SB_equip.nombre:
              cont_A_SB+=1
              
              
        if valor.A_MA is not None:
           A_cont3+=1 
           if ganador==valor.A_MA.nombre:
              cont_A_MA+=1
              
              
        if valor.A_BB is not None:  
           A_cont4+=1 
           if ganador==valor.A_BB.nombre:
              cont_A_BB+=1
         
         
        if valor.A_total_punto is not None: 
           A_cont5+=1 
           if sum>valor.A_total_punto and valor.A_Total_OU=='OVER':
              cont_A_Total+=1
           if sum<=valor.A_total_punto and valor.A_Total_OU=='UNDER':
              cont_A_Total+=1
         
         
       
        if valor_izquierdo>valor_derecho:
            res=valor_izquierdo-valor_derecho
           
        elif valor_izquierdo<valor_derecho:
            res=valor_derecho-valor_izquierdo 
        
        else: 
            res=0
        
        if valor.A_SP_dif is not None:
           A_cont6+=1
           if ganador==valor.A_SP_equip.nombre and res>valor.A_SP_dif :
              cont_A_SP+=1
           
           
           
    if cont_A_ML !=0 and A_cont !=0:
           A_prom=cont_A_ML*100/A_cont
        
    if cont_A_SP !=0 and A_cont6 !=0:
           A_prom6=cont_A_SP*100/A_cont6
           
    if cont_A_Ud !=0 and A_cont1 !=0:
           A_prom1=cont_A_Ud*100/A_cont1
           
    if cont_A_SB !=0 and A_cont2 !=0:
           A_prom2=cont_A_SB*100/A_cont2
           
    if cont_A_MA !=0 and A_cont3 !=0:
           A_prom3=cont_A_MA*100/A_cont3
           
    if cont_A_BB !=0 and A_cont4 !=0:
           A_prom4=cont_A_BB*100/A_cont5
           
    if cont_A_Total !=0 and A_cont5 !=0:
           A_prom5=cont_A_Total*100/A_cont5      
           
           
           
    #Sistema B     
    
    B_ganador=''
    cont_B_ML=0
    cont_B_SP=0
    cont_B_Ud=0
    cont_B_SB=0
    cont_B_MA=0
    cont_B_BB=0
    cont_B_Total=0
    B_cont=0
    B_cont1=0
    B_cont2=0
    B_cont3=0
    B_cont4=0
    B_cont5=0
    B_cont6=0
    B_sum=0
    B_res=0
    B_valor_izquierdo=0
    B_valor_derecho=0
    B_prom=0
    B_prom1=0
    B_prom2=0
    B_prom3=0
    B_prom4=0 
    B_prom5=0
    B_prom6=0
    
    for valor in partidos: 
        
        B_ganador=valor.ganador
        
        B_valor_izquierdo, B_valor_derecho = extraer_valores_de_resultado(valor)
        B_sum= B_valor_izquierdo+B_valor_derecho
        
        if valor.B_ML_equip is not None:
           B_cont+=1
           if B_ganador==valor.B_ML_equip.nombre:
              cont_B_ML+=1 
              
              
        if valor.B_Ud_equip is not None:
           B_cont1+=1      
           if B_ganador==valor.B_Ud_equip.nombre:
              cont_B_Ud+=1
              
              
        if valor.B_SB_equip is not None: 
           B_cont2+=1      
           if B_ganador==valor.B_SB_equip.nombre:
              cont_B_SB+=1
              
              
        if valor.B_MA is not None:
           B_cont3+=1 
           if B_ganador==valor.B_MA.nombre:
              cont_B_MA+=1
              
              
        if valor.B_BB is not None:  
           B_cont4+=1 
           if B_ganador==valor.B_BB.nombre:
              cont_B_BB+=1
         
         
        if valor.B_total_punto is not None: 
           B_cont5+=1 
           if B_sum>valor.B_total_punto and valor.B_Total_OU=='OVER':
              cont_B_Total+=1
           if B_sum<=valor.B_total_punto and valor.B_Total_OU=='UNDER':
              cont_B_Total+=1
         
         
       
        if B_valor_izquierdo>B_valor_derecho:
            B_res=B_valor_izquierdo-B_valor_derecho
           
        elif B_valor_izquierdo<B_valor_derecho:
            B_res=B_valor_derecho-B_valor_izquierdo 
        
        else: 
            B_res=0
        
        if valor.B_SP_dif is not None:
           B_cont6+=1
           if B_ganador==valor.B_SP_equip.nombre and B_res>valor.B_SP_dif :
              cont_B_SP+=1
           
           
           
    if cont_B_ML !=0 and B_cont !=0:
           B_prom=cont_B_ML*100/B_cont
        
    if cont_B_SP !=0 and B_cont6 !=0:
           B_prom6=cont_B_SP*100/B_cont6
           
    if cont_B_Ud !=0 and B_cont1 !=0:
           B_prom1=cont_B_Ud*100/B_cont1
           
    if cont_B_SB !=0 and B_cont2 !=0:
           B_prom2=cont_B_SB*100/B_cont2
           
    if cont_B_MA !=0 and B_cont3 !=0:
           B_prom3=cont_B_MA*100/B_cont3
           
    if cont_B_BB !=0 and B_cont4 !=0:
           B_prom4=cont_B_BB*100/B_cont5
           
    if cont_B_Total !=0 and B_cont5 !=0:
           B_prom5=cont_B_Total*100/B_cont5             
           
           
    C_ganador=''
    cont_C_ML=0
    cont_C_SP=0
    cont_C_Ud=0
    cont_C_SB=0
    cont_C_MA=0
    cont_C_BB=0
    cont_C_Total=0
    C_cont=0
    C_cont1=0
    C_cont2=0
    C_cont3=0
    C_cont4=0
    C_cont5=0
    C_cont6=0
    C_sum=0
    C_res=0
    C_valor_izquierdo=0
    C_valor_derecho=0
    C_prom=0
    C_prom1=0
    C_prom2=0
    C_prom3=0
    C_prom4=0 
    C_prom5=0        
    C_prom6=0
       
    for valor in partidos: 
        
        C_ganador=valor.ganador
            
        C_valor_izquierdo, C_valor_derecho = extraer_valores_de_resultado(valor)
        C_sum= C_valor_izquierdo+C_valor_derecho
            
        if valor.C_ML_equip is not None:
            C_cont+=1
            if C_ganador==valor.C_ML_equip.nombre:
                cont_C_ML+=1 
                
        if valor.C_Ud_equip is not None:
            C_cont1+=1      
            if C_ganador==valor.C_Ud_equip.nombre:
                cont_C_Ud+=1
                
        if valor.C_SB_equip is not None: 
            C_cont2+=1      
            if C_ganador==valor.C_SB_equip.nombre:
                cont_C_SB+=1
                
        if valor.C_MA is not None:
            C_cont3+=1 
            if C_ganador==valor.C_MA.nombre:
                cont_C_MA+=1
                
        if valor.C_BB is not None:  
            C_cont4+=1 
            if C_ganador==valor.C_BB.nombre:
                cont_C_BB+=1
            
            
        if valor.C_total_punto is not None: 
            C_cont5+=1 
            if C_sum>valor.C_total_punto and valor.C_Total_OU=='OVER':
                cont_C_Total+=1
            if C_sum<=valor.C_total_punto and valor.C_Total_OU=='UNDER':
                cont_C_Total+=1
            
            

        if C_valor_izquierdo>C_valor_derecho:
            C_res=C_valor_izquierdo-C_valor_derecho
            
        elif C_valor_izquierdo<C_valor_derecho:
            C_res=C_valor_derecho-C_valor_izquierdo 

        else: 
            C_res=0
            
        if valor.C_SP_dif is not None:
            C_cont6+=1
            if C_ganador==valor.C_SP_equip.nombre and C_res>valor.C_SP_dif :
                cont_C_SP+=1
           
           
    if cont_C_ML !=0 and C_cont !=0:
       C_prom=cont_C_ML*100/C_cont
            
    if cont_C_SP !=0 and C_cont6 !=0:
       C_prom6=cont_C_SP*100/C_cont6
            
    if cont_C_Ud !=0 and C_cont1 !=0:
       C_prom1=cont_C_Ud*100/C_cont1
            
    if cont_C_SB !=0 and C_cont2 !=0:
       C_prom2=cont_C_SB*100/C_cont2
            
    if cont_C_MA !=0 and C_cont3 !=0:
       C_prom3=cont_C_MA*100/C_cont3
            
    if cont_C_BB !=0 and C_cont4 !=0:
       C_prom4=cont_C_BB*100/C_cont5
            
    if cont_C_Total !=0 and C_cont5 !=0:
       C_prom5=cont_C_Total*100/C_cont5       
           
    
    
    D_ganador=''
    cont_D_ML=0
    cont_D_SP=0
    cont_D_Ud=0
    cont_D_SB=0
    cont_D_MA=0
    cont_D_BB=0
    cont_D_Total=0
    D_cont=0
    D_cont1=0
    D_cont2=0
    D_cont3=0
    D_cont4=0
    D_cont5=0
    D_cont6=0
    D_sum=0
    D_res=0
    D_valor_izquierdo=0
    D_valor_derecho=0
    D_prom=0
    D_prom1=0
    D_prom2=0
    D_prom3=0
    D_prom4=0 
    D_prom5=0        
    D_prom6=0

    
    
    
    for valor in partidos: 
        
        D_ganador=valor.ganador
            
        D_valor_izquierdo, D_valor_derecho = extraer_valores_de_resultado(valor)
        D_sum= D_valor_izquierdo+D_valor_derecho
            
        if valor.D_ML_equip is not None:
           D_cont+=1
           if D_ganador==valor.D_ML_equip.nombre:
              cont_D_ML+=1 
            
        if valor.D_Ud_equip is not None:
           D_cont1+=1      
           if D_ganador==valor.D_Ud_equip.nombre:
              cont_D_Ud+=1
            
        if valor.D_SB_equip is not None: 
           D_cont2+=1      
           if D_ganador==valor.D_SB_equip.nombre:
              cont_D_SB+=1
            
        if valor.D_MA is not None:
           D_cont3+=1 
           if D_ganador==valor.D_MA.nombre:
              cont_D_MA+=1
            
        if valor.D_BB is not None:  
           D_cont4+=1 
           if D_ganador==valor.D_BB.nombre:
              cont_D_BB+=1
        
        
        if valor.D_total_punto is not None: 
           D_cont5+=1 
           if D_sum>valor.D_total_punto and valor.D_Total_OU=='OVER':
              cont_D_Total+=1
           if D_sum<=valor.D_total_punto and valor.D_Total_OU=='UNDER':
              cont_D_Total+=1
        
        
    
        if D_valor_izquierdo>D_valor_derecho:
            D_res=D_valor_izquierdo-D_valor_derecho
        
        elif D_valor_izquierdo<D_valor_derecho:
            D_res=D_valor_derecho-D_valor_izquierdo 
        
        else: 
            D_res=0
            
        if valor.D_SP_dif is not None:
           D_cont6+=1
           if D_ganador==valor.D_SP_equip.nombre and D_res>valor.D_SP_dif :
              cont_D_SP+=1
             
           
    if cont_D_ML !=0 and D_cont !=0:
       D_prom=cont_D_ML*100/D_cont
            
    if cont_D_SP !=0 and D_cont6 !=0:
       D_prom6=cont_D_SP*100/D_cont6
            
    if cont_D_Ud !=0 and D_cont1 !=0:
       D_prom1=cont_D_Ud*100/D_cont1
            
    if cont_D_SB !=0 and D_cont2 !=0:
       D_prom2=cont_D_SB*100/D_cont2
            
    if cont_D_MA !=0 and D_cont3 !=0:
       D_prom3=cont_D_MA*100/D_cont3
            
    if cont_D_BB !=0 and D_cont4 !=0:
       D_prom4=cont_D_BB*100/D_cont5
            
    if cont_D_Total !=0 and D_cont5 !=0:
       D_prom5=cont_D_Total*100/D_cont5
        
    
    E_ganador=''
    cont_E_ML=0
    cont_E_SP=0
    cont_E_Ud=0
    cont_E_SB=0
    cont_E_MA=0
    cont_E_BB=0
    cont_E_Total=0
    E_cont=0
    E_cont1=0
    E_cont2=0
    E_cont3=0
    E_cont4=0
    E_cont5=0
    E_cont6=0
    E_sum=0
    E_res=0
    E_valor_izquierdo=0
    E_valor_derecho=0
    E_prom=0
    E_prom1=0
    E_prom2=0
    E_prom3=0
    E_prom4=0 
    E_prom5=0        
    E_prom6=0
       
    for valor in partidos: 
        
        E_ganador=valor.ganador
            
        E_valor_izquierdo, E_valor_derecho = extraer_valores_de_resultado(valor)
        E_sum= E_valor_izquierdo+E_valor_derecho
            
        if valor.E_ML_equip is not None:
           E_cont+=1
           if E_ganador==valor.E_ML_equip.nombre:
              cont_E_ML+=1 
            
        if valor.E_Ud_equip is not None:
           E_cont1+=1      
           if E_ganador==valor.E_Ud_equip.nombre:
              cont_E_Ud+=1
            
        if valor.E_SB_equip is not None: 
           E_cont2+=1      
           if E_ganador==valor.E_SB_equip.nombre:
              cont_E_SB+=1
            
        if valor.E_MA is not None:
           E_cont3+=1 
           if E_ganador==valor.E_MA.nombre:
              cont_E_MA+=1
            
        if valor.E_BB is not None:  
           E_cont4+=1 
           if E_ganador==valor.E_BB.nombre:
              cont_E_BB+=1
        
        
        if valor.E_total_punto is not None: 
           E_cont5+=1 
           if E_sum>valor.E_total_punto and valor.E_Total_OU=='OVER':
              cont_E_Total+=1
           if E_sum<=valor.E_total_punto and valor.E_Total_OU=='UNDER':
              cont_E_Total+=1
        
        
    
        if E_valor_izquierdo>E_valor_derecho:
            E_res=E_valor_izquierdo-E_valor_derecho
        
        elif E_valor_izquierdo<E_valor_derecho:
            E_res=E_valor_derecho-E_valor_izquierdo 
        
        else: 
            E_res=0
            
        if valor.E_SP_dif is not None:
           E_cont6+=1
           if E_ganador==valor.E_SP_equip.nombre and E_res>valor.E_SP_dif :
              cont_E_SP+=1
            
           
    if cont_E_ML !=0 and E_cont !=0:
       E_prom=cont_E_ML*100/E_cont
            
    if cont_E_SP !=0 and E_cont6 !=0:
       E_prom6=cont_E_SP*100/E_cont6
            
    if cont_E_Ud !=0 and E_cont1 !=0:
       E_prom1=cont_E_Ud*100/E_cont1   
        
    if cont_E_SB !=0 and E_cont2 !=0:
       E_prom2=cont_E_SB*100/E_cont2
            
    if cont_E_MA !=0 and E_cont3 !=0:
       E_prom3=cont_E_MA*100/E_cont3
            
    if cont_E_BB !=0 and E_cont4 !=0:
       E_prom4=cont_E_BB*100/E_cont5
            
    if cont_E_Total !=0 and E_cont5 !=0:
       E_prom5=cont_E_Total*100/E_cont5     
    
    
    
    
    F_ganador=''
    cont_F_ML=0
    cont_F_SP=0
    cont_F_Ud=0
    cont_F_SB=0
    cont_F_MA=0
    cont_F_BB=0
    cont_F_Total=0
    F_cont=0
    F_cont1=0
    F_cont2=0
    F_cont3=0
    F_cont4=0
    F_cont5=0
    F_cont6=0
    F_sum=0
    F_res=0
    F_valor_izquierdo=0
    F_valor_derecho=0
    F_prom=0
    F_prom1=0
    F_prom2=0
    F_prom3=0
    F_prom4=0 
    F_prom5=0        
    F_prom6=0
       
    
    for valor in partidos: 
        
 
        F_valor_izquierdo, F_valor_derecho = extraer_valores_de_resultado(valor)
        F_sum = F_valor_izquierdo + F_valor_derecho
                
        if valor.F_ML_equip is not None:
           F_cont+=1
           if F_ganador==valor.F_ML_equip.nombre:
              F_cont_ML+=1 
                
        if valor.F_Ud_equip is not None:
           F_cont1+=1      
           if F_ganador==valor.F_Ud_equip.nombre:
              F_cont_Ud+=1
                
        if valor.F_SB_equip is not None: 
           F_cont2+=1      
           if F_ganador==valor.F_SB_equip.nombre:
              F_cont_SB+=1
                
        if valor.F_MA is not None:
           F_cont3+=1 
           if F_ganador==valor.F_MA.nombre:
              F_cont_MA+=1
                
        if valor.F_BB is not None:  
           F_cont4+=1 
           if F_ganador==valor.F_BB.nombre:
              F_cont_BB+=1
            
            
        if valor.F_total_punto is not None: 
           F_cont5+=1 
           if F_sum>F_valor_izquierdo and valor.F_Total_OU=='OVER':
              F_cont_Total+=1
           if F_sum<=valor.F_total_punto and valor.F_Total_OU=='UNDER':
              F_cont_Total+=1
            
            
        if F_valor_izquierdo>F_valor_derecho:
            F_res=F_valor_izquierdo-F_valor_derecho
            
        elif F_valor_izquierdo<F_valor_derecho:
            F_res=F_valor_derecho-F_valor_izquierdo 
        
        else: 
            F_res=0
                
        if valor.F_SP_dif is not None:
           F_cont6+=1
           if F_ganador==valor.F_SP_equip.nombre and F_res>valor.F_SP_dif :
              F_cont_SP+=1
            
           
    if cont_F_ML !=0 and F_cont !=0:
       F_prom=F_cont_ML*100/F_cont
                
    if cont_F_SP !=0 and F_cont6 !=0:
       F_prom6=F_cont_SP*100/F_cont6
                
    if cont_F_Ud !=0 and F_cont1 !=0:
       F_prom1=F_cont_Ud*100/F_cont1   
            
    if cont_F_SB !=0 and F_cont2 !=0:
       F_prom2=F_cont_SB*100/F_cont2
                
    if cont_F_MA !=0 and F_cont3 !=0:
       F_prom3=F_cont_MA*100/F_cont3
                
    if cont_F_BB !=0 and F_cont4 !=0:
       F_prom4=F_cont_BB*100/F_cont5
                
    if cont_F_Total !=0 and F_cont5 !=0:
       F_prom5=F_cont_Total*100/F_cont5
        
    
    G_ganador=''
    cont_G_ML=0
    cont_G_SP=0
    cont_G_Ud=0
    cont_G_SB=0
    cont_G_MA=0
    cont_G_BB=0
    cont_G_Total=0
    G_cont=0
    G_cont1=0
    G_cont2=0
    G_cont3=0
    G_cont4=0
    G_cont5=0
    G_cont6=0
    G_sum=0
    G_res=0
    G_valor_izquierdo=0
    G_valor_derecho=0
    G_prom=0
    G_prom1=0
    G_prom2=0
    G_prom3=0
    G_prom4=0 
    G_prom5=0        
    G_prom6=0

    for valor in partidos: 
        
        G_valor_izquierdo, G_valor_derecho = extraer_valores_de_resultado(valor)
        G_sum = G_valor_izquierdo + G_valor_derecho
                    
        if valor.G_ML_equip is not None:
           G_cont+=1
           if G_ganador==valor.G_ML_equip.nombre:
              G_cont_ML+=1 
                    
        if valor.G_Ud_equip is not None:
           G_cont1+=1      
           if G_ganador==valor.G_Ud_equip.nombre:
              G_cont_Ud+=1
                    
        if valor.G_SB_equip is not None: 
           G_cont2+=1      
           if G_ganador==valor.G_SB_equip.nombre:
              G_cont_SB+=1
                    
        if valor.G_MA is not None:
           G_cont3+=1 
           if G_ganador==valor.G_MA.nombre:
              G_cont_MA+=1
                    
        if valor.G_BB is not None:  
           G_cont4+=1 
           if G_ganador==valor.G_BB.nombre:
              G_cont_BB+=1
                
                
        if valor.G_total_punto is not None: 
           G_cont5+=1 
           if G_sum>G_valor_izquierdo and valor.G_Total_OU=='OVER':
              G_cont_Total+=1
           if G_sum<=valor.G_total_punto and valor.G_Total_OU=='UNDER':
              G_cont_Total+=1
                
                
        if G_valor_izquierdo>G_valor_derecho:
            G_res=G_valor_izquierdo-G_valor_derecho
                
        elif G_valor_izquierdo<G_valor_derecho:
            G_res=G_valor_derecho-G_valor_izquierdo 
            
        else: 
            G_res=0
                    
        if valor.G_SP_dif is not None:
           G_cont6+=1
           if G_ganador==valor.G_SP_equip.nombre and G_res>valor.G_SP_dif :
              G_cont_SP+=1
            
           
    if cont_G_ML !=0 and G_cont !=0:
       G_prom=G_cont_ML*100/G_cont
                    
    if cont_G_SP !=0 and G_cont6 !=0:
       G_prom6=G_cont_SP*100/G_cont6
                    
    if cont_G_Ud !=0 and G_cont1 !=0:
       G_prom1=G_cont_Ud*100/G_cont1   
                
    if cont_G_SB !=0 and G_cont2 !=0:
       G_prom2=G_cont_SB*100/G_cont2
                    
    if cont_G_MA !=0 and G_cont3 !=0:
       G_prom3=G_cont_MA*100/G_cont3
                    
    if cont_G_BB !=0 and G_cont4 !=0:
       G_prom4=G_cont_BB*100/G_cont5
                    
    if cont_G_Total !=0 and G_cont5 !=0:
       G_prom5=G_cont_Total*100/G_cont5
            
            
            
    H_ganador=''
    cont_H_ML=0
    cont_H_SP=0
    cont_H_Ud=0
    cont_H_SB=0
    cont_H_MA=0
    cont_H_BB=0
    cont_H_Total=0
    H_cont=0
    H_cont1=0
    H_cont2=0
    H_cont3=0
    H_cont4=0
    H_cont5=0
    H_cont6=0
    H_sum=0
    H_res=0
    H_valor_izquierdo=0
    H_valor_derecho=0
    H_prom=0
    H_prom1=0
    H_prom2=0
    H_prom3=0
    H_prom4=0 
    H_prom5=0        
    H_prom6=0
        
            
    for valor in partidos: 
        
        H_valor_izquierdo, H_valor_derecho = extraer_valores_de_resultado(valor)
        H_sum = H_valor_izquierdo + H_valor_derecho
                        
        if valor.H_ML_equip is not None:
           H_cont+=1
           if H_ganador==valor.H_ML_equip.nombre:
              H_cont_ML+=1 
                        
        if valor.H_Ud_equip is not None:
           H_cont1+=1      
           if H_ganador==valor.H_Ud_equip.nombre:
              H_cont_Ud+=1
                        
        if valor.H_SB_equip is not None: 
           H_cont2+=1      
           if H_ganador==valor.H_SB_equip.nombre:
              H_cont_SB+=1
                        
        if valor.H_MA is not None:
           H_cont3+=1 
           if H_ganador==valor.H_MA.nombre:
              H_cont_MA+=1
                        
        if valor.H_BB is not None:  
           H_cont4+=1 
           if H_ganador==valor.H_BB.nombre:
              H_cont_BB+=1
                    
                    
        if valor.H_total_punto is not None: 
           H_cont5+=1 
           if H_sum>H_valor_izquierdo and valor.H_Total_OU=='OVER':
              H_cont_Total+=1
           if H_sum<=valor.H_total_punto and valor.H_Total_OU=='UNDER':
              H_cont_Total+=1
                    
                    
        if H_valor_izquierdo>H_valor_derecho:
                H_res=H_valor_izquierdo-H_valor_derecho
                    
        elif H_valor_izquierdo<H_valor_derecho:
                H_res=H_valor_derecho-H_valor_izquierdo 
                
        else: 
                H_res=0
                        
        if valor.H_SP_dif is not None:
           H_cont6+=1
           if H_ganador==valor.H_SP_equip.nombre and H_res>valor.H_SP_dif :
              H_cont_SP+=1
            
           
    if cont_H_ML !=0 and H_cont !=0:
       H_prom=H_cont_ML*100/H_cont
                    
    if cont_H_SP !=0 and H_cont6 !=0:
       H_prom6=H_cont_SP*100/H_cont6
                    
    if cont_H_Ud !=0 and H_cont1 !=0:
       H_prom1=H_cont_Ud*100/H_cont1   
                
    if cont_H_SB !=0 and H_cont2 !=0:
       H_prom2=H_cont_SB*100/H_cont2
                    
    if cont_H_MA !=0 and H_cont3 !=0:
       H_prom3=H_cont_MA*100/H_cont3
                    
    if cont_H_BB !=0 and H_cont4 !=0:
       H_prom4=H_cont_BB*100/H_cont5
                    
    if cont_H_Total !=0 and H_cont5 !=0:
       H_prom5=H_cont_Total*100/H_cont5        
            
    
    
    I_ganador=''
    cont_I_ML=0
    cont_I_SP=0
    cont_I_Ud=0
    cont_I_SB=0
    cont_I_MA=0
    cont_I_BB=0
    cont_I_Total=0
    I_cont=0
    I_cont1=0
    I_cont2=0
    I_cont3=0
    I_cont4=0
    I_cont5=0
    I_cont6=0
    I_sum=0
    I_res=0
    I_valor_izquierdo=0
    I_valor_derecho=0
    I_prom=0
    I_prom1=0
    I_prom2=0
    I_prom3=0
    I_prom4=0 
    I_prom5=0        
    I_prom6=0
        
            
    for valor in partidos: 
        
        I_valor_izquierdo, I_valor_derecho = extraer_valores_de_resultado(valor)
        I_sum = I_valor_izquierdo + I_valor_derecho
                        
        if valor.I_ML_equip is not None:
           I_cont+=1
           if I_ganador==valor.I_ML_equip.nombre:
              I_cont_ML+=1 
                        
        if valor.I_Ud_equip is not None:
           I_cont1+=1      
           if I_ganador==valor.I_Ud_equip.nombre:
              I_cont_Ud+=1
                        
        if valor.I_SB_equip is not None: 
           I_cont2+=1      
           if I_ganador==valor.I_SB_equip.nombre:
              I_cont_SB+=1
                        
        if valor.I_MA is not None:
           I_cont3+=1 
           if I_ganador==valor.I_MA.nombre:
              I_cont_MA+=1
                        
        if valor.I_BB is not None:  
           I_cont4+=1 
           if I_ganador==valor.I_BB.nombre:
              I_cont_BB+=1
                    
                    
        if valor.I_total_punto is not None: 
           I_cont5+=1 
           if I_sum>I_valor_izquierdo and valor.I_Total_OU=='OVER':
              I_cont_Total+=1
           if I_sum<=valor.I_total_punto and valor.I_Total_OU=='UNDER':
              I_cont_Total+=1
                    
                    
        if I_valor_izquierdo>I_valor_derecho:
                I_res=I_valor_izquierdo-I_valor_derecho
                    
        elif I_valor_izquierdo<I_valor_derecho:
                I_res=I_valor_derecho-I_valor_izquierdo 
                
        else: 
                I_res=0
                        
        if valor.I_SP_dif is not None:
           I_cont6+=1
           if I_ganador==valor.I_SP_equip.nombre and I_res>valor.I_SP_dif :
              I_cont_SP+=1
            
           
    if cont_I_ML !=0 and I_cont !=0:
       I_prom=I_cont_ML*100/I_cont
                        
    if cont_I_SP !=0 and I_cont6 !=0:
       I_prom6=I_cont_SP*100/I_cont6
                        
    if cont_I_Ud !=0 and I_cont1 !=0:
       I_prom1=I_cont_Ud*100/I_cont1   
                    
    if cont_I_SB !=0 and I_cont2 !=0:
       I_prom2=I_cont_SB*100/I_cont2
                        
    if cont_I_MA !=0 and I_cont3 !=0:
       I_prom3=I_cont_MA*100/I_cont3
                        
    if cont_I_BB !=0 and I_cont4 !=0:
       I_prom4=I_cont_BB*100/I_cont5
                        
    if cont_I_Total !=0 and I_cont5 !=0:
       I_prom5=I_cont_Total*100/I_cont5        
            
            
    J_ganador=''
    cont_J_ML=0
    cont_J_SP=0
    cont_J_Ud=0
    cont_J_SB=0
    cont_J_MA=0
    cont_J_BB=0
    cont_J_Total=0
    J_cont=0
    J_cont1=0
    J_cont2=0
    J_cont3=0
    J_cont4=0
    J_cont5=0
    J_cont6=0
    J_sum=0
    J_res=0
    J_valor_izquierdo=0
    J_valor_derecho=0
    J_prom=0
    J_prom1=0
    J_prom2=0
    J_prom3=0
    J_prom4=0 
    J_prom5=0        
    J_prom6=0
        
    for valor in partidos: 
        
        J_valor_izquierdo, J_valor_derecho = extraer_valores_de_resultado(valor)
        J_sum = J_valor_izquierdo + J_valor_derecho
                            
        if valor.J_ML_equip is not None:
           J_cont+=1
           if J_ganador==valor.J_ML_equip.nombre:
              J_cont_ML+=1 
                            
        if valor.J_Ud_equip is not None:
           J_cont1+=1      
           if J_ganador==valor.J_Ud_equip.nombre:
              J_cont_Ud+=1
                            
        if valor.J_SB_equip is not None: 
           J_cont2+=1      
           if J_ganador==valor.J_SB_equip.nombre:
              J_cont_SB+=1
                            
        if valor.J_MA is not None:
           J_cont3+=1 
           if J_ganador==valor.J_MA.nombre:
              J_cont_MA+=1
                            
        if valor.J_BB is not None:  
           J_cont4+=1 
           if J_ganador==valor.J_BB.nombre:
              J_cont_BB+=1
                        
                        
        if valor.J_total_punto is not None: 
           J_cont5+=1 
           if J_sum>J_valor_izquierdo and valor.J_Total_OU=='OVER':
              J_cont_Total+=1
           if J_sum<=valor.J_total_punto and valor.J_Total_OU=='UNDER':
              J_cont_Total+=1
                        
                        
        if J_valor_izquierdo>J_valor_derecho:
                J_res=J_valor_izquierdo-J_valor_derecho
                        
        elif J_valor_izquierdo<J_valor_derecho:
                J_res=J_valor_derecho-J_valor_izquierdo 
                    
        else: 
                J_res=0
                            
        if valor.J_SP_dif is not None:
           J_cont6+=1
           if J_ganador==valor.J_SP_equip.nombre and J_res>valor.J_SP_dif :
              J_cont_SP+=1
            
           
    if cont_J_ML !=0 and J_cont !=0:
       J_prom=J_cont_ML*100/J_cont
                            
    if cont_J_SP !=0 and J_cont6 !=0:
       J_prom6=J_cont_SP*100/J_cont6
                            
    if cont_J_Ud !=0 and J_cont1 !=0:
       J_prom1=J_cont_Ud*100/J_cont1   
                        
    if cont_J_SB !=0 and J_cont2 !=0:
       J_prom2=J_cont_SB*100/J_cont2
                            
    if cont_J_MA !=0 and J_cont3 !=0:
       J_prom3=J_cont_MA*100/J_cont3
                            
    if cont_J_BB !=0 and J_cont4 !=0:
       J_prom4=J_cont_BB*100/J_cont5
                            
    if cont_J_Total !=0 and J_cont5 !=0:
       J_prom5=J_cont_Total*100/J_cont5      
       
       
    mejor_prom_ML=0
    mejor_prom_SP=0
    mejor_prom_T=0
    mejor_prom_Ud=0
    mejor_prom_SB=0
    mejor_prom_MA=0     
    mejor_prom_BB=0
    nombre_s=0
    nombre_s1=0
    nombre_s2=0
    nombre_s3=0
    nombre_s4=0
    nombre_s5=0
    nombre_s6=0
    
    
    list_ML=[A_prom,B_prom,C_prom,D_prom,E_prom,F_prom,G_prom,H_prom,I_prom,J_prom]
    list_SP=[A_prom6,B_prom6,C_prom6,D_prom6,E_prom6,F_prom6,G_prom6,H_prom6,I_prom6,J_prom6]
    list_T=[A_prom5,B_prom5,C_prom5,D_prom5,E_prom5,F_prom5,G_prom5,H_prom5,I_prom5,J_prom5]
    list_Ud=[A_prom1,B_prom1,C_prom1,D_prom1,E_prom1,F_prom1,G_prom1,H_prom1,I_prom1,J_prom1]     
    list_SB=[A_prom2,B_prom2,C_prom2,D_prom2,E_prom2,F_prom2,G_prom2,H_prom2,I_prom2,J_prom2]
    list_MA=[A_prom3,B_prom3,C_prom3,D_prom3,E_prom3,F_prom3,G_prom3,H_prom3,I_prom3,J_prom3]
    list_BB=[A_prom4,B_prom4,C_prom4,D_prom4,E_prom4,F_prom4,G_prom4,H_prom4,I_prom4,J_prom4]
    
    lista_sistemas=['VeriBet','Action Network','Sports Insights','PFF','Covers','Team Rankings','BetQL','Odds Jams','Scores and Odds','Betting on Cash']
       
    for indice,i in enumerate(list_ML):
        if i>mejor_prom_ML:
           mejor_prom_ML=i   
           nombre_s=indice
           
        
    for indice,i in enumerate(list_SP):
        if i>mejor_prom_SP:
           mejor_prom_SP=i        
           nombre_s1=indice
            
    for indice,i in enumerate( list_T):
        if i>mejor_prom_T:
           mejor_prom_T=i         
           nombre_s2=indice
           
    for indice,i in enumerate(list_Ud):
        if i>mejor_prom_Ud:
           mejor_prom_Ud=i 
           nombre_s3=indice
           
    for indice,i in enumerate(list_SB):
        if i>mejor_prom_SB:
           mejor_prom_SB=i 
           nombre_s4=indice
           
    for indice,i in enumerate(list_MA):
        if i>mejor_prom_MA:
           mejor_prom_MA=i 
           nombre_s5=indice
           
    for indice,i in enumerate(list_BB):
        if i>mejor_prom_BB:
           mejor_prom_BB=i 
           nombre_s6=indice
           
           
           
           
           
    for indice,i in enumerate(lista_sistemas):
        if nombre_s==indice:
           nombre_s=i       
           break
              
    for indice,i in enumerate(lista_sistemas):
        if nombre_s1==indice:
           nombre_s1=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s2==indice:
           nombre_s2=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s3==indice:
           nombre_s3=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s4==indice:
           nombre_s4=i       
           break
    
    for indice,i in enumerate(lista_sistemas):
        if nombre_s5==indice:
           nombre_s5=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s6==indice:
           nombre_s6=i       
           break          
              
              
              
              
    return render(request,'Futbol/resultados_sistemas.html', {'cont_A_ML':cont_A_ML, 'cont_A_SP':cont_A_SP, 'cont_A_Ud':cont_A_Ud, 
                                                              'cont_A_MA':cont_A_MA,'cont_A_SB':cont_A_SB,'cont_A_BB':cont_A_BB,
                                                              'cont_A_Total':cont_A_Total,'A_cont':A_cont,'A_cont1':A_cont1,'A_cont2':A_cont2,
                                                              'A_cont3':A_cont3,'A_cont4':A_cont4,'A_cont5':A_cont5,'A_cont6':A_cont6, 
                                                              'A_prom':A_prom,'A_prom1':A_prom1,'A_prom2':A_prom2,'A_prom3':A_prom3,'A_prom4':A_prom4,
                                                              'A_prom5':A_prom5,'A_prom6':A_prom6,'cont_B_ML': cont_B_ML, 'cont_B_SP': cont_B_SP, 
                                                              'cont_B_Ud': cont_B_Ud, 'cont_B_MA': cont_B_MA, 'cont_B_SB': cont_B_SB, 'cont_B_BB': cont_B_BB,
                                                              'cont_B_Total': cont_B_Total, 'B_cont': B_cont, 'B_cont1': B_cont1, 'B_cont2': B_cont2,
                                                              'B_cont3': B_cont3, 'B_cont4': B_cont4, 'B_cont5': B_cont5, 'B_cont6': B_cont6, 'B_prom': B_prom,
                                                              'B_prom1': B_prom1, 'B_prom2': B_prom2, 'B_prom3': B_prom3, 'B_prom4': B_prom4, 'B_prom5': B_prom5, 
                                                              'B_prom6': B_prom6,'cont_C_ML': cont_C_ML, 'cont_C_SP': cont_C_SP, 'cont_C_Ud': cont_C_Ud, 
                                                              'cont_C_MA': cont_C_MA, 'cont_C_SB': cont_C_SB, 'cont_C_BB': cont_C_BB, 'cont_C_Total': cont_C_Total,
                                                              'C_cont': C_cont, 'C_cont1': C_cont1, 'C_cont2': C_cont2, 'C_cont3': C_cont3, 'C_cont4': C_cont4,
                                                              'C_cont5': C_cont5, 'C_cont6': C_cont6, 'C_prom': C_prom, 'C_prom1': C_prom1, 'C_prom2': C_prom2,
                                                              'C_prom3': C_prom3, 'C_prom4': C_prom4, 'C_prom5': C_prom5, 'C_prom6': C_prom6, 'cont_D_ML': cont_D_ML,
                                                              'cont_D_SP': cont_D_SP, 'cont_D_Ud': cont_D_Ud, 'cont_D_MA': cont_D_MA, 'cont_D_SB': cont_D_SB,
                                                              'cont_D_BB': cont_D_BB, 'cont_D_Total':cont_D_Total, 'D_cont': D_cont, 'D_cont1': D_cont1,
                                                              'D_cont2': D_cont2, 'D_cont3': D_cont3, 'D_cont4': D_cont4,'D_cont5': D_cont5, 'D_cont6': D_cont6,
                                                              'D_prom': D_prom, 'D_prom1': D_prom1, 'D_prom2': D_prom2,'D_prom3': D_prom3, 'D_prom4': D_prom4, 
                                                              'D_prom5': D_prom5, 'D_prom6': D_prom6, 'cont_E_ML': cont_E_ML, 'cont_E_SP': cont_E_SP, 
                                                              'cont_E_Ud': cont_E_Ud, 'cont_E_MA': cont_E_MA, 'cont_E_SB': cont_E_SB, 'cont_E_BB': cont_E_BB, 
                                                              'cont_E_Total': cont_E_Total,'E_cont': E_cont, 'E_cont1': E_cont1, 'E_cont2': E_cont2, 'E_cont3': E_cont3,
                                                              'E_cont4': E_cont4,'E_cont5': E_cont5, 'E_cont6': E_cont6, 'E_prom': E_prom, 'E_prom1': E_prom1, 
                                                              'E_prom2': E_prom2,'E_prom3': E_prom3, 'E_prom4': E_prom4, 'E_prom5': E_prom5, 'E_prom6': E_prom6,
                                                              'cont_F_ML': cont_F_ML, 'cont_F_SP': cont_F_SP, 'cont_F_Ud': cont_F_Ud, 'cont_F_MA': cont_F_MA, 
                                                              'cont_F_SB': cont_F_SB, 'cont_F_BB': cont_F_BB, 'cont_F_Total': cont_F_Total,'F_cont': F_cont, 
                                                              'F_cont1': F_cont1, 'F_cont2': F_cont2, 'F_cont3': F_cont3,'F_cont4': F_cont4,'F_cont5': F_cont5, 
                                                              'F_cont6': F_cont6, 'F_prom': F_prom, 'F_prom1': F_prom1, 'F_prom2': F_prom2,'F_prom3': F_prom3, 
                                                              'F_prom4': F_prom4, 'F_prom5': F_prom5, 'F_prom6': F_prom6,'cont_G_ML': cont_G_ML, 'cont_G_SP': cont_G_SP,
                                                              'cont_G_Ud': cont_G_Ud, 'cont_G_MA':cont_G_MA, 'cont_G_SB':cont_G_SB, 'cont_G_BB': cont_G_BB,
                                                              'cont_G_Total':cont_G_Total,'G_cont': G_cont, 'G_cont1': G_cont1, 'G_cont2': G_cont2, 'G_cont3': G_cont3,
                                                              'G_cont4': G_cont4,'G_cont5': G_cont5, 'G_cont6': G_cont6, 'G_prom': G_prom, 'G_prom1': G_prom1, 
                                                              'G_prom2': G_prom2,'G_prom3': G_prom3, 'G_prom4': G_prom4, 'G_prom5': G_prom5, 'G_prom6': G_prom6,
                                                              'cont_H_ML': cont_H_ML, 'cont_H_SP': cont_H_SP, 'cont_H_Ud': cont_H_Ud, 'cont_H_MA':cont_H_MA,
                                                              'cont_H_SB': cont_H_SB, 'cont_H_BB': cont_H_BB, 'cont_H_Total':cont_H_Total,'H_cont': H_cont,
                                                              'H_cont1': H_cont1, 'H_cont2': H_cont2, 'H_cont3': H_cont3,'H_cont4': H_cont4,'H_cont5': H_cont5,
                                                              'H_cont6': H_cont6, 'H_prom': H_prom, 'H_prom1': H_prom1, 'H_prom2': H_prom2,'H_prom3': H_prom3, 
                                                              'H_prom4': H_prom4, 'H_prom5': H_prom5, 'H_prom6': H_prom6,'cont_I_ML': cont_I_ML, 'cont_I_SP': cont_I_SP,
                                                              'cont_I_Ud': cont_I_Ud, 'cont_I_MA': cont_I_MA, 'cont_I_SB': cont_I_SB, 'cont_I_BB': cont_I_BB, 
                                                              'cont_I_Total': cont_I_Total,'I_cont': I_cont, 'I_cont1': I_cont1, 'I_cont2': I_cont2, 'I_cont3': I_cont3,
                                                              'I_cont4': I_cont4,'I_cont5': I_cont5, 'I_cont6': I_cont6, 'I_prom': I_prom, 'I_prom1': I_prom1,
                                                              'I_prom2': I_prom2,'I_prom3': I_prom3, 'I_prom4': I_prom4, 'I_prom5': I_prom5, 'I_prom6': I_prom6,
                                                              'cont_J_ML': cont_J_ML, 'cont_J_SP': cont_J_SP, 'cont_J_Ud': cont_J_Ud, 'cont_J_MA': cont_J_MA,
                                                              'cont_J_SB': cont_J_SB, 'cont_J_BB':cont_J_BB, 'cont_J_Total': cont_J_Total,'J_cont': J_cont, 
                                                              'J_cont1': J_cont1, 'J_cont2': J_cont2, 'J_cont3': J_cont3,'J_cont4': J_cont4,'J_cont5': J_cont5, 
                                                              'J_cont6': J_cont6, 'J_prom': J_prom, 'J_prom1': J_prom1, 'J_prom2': J_prom2,'J_prom3': J_prom3, 
                                                              'J_prom4': J_prom4, 'J_prom5': J_prom5, 'J_prom6': J_prom6,'nombre_s':nombre_s,'nombre_s1':nombre_s1,
                                                              'nombre_s2':nombre_s2,'nombre_s3':nombre_s3,'nombre_s4':nombre_s4,'nombre_s5':nombre_s5,'nombre_s6':nombre_s6,
                                                              'mejor_prom_ML':mejor_prom_ML,'mejor_prom_SP':mejor_prom_SP,'mejor_prom_T':mejor_prom_T,
                                                              'mejor_prom_Ud':mejor_prom_Ud,'mejor_prom_SB':mejor_prom_SB,'mejor_prom_MA':mejor_prom_MA,'mejor_prom_BB':mejor_prom_BB,  })
    
    

#Baseball
  
def Crear_Baseball(request):
    if request.method == 'POST':
        formulario = baseball_form(request.POST)
        if formulario.is_valid():
            formulario.clean()
            objeto_creado = formulario.save()
            
          
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = Baseball.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = Baseball.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = Baseball.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = Baseball.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'Baseball/informes.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,  'formulario':formulario, 'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })
       
        else:
            return render(request, 'Baseball/crear_baseball.html', {'formulario': formulario})
    else:
        formulario = baseball_form()
        return render(request, 'Baseball/crear_baseball.html', {'formulario': formulario})

def Listar_Baseball(request):
    lista =Baseball.objects.all().order_by('fecha')
    return render(request, 'Baseball/listar_baseball.html', {'lista':lista} )

def Eliminar_Baseball(request, id):
    f = get_object_or_404(Baseball, id=id)
    f.delete()
    return redirect('listar_baseball')

def Buscar_Baseball(request):
    resultados = []
    if request.method == 'POST':
        termino_busqueda = request.POST.get('searchbar')
        
        if termino_busqueda:
            # Construye condiciones para buscar en el nombre del equipo local o visitante
            condiciones = (
                Q(equipo_local__nombre__icontains=termino_busqueda) |
                Q(equipo_visitante__nombre__icontains=termino_busqueda)
            )
            
            # Filtra los resultados basándose en las condiciones construidas
            resultados = Baseball.objects.filter(condiciones)
        

        return render(request, 'Baseball/resultados.html', {'resultados': resultados})
    return render(request, 'Baseball/listar_baseball.html')

def Resultado_Baseball(request, id):
    f = Baseball.objects.get(id=id)
    
    equipo_local = f.equipo_local.nombre
    equipo_visitante = f.equipo_visitante.nombre
    opciones_ganador = [ equipo_local,equipo_visitante,'Empate' ]
    
    if request.method == 'POST':
        form = resultado_baseball_form(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return redirect('listar_baseball')
    else:
        form = resultado_baseball_form( instance=f)

    return render(request, 'Baseball/resultado_baseball.html', {'form': form,'opciones_ganador': opciones_ganador})

def Informe_Resultado_Baseball(request, id):
            objeto_creado = Baseball.objects.get(id=id)
    
    
   
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = Baseball.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = Baseball.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = Baseball.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = Baseball.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'Baseball/informe_lista.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })

def Resultados_Sistemas_Baseball(request): 
    
    partidos_filtrados = Baseball.objects.exclude(ganador__isnull=True).exclude(resultado__isnull=True)
    partidos = partidos_filtrados.order_by('-fecha')[:20]
    
    
    #Sistema A
    
    ganador=''
    cont_A_ML=0
    cont_A_SP=0
    cont_A_Ud=0
    cont_A_SB=0
    cont_A_MA=0
    cont_A_BB=0
    cont_A_Total=0
    A_cont=0
    A_cont1=0
    A_cont2=0
    A_cont3=0
    A_cont4=0
    A_cont5=0
    A_cont6=0
    sum=0
    res=0
    valor_izquierdo=0
    valor_derecho=0
    A_prom=0
    A_prom1=0
    A_prom2=0
    A_prom3=0
    A_prom4=0 
    A_prom5=0
    A_prom6=0
    
    for valor in partidos: 
        
        ganador=valor.ganador
        
        valor_izquierdo, valor_derecho = extraer_valores_de_resultado(valor)
        sum= valor_izquierdo+valor_derecho
        
        if valor.A_ML_equip is not None:
           A_cont+=1
           if ganador==valor.A_ML_equip.nombre:
              cont_A_ML+=1 
              
              
        if valor.A_Ud_equip is not None:
           A_cont1+=1      
           if ganador==valor.A_Ud_equip.nombre:
              cont_A_Ud+=1
              
              
        if valor.A_SB_equip is not None: 
           A_cont2+=1      
           if ganador==valor.A_SB_equip.nombre:
              cont_A_SB+=1
              
              
        if valor.A_MA is not None:
           A_cont3+=1 
           if ganador==valor.A_MA.nombre:
              cont_A_MA+=1
              
              
        if valor.A_BB is not None:  
           A_cont4+=1 
           if ganador==valor.A_BB.nombre:
              cont_A_BB+=1
         
         
        if valor.A_total_punto is not None: 
           A_cont5+=1 
           if sum>valor.A_total_punto and valor.A_Total_OU=='OVER':
              cont_A_Total+=1
           if sum<=valor.A_total_punto and valor.A_Total_OU=='UNDER':
              cont_A_Total+=1
         
         
       
        if valor_izquierdo>valor_derecho:
            res=valor_izquierdo-valor_derecho
           
        elif valor_izquierdo<valor_derecho:
            res=valor_derecho-valor_izquierdo 
        
        else: 
            res=0
        
        if valor.A_SP_dif is not None:
           A_cont6+=1
           if ganador==valor.A_SP_equip.nombre and res>valor.A_SP_dif :
              cont_A_SP+=1
           
           
           
    if cont_A_ML !=0 and A_cont !=0:
           A_prom=cont_A_ML*100/A_cont
        
    if cont_A_SP !=0 and A_cont6 !=0:
           A_prom6=cont_A_SP*100/A_cont6
           
    if cont_A_Ud !=0 and A_cont1 !=0:
           A_prom1=cont_A_Ud*100/A_cont1
           
    if cont_A_SB !=0 and A_cont2 !=0:
           A_prom2=cont_A_SB*100/A_cont2
           
    if cont_A_MA !=0 and A_cont3 !=0:
           A_prom3=cont_A_MA*100/A_cont3
           
    if cont_A_BB !=0 and A_cont4 !=0:
           A_prom4=cont_A_BB*100/A_cont5
           
    if cont_A_Total !=0 and A_cont5 !=0:
           A_prom5=cont_A_Total*100/A_cont5      
           
           
           
    #Sistema B     
    
    B_ganador=''
    cont_B_ML=0
    cont_B_SP=0
    cont_B_Ud=0
    cont_B_SB=0
    cont_B_MA=0
    cont_B_BB=0
    cont_B_Total=0
    B_cont=0
    B_cont1=0
    B_cont2=0
    B_cont3=0
    B_cont4=0
    B_cont5=0
    B_cont6=0
    B_sum=0
    B_res=0
    B_valor_izquierdo=0
    B_valor_derecho=0
    B_prom=0
    B_prom1=0
    B_prom2=0
    B_prom3=0
    B_prom4=0 
    B_prom5=0
    B_prom6=0
    
    for valor in partidos: 
        
        B_ganador=valor.ganador
        
        B_valor_izquierdo, B_valor_derecho = extraer_valores_de_resultado(valor)
        B_sum= B_valor_izquierdo+B_valor_derecho
        
        if valor.B_ML_equip is not None:
           B_cont+=1
           if B_ganador==valor.B_ML_equip.nombre:
              cont_B_ML+=1 
              
              
        if valor.B_Ud_equip is not None:
           B_cont1+=1      
           if B_ganador==valor.B_Ud_equip.nombre:
              cont_B_Ud+=1
              
              
        if valor.B_SB_equip is not None: 
           B_cont2+=1      
           if B_ganador==valor.B_SB_equip.nombre:
              cont_B_SB+=1
              
              
        if valor.B_MA is not None:
           B_cont3+=1 
           if B_ganador==valor.B_MA.nombre:
              cont_B_MA+=1
              
              
        if valor.B_BB is not None:  
           B_cont4+=1 
           if B_ganador==valor.B_BB.nombre:
              cont_B_BB+=1
         
         
        if valor.B_total_punto is not None: 
           B_cont5+=1 
           if B_sum>valor.B_total_punto and valor.B_Total_OU=='OVER':
              cont_B_Total+=1
           if B_sum<=valor.B_total_punto and valor.B_Total_OU=='UNDER':
              cont_B_Total+=1
         
         
       
        if B_valor_izquierdo>B_valor_derecho:
            B_res=B_valor_izquierdo-B_valor_derecho
           
        elif B_valor_izquierdo<B_valor_derecho:
            B_res=B_valor_derecho-B_valor_izquierdo 
        
        else: 
            B_res=0
        
        if valor.B_SP_dif is not None:
           B_cont6+=1
           if B_ganador==valor.B_SP_equip.nombre and B_res>valor.B_SP_dif :
              cont_B_SP+=1
           
           
           
    if cont_B_ML !=0 and B_cont !=0:
           B_prom=cont_B_ML*100/B_cont
        
    if cont_B_SP !=0 and B_cont6 !=0:
           B_prom6=cont_B_SP*100/B_cont6
           
    if cont_B_Ud !=0 and B_cont1 !=0:
           B_prom1=cont_B_Ud*100/B_cont1
           
    if cont_B_SB !=0 and B_cont2 !=0:
           B_prom2=cont_B_SB*100/B_cont2
           
    if cont_B_MA !=0 and B_cont3 !=0:
           B_prom3=cont_B_MA*100/B_cont3
           
    if cont_B_BB !=0 and B_cont4 !=0:
           B_prom4=cont_B_BB*100/B_cont5
           
    if cont_B_Total !=0 and B_cont5 !=0:
           B_prom5=cont_B_Total*100/B_cont5             
           
           
    C_ganador=''
    cont_C_ML=0
    cont_C_SP=0
    cont_C_Ud=0
    cont_C_SB=0
    cont_C_MA=0
    cont_C_BB=0
    cont_C_Total=0
    C_cont=0
    C_cont1=0
    C_cont2=0
    C_cont3=0
    C_cont4=0
    C_cont5=0
    C_cont6=0
    C_sum=0
    C_res=0
    C_valor_izquierdo=0
    C_valor_derecho=0
    C_prom=0
    C_prom1=0
    C_prom2=0
    C_prom3=0
    C_prom4=0 
    C_prom5=0        
    C_prom6=0
       
    for valor in partidos: 
        
        C_ganador=valor.ganador
            
        C_valor_izquierdo, C_valor_derecho = extraer_valores_de_resultado(valor)
        C_sum= C_valor_izquierdo+C_valor_derecho
            
        if valor.C_ML_equip is not None:
            C_cont+=1
            if C_ganador==valor.C_ML_equip.nombre:
                cont_C_ML+=1 
                
        if valor.C_Ud_equip is not None:
            C_cont1+=1      
            if C_ganador==valor.C_Ud_equip.nombre:
                cont_C_Ud+=1
                
        if valor.C_SB_equip is not None: 
            C_cont2+=1      
            if C_ganador==valor.C_SB_equip.nombre:
                cont_C_SB+=1
                
        if valor.C_MA is not None:
            C_cont3+=1 
            if C_ganador==valor.C_MA.nombre:
                cont_C_MA+=1
                
        if valor.C_BB is not None:  
            C_cont4+=1 
            if C_ganador==valor.C_BB.nombre:
                cont_C_BB+=1
            
            
        if valor.C_total_punto is not None: 
            C_cont5+=1 
            if C_sum>valor.C_total_punto and valor.C_Total_OU=='OVER':
                cont_C_Total+=1
            if C_sum<=valor.C_total_punto and valor.C_Total_OU=='UNDER':
                cont_C_Total+=1
            
            

        if C_valor_izquierdo>C_valor_derecho:
            C_res=C_valor_izquierdo-C_valor_derecho
            
        elif C_valor_izquierdo<C_valor_derecho:
            C_res=C_valor_derecho-C_valor_izquierdo 

        else: 
            C_res=0
            
        if valor.C_SP_dif is not None:
            C_cont6+=1
            if C_ganador==valor.C_SP_equip.nombre and C_res>valor.C_SP_dif :
                cont_C_SP+=1
           
           
    if cont_C_ML !=0 and C_cont !=0:
       C_prom=cont_C_ML*100/C_cont
            
    if cont_C_SP !=0 and C_cont6 !=0:
       C_prom6=cont_C_SP*100/C_cont6
            
    if cont_C_Ud !=0 and C_cont1 !=0:
       C_prom1=cont_C_Ud*100/C_cont1
            
    if cont_C_SB !=0 and C_cont2 !=0:
       C_prom2=cont_C_SB*100/C_cont2
            
    if cont_C_MA !=0 and C_cont3 !=0:
       C_prom3=cont_C_MA*100/C_cont3
            
    if cont_C_BB !=0 and C_cont4 !=0:
       C_prom4=cont_C_BB*100/C_cont5
            
    if cont_C_Total !=0 and C_cont5 !=0:
       C_prom5=cont_C_Total*100/C_cont5       
           
    
    
    D_ganador=''
    cont_D_ML=0
    cont_D_SP=0
    cont_D_Ud=0
    cont_D_SB=0
    cont_D_MA=0
    cont_D_BB=0
    cont_D_Total=0
    D_cont=0
    D_cont1=0
    D_cont2=0
    D_cont3=0
    D_cont4=0
    D_cont5=0
    D_cont6=0
    D_sum=0
    D_res=0
    D_valor_izquierdo=0
    D_valor_derecho=0
    D_prom=0
    D_prom1=0
    D_prom2=0
    D_prom3=0
    D_prom4=0 
    D_prom5=0        
    D_prom6=0

    
    
    
    for valor in partidos: 
        
        D_ganador=valor.ganador
            
        D_valor_izquierdo, D_valor_derecho = extraer_valores_de_resultado(valor)
        D_sum= D_valor_izquierdo+D_valor_derecho
            
        if valor.D_ML_equip is not None:
           D_cont+=1
           if D_ganador==valor.D_ML_equip.nombre:
              cont_D_ML+=1 
            
        if valor.D_Ud_equip is not None:
           D_cont1+=1      
           if D_ganador==valor.D_Ud_equip.nombre:
              cont_D_Ud+=1
            
        if valor.D_SB_equip is not None: 
           D_cont2+=1      
           if D_ganador==valor.D_SB_equip.nombre:
              cont_D_SB+=1
            
        if valor.D_MA is not None:
           D_cont3+=1 
           if D_ganador==valor.D_MA.nombre:
              cont_D_MA+=1
            
        if valor.D_BB is not None:  
           D_cont4+=1 
           if D_ganador==valor.D_BB.nombre:
              cont_D_BB+=1
        
        
        if valor.D_total_punto is not None: 
           D_cont5+=1 
           if D_sum>valor.D_total_punto and valor.D_Total_OU=='OVER':
              cont_D_Total+=1
           if D_sum<=valor.D_total_punto and valor.D_Total_OU=='UNDER':
              cont_D_Total+=1
        
        
    
        if D_valor_izquierdo>D_valor_derecho:
            D_res=D_valor_izquierdo-D_valor_derecho
        
        elif D_valor_izquierdo<D_valor_derecho:
            D_res=D_valor_derecho-D_valor_izquierdo 
        
        else: 
            D_res=0
            
        if valor.D_SP_dif is not None:
           D_cont6+=1
           if D_ganador==valor.D_SP_equip.nombre and D_res>valor.D_SP_dif :
              cont_D_SP+=1
             
           
    if cont_D_ML !=0 and D_cont !=0:
       D_prom=cont_D_ML*100/D_cont
            
    if cont_D_SP !=0 and D_cont6 !=0:
       D_prom6=cont_D_SP*100/D_cont6
            
    if cont_D_Ud !=0 and D_cont1 !=0:
       D_prom1=cont_D_Ud*100/D_cont1
            
    if cont_D_SB !=0 and D_cont2 !=0:
       D_prom2=cont_D_SB*100/D_cont2
            
    if cont_D_MA !=0 and D_cont3 !=0:
       D_prom3=cont_D_MA*100/D_cont3
            
    if cont_D_BB !=0 and D_cont4 !=0:
       D_prom4=cont_D_BB*100/D_cont5
            
    if cont_D_Total !=0 and D_cont5 !=0:
       D_prom5=cont_D_Total*100/D_cont5
        
    
    E_ganador=''
    cont_E_ML=0
    cont_E_SP=0
    cont_E_Ud=0
    cont_E_SB=0
    cont_E_MA=0
    cont_E_BB=0
    cont_E_Total=0
    E_cont=0
    E_cont1=0
    E_cont2=0
    E_cont3=0
    E_cont4=0
    E_cont5=0
    E_cont6=0
    E_sum=0
    E_res=0
    E_valor_izquierdo=0
    E_valor_derecho=0
    E_prom=0
    E_prom1=0
    E_prom2=0
    E_prom3=0
    E_prom4=0 
    E_prom5=0        
    E_prom6=0
       
    for valor in partidos: 
        
        E_ganador=valor.ganador
            
        E_valor_izquierdo, E_valor_derecho = extraer_valores_de_resultado(valor)
        E_sum= E_valor_izquierdo+E_valor_derecho
            
        if valor.E_ML_equip is not None:
           E_cont+=1
           if E_ganador==valor.E_ML_equip.nombre:
              cont_E_ML+=1 
            
        if valor.E_Ud_equip is not None:
           E_cont1+=1      
           if E_ganador==valor.E_Ud_equip.nombre:
              cont_E_Ud+=1
            
        if valor.E_SB_equip is not None: 
           E_cont2+=1      
           if E_ganador==valor.E_SB_equip.nombre:
              cont_E_SB+=1
            
        if valor.E_MA is not None:
           E_cont3+=1 
           if E_ganador==valor.E_MA.nombre:
              cont_E_MA+=1
            
        if valor.E_BB is not None:  
           E_cont4+=1 
           if E_ganador==valor.E_BB.nombre:
              cont_E_BB+=1
        
        
        if valor.E_total_punto is not None: 
           E_cont5+=1 
           if E_sum>valor.E_total_punto and valor.E_Total_OU=='OVER':
              cont_E_Total+=1
           if E_sum<=valor.E_total_punto and valor.E_Total_OU=='UNDER':
              cont_E_Total+=1
        
        
    
        if E_valor_izquierdo>E_valor_derecho:
            E_res=E_valor_izquierdo-E_valor_derecho
        
        elif E_valor_izquierdo<E_valor_derecho:
            E_res=E_valor_derecho-E_valor_izquierdo 
        
        else: 
            E_res=0
            
        if valor.E_SP_dif is not None:
           E_cont6+=1
           if E_ganador==valor.E_SP_equip.nombre and E_res>valor.E_SP_dif :
              cont_E_SP+=1
            
           
    if cont_E_ML !=0 and E_cont !=0:
       E_prom=cont_E_ML*100/E_cont
            
    if cont_E_SP !=0 and E_cont6 !=0:
       E_prom6=cont_E_SP*100/E_cont6
            
    if cont_E_Ud !=0 and E_cont1 !=0:
       E_prom1=cont_E_Ud*100/E_cont1   
        
    if cont_E_SB !=0 and E_cont2 !=0:
       E_prom2=cont_E_SB*100/E_cont2
            
    if cont_E_MA !=0 and E_cont3 !=0:
       E_prom3=cont_E_MA*100/E_cont3
            
    if cont_E_BB !=0 and E_cont4 !=0:
       E_prom4=cont_E_BB*100/E_cont5
            
    if cont_E_Total !=0 and E_cont5 !=0:
       E_prom5=cont_E_Total*100/E_cont5     
    
    
    
    
    F_ganador=''
    cont_F_ML=0
    cont_F_SP=0
    cont_F_Ud=0
    cont_F_SB=0
    cont_F_MA=0
    cont_F_BB=0
    cont_F_Total=0
    F_cont=0
    F_cont1=0
    F_cont2=0
    F_cont3=0
    F_cont4=0
    F_cont5=0
    F_cont6=0
    F_sum=0
    F_res=0
    F_valor_izquierdo=0
    F_valor_derecho=0
    F_prom=0
    F_prom1=0
    F_prom2=0
    F_prom3=0
    F_prom4=0 
    F_prom5=0        
    F_prom6=0
       
    
    for valor in partidos: 
        
 
        F_valor_izquierdo, F_valor_derecho = extraer_valores_de_resultado(valor)
        F_sum = F_valor_izquierdo + F_valor_derecho
                
        if valor.F_ML_equip is not None:
           F_cont+=1
           if F_ganador==valor.F_ML_equip.nombre:
              F_cont_ML+=1 
                
        if valor.F_Ud_equip is not None:
           F_cont1+=1      
           if F_ganador==valor.F_Ud_equip.nombre:
              F_cont_Ud+=1
                
        if valor.F_SB_equip is not None: 
           F_cont2+=1      
           if F_ganador==valor.F_SB_equip.nombre:
              F_cont_SB+=1
                
        if valor.F_MA is not None:
           F_cont3+=1 
           if F_ganador==valor.F_MA.nombre:
              F_cont_MA+=1
                
        if valor.F_BB is not None:  
           F_cont4+=1 
           if F_ganador==valor.F_BB.nombre:
              F_cont_BB+=1
            
            
        if valor.F_total_punto is not None: 
           F_cont5+=1 
           if F_sum>F_valor_izquierdo and valor.F_Total_OU=='OVER':
              F_cont_Total+=1
           if F_sum<=valor.F_total_punto and valor.F_Total_OU=='UNDER':
              F_cont_Total+=1
            
            
        if F_valor_izquierdo>F_valor_derecho:
            F_res=F_valor_izquierdo-F_valor_derecho
            
        elif F_valor_izquierdo<F_valor_derecho:
            F_res=F_valor_derecho-F_valor_izquierdo 
        
        else: 
            F_res=0
                
        if valor.F_SP_dif is not None:
           F_cont6+=1
           if F_ganador==valor.F_SP_equip.nombre and F_res>valor.F_SP_dif :
              F_cont_SP+=1
            
           
    if cont_F_ML !=0 and F_cont !=0:
       F_prom=F_cont_ML*100/F_cont
                
    if cont_F_SP !=0 and F_cont6 !=0:
       F_prom6=F_cont_SP*100/F_cont6
                
    if cont_F_Ud !=0 and F_cont1 !=0:
       F_prom1=F_cont_Ud*100/F_cont1   
            
    if cont_F_SB !=0 and F_cont2 !=0:
       F_prom2=F_cont_SB*100/F_cont2
                
    if cont_F_MA !=0 and F_cont3 !=0:
       F_prom3=F_cont_MA*100/F_cont3
                
    if cont_F_BB !=0 and F_cont4 !=0:
       F_prom4=F_cont_BB*100/F_cont5
                
    if cont_F_Total !=0 and F_cont5 !=0:
       F_prom5=F_cont_Total*100/F_cont5
        
    
    G_ganador=''
    cont_G_ML=0
    cont_G_SP=0
    cont_G_Ud=0
    cont_G_SB=0
    cont_G_MA=0
    cont_G_BB=0
    cont_G_Total=0
    G_cont=0
    G_cont1=0
    G_cont2=0
    G_cont3=0
    G_cont4=0
    G_cont5=0
    G_cont6=0
    G_sum=0
    G_res=0
    G_valor_izquierdo=0
    G_valor_derecho=0
    G_prom=0
    G_prom1=0
    G_prom2=0
    G_prom3=0
    G_prom4=0 
    G_prom5=0        
    G_prom6=0

    for valor in partidos: 
        
        G_valor_izquierdo, G_valor_derecho = extraer_valores_de_resultado(valor)
        G_sum = G_valor_izquierdo + G_valor_derecho
                    
        if valor.G_ML_equip is not None:
           G_cont+=1
           if G_ganador==valor.G_ML_equip.nombre:
              G_cont_ML+=1 
                    
        if valor.G_Ud_equip is not None:
           G_cont1+=1      
           if G_ganador==valor.G_Ud_equip.nombre:
              G_cont_Ud+=1
                    
        if valor.G_SB_equip is not None: 
           G_cont2+=1      
           if G_ganador==valor.G_SB_equip.nombre:
              G_cont_SB+=1
                    
        if valor.G_MA is not None:
           G_cont3+=1 
           if G_ganador==valor.G_MA.nombre:
              G_cont_MA+=1
                    
        if valor.G_BB is not None:  
           G_cont4+=1 
           if G_ganador==valor.G_BB.nombre:
              G_cont_BB+=1
                
                
        if valor.G_total_punto is not None: 
           G_cont5+=1 
           if G_sum>G_valor_izquierdo and valor.G_Total_OU=='OVER':
              G_cont_Total+=1
           if G_sum<=valor.G_total_punto and valor.G_Total_OU=='UNDER':
              G_cont_Total+=1
                
                
        if G_valor_izquierdo>G_valor_derecho:
            G_res=G_valor_izquierdo-G_valor_derecho
                
        elif G_valor_izquierdo<G_valor_derecho:
            G_res=G_valor_derecho-G_valor_izquierdo 
            
        else: 
            G_res=0
                    
        if valor.G_SP_dif is not None:
           G_cont6+=1
           if G_ganador==valor.G_SP_equip.nombre and G_res>valor.G_SP_dif :
              G_cont_SP+=1
            
           
    if cont_G_ML !=0 and G_cont !=0:
       G_prom=G_cont_ML*100/G_cont
                    
    if cont_G_SP !=0 and G_cont6 !=0:
       G_prom6=G_cont_SP*100/G_cont6
                    
    if cont_G_Ud !=0 and G_cont1 !=0:
       G_prom1=G_cont_Ud*100/G_cont1   
                
    if cont_G_SB !=0 and G_cont2 !=0:
       G_prom2=G_cont_SB*100/G_cont2
                    
    if cont_G_MA !=0 and G_cont3 !=0:
       G_prom3=G_cont_MA*100/G_cont3
                    
    if cont_G_BB !=0 and G_cont4 !=0:
       G_prom4=G_cont_BB*100/G_cont5
                    
    if cont_G_Total !=0 and G_cont5 !=0:
       G_prom5=G_cont_Total*100/G_cont5
            
            
            
    H_ganador=''
    cont_H_ML=0
    cont_H_SP=0
    cont_H_Ud=0
    cont_H_SB=0
    cont_H_MA=0
    cont_H_BB=0
    cont_H_Total=0
    H_cont=0
    H_cont1=0
    H_cont2=0
    H_cont3=0
    H_cont4=0
    H_cont5=0
    H_cont6=0
    H_sum=0
    H_res=0
    H_valor_izquierdo=0
    H_valor_derecho=0
    H_prom=0
    H_prom1=0
    H_prom2=0
    H_prom3=0
    H_prom4=0 
    H_prom5=0        
    H_prom6=0
        
            
    for valor in partidos: 
        
        H_valor_izquierdo, H_valor_derecho = extraer_valores_de_resultado(valor)
        H_sum = H_valor_izquierdo + H_valor_derecho
                        
        if valor.H_ML_equip is not None:
           H_cont+=1
           if H_ganador==valor.H_ML_equip.nombre:
              H_cont_ML+=1 
                        
        if valor.H_Ud_equip is not None:
           H_cont1+=1      
           if H_ganador==valor.H_Ud_equip.nombre:
              H_cont_Ud+=1
                        
        if valor.H_SB_equip is not None: 
           H_cont2+=1      
           if H_ganador==valor.H_SB_equip.nombre:
              H_cont_SB+=1
                        
        if valor.H_MA is not None:
           H_cont3+=1 
           if H_ganador==valor.H_MA.nombre:
              H_cont_MA+=1
                        
        if valor.H_BB is not None:  
           H_cont4+=1 
           if H_ganador==valor.H_BB.nombre:
              H_cont_BB+=1
                    
                    
        if valor.H_total_punto is not None: 
           H_cont5+=1 
           if H_sum>H_valor_izquierdo and valor.H_Total_OU=='OVER':
              H_cont_Total+=1
           if H_sum<=valor.H_total_punto and valor.H_Total_OU=='UNDER':
              H_cont_Total+=1
                    
                    
        if H_valor_izquierdo>H_valor_derecho:
                H_res=H_valor_izquierdo-H_valor_derecho
                    
        elif H_valor_izquierdo<H_valor_derecho:
                H_res=H_valor_derecho-H_valor_izquierdo 
                
        else: 
                H_res=0
                        
        if valor.H_SP_dif is not None:
           H_cont6+=1
           if H_ganador==valor.H_SP_equip.nombre and H_res>valor.H_SP_dif :
              H_cont_SP+=1
            
           
    if cont_H_ML !=0 and H_cont !=0:
       H_prom=H_cont_ML*100/H_cont
                    
    if cont_H_SP !=0 and H_cont6 !=0:
       H_prom6=H_cont_SP*100/H_cont6
                    
    if cont_H_Ud !=0 and H_cont1 !=0:
       H_prom1=H_cont_Ud*100/H_cont1   
                
    if cont_H_SB !=0 and H_cont2 !=0:
       H_prom2=H_cont_SB*100/H_cont2
                    
    if cont_H_MA !=0 and H_cont3 !=0:
       H_prom3=H_cont_MA*100/H_cont3
                    
    if cont_H_BB !=0 and H_cont4 !=0:
       H_prom4=H_cont_BB*100/H_cont5
                    
    if cont_H_Total !=0 and H_cont5 !=0:
       H_prom5=H_cont_Total*100/H_cont5        
            
    
    
    I_ganador=''
    cont_I_ML=0
    cont_I_SP=0
    cont_I_Ud=0
    cont_I_SB=0
    cont_I_MA=0
    cont_I_BB=0
    cont_I_Total=0
    I_cont=0
    I_cont1=0
    I_cont2=0
    I_cont3=0
    I_cont4=0
    I_cont5=0
    I_cont6=0
    I_sum=0
    I_res=0
    I_valor_izquierdo=0
    I_valor_derecho=0
    I_prom=0
    I_prom1=0
    I_prom2=0
    I_prom3=0
    I_prom4=0 
    I_prom5=0        
    I_prom6=0
        
            
    for valor in partidos: 
        
        I_valor_izquierdo, I_valor_derecho = extraer_valores_de_resultado(valor)
        I_sum = I_valor_izquierdo + I_valor_derecho
                        
        if valor.I_ML_equip is not None:
           I_cont+=1
           if I_ganador==valor.I_ML_equip.nombre:
              I_cont_ML+=1 
                        
        if valor.I_Ud_equip is not None:
           I_cont1+=1      
           if I_ganador==valor.I_Ud_equip.nombre:
              I_cont_Ud+=1
                        
        if valor.I_SB_equip is not None: 
           I_cont2+=1      
           if I_ganador==valor.I_SB_equip.nombre:
              I_cont_SB+=1
                        
        if valor.I_MA is not None:
           I_cont3+=1 
           if I_ganador==valor.I_MA.nombre:
              I_cont_MA+=1
                        
        if valor.I_BB is not None:  
           I_cont4+=1 
           if I_ganador==valor.I_BB.nombre:
              I_cont_BB+=1
                    
                    
        if valor.I_total_punto is not None: 
           I_cont5+=1 
           if I_sum>I_valor_izquierdo and valor.I_Total_OU=='OVER':
              I_cont_Total+=1
           if I_sum<=valor.I_total_punto and valor.I_Total_OU=='UNDER':
              I_cont_Total+=1
                    
                    
        if I_valor_izquierdo>I_valor_derecho:
                I_res=I_valor_izquierdo-I_valor_derecho
                    
        elif I_valor_izquierdo<I_valor_derecho:
                I_res=I_valor_derecho-I_valor_izquierdo 
                
        else: 
                I_res=0
                        
        if valor.I_SP_dif is not None:
           I_cont6+=1
           if I_ganador==valor.I_SP_equip.nombre and I_res>valor.I_SP_dif :
              I_cont_SP+=1
            
           
    if cont_I_ML !=0 and I_cont !=0:
       I_prom=I_cont_ML*100/I_cont
                        
    if cont_I_SP !=0 and I_cont6 !=0:
       I_prom6=I_cont_SP*100/I_cont6
                        
    if cont_I_Ud !=0 and I_cont1 !=0:
       I_prom1=I_cont_Ud*100/I_cont1   
                    
    if cont_I_SB !=0 and I_cont2 !=0:
       I_prom2=I_cont_SB*100/I_cont2
                        
    if cont_I_MA !=0 and I_cont3 !=0:
       I_prom3=I_cont_MA*100/I_cont3
                        
    if cont_I_BB !=0 and I_cont4 !=0:
       I_prom4=I_cont_BB*100/I_cont5
                        
    if cont_I_Total !=0 and I_cont5 !=0:
       I_prom5=I_cont_Total*100/I_cont5        
            
            
    J_ganador=''
    cont_J_ML=0
    cont_J_SP=0
    cont_J_Ud=0
    cont_J_SB=0
    cont_J_MA=0
    cont_J_BB=0
    cont_J_Total=0
    J_cont=0
    J_cont1=0
    J_cont2=0
    J_cont3=0
    J_cont4=0
    J_cont5=0
    J_cont6=0
    J_sum=0
    J_res=0
    J_valor_izquierdo=0
    J_valor_derecho=0
    J_prom=0
    J_prom1=0
    J_prom2=0
    J_prom3=0
    J_prom4=0 
    J_prom5=0        
    J_prom6=0
        
    for valor in partidos: 
        
        J_valor_izquierdo, J_valor_derecho = extraer_valores_de_resultado(valor)
        J_sum = J_valor_izquierdo + J_valor_derecho
                            
        if valor.J_ML_equip is not None:
           J_cont+=1
           if J_ganador==valor.J_ML_equip.nombre:
              J_cont_ML+=1 
                            
        if valor.J_Ud_equip is not None:
           J_cont1+=1      
           if J_ganador==valor.J_Ud_equip.nombre:
              J_cont_Ud+=1
                            
        if valor.J_SB_equip is not None: 
           J_cont2+=1      
           if J_ganador==valor.J_SB_equip.nombre:
              J_cont_SB+=1
                            
        if valor.J_MA is not None:
           J_cont3+=1 
           if J_ganador==valor.J_MA.nombre:
              J_cont_MA+=1
                            
        if valor.J_BB is not None:  
           J_cont4+=1 
           if J_ganador==valor.J_BB.nombre:
              J_cont_BB+=1
                        
                        
        if valor.J_total_punto is not None: 
           J_cont5+=1 
           if J_sum>J_valor_izquierdo and valor.J_Total_OU=='OVER':
              J_cont_Total+=1
           if J_sum<=valor.J_total_punto and valor.J_Total_OU=='UNDER':
              J_cont_Total+=1
                        
                        
        if J_valor_izquierdo>J_valor_derecho:
                J_res=J_valor_izquierdo-J_valor_derecho
                        
        elif J_valor_izquierdo<J_valor_derecho:
                J_res=J_valor_derecho-J_valor_izquierdo 
                    
        else: 
                J_res=0
                            
        if valor.J_SP_dif is not None:
           J_cont6+=1
           if J_ganador==valor.J_SP_equip.nombre and J_res>valor.J_SP_dif :
              J_cont_SP+=1
            
           
    if cont_J_ML !=0 and J_cont !=0:
       J_prom=J_cont_ML*100/J_cont
                            
    if cont_J_SP !=0 and J_cont6 !=0:
       J_prom6=J_cont_SP*100/J_cont6
                            
    if cont_J_Ud !=0 and J_cont1 !=0:
       J_prom1=J_cont_Ud*100/J_cont1   
                        
    if cont_J_SB !=0 and J_cont2 !=0:
       J_prom2=J_cont_SB*100/J_cont2
                            
    if cont_J_MA !=0 and J_cont3 !=0:
       J_prom3=J_cont_MA*100/J_cont3
                            
    if cont_J_BB !=0 and J_cont4 !=0:
       J_prom4=J_cont_BB*100/J_cont5
                            
    if cont_J_Total !=0 and J_cont5 !=0:
       J_prom5=J_cont_Total*100/J_cont5      
       
       
    mejor_prom_ML=0
    mejor_prom_SP=0
    mejor_prom_T=0
    mejor_prom_Ud=0
    mejor_prom_SB=0
    mejor_prom_MA=0     
    mejor_prom_BB=0
    nombre_s=0
    nombre_s1=0
    nombre_s2=0
    nombre_s3=0
    nombre_s4=0
    nombre_s5=0
    nombre_s6=0
    
    
    list_ML=[A_prom,B_prom,C_prom,D_prom,E_prom,F_prom,G_prom,H_prom,I_prom,J_prom]
    list_SP=[A_prom6,B_prom6,C_prom6,D_prom6,E_prom6,F_prom6,G_prom6,H_prom6,I_prom6,J_prom6]
    list_T=[A_prom5,B_prom5,C_prom5,D_prom5,E_prom5,F_prom5,G_prom5,H_prom5,I_prom5,J_prom5]
    list_Ud=[A_prom1,B_prom1,C_prom1,D_prom1,E_prom1,F_prom1,G_prom1,H_prom1,I_prom1,J_prom1]     
    list_SB=[A_prom2,B_prom2,C_prom2,D_prom2,E_prom2,F_prom2,G_prom2,H_prom2,I_prom2,J_prom2]
    list_MA=[A_prom3,B_prom3,C_prom3,D_prom3,E_prom3,F_prom3,G_prom3,H_prom3,I_prom3,J_prom3]
    list_BB=[A_prom4,B_prom4,C_prom4,D_prom4,E_prom4,F_prom4,G_prom4,H_prom4,I_prom4,J_prom4]
    
    lista_sistemas=['VeriBet','Action Network','Sports Insights','PFF','Covers','Team Rankings','BetQL','Odds Jams','Scores and Odds','Betting on Cash']
       
    for indice,i in enumerate(list_ML):
        if i>mejor_prom_ML:
           mejor_prom_ML=i   
           nombre_s=indice
           
        
    for indice,i in enumerate(list_SP):
        if i>mejor_prom_SP:
           mejor_prom_SP=i        
           nombre_s1=indice
            
    for indice,i in enumerate( list_T):
        if i>mejor_prom_T:
           mejor_prom_T=i         
           nombre_s2=indice
           
    for indice,i in enumerate(list_Ud):
        if i>mejor_prom_Ud:
           mejor_prom_Ud=i 
           nombre_s3=indice
           
    for indice,i in enumerate(list_SB):
        if i>mejor_prom_SB:
           mejor_prom_SB=i 
           nombre_s4=indice
           
    for indice,i in enumerate(list_MA):
        if i>mejor_prom_MA:
           mejor_prom_MA=i 
           nombre_s5=indice
           
    for indice,i in enumerate(list_BB):
        if i>mejor_prom_BB:
           mejor_prom_BB=i 
           nombre_s6=indice
           
           
           
           
           
    for indice,i in enumerate(lista_sistemas):
        if nombre_s==indice:
           nombre_s=i       
           break
              
    for indice,i in enumerate(lista_sistemas):
        if nombre_s1==indice:
           nombre_s1=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s2==indice:
           nombre_s2=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s3==indice:
           nombre_s3=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s4==indice:
           nombre_s4=i       
           break
    
    for indice,i in enumerate(lista_sistemas):
        if nombre_s5==indice:
           nombre_s5=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s6==indice:
           nombre_s6=i       
           break          
              
              
              
              
    return render(request,'Baseball/resultados_sistemas.html', {'cont_A_ML':cont_A_ML, 'cont_A_SP':cont_A_SP, 'cont_A_Ud':cont_A_Ud, 
                                                              'cont_A_MA':cont_A_MA,'cont_A_SB':cont_A_SB,'cont_A_BB':cont_A_BB,
                                                              'cont_A_Total':cont_A_Total,'A_cont':A_cont,'A_cont1':A_cont1,'A_cont2':A_cont2,
                                                              'A_cont3':A_cont3,'A_cont4':A_cont4,'A_cont5':A_cont5,'A_cont6':A_cont6, 
                                                              'A_prom':A_prom,'A_prom1':A_prom1,'A_prom2':A_prom2,'A_prom3':A_prom3,'A_prom4':A_prom4,
                                                              'A_prom5':A_prom5,'A_prom6':A_prom6,'cont_B_ML': cont_B_ML, 'cont_B_SP': cont_B_SP, 
                                                              'cont_B_Ud': cont_B_Ud, 'cont_B_MA': cont_B_MA, 'cont_B_SB': cont_B_SB, 'cont_B_BB': cont_B_BB,
                                                              'cont_B_Total': cont_B_Total, 'B_cont': B_cont, 'B_cont1': B_cont1, 'B_cont2': B_cont2,
                                                              'B_cont3': B_cont3, 'B_cont4': B_cont4, 'B_cont5': B_cont5, 'B_cont6': B_cont6, 'B_prom': B_prom,
                                                              'B_prom1': B_prom1, 'B_prom2': B_prom2, 'B_prom3': B_prom3, 'B_prom4': B_prom4, 'B_prom5': B_prom5, 
                                                              'B_prom6': B_prom6,'cont_C_ML': cont_C_ML, 'cont_C_SP': cont_C_SP, 'cont_C_Ud': cont_C_Ud, 
                                                              'cont_C_MA': cont_C_MA, 'cont_C_SB': cont_C_SB, 'cont_C_BB': cont_C_BB, 'cont_C_Total': cont_C_Total,
                                                              'C_cont': C_cont, 'C_cont1': C_cont1, 'C_cont2': C_cont2, 'C_cont3': C_cont3, 'C_cont4': C_cont4,
                                                              'C_cont5': C_cont5, 'C_cont6': C_cont6, 'C_prom': C_prom, 'C_prom1': C_prom1, 'C_prom2': C_prom2,
                                                              'C_prom3': C_prom3, 'C_prom4': C_prom4, 'C_prom5': C_prom5, 'C_prom6': C_prom6, 'cont_D_ML': cont_D_ML,
                                                              'cont_D_SP': cont_D_SP, 'cont_D_Ud': cont_D_Ud, 'cont_D_MA': cont_D_MA, 'cont_D_SB': cont_D_SB,
                                                              'cont_D_BB': cont_D_BB, 'cont_D_Total':cont_D_Total, 'D_cont': D_cont, 'D_cont1': D_cont1,
                                                              'D_cont2': D_cont2, 'D_cont3': D_cont3, 'D_cont4': D_cont4,'D_cont5': D_cont5, 'D_cont6': D_cont6,
                                                              'D_prom': D_prom, 'D_prom1': D_prom1, 'D_prom2': D_prom2,'D_prom3': D_prom3, 'D_prom4': D_prom4, 
                                                              'D_prom5': D_prom5, 'D_prom6': D_prom6, 'cont_E_ML': cont_E_ML, 'cont_E_SP': cont_E_SP, 
                                                              'cont_E_Ud': cont_E_Ud, 'cont_E_MA': cont_E_MA, 'cont_E_SB': cont_E_SB, 'cont_E_BB': cont_E_BB, 
                                                              'cont_E_Total': cont_E_Total,'E_cont': E_cont, 'E_cont1': E_cont1, 'E_cont2': E_cont2, 'E_cont3': E_cont3,
                                                              'E_cont4': E_cont4,'E_cont5': E_cont5, 'E_cont6': E_cont6, 'E_prom': E_prom, 'E_prom1': E_prom1, 
                                                              'E_prom2': E_prom2,'E_prom3': E_prom3, 'E_prom4': E_prom4, 'E_prom5': E_prom5, 'E_prom6': E_prom6,
                                                              'cont_F_ML': cont_F_ML, 'cont_F_SP': cont_F_SP, 'cont_F_Ud': cont_F_Ud, 'cont_F_MA': cont_F_MA, 
                                                              'cont_F_SB': cont_F_SB, 'cont_F_BB': cont_F_BB, 'cont_F_Total': cont_F_Total,'F_cont': F_cont, 
                                                              'F_cont1': F_cont1, 'F_cont2': F_cont2, 'F_cont3': F_cont3,'F_cont4': F_cont4,'F_cont5': F_cont5, 
                                                              'F_cont6': F_cont6, 'F_prom': F_prom, 'F_prom1': F_prom1, 'F_prom2': F_prom2,'F_prom3': F_prom3, 
                                                              'F_prom4': F_prom4, 'F_prom5': F_prom5, 'F_prom6': F_prom6,'cont_G_ML': cont_G_ML, 'cont_G_SP': cont_G_SP,
                                                              'cont_G_Ud': cont_G_Ud, 'cont_G_MA':cont_G_MA, 'cont_G_SB':cont_G_SB, 'cont_G_BB': cont_G_BB,
                                                              'cont_G_Total':cont_G_Total,'G_cont': G_cont, 'G_cont1': G_cont1, 'G_cont2': G_cont2, 'G_cont3': G_cont3,
                                                              'G_cont4': G_cont4,'G_cont5': G_cont5, 'G_cont6': G_cont6, 'G_prom': G_prom, 'G_prom1': G_prom1, 
                                                              'G_prom2': G_prom2,'G_prom3': G_prom3, 'G_prom4': G_prom4, 'G_prom5': G_prom5, 'G_prom6': G_prom6,
                                                              'cont_H_ML': cont_H_ML, 'cont_H_SP': cont_H_SP, 'cont_H_Ud': cont_H_Ud, 'cont_H_MA':cont_H_MA,
                                                              'cont_H_SB': cont_H_SB, 'cont_H_BB': cont_H_BB, 'cont_H_Total':cont_H_Total,'H_cont': H_cont,
                                                              'H_cont1': H_cont1, 'H_cont2': H_cont2, 'H_cont3': H_cont3,'H_cont4': H_cont4,'H_cont5': H_cont5,
                                                              'H_cont6': H_cont6, 'H_prom': H_prom, 'H_prom1': H_prom1, 'H_prom2': H_prom2,'H_prom3': H_prom3, 
                                                              'H_prom4': H_prom4, 'H_prom5': H_prom5, 'H_prom6': H_prom6,'cont_I_ML': cont_I_ML, 'cont_I_SP': cont_I_SP,
                                                              'cont_I_Ud': cont_I_Ud, 'cont_I_MA': cont_I_MA, 'cont_I_SB': cont_I_SB, 'cont_I_BB': cont_I_BB, 
                                                              'cont_I_Total': cont_I_Total,'I_cont': I_cont, 'I_cont1': I_cont1, 'I_cont2': I_cont2, 'I_cont3': I_cont3,
                                                              'I_cont4': I_cont4,'I_cont5': I_cont5, 'I_cont6': I_cont6, 'I_prom': I_prom, 'I_prom1': I_prom1,
                                                              'I_prom2': I_prom2,'I_prom3': I_prom3, 'I_prom4': I_prom4, 'I_prom5': I_prom5, 'I_prom6': I_prom6,
                                                              'cont_J_ML': cont_J_ML, 'cont_J_SP': cont_J_SP, 'cont_J_Ud': cont_J_Ud, 'cont_J_MA': cont_J_MA,
                                                              'cont_J_SB': cont_J_SB, 'cont_J_BB':cont_J_BB, 'cont_J_Total': cont_J_Total,'J_cont': J_cont, 
                                                              'J_cont1': J_cont1, 'J_cont2': J_cont2, 'J_cont3': J_cont3,'J_cont4': J_cont4,'J_cont5': J_cont5, 
                                                              'J_cont6': J_cont6, 'J_prom': J_prom, 'J_prom1': J_prom1, 'J_prom2': J_prom2,'J_prom3': J_prom3, 
                                                              'J_prom4': J_prom4, 'J_prom5': J_prom5, 'J_prom6': J_prom6,'nombre_s':nombre_s,'nombre_s1':nombre_s1,
                                                              'nombre_s2':nombre_s2,'nombre_s3':nombre_s3,'nombre_s4':nombre_s4,'nombre_s5':nombre_s5,'nombre_s6':nombre_s6,
                                                              'mejor_prom_ML':mejor_prom_ML,'mejor_prom_SP':mejor_prom_SP,'mejor_prom_T':mejor_prom_T,
                                                              'mejor_prom_Ud':mejor_prom_Ud,'mejor_prom_SB':mejor_prom_SB,'mejor_prom_MA':mejor_prom_MA,'mejor_prom_BB':mejor_prom_BB,  })
    
    
    
#Hockey

def Crear_Hockey(request):
    if request.method == 'POST':
        formulario = Hockey_form(request.POST)
        if formulario.is_valid():
            formulario.clean()
            objeto_creado = formulario.save()
            
          
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = Hockey.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = Hockey.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = Hockey.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = Hockey.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'Hockey/informes.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,  'formulario':formulario, 'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })
       
        else:
            return render(request, 'Hockey/crear_hockey.html', {'formulario': formulario})
    else:
        formulario = Hockey_form()
        return render(request, 'Hockey/crear_hockey.html', {'formulario': formulario})
 
def Listar_Hockey(request):
    lista =Hockey.objects.all().order_by('fecha')
    return render(request, 'Hockey/listar_hockey.html', {'lista':lista} )

def Eliminar_Hockey(request, id):
    f = get_object_or_404(Hockey, id=id)
    f.delete()
    return redirect('listar_hockey')

def Buscar_Hockey(request):
    resultados = []
    if request.method == 'POST':
        termino_busqueda = request.POST.get('searchbar')
        
        if termino_busqueda:
            # Construye condiciones para buscar en el nombre del equipo local o visitante
            condiciones = (
                Q(equipo_local__nombre__icontains=termino_busqueda) |
                Q(equipo_visitante__nombre__icontains=termino_busqueda)
            )
            
            # Filtra los resultados basándose en las condiciones construidas
            resultados = Hockey.objects.filter(condiciones)
        

        return render(request, 'Hockey/resultados.html', {'resultados': resultados})
    return render(request, 'Hockey/listar_hockey.html')

def Resultado_Hockey(request, id):
    f = Hockey.objects.get(id=id)
    
    equipo_local = f.equipo_local.nombre
    equipo_visitante = f.equipo_visitante.nombre
    opciones_ganador = [ equipo_local,equipo_visitante,'Empate' ]
    
    if request.method == 'POST':
        form = resultado_Hockey_form(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return redirect('listar_hockey')
    else:
        form = resultado_Hockey_form( instance=f)

    return render(request, 'Hockey/resultado_hockey.html', {'form': form,'opciones_ganador': opciones_ganador})

def Informe_Resultado_Hockey(request, id):
            objeto_creado = Hockey.objects.get(id=id)
    
    
   
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = Hockey.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = Hockey.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = Hockey.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = Hockey.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'Hockey/informe_lista.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })

def Resultados_Sistemas_Hockey(request): 
    
    partidos_filtrados = Hockey.objects.exclude(ganador__isnull=True).exclude(resultado__isnull=True)
    partidos = partidos_filtrados.order_by('-fecha')[:20]
    
    
    #Sistema A
    
    ganador=''
    cont_A_ML=0
    cont_A_SP=0
    cont_A_Ud=0
    cont_A_SB=0
    cont_A_MA=0
    cont_A_BB=0
    cont_A_Total=0
    A_cont=0
    A_cont1=0
    A_cont2=0
    A_cont3=0
    A_cont4=0
    A_cont5=0
    A_cont6=0
    sum=0
    res=0
    valor_izquierdo=0
    valor_derecho=0
    A_prom=0
    A_prom1=0
    A_prom2=0
    A_prom3=0
    A_prom4=0 
    A_prom5=0
    A_prom6=0
    
    for valor in partidos: 
        
        ganador=valor.ganador
        
        valor_izquierdo, valor_derecho = extraer_valores_de_resultado(valor)
        sum= valor_izquierdo+valor_derecho
        
        if valor.A_ML_equip is not None:
           A_cont+=1
           if ganador==valor.A_ML_equip.nombre:
              cont_A_ML+=1 
              
              
        if valor.A_Ud_equip is not None:
           A_cont1+=1      
           if ganador==valor.A_Ud_equip.nombre:
              cont_A_Ud+=1
              
              
        if valor.A_SB_equip is not None: 
           A_cont2+=1      
           if ganador==valor.A_SB_equip.nombre:
              cont_A_SB+=1
              
              
        if valor.A_MA is not None:
           A_cont3+=1 
           if ganador==valor.A_MA.nombre:
              cont_A_MA+=1
              
              
        if valor.A_BB is not None:  
           A_cont4+=1 
           if ganador==valor.A_BB.nombre:
              cont_A_BB+=1
         
         
        if valor.A_total_punto is not None: 
           A_cont5+=1 
           if sum>valor.A_total_punto and valor.A_Total_OU=='OVER':
              cont_A_Total+=1
           if sum<=valor.A_total_punto and valor.A_Total_OU=='UNDER':
              cont_A_Total+=1
         
         
       
        if valor_izquierdo>valor_derecho:
            res=valor_izquierdo-valor_derecho
           
        elif valor_izquierdo<valor_derecho:
            res=valor_derecho-valor_izquierdo 
        
        else: 
            res=0
        
        if valor.A_SP_dif is not None:
           A_cont6+=1
           if ganador==valor.A_SP_equip.nombre and res>valor.A_SP_dif :
              cont_A_SP+=1
           
           
           
    if cont_A_ML !=0 and A_cont !=0:
           A_prom=cont_A_ML*100/A_cont
        
    if cont_A_SP !=0 and A_cont6 !=0:
           A_prom6=cont_A_SP*100/A_cont6
           
    if cont_A_Ud !=0 and A_cont1 !=0:
           A_prom1=cont_A_Ud*100/A_cont1
           
    if cont_A_SB !=0 and A_cont2 !=0:
           A_prom2=cont_A_SB*100/A_cont2
           
    if cont_A_MA !=0 and A_cont3 !=0:
           A_prom3=cont_A_MA*100/A_cont3
           
    if cont_A_BB !=0 and A_cont4 !=0:
           A_prom4=cont_A_BB*100/A_cont5
           
    if cont_A_Total !=0 and A_cont5 !=0:
           A_prom5=cont_A_Total*100/A_cont5      
           
           
           
    #Sistema B     
    
    B_ganador=''
    cont_B_ML=0
    cont_B_SP=0
    cont_B_Ud=0
    cont_B_SB=0
    cont_B_MA=0
    cont_B_BB=0
    cont_B_Total=0
    B_cont=0
    B_cont1=0
    B_cont2=0
    B_cont3=0
    B_cont4=0
    B_cont5=0
    B_cont6=0
    B_sum=0
    B_res=0
    B_valor_izquierdo=0
    B_valor_derecho=0
    B_prom=0
    B_prom1=0
    B_prom2=0
    B_prom3=0
    B_prom4=0 
    B_prom5=0
    B_prom6=0
    
    for valor in partidos: 
        
        B_ganador=valor.ganador
        
        B_valor_izquierdo, B_valor_derecho = extraer_valores_de_resultado(valor)
        B_sum= B_valor_izquierdo+B_valor_derecho
        
        if valor.B_ML_equip is not None:
           B_cont+=1
           if B_ganador==valor.B_ML_equip.nombre:
              cont_B_ML+=1 
              
              
        if valor.B_Ud_equip is not None:
           B_cont1+=1      
           if B_ganador==valor.B_Ud_equip.nombre:
              cont_B_Ud+=1
              
              
        if valor.B_SB_equip is not None: 
           B_cont2+=1      
           if B_ganador==valor.B_SB_equip.nombre:
              cont_B_SB+=1
              
              
        if valor.B_MA is not None:
           B_cont3+=1 
           if B_ganador==valor.B_MA.nombre:
              cont_B_MA+=1
              
              
        if valor.B_BB is not None:  
           B_cont4+=1 
           if B_ganador==valor.B_BB.nombre:
              cont_B_BB+=1
         
         
        if valor.B_total_punto is not None: 
           B_cont5+=1 
           if B_sum>valor.B_total_punto and valor.B_Total_OU=='OVER':
              cont_B_Total+=1
           if B_sum<=valor.B_total_punto and valor.B_Total_OU=='UNDER':
              cont_B_Total+=1
         
         
       
        if B_valor_izquierdo>B_valor_derecho:
            B_res=B_valor_izquierdo-B_valor_derecho
           
        elif B_valor_izquierdo<B_valor_derecho:
            B_res=B_valor_derecho-B_valor_izquierdo 
        
        else: 
            B_res=0
        
        if valor.B_SP_dif is not None:
           B_cont6+=1
           if B_ganador==valor.B_SP_equip.nombre and B_res>valor.B_SP_dif :
              cont_B_SP+=1
           
           
           
    if cont_B_ML !=0 and B_cont !=0:
           B_prom=cont_B_ML*100/B_cont
        
    if cont_B_SP !=0 and B_cont6 !=0:
           B_prom6=cont_B_SP*100/B_cont6
           
    if cont_B_Ud !=0 and B_cont1 !=0:
           B_prom1=cont_B_Ud*100/B_cont1
           
    if cont_B_SB !=0 and B_cont2 !=0:
           B_prom2=cont_B_SB*100/B_cont2
           
    if cont_B_MA !=0 and B_cont3 !=0:
           B_prom3=cont_B_MA*100/B_cont3
           
    if cont_B_BB !=0 and B_cont4 !=0:
           B_prom4=cont_B_BB*100/B_cont5
           
    if cont_B_Total !=0 and B_cont5 !=0:
           B_prom5=cont_B_Total*100/B_cont5             
           
           
    C_ganador=''
    cont_C_ML=0
    cont_C_SP=0
    cont_C_Ud=0
    cont_C_SB=0
    cont_C_MA=0
    cont_C_BB=0
    cont_C_Total=0
    C_cont=0
    C_cont1=0
    C_cont2=0
    C_cont3=0
    C_cont4=0
    C_cont5=0
    C_cont6=0
    C_sum=0
    C_res=0
    C_valor_izquierdo=0
    C_valor_derecho=0
    C_prom=0
    C_prom1=0
    C_prom2=0
    C_prom3=0
    C_prom4=0 
    C_prom5=0        
    C_prom6=0
       
    for valor in partidos: 
        
        C_ganador=valor.ganador
            
        C_valor_izquierdo, C_valor_derecho = extraer_valores_de_resultado(valor)
        C_sum= C_valor_izquierdo+C_valor_derecho
            
        if valor.C_ML_equip is not None:
            C_cont+=1
            if C_ganador==valor.C_ML_equip.nombre:
                cont_C_ML+=1 
                
        if valor.C_Ud_equip is not None:
            C_cont1+=1      
            if C_ganador==valor.C_Ud_equip.nombre:
                cont_C_Ud+=1
                
        if valor.C_SB_equip is not None: 
            C_cont2+=1      
            if C_ganador==valor.C_SB_equip.nombre:
                cont_C_SB+=1
                
        if valor.C_MA is not None:
            C_cont3+=1 
            if C_ganador==valor.C_MA.nombre:
                cont_C_MA+=1
                
        if valor.C_BB is not None:  
            C_cont4+=1 
            if C_ganador==valor.C_BB.nombre:
                cont_C_BB+=1
            
            
        if valor.C_total_punto is not None: 
            C_cont5+=1 
            if C_sum>valor.C_total_punto and valor.C_Total_OU=='OVER':
                cont_C_Total+=1
            if C_sum<=valor.C_total_punto and valor.C_Total_OU=='UNDER':
                cont_C_Total+=1
            
            

        if C_valor_izquierdo>C_valor_derecho:
            C_res=C_valor_izquierdo-C_valor_derecho
            
        elif C_valor_izquierdo<C_valor_derecho:
            C_res=C_valor_derecho-C_valor_izquierdo 

        else: 
            C_res=0
            
        if valor.C_SP_dif is not None:
            C_cont6+=1
            if C_ganador==valor.C_SP_equip.nombre and C_res>valor.C_SP_dif :
                cont_C_SP+=1
           
           
    if cont_C_ML !=0 and C_cont !=0:
       C_prom=cont_C_ML*100/C_cont
            
    if cont_C_SP !=0 and C_cont6 !=0:
       C_prom6=cont_C_SP*100/C_cont6
            
    if cont_C_Ud !=0 and C_cont1 !=0:
       C_prom1=cont_C_Ud*100/C_cont1
            
    if cont_C_SB !=0 and C_cont2 !=0:
       C_prom2=cont_C_SB*100/C_cont2
            
    if cont_C_MA !=0 and C_cont3 !=0:
       C_prom3=cont_C_MA*100/C_cont3
            
    if cont_C_BB !=0 and C_cont4 !=0:
       C_prom4=cont_C_BB*100/C_cont5
            
    if cont_C_Total !=0 and C_cont5 !=0:
       C_prom5=cont_C_Total*100/C_cont5       
           
    
    
    D_ganador=''
    cont_D_ML=0
    cont_D_SP=0
    cont_D_Ud=0
    cont_D_SB=0
    cont_D_MA=0
    cont_D_BB=0
    cont_D_Total=0
    D_cont=0
    D_cont1=0
    D_cont2=0
    D_cont3=0
    D_cont4=0
    D_cont5=0
    D_cont6=0
    D_sum=0
    D_res=0
    D_valor_izquierdo=0
    D_valor_derecho=0
    D_prom=0
    D_prom1=0
    D_prom2=0
    D_prom3=0
    D_prom4=0 
    D_prom5=0        
    D_prom6=0

    
    
    
    for valor in partidos: 
        
        D_ganador=valor.ganador
            
        D_valor_izquierdo, D_valor_derecho = extraer_valores_de_resultado(valor)
        D_sum= D_valor_izquierdo+D_valor_derecho
            
        if valor.D_ML_equip is not None:
           D_cont+=1
           if D_ganador==valor.D_ML_equip.nombre:
              cont_D_ML+=1 
            
        if valor.D_Ud_equip is not None:
           D_cont1+=1      
           if D_ganador==valor.D_Ud_equip.nombre:
              cont_D_Ud+=1
            
        if valor.D_SB_equip is not None: 
           D_cont2+=1      
           if D_ganador==valor.D_SB_equip.nombre:
              cont_D_SB+=1
            
        if valor.D_MA is not None:
           D_cont3+=1 
           if D_ganador==valor.D_MA.nombre:
              cont_D_MA+=1
            
        if valor.D_BB is not None:  
           D_cont4+=1 
           if D_ganador==valor.D_BB.nombre:
              cont_D_BB+=1
        
        
        if valor.D_total_punto is not None: 
           D_cont5+=1 
           if D_sum>valor.D_total_punto and valor.D_Total_OU=='OVER':
              cont_D_Total+=1
           if D_sum<=valor.D_total_punto and valor.D_Total_OU=='UNDER':
              cont_D_Total+=1
        
        
    
        if D_valor_izquierdo>D_valor_derecho:
            D_res=D_valor_izquierdo-D_valor_derecho
        
        elif D_valor_izquierdo<D_valor_derecho:
            D_res=D_valor_derecho-D_valor_izquierdo 
        
        else: 
            D_res=0
            
        if valor.D_SP_dif is not None:
           D_cont6+=1
           if D_ganador==valor.D_SP_equip.nombre and D_res>valor.D_SP_dif :
              cont_D_SP+=1
             
           
    if cont_D_ML !=0 and D_cont !=0:
       D_prom=cont_D_ML*100/D_cont
            
    if cont_D_SP !=0 and D_cont6 !=0:
       D_prom6=cont_D_SP*100/D_cont6
            
    if cont_D_Ud !=0 and D_cont1 !=0:
       D_prom1=cont_D_Ud*100/D_cont1
            
    if cont_D_SB !=0 and D_cont2 !=0:
       D_prom2=cont_D_SB*100/D_cont2
            
    if cont_D_MA !=0 and D_cont3 !=0:
       D_prom3=cont_D_MA*100/D_cont3
            
    if cont_D_BB !=0 and D_cont4 !=0:
       D_prom4=cont_D_BB*100/D_cont5
            
    if cont_D_Total !=0 and D_cont5 !=0:
       D_prom5=cont_D_Total*100/D_cont5
        
    
    E_ganador=''
    cont_E_ML=0
    cont_E_SP=0
    cont_E_Ud=0
    cont_E_SB=0
    cont_E_MA=0
    cont_E_BB=0
    cont_E_Total=0
    E_cont=0
    E_cont1=0
    E_cont2=0
    E_cont3=0
    E_cont4=0
    E_cont5=0
    E_cont6=0
    E_sum=0
    E_res=0
    E_valor_izquierdo=0
    E_valor_derecho=0
    E_prom=0
    E_prom1=0
    E_prom2=0
    E_prom3=0
    E_prom4=0 
    E_prom5=0        
    E_prom6=0
       
    for valor in partidos: 
        
        E_ganador=valor.ganador
            
        E_valor_izquierdo, E_valor_derecho = extraer_valores_de_resultado(valor)
        E_sum= E_valor_izquierdo+E_valor_derecho
            
        if valor.E_ML_equip is not None:
           E_cont+=1
           if E_ganador==valor.E_ML_equip.nombre:
              cont_E_ML+=1 
            
        if valor.E_Ud_equip is not None:
           E_cont1+=1      
           if E_ganador==valor.E_Ud_equip.nombre:
              cont_E_Ud+=1
            
        if valor.E_SB_equip is not None: 
           E_cont2+=1      
           if E_ganador==valor.E_SB_equip.nombre:
              cont_E_SB+=1
            
        if valor.E_MA is not None:
           E_cont3+=1 
           if E_ganador==valor.E_MA.nombre:
              cont_E_MA+=1
            
        if valor.E_BB is not None:  
           E_cont4+=1 
           if E_ganador==valor.E_BB.nombre:
              cont_E_BB+=1
        
        
        if valor.E_total_punto is not None: 
           E_cont5+=1 
           if E_sum>valor.E_total_punto and valor.E_Total_OU=='OVER':
              cont_E_Total+=1
           if E_sum<=valor.E_total_punto and valor.E_Total_OU=='UNDER':
              cont_E_Total+=1
        
        
    
        if E_valor_izquierdo>E_valor_derecho:
            E_res=E_valor_izquierdo-E_valor_derecho
        
        elif E_valor_izquierdo<E_valor_derecho:
            E_res=E_valor_derecho-E_valor_izquierdo 
        
        else: 
            E_res=0
            
        if valor.E_SP_dif is not None:
           E_cont6+=1
           if E_ganador==valor.E_SP_equip.nombre and E_res>valor.E_SP_dif :
              cont_E_SP+=1
            
           
    if cont_E_ML !=0 and E_cont !=0:
       E_prom=cont_E_ML*100/E_cont
            
    if cont_E_SP !=0 and E_cont6 !=0:
       E_prom6=cont_E_SP*100/E_cont6
            
    if cont_E_Ud !=0 and E_cont1 !=0:
       E_prom1=cont_E_Ud*100/E_cont1   
        
    if cont_E_SB !=0 and E_cont2 !=0:
       E_prom2=cont_E_SB*100/E_cont2
            
    if cont_E_MA !=0 and E_cont3 !=0:
       E_prom3=cont_E_MA*100/E_cont3
            
    if cont_E_BB !=0 and E_cont4 !=0:
       E_prom4=cont_E_BB*100/E_cont5
            
    if cont_E_Total !=0 and E_cont5 !=0:
       E_prom5=cont_E_Total*100/E_cont5     
    
    
    
    
    F_ganador=''
    cont_F_ML=0
    cont_F_SP=0
    cont_F_Ud=0
    cont_F_SB=0
    cont_F_MA=0
    cont_F_BB=0
    cont_F_Total=0
    F_cont=0
    F_cont1=0
    F_cont2=0
    F_cont3=0
    F_cont4=0
    F_cont5=0
    F_cont6=0
    F_sum=0
    F_res=0
    F_valor_izquierdo=0
    F_valor_derecho=0
    F_prom=0
    F_prom1=0
    F_prom2=0
    F_prom3=0
    F_prom4=0 
    F_prom5=0        
    F_prom6=0
       
    
    for valor in partidos: 
        
 
        F_valor_izquierdo, F_valor_derecho = extraer_valores_de_resultado(valor)
        F_sum = F_valor_izquierdo + F_valor_derecho
                
        if valor.F_ML_equip is not None:
           F_cont+=1
           if F_ganador==valor.F_ML_equip.nombre:
              F_cont_ML+=1 
                
        if valor.F_Ud_equip is not None:
           F_cont1+=1      
           if F_ganador==valor.F_Ud_equip.nombre:
              F_cont_Ud+=1
                
        if valor.F_SB_equip is not None: 
           F_cont2+=1      
           if F_ganador==valor.F_SB_equip.nombre:
              F_cont_SB+=1
                
        if valor.F_MA is not None:
           F_cont3+=1 
           if F_ganador==valor.F_MA.nombre:
              F_cont_MA+=1
                
        if valor.F_BB is not None:  
           F_cont4+=1 
           if F_ganador==valor.F_BB.nombre:
              F_cont_BB+=1
            
            
        if valor.F_total_punto is not None: 
           F_cont5+=1 
           if F_sum>F_valor_izquierdo and valor.F_Total_OU=='OVER':
              F_cont_Total+=1
           if F_sum<=valor.F_total_punto and valor.F_Total_OU=='UNDER':
              F_cont_Total+=1
            
            
        if F_valor_izquierdo>F_valor_derecho:
            F_res=F_valor_izquierdo-F_valor_derecho
            
        elif F_valor_izquierdo<F_valor_derecho:
            F_res=F_valor_derecho-F_valor_izquierdo 
        
        else: 
            F_res=0
                
        if valor.F_SP_dif is not None:
           F_cont6+=1
           if F_ganador==valor.F_SP_equip.nombre and F_res>valor.F_SP_dif :
              F_cont_SP+=1
            
           
    if cont_F_ML !=0 and F_cont !=0:
       F_prom=F_cont_ML*100/F_cont
                
    if cont_F_SP !=0 and F_cont6 !=0:
       F_prom6=F_cont_SP*100/F_cont6
                
    if cont_F_Ud !=0 and F_cont1 !=0:
       F_prom1=F_cont_Ud*100/F_cont1   
            
    if cont_F_SB !=0 and F_cont2 !=0:
       F_prom2=F_cont_SB*100/F_cont2
                
    if cont_F_MA !=0 and F_cont3 !=0:
       F_prom3=F_cont_MA*100/F_cont3
                
    if cont_F_BB !=0 and F_cont4 !=0:
       F_prom4=F_cont_BB*100/F_cont5
                
    if cont_F_Total !=0 and F_cont5 !=0:
       F_prom5=F_cont_Total*100/F_cont5
        
    
    G_ganador=''
    cont_G_ML=0
    cont_G_SP=0
    cont_G_Ud=0
    cont_G_SB=0
    cont_G_MA=0
    cont_G_BB=0
    cont_G_Total=0
    G_cont=0
    G_cont1=0
    G_cont2=0
    G_cont3=0
    G_cont4=0
    G_cont5=0
    G_cont6=0
    G_sum=0
    G_res=0
    G_valor_izquierdo=0
    G_valor_derecho=0
    G_prom=0
    G_prom1=0
    G_prom2=0
    G_prom3=0
    G_prom4=0 
    G_prom5=0        
    G_prom6=0

    for valor in partidos: 
        
        G_valor_izquierdo, G_valor_derecho = extraer_valores_de_resultado(valor)
        G_sum = G_valor_izquierdo + G_valor_derecho
                    
        if valor.G_ML_equip is not None:
           G_cont+=1
           if G_ganador==valor.G_ML_equip.nombre:
              G_cont_ML+=1 
                    
        if valor.G_Ud_equip is not None:
           G_cont1+=1      
           if G_ganador==valor.G_Ud_equip.nombre:
              G_cont_Ud+=1
                    
        if valor.G_SB_equip is not None: 
           G_cont2+=1      
           if G_ganador==valor.G_SB_equip.nombre:
              G_cont_SB+=1
                    
        if valor.G_MA is not None:
           G_cont3+=1 
           if G_ganador==valor.G_MA.nombre:
              G_cont_MA+=1
                    
        if valor.G_BB is not None:  
           G_cont4+=1 
           if G_ganador==valor.G_BB.nombre:
              G_cont_BB+=1
                
                
        if valor.G_total_punto is not None: 
           G_cont5+=1 
           if G_sum>G_valor_izquierdo and valor.G_Total_OU=='OVER':
              G_cont_Total+=1
           if G_sum<=valor.G_total_punto and valor.G_Total_OU=='UNDER':
              G_cont_Total+=1
                
                
        if G_valor_izquierdo>G_valor_derecho:
            G_res=G_valor_izquierdo-G_valor_derecho
                
        elif G_valor_izquierdo<G_valor_derecho:
            G_res=G_valor_derecho-G_valor_izquierdo 
            
        else: 
            G_res=0
                    
        if valor.G_SP_dif is not None:
           G_cont6+=1
           if G_ganador==valor.G_SP_equip.nombre and G_res>valor.G_SP_dif :
              G_cont_SP+=1
            
           
    if cont_G_ML !=0 and G_cont !=0:
       G_prom=G_cont_ML*100/G_cont
                    
    if cont_G_SP !=0 and G_cont6 !=0:
       G_prom6=G_cont_SP*100/G_cont6
                    
    if cont_G_Ud !=0 and G_cont1 !=0:
       G_prom1=G_cont_Ud*100/G_cont1   
                
    if cont_G_SB !=0 and G_cont2 !=0:
       G_prom2=G_cont_SB*100/G_cont2
                    
    if cont_G_MA !=0 and G_cont3 !=0:
       G_prom3=G_cont_MA*100/G_cont3
                    
    if cont_G_BB !=0 and G_cont4 !=0:
       G_prom4=G_cont_BB*100/G_cont5
                    
    if cont_G_Total !=0 and G_cont5 !=0:
       G_prom5=G_cont_Total*100/G_cont5
            
            
            
    H_ganador=''
    cont_H_ML=0
    cont_H_SP=0
    cont_H_Ud=0
    cont_H_SB=0
    cont_H_MA=0
    cont_H_BB=0
    cont_H_Total=0
    H_cont=0
    H_cont1=0
    H_cont2=0
    H_cont3=0
    H_cont4=0
    H_cont5=0
    H_cont6=0
    H_sum=0
    H_res=0
    H_valor_izquierdo=0
    H_valor_derecho=0
    H_prom=0
    H_prom1=0
    H_prom2=0
    H_prom3=0
    H_prom4=0 
    H_prom5=0        
    H_prom6=0
        
            
    for valor in partidos: 
        
        H_valor_izquierdo, H_valor_derecho = extraer_valores_de_resultado(valor)
        H_sum = H_valor_izquierdo + H_valor_derecho
                        
        if valor.H_ML_equip is not None:
           H_cont+=1
           if H_ganador==valor.H_ML_equip.nombre:
              H_cont_ML+=1 
                        
        if valor.H_Ud_equip is not None:
           H_cont1+=1      
           if H_ganador==valor.H_Ud_equip.nombre:
              H_cont_Ud+=1
                        
        if valor.H_SB_equip is not None: 
           H_cont2+=1      
           if H_ganador==valor.H_SB_equip.nombre:
              H_cont_SB+=1
                        
        if valor.H_MA is not None:
           H_cont3+=1 
           if H_ganador==valor.H_MA.nombre:
              H_cont_MA+=1
                        
        if valor.H_BB is not None:  
           H_cont4+=1 
           if H_ganador==valor.H_BB.nombre:
              H_cont_BB+=1
                    
                    
        if valor.H_total_punto is not None: 
           H_cont5+=1 
           if H_sum>H_valor_izquierdo and valor.H_Total_OU=='OVER':
              H_cont_Total+=1
           if H_sum<=valor.H_total_punto and valor.H_Total_OU=='UNDER':
              H_cont_Total+=1
                    
                    
        if H_valor_izquierdo>H_valor_derecho:
                H_res=H_valor_izquierdo-H_valor_derecho
                    
        elif H_valor_izquierdo<H_valor_derecho:
                H_res=H_valor_derecho-H_valor_izquierdo 
                
        else: 
                H_res=0
                        
        if valor.H_SP_dif is not None:
           H_cont6+=1
           if H_ganador==valor.H_SP_equip.nombre and H_res>valor.H_SP_dif :
              H_cont_SP+=1
            
           
    if cont_H_ML !=0 and H_cont !=0:
       H_prom=H_cont_ML*100/H_cont
                    
    if cont_H_SP !=0 and H_cont6 !=0:
       H_prom6=H_cont_SP*100/H_cont6
                    
    if cont_H_Ud !=0 and H_cont1 !=0:
       H_prom1=H_cont_Ud*100/H_cont1   
                
    if cont_H_SB !=0 and H_cont2 !=0:
       H_prom2=H_cont_SB*100/H_cont2
                    
    if cont_H_MA !=0 and H_cont3 !=0:
       H_prom3=H_cont_MA*100/H_cont3
                    
    if cont_H_BB !=0 and H_cont4 !=0:
       H_prom4=H_cont_BB*100/H_cont5
                    
    if cont_H_Total !=0 and H_cont5 !=0:
       H_prom5=H_cont_Total*100/H_cont5        
            
    
    
    I_ganador=''
    cont_I_ML=0
    cont_I_SP=0
    cont_I_Ud=0
    cont_I_SB=0
    cont_I_MA=0
    cont_I_BB=0
    cont_I_Total=0
    I_cont=0
    I_cont1=0
    I_cont2=0
    I_cont3=0
    I_cont4=0
    I_cont5=0
    I_cont6=0
    I_sum=0
    I_res=0
    I_valor_izquierdo=0
    I_valor_derecho=0
    I_prom=0
    I_prom1=0
    I_prom2=0
    I_prom3=0
    I_prom4=0 
    I_prom5=0        
    I_prom6=0
        
            
    for valor in partidos: 
        
        I_valor_izquierdo, I_valor_derecho = extraer_valores_de_resultado(valor)
        I_sum = I_valor_izquierdo + I_valor_derecho
                        
        if valor.I_ML_equip is not None:
           I_cont+=1
           if I_ganador==valor.I_ML_equip.nombre:
              I_cont_ML+=1 
                        
        if valor.I_Ud_equip is not None:
           I_cont1+=1      
           if I_ganador==valor.I_Ud_equip.nombre:
              I_cont_Ud+=1
                        
        if valor.I_SB_equip is not None: 
           I_cont2+=1      
           if I_ganador==valor.I_SB_equip.nombre:
              I_cont_SB+=1
                        
        if valor.I_MA is not None:
           I_cont3+=1 
           if I_ganador==valor.I_MA.nombre:
              I_cont_MA+=1
                        
        if valor.I_BB is not None:  
           I_cont4+=1 
           if I_ganador==valor.I_BB.nombre:
              I_cont_BB+=1
                    
                    
        if valor.I_total_punto is not None: 
           I_cont5+=1 
           if I_sum>I_valor_izquierdo and valor.I_Total_OU=='OVER':
              I_cont_Total+=1
           if I_sum<=valor.I_total_punto and valor.I_Total_OU=='UNDER':
              I_cont_Total+=1
                    
                    
        if I_valor_izquierdo>I_valor_derecho:
                I_res=I_valor_izquierdo-I_valor_derecho
                    
        elif I_valor_izquierdo<I_valor_derecho:
                I_res=I_valor_derecho-I_valor_izquierdo 
                
        else: 
                I_res=0
                        
        if valor.I_SP_dif is not None:
           I_cont6+=1
           if I_ganador==valor.I_SP_equip.nombre and I_res>valor.I_SP_dif :
              I_cont_SP+=1
            
           
    if cont_I_ML !=0 and I_cont !=0:
       I_prom=I_cont_ML*100/I_cont
                        
    if cont_I_SP !=0 and I_cont6 !=0:
       I_prom6=I_cont_SP*100/I_cont6
                        
    if cont_I_Ud !=0 and I_cont1 !=0:
       I_prom1=I_cont_Ud*100/I_cont1   
                    
    if cont_I_SB !=0 and I_cont2 !=0:
       I_prom2=I_cont_SB*100/I_cont2
                        
    if cont_I_MA !=0 and I_cont3 !=0:
       I_prom3=I_cont_MA*100/I_cont3
                        
    if cont_I_BB !=0 and I_cont4 !=0:
       I_prom4=I_cont_BB*100/I_cont5
                        
    if cont_I_Total !=0 and I_cont5 !=0:
       I_prom5=I_cont_Total*100/I_cont5        
            
            
    J_ganador=''
    cont_J_ML=0
    cont_J_SP=0
    cont_J_Ud=0
    cont_J_SB=0
    cont_J_MA=0
    cont_J_BB=0
    cont_J_Total=0
    J_cont=0
    J_cont1=0
    J_cont2=0
    J_cont3=0
    J_cont4=0
    J_cont5=0
    J_cont6=0
    J_sum=0
    J_res=0
    J_valor_izquierdo=0
    J_valor_derecho=0
    J_prom=0
    J_prom1=0
    J_prom2=0
    J_prom3=0
    J_prom4=0 
    J_prom5=0        
    J_prom6=0
        
    for valor in partidos: 
        
        J_valor_izquierdo, J_valor_derecho = extraer_valores_de_resultado(valor)
        J_sum = J_valor_izquierdo + J_valor_derecho
                            
        if valor.J_ML_equip is not None:
           J_cont+=1
           if J_ganador==valor.J_ML_equip.nombre:
              J_cont_ML+=1 
                            
        if valor.J_Ud_equip is not None:
           J_cont1+=1      
           if J_ganador==valor.J_Ud_equip.nombre:
              J_cont_Ud+=1
                            
        if valor.J_SB_equip is not None: 
           J_cont2+=1      
           if J_ganador==valor.J_SB_equip.nombre:
              J_cont_SB+=1
                            
        if valor.J_MA is not None:
           J_cont3+=1 
           if J_ganador==valor.J_MA.nombre:
              J_cont_MA+=1
                            
        if valor.J_BB is not None:  
           J_cont4+=1 
           if J_ganador==valor.J_BB.nombre:
              J_cont_BB+=1
                        
                        
        if valor.J_total_punto is not None: 
           J_cont5+=1 
           if J_sum>J_valor_izquierdo and valor.J_Total_OU=='OVER':
              J_cont_Total+=1
           if J_sum<=valor.J_total_punto and valor.J_Total_OU=='UNDER':
              J_cont_Total+=1
                        
                        
        if J_valor_izquierdo>J_valor_derecho:
                J_res=J_valor_izquierdo-J_valor_derecho
                        
        elif J_valor_izquierdo<J_valor_derecho:
                J_res=J_valor_derecho-J_valor_izquierdo 
                    
        else: 
                J_res=0
                            
        if valor.J_SP_dif is not None:
           J_cont6+=1
           if J_ganador==valor.J_SP_equip.nombre and J_res>valor.J_SP_dif :
              J_cont_SP+=1
            
           
    if cont_J_ML !=0 and J_cont !=0:
       J_prom=J_cont_ML*100/J_cont
                            
    if cont_J_SP !=0 and J_cont6 !=0:
       J_prom6=J_cont_SP*100/J_cont6
                            
    if cont_J_Ud !=0 and J_cont1 !=0:
       J_prom1=J_cont_Ud*100/J_cont1   
                        
    if cont_J_SB !=0 and J_cont2 !=0:
       J_prom2=J_cont_SB*100/J_cont2
                            
    if cont_J_MA !=0 and J_cont3 !=0:
       J_prom3=J_cont_MA*100/J_cont3
                            
    if cont_J_BB !=0 and J_cont4 !=0:
       J_prom4=J_cont_BB*100/J_cont5
                            
    if cont_J_Total !=0 and J_cont5 !=0:
       J_prom5=J_cont_Total*100/J_cont5      
       
       
    mejor_prom_ML=0
    mejor_prom_SP=0
    mejor_prom_T=0
    mejor_prom_Ud=0
    mejor_prom_SB=0
    mejor_prom_MA=0     
    mejor_prom_BB=0
    nombre_s=0
    nombre_s1=0
    nombre_s2=0
    nombre_s3=0
    nombre_s4=0
    nombre_s5=0
    nombre_s6=0
    
    
    list_ML=[A_prom,B_prom,C_prom,D_prom,E_prom,F_prom,G_prom,H_prom,I_prom,J_prom]
    list_SP=[A_prom6,B_prom6,C_prom6,D_prom6,E_prom6,F_prom6,G_prom6,H_prom6,I_prom6,J_prom6]
    list_T=[A_prom5,B_prom5,C_prom5,D_prom5,E_prom5,F_prom5,G_prom5,H_prom5,I_prom5,J_prom5]
    list_Ud=[A_prom1,B_prom1,C_prom1,D_prom1,E_prom1,F_prom1,G_prom1,H_prom1,I_prom1,J_prom1]     
    list_SB=[A_prom2,B_prom2,C_prom2,D_prom2,E_prom2,F_prom2,G_prom2,H_prom2,I_prom2,J_prom2]
    list_MA=[A_prom3,B_prom3,C_prom3,D_prom3,E_prom3,F_prom3,G_prom3,H_prom3,I_prom3,J_prom3]
    list_BB=[A_prom4,B_prom4,C_prom4,D_prom4,E_prom4,F_prom4,G_prom4,H_prom4,I_prom4,J_prom4]
    
    lista_sistemas=['VeriBet','Action Network','Sports Insights','PFF','Covers','Team Rankings','BetQL','Odds Jams','Scores and Odds','Betting on Cash']
       
    for indice,i in enumerate(list_ML):
        if i>mejor_prom_ML:
           mejor_prom_ML=i   
           nombre_s=indice
           
        
    for indice,i in enumerate(list_SP):
        if i>mejor_prom_SP:
           mejor_prom_SP=i        
           nombre_s1=indice
            
    for indice,i in enumerate( list_T):
        if i>mejor_prom_T:
           mejor_prom_T=i         
           nombre_s2=indice
           
    for indice,i in enumerate(list_Ud):
        if i>mejor_prom_Ud:
           mejor_prom_Ud=i 
           nombre_s3=indice
           
    for indice,i in enumerate(list_SB):
        if i>mejor_prom_SB:
           mejor_prom_SB=i 
           nombre_s4=indice
           
    for indice,i in enumerate(list_MA):
        if i>mejor_prom_MA:
           mejor_prom_MA=i 
           nombre_s5=indice
           
    for indice,i in enumerate(list_BB):
        if i>mejor_prom_BB:
           mejor_prom_BB=i 
           nombre_s6=indice
           
           
           
           
           
    for indice,i in enumerate(lista_sistemas):
        if nombre_s==indice:
           nombre_s=i       
           break
              
    for indice,i in enumerate(lista_sistemas):
        if nombre_s1==indice:
           nombre_s1=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s2==indice:
           nombre_s2=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s3==indice:
           nombre_s3=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s4==indice:
           nombre_s4=i       
           break
    
    for indice,i in enumerate(lista_sistemas):
        if nombre_s5==indice:
           nombre_s5=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s6==indice:
           nombre_s6=i       
           break          
              
              
              
              
    return render(request,'Hockey/resultados_sistemas.html', {'cont_A_ML':cont_A_ML, 'cont_A_SP':cont_A_SP, 'cont_A_Ud':cont_A_Ud, 
                                                              'cont_A_MA':cont_A_MA,'cont_A_SB':cont_A_SB,'cont_A_BB':cont_A_BB,
                                                              'cont_A_Total':cont_A_Total,'A_cont':A_cont,'A_cont1':A_cont1,'A_cont2':A_cont2,
                                                              'A_cont3':A_cont3,'A_cont4':A_cont4,'A_cont5':A_cont5,'A_cont6':A_cont6, 
                                                              'A_prom':A_prom,'A_prom1':A_prom1,'A_prom2':A_prom2,'A_prom3':A_prom3,'A_prom4':A_prom4,
                                                              'A_prom5':A_prom5,'A_prom6':A_prom6,'cont_B_ML': cont_B_ML, 'cont_B_SP': cont_B_SP, 
                                                              'cont_B_Ud': cont_B_Ud, 'cont_B_MA': cont_B_MA, 'cont_B_SB': cont_B_SB, 'cont_B_BB': cont_B_BB,
                                                              'cont_B_Total': cont_B_Total, 'B_cont': B_cont, 'B_cont1': B_cont1, 'B_cont2': B_cont2,
                                                              'B_cont3': B_cont3, 'B_cont4': B_cont4, 'B_cont5': B_cont5, 'B_cont6': B_cont6, 'B_prom': B_prom,
                                                              'B_prom1': B_prom1, 'B_prom2': B_prom2, 'B_prom3': B_prom3, 'B_prom4': B_prom4, 'B_prom5': B_prom5, 
                                                              'B_prom6': B_prom6,'cont_C_ML': cont_C_ML, 'cont_C_SP': cont_C_SP, 'cont_C_Ud': cont_C_Ud, 
                                                              'cont_C_MA': cont_C_MA, 'cont_C_SB': cont_C_SB, 'cont_C_BB': cont_C_BB, 'cont_C_Total': cont_C_Total,
                                                              'C_cont': C_cont, 'C_cont1': C_cont1, 'C_cont2': C_cont2, 'C_cont3': C_cont3, 'C_cont4': C_cont4,
                                                              'C_cont5': C_cont5, 'C_cont6': C_cont6, 'C_prom': C_prom, 'C_prom1': C_prom1, 'C_prom2': C_prom2,
                                                              'C_prom3': C_prom3, 'C_prom4': C_prom4, 'C_prom5': C_prom5, 'C_prom6': C_prom6, 'cont_D_ML': cont_D_ML,
                                                              'cont_D_SP': cont_D_SP, 'cont_D_Ud': cont_D_Ud, 'cont_D_MA': cont_D_MA, 'cont_D_SB': cont_D_SB,
                                                              'cont_D_BB': cont_D_BB, 'cont_D_Total':cont_D_Total, 'D_cont': D_cont, 'D_cont1': D_cont1,
                                                              'D_cont2': D_cont2, 'D_cont3': D_cont3, 'D_cont4': D_cont4,'D_cont5': D_cont5, 'D_cont6': D_cont6,
                                                              'D_prom': D_prom, 'D_prom1': D_prom1, 'D_prom2': D_prom2,'D_prom3': D_prom3, 'D_prom4': D_prom4, 
                                                              'D_prom5': D_prom5, 'D_prom6': D_prom6, 'cont_E_ML': cont_E_ML, 'cont_E_SP': cont_E_SP, 
                                                              'cont_E_Ud': cont_E_Ud, 'cont_E_MA': cont_E_MA, 'cont_E_SB': cont_E_SB, 'cont_E_BB': cont_E_BB, 
                                                              'cont_E_Total': cont_E_Total,'E_cont': E_cont, 'E_cont1': E_cont1, 'E_cont2': E_cont2, 'E_cont3': E_cont3,
                                                              'E_cont4': E_cont4,'E_cont5': E_cont5, 'E_cont6': E_cont6, 'E_prom': E_prom, 'E_prom1': E_prom1, 
                                                              'E_prom2': E_prom2,'E_prom3': E_prom3, 'E_prom4': E_prom4, 'E_prom5': E_prom5, 'E_prom6': E_prom6,
                                                              'cont_F_ML': cont_F_ML, 'cont_F_SP': cont_F_SP, 'cont_F_Ud': cont_F_Ud, 'cont_F_MA': cont_F_MA, 
                                                              'cont_F_SB': cont_F_SB, 'cont_F_BB': cont_F_BB, 'cont_F_Total': cont_F_Total,'F_cont': F_cont, 
                                                              'F_cont1': F_cont1, 'F_cont2': F_cont2, 'F_cont3': F_cont3,'F_cont4': F_cont4,'F_cont5': F_cont5, 
                                                              'F_cont6': F_cont6, 'F_prom': F_prom, 'F_prom1': F_prom1, 'F_prom2': F_prom2,'F_prom3': F_prom3, 
                                                              'F_prom4': F_prom4, 'F_prom5': F_prom5, 'F_prom6': F_prom6,'cont_G_ML': cont_G_ML, 'cont_G_SP': cont_G_SP,
                                                              'cont_G_Ud': cont_G_Ud, 'cont_G_MA':cont_G_MA, 'cont_G_SB':cont_G_SB, 'cont_G_BB': cont_G_BB,
                                                              'cont_G_Total':cont_G_Total,'G_cont': G_cont, 'G_cont1': G_cont1, 'G_cont2': G_cont2, 'G_cont3': G_cont3,
                                                              'G_cont4': G_cont4,'G_cont5': G_cont5, 'G_cont6': G_cont6, 'G_prom': G_prom, 'G_prom1': G_prom1, 
                                                              'G_prom2': G_prom2,'G_prom3': G_prom3, 'G_prom4': G_prom4, 'G_prom5': G_prom5, 'G_prom6': G_prom6,
                                                              'cont_H_ML': cont_H_ML, 'cont_H_SP': cont_H_SP, 'cont_H_Ud': cont_H_Ud, 'cont_H_MA':cont_H_MA,
                                                              'cont_H_SB': cont_H_SB, 'cont_H_BB': cont_H_BB, 'cont_H_Total':cont_H_Total,'H_cont': H_cont,
                                                              'H_cont1': H_cont1, 'H_cont2': H_cont2, 'H_cont3': H_cont3,'H_cont4': H_cont4,'H_cont5': H_cont5,
                                                              'H_cont6': H_cont6, 'H_prom': H_prom, 'H_prom1': H_prom1, 'H_prom2': H_prom2,'H_prom3': H_prom3, 
                                                              'H_prom4': H_prom4, 'H_prom5': H_prom5, 'H_prom6': H_prom6,'cont_I_ML': cont_I_ML, 'cont_I_SP': cont_I_SP,
                                                              'cont_I_Ud': cont_I_Ud, 'cont_I_MA': cont_I_MA, 'cont_I_SB': cont_I_SB, 'cont_I_BB': cont_I_BB, 
                                                              'cont_I_Total': cont_I_Total,'I_cont': I_cont, 'I_cont1': I_cont1, 'I_cont2': I_cont2, 'I_cont3': I_cont3,
                                                              'I_cont4': I_cont4,'I_cont5': I_cont5, 'I_cont6': I_cont6, 'I_prom': I_prom, 'I_prom1': I_prom1,
                                                              'I_prom2': I_prom2,'I_prom3': I_prom3, 'I_prom4': I_prom4, 'I_prom5': I_prom5, 'I_prom6': I_prom6,
                                                              'cont_J_ML': cont_J_ML, 'cont_J_SP': cont_J_SP, 'cont_J_Ud': cont_J_Ud, 'cont_J_MA': cont_J_MA,
                                                              'cont_J_SB': cont_J_SB, 'cont_J_BB':cont_J_BB, 'cont_J_Total': cont_J_Total,'J_cont': J_cont, 
                                                              'J_cont1': J_cont1, 'J_cont2': J_cont2, 'J_cont3': J_cont3,'J_cont4': J_cont4,'J_cont5': J_cont5, 
                                                              'J_cont6': J_cont6, 'J_prom': J_prom, 'J_prom1': J_prom1, 'J_prom2': J_prom2,'J_prom3': J_prom3, 
                                                              'J_prom4': J_prom4, 'J_prom5': J_prom5, 'J_prom6': J_prom6,'nombre_s':nombre_s,'nombre_s1':nombre_s1,
                                                              'nombre_s2':nombre_s2,'nombre_s3':nombre_s3,'nombre_s4':nombre_s4,'nombre_s5':nombre_s5,'nombre_s6':nombre_s6,
                                                              'mejor_prom_ML':mejor_prom_ML,'mejor_prom_SP':mejor_prom_SP,'mejor_prom_T':mejor_prom_T,
                                                              'mejor_prom_Ud':mejor_prom_Ud,'mejor_prom_SB':mejor_prom_SB,'mejor_prom_MA':mejor_prom_MA,'mejor_prom_BB':mejor_prom_BB,  })
    


#NBA profecional

def Crear_NBA(request):
    if request.method == 'POST':
        formulario = NBA_Profecional_form(request.POST)
        if formulario.is_valid():
            formulario.clean()
            objeto_creado = formulario.save()
            
          
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NBA_Profecional.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NBA_Profecional.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NBA_Profecional.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NBA_Profecional.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NBA_Profecional/informes.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,  'formulario':formulario, 'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })
       
        else:
            return render(request, 'NBA_Profecional/crear_NBA_profecional.html', {'formulario': formulario})
    else:
        formulario = NBA_Profecional_form()
        return render(request, 'NBA_Profecional/crear_NBA_profecional.html', {'formulario': formulario})

def Listar_NBA(request):
    lista =NBA_Profecional.objects.all().order_by('fecha')
    return render(request, 'NBA_Profecional/listar_NBA_profecional.html', {'lista':lista} )

def Eliminar_NBA(request, id):
    f = get_object_or_404(NBA_Profecional, id=id)
    f.delete()
    return redirect('listar_NBA_profecional')

def Buscar_NBA(request):
    resultados = []
    if request.method == 'POST':
        termino_busqueda = request.POST.get('searchbar')
        
        if termino_busqueda:
            # Construye condiciones para buscar en el nombre del equipo local o visitante
            condiciones = (
                Q(equipo_local__nombre__icontains=termino_busqueda) |
                Q(equipo_visitante__nombre__icontains=termino_busqueda)
            )
            
            # Filtra los resultados basándose en las condiciones construidas
            resultados = NBA_Profecional.objects.filter(condiciones)
        

        return render(request, 'NBA_Profecional/resultados.html', {'resultados': resultados})
    return render(request, 'NBA_Profecional/listar_NBA_profecional.html')

def Resultado_NBA(request, id):
    f = NBA_Profecional.objects.get(id=id)
    
    equipo_local = f.equipo_local.nombre
    equipo_visitante = f.equipo_visitante.nombre
    opciones_ganador = [ equipo_local,equipo_visitante,'Empate' ]
    
    if request.method == 'POST':
        form = resultado_NBA_Profecional_form(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return redirect('listar_NBA_profecional')
    else:
        form = resultado_NBA_Profecional_form( instance=f)

    return render(request, 'NBA_Profecional/resultado_NBA_profecional.html', {'form': form,'opciones_ganador': opciones_ganador})

def Informe_Resultado_NBA(request, id):
            objeto_creado = NBA_Profecional.objects.get(id=id)
    
    
   
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NBA_Profecional.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NBA_Profecional.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NBA_Profecional.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NBA_Profecional.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NBA_Profecional/informe_lista.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })

def Resultados_Sistemas_NBA(request): 
    
    partidos_filtrados = NBA_Profecional.objects.exclude(ganador__isnull=True).exclude(resultado__isnull=True)
    partidos = partidos_filtrados.order_by('-fecha')[:20]
    
    
    #Sistema A
    
    ganador=''
    cont_A_ML=0
    cont_A_SP=0
    cont_A_Ud=0
    cont_A_SB=0
    cont_A_MA=0
    cont_A_BB=0
    cont_A_Total=0
    A_cont=0
    A_cont1=0
    A_cont2=0
    A_cont3=0
    A_cont4=0
    A_cont5=0
    A_cont6=0
    sum=0
    res=0
    valor_izquierdo=0
    valor_derecho=0
    A_prom=0
    A_prom1=0
    A_prom2=0
    A_prom3=0
    A_prom4=0 
    A_prom5=0
    A_prom6=0
    
    for valor in partidos: 
        
        ganador=valor.ganador
        
        valor_izquierdo, valor_derecho = extraer_valores_de_resultado(valor)
        sum= valor_izquierdo+valor_derecho
        
        if valor.A_ML_equip is not None:
           A_cont+=1
           if ganador==valor.A_ML_equip.nombre:
              cont_A_ML+=1 
              
              
        if valor.A_Ud_equip is not None:
           A_cont1+=1      
           if ganador==valor.A_Ud_equip.nombre:
              cont_A_Ud+=1
              
              
        if valor.A_SB_equip is not None: 
           A_cont2+=1      
           if ganador==valor.A_SB_equip.nombre:
              cont_A_SB+=1
              
              
        if valor.A_MA is not None:
           A_cont3+=1 
           if ganador==valor.A_MA.nombre:
              cont_A_MA+=1
              
              
        if valor.A_BB is not None:  
           A_cont4+=1 
           if ganador==valor.A_BB.nombre:
              cont_A_BB+=1
         
         
        if valor.A_total_punto is not None: 
           A_cont5+=1 
           if sum>valor.A_total_punto and valor.A_Total_OU=='OVER':
              cont_A_Total+=1
           if sum<=valor.A_total_punto and valor.A_Total_OU=='UNDER':
              cont_A_Total+=1
         
         
       
        if valor_izquierdo>valor_derecho:
            res=valor_izquierdo-valor_derecho
           
        elif valor_izquierdo<valor_derecho:
            res=valor_derecho-valor_izquierdo 
        
        else: 
            res=0
        
        if valor.A_SP_dif is not None:
           A_cont6+=1
           if ganador==valor.A_SP_equip.nombre and res>valor.A_SP_dif :
              cont_A_SP+=1
           
           
           
    if cont_A_ML !=0 and A_cont !=0:
           A_prom=cont_A_ML*100/A_cont
        
    if cont_A_SP !=0 and A_cont6 !=0:
           A_prom6=cont_A_SP*100/A_cont6
           
    if cont_A_Ud !=0 and A_cont1 !=0:
           A_prom1=cont_A_Ud*100/A_cont1
           
    if cont_A_SB !=0 and A_cont2 !=0:
           A_prom2=cont_A_SB*100/A_cont2
           
    if cont_A_MA !=0 and A_cont3 !=0:
           A_prom3=cont_A_MA*100/A_cont3
           
    if cont_A_BB !=0 and A_cont4 !=0:
           A_prom4=cont_A_BB*100/A_cont5
           
    if cont_A_Total !=0 and A_cont5 !=0:
           A_prom5=cont_A_Total*100/A_cont5      
           
           
           
    #Sistema B     
    
    B_ganador=''
    cont_B_ML=0
    cont_B_SP=0
    cont_B_Ud=0
    cont_B_SB=0
    cont_B_MA=0
    cont_B_BB=0
    cont_B_Total=0
    B_cont=0
    B_cont1=0
    B_cont2=0
    B_cont3=0
    B_cont4=0
    B_cont5=0
    B_cont6=0
    B_sum=0
    B_res=0
    B_valor_izquierdo=0
    B_valor_derecho=0
    B_prom=0
    B_prom1=0
    B_prom2=0
    B_prom3=0
    B_prom4=0 
    B_prom5=0
    B_prom6=0
    
    for valor in partidos: 
        
        B_ganador=valor.ganador
        
        B_valor_izquierdo, B_valor_derecho = extraer_valores_de_resultado(valor)
        B_sum= B_valor_izquierdo+B_valor_derecho
        
        if valor.B_ML_equip is not None:
           B_cont+=1
           if B_ganador==valor.B_ML_equip.nombre:
              cont_B_ML+=1 
              
              
        if valor.B_Ud_equip is not None:
           B_cont1+=1      
           if B_ganador==valor.B_Ud_equip.nombre:
              cont_B_Ud+=1
              
              
        if valor.B_SB_equip is not None: 
           B_cont2+=1      
           if B_ganador==valor.B_SB_equip.nombre:
              cont_B_SB+=1
              
              
        if valor.B_MA is not None:
           B_cont3+=1 
           if B_ganador==valor.B_MA.nombre:
              cont_B_MA+=1
              
              
        if valor.B_BB is not None:  
           B_cont4+=1 
           if B_ganador==valor.B_BB.nombre:
              cont_B_BB+=1
         
         
        if valor.B_total_punto is not None: 
           B_cont5+=1 
           if B_sum>valor.B_total_punto and valor.B_Total_OU=='OVER':
              cont_B_Total+=1
           if B_sum<=valor.B_total_punto and valor.B_Total_OU=='UNDER':
              cont_B_Total+=1
         
         
       
        if B_valor_izquierdo>B_valor_derecho:
            B_res=B_valor_izquierdo-B_valor_derecho
           
        elif B_valor_izquierdo<B_valor_derecho:
            B_res=B_valor_derecho-B_valor_izquierdo 
        
        else: 
            B_res=0
        
        if valor.B_SP_dif is not None:
           B_cont6+=1
           if B_ganador==valor.B_SP_equip.nombre and B_res>valor.B_SP_dif :
              cont_B_SP+=1
           
           
           
    if cont_B_ML !=0 and B_cont !=0:
           B_prom=cont_B_ML*100/B_cont
        
    if cont_B_SP !=0 and B_cont6 !=0:
           B_prom6=cont_B_SP*100/B_cont6
           
    if cont_B_Ud !=0 and B_cont1 !=0:
           B_prom1=cont_B_Ud*100/B_cont1
           
    if cont_B_SB !=0 and B_cont2 !=0:
           B_prom2=cont_B_SB*100/B_cont2
           
    if cont_B_MA !=0 and B_cont3 !=0:
           B_prom3=cont_B_MA*100/B_cont3
           
    if cont_B_BB !=0 and B_cont4 !=0:
           B_prom4=cont_B_BB*100/B_cont5
           
    if cont_B_Total !=0 and B_cont5 !=0:
           B_prom5=cont_B_Total*100/B_cont5             
           
           
    C_ganador=''
    cont_C_ML=0
    cont_C_SP=0
    cont_C_Ud=0
    cont_C_SB=0
    cont_C_MA=0
    cont_C_BB=0
    cont_C_Total=0
    C_cont=0
    C_cont1=0
    C_cont2=0
    C_cont3=0
    C_cont4=0
    C_cont5=0
    C_cont6=0
    C_sum=0
    C_res=0
    C_valor_izquierdo=0
    C_valor_derecho=0
    C_prom=0
    C_prom1=0
    C_prom2=0
    C_prom3=0
    C_prom4=0 
    C_prom5=0        
    C_prom6=0
       
    for valor in partidos: 
        
        C_ganador=valor.ganador
            
        C_valor_izquierdo, C_valor_derecho = extraer_valores_de_resultado(valor)
        C_sum= C_valor_izquierdo+C_valor_derecho
            
        if valor.C_ML_equip is not None:
            C_cont+=1
            if C_ganador==valor.C_ML_equip.nombre:
                cont_C_ML+=1 
                
        if valor.C_Ud_equip is not None:
            C_cont1+=1      
            if C_ganador==valor.C_Ud_equip.nombre:
                cont_C_Ud+=1
                
        if valor.C_SB_equip is not None: 
            C_cont2+=1      
            if C_ganador==valor.C_SB_equip.nombre:
                cont_C_SB+=1
                
        if valor.C_MA is not None:
            C_cont3+=1 
            if C_ganador==valor.C_MA.nombre:
                cont_C_MA+=1
                
        if valor.C_BB is not None:  
            C_cont4+=1 
            if C_ganador==valor.C_BB.nombre:
                cont_C_BB+=1
            
            
        if valor.C_total_punto is not None: 
            C_cont5+=1 
            if C_sum>valor.C_total_punto and valor.C_Total_OU=='OVER':
                cont_C_Total+=1
            if C_sum<=valor.C_total_punto and valor.C_Total_OU=='UNDER':
                cont_C_Total+=1
            
            

        if C_valor_izquierdo>C_valor_derecho:
            C_res=C_valor_izquierdo-C_valor_derecho
            
        elif C_valor_izquierdo<C_valor_derecho:
            C_res=C_valor_derecho-C_valor_izquierdo 

        else: 
            C_res=0
            
        if valor.C_SP_dif is not None:
            C_cont6+=1
            if C_ganador==valor.C_SP_equip.nombre and C_res>valor.C_SP_dif :
                cont_C_SP+=1
           
           
    if cont_C_ML !=0 and C_cont !=0:
       C_prom=cont_C_ML*100/C_cont
            
    if cont_C_SP !=0 and C_cont6 !=0:
       C_prom6=cont_C_SP*100/C_cont6
            
    if cont_C_Ud !=0 and C_cont1 !=0:
       C_prom1=cont_C_Ud*100/C_cont1
            
    if cont_C_SB !=0 and C_cont2 !=0:
       C_prom2=cont_C_SB*100/C_cont2
            
    if cont_C_MA !=0 and C_cont3 !=0:
       C_prom3=cont_C_MA*100/C_cont3
            
    if cont_C_BB !=0 and C_cont4 !=0:
       C_prom4=cont_C_BB*100/C_cont5
            
    if cont_C_Total !=0 and C_cont5 !=0:
       C_prom5=cont_C_Total*100/C_cont5       
           
    
    
    D_ganador=''
    cont_D_ML=0
    cont_D_SP=0
    cont_D_Ud=0
    cont_D_SB=0
    cont_D_MA=0
    cont_D_BB=0
    cont_D_Total=0
    D_cont=0
    D_cont1=0
    D_cont2=0
    D_cont3=0
    D_cont4=0
    D_cont5=0
    D_cont6=0
    D_sum=0
    D_res=0
    D_valor_izquierdo=0
    D_valor_derecho=0
    D_prom=0
    D_prom1=0
    D_prom2=0
    D_prom3=0
    D_prom4=0 
    D_prom5=0        
    D_prom6=0

    
    
    
    for valor in partidos: 
        
        D_ganador=valor.ganador
            
        D_valor_izquierdo, D_valor_derecho = extraer_valores_de_resultado(valor)
        D_sum= D_valor_izquierdo+D_valor_derecho
            
        if valor.D_ML_equip is not None:
           D_cont+=1
           if D_ganador==valor.D_ML_equip.nombre:
              cont_D_ML+=1 
            
        if valor.D_Ud_equip is not None:
           D_cont1+=1      
           if D_ganador==valor.D_Ud_equip.nombre:
              cont_D_Ud+=1
            
        if valor.D_SB_equip is not None: 
           D_cont2+=1      
           if D_ganador==valor.D_SB_equip.nombre:
              cont_D_SB+=1
            
        if valor.D_MA is not None:
           D_cont3+=1 
           if D_ganador==valor.D_MA.nombre:
              cont_D_MA+=1
            
        if valor.D_BB is not None:  
           D_cont4+=1 
           if D_ganador==valor.D_BB.nombre:
              cont_D_BB+=1
        
        
        if valor.D_total_punto is not None: 
           D_cont5+=1 
           if D_sum>valor.D_total_punto and valor.D_Total_OU=='OVER':
              cont_D_Total+=1
           if D_sum<=valor.D_total_punto and valor.D_Total_OU=='UNDER':
              cont_D_Total+=1
        
        
    
        if D_valor_izquierdo>D_valor_derecho:
            D_res=D_valor_izquierdo-D_valor_derecho
        
        elif D_valor_izquierdo<D_valor_derecho:
            D_res=D_valor_derecho-D_valor_izquierdo 
        
        else: 
            D_res=0
            
        if valor.D_SP_dif is not None:
           D_cont6+=1
           if D_ganador==valor.D_SP_equip.nombre and D_res>valor.D_SP_dif :
              cont_D_SP+=1
             
           
    if cont_D_ML !=0 and D_cont !=0:
       D_prom=cont_D_ML*100/D_cont
            
    if cont_D_SP !=0 and D_cont6 !=0:
       D_prom6=cont_D_SP*100/D_cont6
            
    if cont_D_Ud !=0 and D_cont1 !=0:
       D_prom1=cont_D_Ud*100/D_cont1
            
    if cont_D_SB !=0 and D_cont2 !=0:
       D_prom2=cont_D_SB*100/D_cont2
            
    if cont_D_MA !=0 and D_cont3 !=0:
       D_prom3=cont_D_MA*100/D_cont3
            
    if cont_D_BB !=0 and D_cont4 !=0:
       D_prom4=cont_D_BB*100/D_cont5
            
    if cont_D_Total !=0 and D_cont5 !=0:
       D_prom5=cont_D_Total*100/D_cont5
        
    
    E_ganador=''
    cont_E_ML=0
    cont_E_SP=0
    cont_E_Ud=0
    cont_E_SB=0
    cont_E_MA=0
    cont_E_BB=0
    cont_E_Total=0
    E_cont=0
    E_cont1=0
    E_cont2=0
    E_cont3=0
    E_cont4=0
    E_cont5=0
    E_cont6=0
    E_sum=0
    E_res=0
    E_valor_izquierdo=0
    E_valor_derecho=0
    E_prom=0
    E_prom1=0
    E_prom2=0
    E_prom3=0
    E_prom4=0 
    E_prom5=0        
    E_prom6=0
       
    for valor in partidos: 
        
        E_ganador=valor.ganador
            
        E_valor_izquierdo, E_valor_derecho = extraer_valores_de_resultado(valor)
        E_sum= E_valor_izquierdo+E_valor_derecho
            
        if valor.E_ML_equip is not None:
           E_cont+=1
           if E_ganador==valor.E_ML_equip.nombre:
              cont_E_ML+=1 
            
        if valor.E_Ud_equip is not None:
           E_cont1+=1      
           if E_ganador==valor.E_Ud_equip.nombre:
              cont_E_Ud+=1
            
        if valor.E_SB_equip is not None: 
           E_cont2+=1      
           if E_ganador==valor.E_SB_equip.nombre:
              cont_E_SB+=1
            
        if valor.E_MA is not None:
           E_cont3+=1 
           if E_ganador==valor.E_MA.nombre:
              cont_E_MA+=1
            
        if valor.E_BB is not None:  
           E_cont4+=1 
           if E_ganador==valor.E_BB.nombre:
              cont_E_BB+=1
        
        
        if valor.E_total_punto is not None: 
           E_cont5+=1 
           if E_sum>valor.E_total_punto and valor.E_Total_OU=='OVER':
              cont_E_Total+=1
           if E_sum<=valor.E_total_punto and valor.E_Total_OU=='UNDER':
              cont_E_Total+=1
        
        
    
        if E_valor_izquierdo>E_valor_derecho:
            E_res=E_valor_izquierdo-E_valor_derecho
        
        elif E_valor_izquierdo<E_valor_derecho:
            E_res=E_valor_derecho-E_valor_izquierdo 
        
        else: 
            E_res=0
            
        if valor.E_SP_dif is not None:
           E_cont6+=1
           if E_ganador==valor.E_SP_equip.nombre and E_res>valor.E_SP_dif :
              cont_E_SP+=1
            
           
    if cont_E_ML !=0 and E_cont !=0:
       E_prom=cont_E_ML*100/E_cont
            
    if cont_E_SP !=0 and E_cont6 !=0:
       E_prom6=cont_E_SP*100/E_cont6
            
    if cont_E_Ud !=0 and E_cont1 !=0:
       E_prom1=cont_E_Ud*100/E_cont1   
        
    if cont_E_SB !=0 and E_cont2 !=0:
       E_prom2=cont_E_SB*100/E_cont2
            
    if cont_E_MA !=0 and E_cont3 !=0:
       E_prom3=cont_E_MA*100/E_cont3
            
    if cont_E_BB !=0 and E_cont4 !=0:
       E_prom4=cont_E_BB*100/E_cont5
            
    if cont_E_Total !=0 and E_cont5 !=0:
       E_prom5=cont_E_Total*100/E_cont5     
    
    
    
    
    F_ganador=''
    cont_F_ML=0
    cont_F_SP=0
    cont_F_Ud=0
    cont_F_SB=0
    cont_F_MA=0
    cont_F_BB=0
    cont_F_Total=0
    F_cont=0
    F_cont1=0
    F_cont2=0
    F_cont3=0
    F_cont4=0
    F_cont5=0
    F_cont6=0
    F_sum=0
    F_res=0
    F_valor_izquierdo=0
    F_valor_derecho=0
    F_prom=0
    F_prom1=0
    F_prom2=0
    F_prom3=0
    F_prom4=0 
    F_prom5=0        
    F_prom6=0
       
    
    for valor in partidos: 
        
 
        F_valor_izquierdo, F_valor_derecho = extraer_valores_de_resultado(valor)
        F_sum = F_valor_izquierdo + F_valor_derecho
                
        if valor.F_ML_equip is not None:
           F_cont+=1
           if F_ganador==valor.F_ML_equip.nombre:
              F_cont_ML+=1 
                
        if valor.F_Ud_equip is not None:
           F_cont1+=1      
           if F_ganador==valor.F_Ud_equip.nombre:
              F_cont_Ud+=1
                
        if valor.F_SB_equip is not None: 
           F_cont2+=1      
           if F_ganador==valor.F_SB_equip.nombre:
              F_cont_SB+=1
                
        if valor.F_MA is not None:
           F_cont3+=1 
           if F_ganador==valor.F_MA.nombre:
              F_cont_MA+=1
                
        if valor.F_BB is not None:  
           F_cont4+=1 
           if F_ganador==valor.F_BB.nombre:
              F_cont_BB+=1
            
            
        if valor.F_total_punto is not None: 
           F_cont5+=1 
           if F_sum>F_valor_izquierdo and valor.F_Total_OU=='OVER':
              F_cont_Total+=1
           if F_sum<=valor.F_total_punto and valor.F_Total_OU=='UNDER':
              F_cont_Total+=1
            
            
        if F_valor_izquierdo>F_valor_derecho:
            F_res=F_valor_izquierdo-F_valor_derecho
            
        elif F_valor_izquierdo<F_valor_derecho:
            F_res=F_valor_derecho-F_valor_izquierdo 
        
        else: 
            F_res=0
                
        if valor.F_SP_dif is not None:
           F_cont6+=1
           if F_ganador==valor.F_SP_equip.nombre and F_res>valor.F_SP_dif :
              F_cont_SP+=1
            
           
    if cont_F_ML !=0 and F_cont !=0:
       F_prom=F_cont_ML*100/F_cont
                
    if cont_F_SP !=0 and F_cont6 !=0:
       F_prom6=F_cont_SP*100/F_cont6
                
    if cont_F_Ud !=0 and F_cont1 !=0:
       F_prom1=F_cont_Ud*100/F_cont1   
            
    if cont_F_SB !=0 and F_cont2 !=0:
       F_prom2=F_cont_SB*100/F_cont2
                
    if cont_F_MA !=0 and F_cont3 !=0:
       F_prom3=F_cont_MA*100/F_cont3
                
    if cont_F_BB !=0 and F_cont4 !=0:
       F_prom4=F_cont_BB*100/F_cont5
                
    if cont_F_Total !=0 and F_cont5 !=0:
       F_prom5=F_cont_Total*100/F_cont5
        
    
    G_ganador=''
    cont_G_ML=0
    cont_G_SP=0
    cont_G_Ud=0
    cont_G_SB=0
    cont_G_MA=0
    cont_G_BB=0
    cont_G_Total=0
    G_cont=0
    G_cont1=0
    G_cont2=0
    G_cont3=0
    G_cont4=0
    G_cont5=0
    G_cont6=0
    G_sum=0
    G_res=0
    G_valor_izquierdo=0
    G_valor_derecho=0
    G_prom=0
    G_prom1=0
    G_prom2=0
    G_prom3=0
    G_prom4=0 
    G_prom5=0        
    G_prom6=0

    for valor in partidos: 
        
        G_valor_izquierdo, G_valor_derecho = extraer_valores_de_resultado(valor)
        G_sum = G_valor_izquierdo + G_valor_derecho
                    
        if valor.G_ML_equip is not None:
           G_cont+=1
           if G_ganador==valor.G_ML_equip.nombre:
              G_cont_ML+=1 
                    
        if valor.G_Ud_equip is not None:
           G_cont1+=1      
           if G_ganador==valor.G_Ud_equip.nombre:
              G_cont_Ud+=1
                    
        if valor.G_SB_equip is not None: 
           G_cont2+=1      
           if G_ganador==valor.G_SB_equip.nombre:
              G_cont_SB+=1
                    
        if valor.G_MA is not None:
           G_cont3+=1 
           if G_ganador==valor.G_MA.nombre:
              G_cont_MA+=1
                    
        if valor.G_BB is not None:  
           G_cont4+=1 
           if G_ganador==valor.G_BB.nombre:
              G_cont_BB+=1
                
                
        if valor.G_total_punto is not None: 
           G_cont5+=1 
           if G_sum>G_valor_izquierdo and valor.G_Total_OU=='OVER':
              G_cont_Total+=1
           if G_sum<=valor.G_total_punto and valor.G_Total_OU=='UNDER':
              G_cont_Total+=1
                
                
        if G_valor_izquierdo>G_valor_derecho:
            G_res=G_valor_izquierdo-G_valor_derecho
                
        elif G_valor_izquierdo<G_valor_derecho:
            G_res=G_valor_derecho-G_valor_izquierdo 
            
        else: 
            G_res=0
                    
        if valor.G_SP_dif is not None:
           G_cont6+=1
           if G_ganador==valor.G_SP_equip.nombre and G_res>valor.G_SP_dif :
              G_cont_SP+=1
            
           
    if cont_G_ML !=0 and G_cont !=0:
       G_prom=G_cont_ML*100/G_cont
                    
    if cont_G_SP !=0 and G_cont6 !=0:
       G_prom6=G_cont_SP*100/G_cont6
                    
    if cont_G_Ud !=0 and G_cont1 !=0:
       G_prom1=G_cont_Ud*100/G_cont1   
                
    if cont_G_SB !=0 and G_cont2 !=0:
       G_prom2=G_cont_SB*100/G_cont2
                    
    if cont_G_MA !=0 and G_cont3 !=0:
       G_prom3=G_cont_MA*100/G_cont3
                    
    if cont_G_BB !=0 and G_cont4 !=0:
       G_prom4=G_cont_BB*100/G_cont5
                    
    if cont_G_Total !=0 and G_cont5 !=0:
       G_prom5=G_cont_Total*100/G_cont5
            
            
            
    H_ganador=''
    cont_H_ML=0
    cont_H_SP=0
    cont_H_Ud=0
    cont_H_SB=0
    cont_H_MA=0
    cont_H_BB=0
    cont_H_Total=0
    H_cont=0
    H_cont1=0
    H_cont2=0
    H_cont3=0
    H_cont4=0
    H_cont5=0
    H_cont6=0
    H_sum=0
    H_res=0
    H_valor_izquierdo=0
    H_valor_derecho=0
    H_prom=0
    H_prom1=0
    H_prom2=0
    H_prom3=0
    H_prom4=0 
    H_prom5=0        
    H_prom6=0
        
            
    for valor in partidos: 
        
        H_valor_izquierdo, H_valor_derecho = extraer_valores_de_resultado(valor)
        H_sum = H_valor_izquierdo + H_valor_derecho
                        
        if valor.H_ML_equip is not None:
           H_cont+=1
           if H_ganador==valor.H_ML_equip.nombre:
              H_cont_ML+=1 
                        
        if valor.H_Ud_equip is not None:
           H_cont1+=1      
           if H_ganador==valor.H_Ud_equip.nombre:
              H_cont_Ud+=1
                        
        if valor.H_SB_equip is not None: 
           H_cont2+=1      
           if H_ganador==valor.H_SB_equip.nombre:
              H_cont_SB+=1
                        
        if valor.H_MA is not None:
           H_cont3+=1 
           if H_ganador==valor.H_MA.nombre:
              H_cont_MA+=1
                        
        if valor.H_BB is not None:  
           H_cont4+=1 
           if H_ganador==valor.H_BB.nombre:
              H_cont_BB+=1
                    
                    
        if valor.H_total_punto is not None: 
           H_cont5+=1 
           if H_sum>H_valor_izquierdo and valor.H_Total_OU=='OVER':
              H_cont_Total+=1
           if H_sum<=valor.H_total_punto and valor.H_Total_OU=='UNDER':
              H_cont_Total+=1
                    
                    
        if H_valor_izquierdo>H_valor_derecho:
                H_res=H_valor_izquierdo-H_valor_derecho
                    
        elif H_valor_izquierdo<H_valor_derecho:
                H_res=H_valor_derecho-H_valor_izquierdo 
                
        else: 
                H_res=0
                        
        if valor.H_SP_dif is not None:
           H_cont6+=1
           if H_ganador==valor.H_SP_equip.nombre and H_res>valor.H_SP_dif :
              H_cont_SP+=1
            
           
    if cont_H_ML !=0 and H_cont !=0:
       H_prom=H_cont_ML*100/H_cont
                    
    if cont_H_SP !=0 and H_cont6 !=0:
       H_prom6=H_cont_SP*100/H_cont6
                    
    if cont_H_Ud !=0 and H_cont1 !=0:
       H_prom1=H_cont_Ud*100/H_cont1   
                
    if cont_H_SB !=0 and H_cont2 !=0:
       H_prom2=H_cont_SB*100/H_cont2
                    
    if cont_H_MA !=0 and H_cont3 !=0:
       H_prom3=H_cont_MA*100/H_cont3
                    
    if cont_H_BB !=0 and H_cont4 !=0:
       H_prom4=H_cont_BB*100/H_cont5
                    
    if cont_H_Total !=0 and H_cont5 !=0:
       H_prom5=H_cont_Total*100/H_cont5        
            
    
    
    I_ganador=''
    cont_I_ML=0
    cont_I_SP=0
    cont_I_Ud=0
    cont_I_SB=0
    cont_I_MA=0
    cont_I_BB=0
    cont_I_Total=0
    I_cont=0
    I_cont1=0
    I_cont2=0
    I_cont3=0
    I_cont4=0
    I_cont5=0
    I_cont6=0
    I_sum=0
    I_res=0
    I_valor_izquierdo=0
    I_valor_derecho=0
    I_prom=0
    I_prom1=0
    I_prom2=0
    I_prom3=0
    I_prom4=0 
    I_prom5=0        
    I_prom6=0
        
            
    for valor in partidos: 
        
        I_valor_izquierdo, I_valor_derecho = extraer_valores_de_resultado(valor)
        I_sum = I_valor_izquierdo + I_valor_derecho
                        
        if valor.I_ML_equip is not None:
           I_cont+=1
           if I_ganador==valor.I_ML_equip.nombre:
              I_cont_ML+=1 
                        
        if valor.I_Ud_equip is not None:
           I_cont1+=1      
           if I_ganador==valor.I_Ud_equip.nombre:
              I_cont_Ud+=1
                        
        if valor.I_SB_equip is not None: 
           I_cont2+=1      
           if I_ganador==valor.I_SB_equip.nombre:
              I_cont_SB+=1
                        
        if valor.I_MA is not None:
           I_cont3+=1 
           if I_ganador==valor.I_MA.nombre:
              I_cont_MA+=1
                        
        if valor.I_BB is not None:  
           I_cont4+=1 
           if I_ganador==valor.I_BB.nombre:
              I_cont_BB+=1
                    
                    
        if valor.I_total_punto is not None: 
           I_cont5+=1 
           if I_sum>I_valor_izquierdo and valor.I_Total_OU=='OVER':
              I_cont_Total+=1
           if I_sum<=valor.I_total_punto and valor.I_Total_OU=='UNDER':
              I_cont_Total+=1
                    
                    
        if I_valor_izquierdo>I_valor_derecho:
                I_res=I_valor_izquierdo-I_valor_derecho
                    
        elif I_valor_izquierdo<I_valor_derecho:
                I_res=I_valor_derecho-I_valor_izquierdo 
                
        else: 
                I_res=0
                        
        if valor.I_SP_dif is not None:
           I_cont6+=1
           if I_ganador==valor.I_SP_equip.nombre and I_res>valor.I_SP_dif :
              I_cont_SP+=1
            
           
    if cont_I_ML !=0 and I_cont !=0:
       I_prom=I_cont_ML*100/I_cont
                        
    if cont_I_SP !=0 and I_cont6 !=0:
       I_prom6=I_cont_SP*100/I_cont6
                        
    if cont_I_Ud !=0 and I_cont1 !=0:
       I_prom1=I_cont_Ud*100/I_cont1   
                    
    if cont_I_SB !=0 and I_cont2 !=0:
       I_prom2=I_cont_SB*100/I_cont2
                        
    if cont_I_MA !=0 and I_cont3 !=0:
       I_prom3=I_cont_MA*100/I_cont3
                        
    if cont_I_BB !=0 and I_cont4 !=0:
       I_prom4=I_cont_BB*100/I_cont5
                        
    if cont_I_Total !=0 and I_cont5 !=0:
       I_prom5=I_cont_Total*100/I_cont5        
            
            
    J_ganador=''
    cont_J_ML=0
    cont_J_SP=0
    cont_J_Ud=0
    cont_J_SB=0
    cont_J_MA=0
    cont_J_BB=0
    cont_J_Total=0
    J_cont=0
    J_cont1=0
    J_cont2=0
    J_cont3=0
    J_cont4=0
    J_cont5=0
    J_cont6=0
    J_sum=0
    J_res=0
    J_valor_izquierdo=0
    J_valor_derecho=0
    J_prom=0
    J_prom1=0
    J_prom2=0
    J_prom3=0
    J_prom4=0 
    J_prom5=0        
    J_prom6=0
        
    for valor in partidos: 
        
        J_valor_izquierdo, J_valor_derecho = extraer_valores_de_resultado(valor)
        J_sum = J_valor_izquierdo + J_valor_derecho
                            
        if valor.J_ML_equip is not None:
           J_cont+=1
           if J_ganador==valor.J_ML_equip.nombre:
              J_cont_ML+=1 
                            
        if valor.J_Ud_equip is not None:
           J_cont1+=1      
           if J_ganador==valor.J_Ud_equip.nombre:
              J_cont_Ud+=1
                            
        if valor.J_SB_equip is not None: 
           J_cont2+=1      
           if J_ganador==valor.J_SB_equip.nombre:
              J_cont_SB+=1
                            
        if valor.J_MA is not None:
           J_cont3+=1 
           if J_ganador==valor.J_MA.nombre:
              J_cont_MA+=1
                            
        if valor.J_BB is not None:  
           J_cont4+=1 
           if J_ganador==valor.J_BB.nombre:
              J_cont_BB+=1
                        
                        
        if valor.J_total_punto is not None: 
           J_cont5+=1 
           if J_sum>J_valor_izquierdo and valor.J_Total_OU=='OVER':
              J_cont_Total+=1
           if J_sum<=valor.J_total_punto and valor.J_Total_OU=='UNDER':
              J_cont_Total+=1
                        
                        
        if J_valor_izquierdo>J_valor_derecho:
                J_res=J_valor_izquierdo-J_valor_derecho
                        
        elif J_valor_izquierdo<J_valor_derecho:
                J_res=J_valor_derecho-J_valor_izquierdo 
                    
        else: 
                J_res=0
                            
        if valor.J_SP_dif is not None:
           J_cont6+=1
           if J_ganador==valor.J_SP_equip.nombre and J_res>valor.J_SP_dif :
              J_cont_SP+=1
            
           
    if cont_J_ML !=0 and J_cont !=0:
       J_prom=J_cont_ML*100/J_cont
                            
    if cont_J_SP !=0 and J_cont6 !=0:
       J_prom6=J_cont_SP*100/J_cont6
                            
    if cont_J_Ud !=0 and J_cont1 !=0:
       J_prom1=J_cont_Ud*100/J_cont1   
                        
    if cont_J_SB !=0 and J_cont2 !=0:
       J_prom2=J_cont_SB*100/J_cont2
                            
    if cont_J_MA !=0 and J_cont3 !=0:
       J_prom3=J_cont_MA*100/J_cont3
                            
    if cont_J_BB !=0 and J_cont4 !=0:
       J_prom4=J_cont_BB*100/J_cont5
                            
    if cont_J_Total !=0 and J_cont5 !=0:
       J_prom5=J_cont_Total*100/J_cont5      
       
       
    mejor_prom_ML=0
    mejor_prom_SP=0
    mejor_prom_T=0
    mejor_prom_Ud=0
    mejor_prom_SB=0
    mejor_prom_MA=0     
    mejor_prom_BB=0
    nombre_s=0
    nombre_s1=0
    nombre_s2=0
    nombre_s3=0
    nombre_s4=0
    nombre_s5=0
    nombre_s6=0
    
    
    list_ML=[A_prom,B_prom,C_prom,D_prom,E_prom,F_prom,G_prom,H_prom,I_prom,J_prom]
    list_SP=[A_prom6,B_prom6,C_prom6,D_prom6,E_prom6,F_prom6,G_prom6,H_prom6,I_prom6,J_prom6]
    list_T=[A_prom5,B_prom5,C_prom5,D_prom5,E_prom5,F_prom5,G_prom5,H_prom5,I_prom5,J_prom5]
    list_Ud=[A_prom1,B_prom1,C_prom1,D_prom1,E_prom1,F_prom1,G_prom1,H_prom1,I_prom1,J_prom1]     
    list_SB=[A_prom2,B_prom2,C_prom2,D_prom2,E_prom2,F_prom2,G_prom2,H_prom2,I_prom2,J_prom2]
    list_MA=[A_prom3,B_prom3,C_prom3,D_prom3,E_prom3,F_prom3,G_prom3,H_prom3,I_prom3,J_prom3]
    list_BB=[A_prom4,B_prom4,C_prom4,D_prom4,E_prom4,F_prom4,G_prom4,H_prom4,I_prom4,J_prom4]
    
    lista_sistemas=['VeriBet','Action Network','Sports Insights','PFF','Covers','Team Rankings','BetQL','Odds Jams','Scores and Odds','Betting on Cash']
       
    for indice,i in enumerate(list_ML):
        if i>mejor_prom_ML:
           mejor_prom_ML=i   
           nombre_s=indice
           
        
    for indice,i in enumerate(list_SP):
        if i>mejor_prom_SP:
           mejor_prom_SP=i        
           nombre_s1=indice
            
    for indice,i in enumerate( list_T):
        if i>mejor_prom_T:
           mejor_prom_T=i         
           nombre_s2=indice
           
    for indice,i in enumerate(list_Ud):
        if i>mejor_prom_Ud:
           mejor_prom_Ud=i 
           nombre_s3=indice
           
    for indice,i in enumerate(list_SB):
        if i>mejor_prom_SB:
           mejor_prom_SB=i 
           nombre_s4=indice
           
    for indice,i in enumerate(list_MA):
        if i>mejor_prom_MA:
           mejor_prom_MA=i 
           nombre_s5=indice
           
    for indice,i in enumerate(list_BB):
        if i>mejor_prom_BB:
           mejor_prom_BB=i 
           nombre_s6=indice
           
           
           
           
           
    for indice,i in enumerate(lista_sistemas):
        if nombre_s==indice:
           nombre_s=i       
           break
              
    for indice,i in enumerate(lista_sistemas):
        if nombre_s1==indice:
           nombre_s1=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s2==indice:
           nombre_s2=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s3==indice:
           nombre_s3=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s4==indice:
           nombre_s4=i       
           break
    
    for indice,i in enumerate(lista_sistemas):
        if nombre_s5==indice:
           nombre_s5=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s6==indice:
           nombre_s6=i       
           break          
              
              
              
              
    return render(request,'NBA_Profecional/resultados_sistemas.html', {'cont_A_ML':cont_A_ML, 'cont_A_SP':cont_A_SP, 'cont_A_Ud':cont_A_Ud, 
                                                              'cont_A_MA':cont_A_MA,'cont_A_SB':cont_A_SB,'cont_A_BB':cont_A_BB,
                                                              'cont_A_Total':cont_A_Total,'A_cont':A_cont,'A_cont1':A_cont1,'A_cont2':A_cont2,
                                                              'A_cont3':A_cont3,'A_cont4':A_cont4,'A_cont5':A_cont5,'A_cont6':A_cont6, 
                                                              'A_prom':A_prom,'A_prom1':A_prom1,'A_prom2':A_prom2,'A_prom3':A_prom3,'A_prom4':A_prom4,
                                                              'A_prom5':A_prom5,'A_prom6':A_prom6,'cont_B_ML': cont_B_ML, 'cont_B_SP': cont_B_SP, 
                                                              'cont_B_Ud': cont_B_Ud, 'cont_B_MA': cont_B_MA, 'cont_B_SB': cont_B_SB, 'cont_B_BB': cont_B_BB,
                                                              'cont_B_Total': cont_B_Total, 'B_cont': B_cont, 'B_cont1': B_cont1, 'B_cont2': B_cont2,
                                                              'B_cont3': B_cont3, 'B_cont4': B_cont4, 'B_cont5': B_cont5, 'B_cont6': B_cont6, 'B_prom': B_prom,
                                                              'B_prom1': B_prom1, 'B_prom2': B_prom2, 'B_prom3': B_prom3, 'B_prom4': B_prom4, 'B_prom5': B_prom5, 
                                                              'B_prom6': B_prom6,'cont_C_ML': cont_C_ML, 'cont_C_SP': cont_C_SP, 'cont_C_Ud': cont_C_Ud, 
                                                              'cont_C_MA': cont_C_MA, 'cont_C_SB': cont_C_SB, 'cont_C_BB': cont_C_BB, 'cont_C_Total': cont_C_Total,
                                                              'C_cont': C_cont, 'C_cont1': C_cont1, 'C_cont2': C_cont2, 'C_cont3': C_cont3, 'C_cont4': C_cont4,
                                                              'C_cont5': C_cont5, 'C_cont6': C_cont6, 'C_prom': C_prom, 'C_prom1': C_prom1, 'C_prom2': C_prom2,
                                                              'C_prom3': C_prom3, 'C_prom4': C_prom4, 'C_prom5': C_prom5, 'C_prom6': C_prom6, 'cont_D_ML': cont_D_ML,
                                                              'cont_D_SP': cont_D_SP, 'cont_D_Ud': cont_D_Ud, 'cont_D_MA': cont_D_MA, 'cont_D_SB': cont_D_SB,
                                                              'cont_D_BB': cont_D_BB, 'cont_D_Total':cont_D_Total, 'D_cont': D_cont, 'D_cont1': D_cont1,
                                                              'D_cont2': D_cont2, 'D_cont3': D_cont3, 'D_cont4': D_cont4,'D_cont5': D_cont5, 'D_cont6': D_cont6,
                                                              'D_prom': D_prom, 'D_prom1': D_prom1, 'D_prom2': D_prom2,'D_prom3': D_prom3, 'D_prom4': D_prom4, 
                                                              'D_prom5': D_prom5, 'D_prom6': D_prom6, 'cont_E_ML': cont_E_ML, 'cont_E_SP': cont_E_SP, 
                                                              'cont_E_Ud': cont_E_Ud, 'cont_E_MA': cont_E_MA, 'cont_E_SB': cont_E_SB, 'cont_E_BB': cont_E_BB, 
                                                              'cont_E_Total': cont_E_Total,'E_cont': E_cont, 'E_cont1': E_cont1, 'E_cont2': E_cont2, 'E_cont3': E_cont3,
                                                              'E_cont4': E_cont4,'E_cont5': E_cont5, 'E_cont6': E_cont6, 'E_prom': E_prom, 'E_prom1': E_prom1, 
                                                              'E_prom2': E_prom2,'E_prom3': E_prom3, 'E_prom4': E_prom4, 'E_prom5': E_prom5, 'E_prom6': E_prom6,
                                                              'cont_F_ML': cont_F_ML, 'cont_F_SP': cont_F_SP, 'cont_F_Ud': cont_F_Ud, 'cont_F_MA': cont_F_MA, 
                                                              'cont_F_SB': cont_F_SB, 'cont_F_BB': cont_F_BB, 'cont_F_Total': cont_F_Total,'F_cont': F_cont, 
                                                              'F_cont1': F_cont1, 'F_cont2': F_cont2, 'F_cont3': F_cont3,'F_cont4': F_cont4,'F_cont5': F_cont5, 
                                                              'F_cont6': F_cont6, 'F_prom': F_prom, 'F_prom1': F_prom1, 'F_prom2': F_prom2,'F_prom3': F_prom3, 
                                                              'F_prom4': F_prom4, 'F_prom5': F_prom5, 'F_prom6': F_prom6,'cont_G_ML': cont_G_ML, 'cont_G_SP': cont_G_SP,
                                                              'cont_G_Ud': cont_G_Ud, 'cont_G_MA':cont_G_MA, 'cont_G_SB':cont_G_SB, 'cont_G_BB': cont_G_BB,
                                                              'cont_G_Total':cont_G_Total,'G_cont': G_cont, 'G_cont1': G_cont1, 'G_cont2': G_cont2, 'G_cont3': G_cont3,
                                                              'G_cont4': G_cont4,'G_cont5': G_cont5, 'G_cont6': G_cont6, 'G_prom': G_prom, 'G_prom1': G_prom1, 
                                                              'G_prom2': G_prom2,'G_prom3': G_prom3, 'G_prom4': G_prom4, 'G_prom5': G_prom5, 'G_prom6': G_prom6,
                                                              'cont_H_ML': cont_H_ML, 'cont_H_SP': cont_H_SP, 'cont_H_Ud': cont_H_Ud, 'cont_H_MA':cont_H_MA,
                                                              'cont_H_SB': cont_H_SB, 'cont_H_BB': cont_H_BB, 'cont_H_Total':cont_H_Total,'H_cont': H_cont,
                                                              'H_cont1': H_cont1, 'H_cont2': H_cont2, 'H_cont3': H_cont3,'H_cont4': H_cont4,'H_cont5': H_cont5,
                                                              'H_cont6': H_cont6, 'H_prom': H_prom, 'H_prom1': H_prom1, 'H_prom2': H_prom2,'H_prom3': H_prom3, 
                                                              'H_prom4': H_prom4, 'H_prom5': H_prom5, 'H_prom6': H_prom6,'cont_I_ML': cont_I_ML, 'cont_I_SP': cont_I_SP,
                                                              'cont_I_Ud': cont_I_Ud, 'cont_I_MA': cont_I_MA, 'cont_I_SB': cont_I_SB, 'cont_I_BB': cont_I_BB, 
                                                              'cont_I_Total': cont_I_Total,'I_cont': I_cont, 'I_cont1': I_cont1, 'I_cont2': I_cont2, 'I_cont3': I_cont3,
                                                              'I_cont4': I_cont4,'I_cont5': I_cont5, 'I_cont6': I_cont6, 'I_prom': I_prom, 'I_prom1': I_prom1,
                                                              'I_prom2': I_prom2,'I_prom3': I_prom3, 'I_prom4': I_prom4, 'I_prom5': I_prom5, 'I_prom6': I_prom6,
                                                              'cont_J_ML': cont_J_ML, 'cont_J_SP': cont_J_SP, 'cont_J_Ud': cont_J_Ud, 'cont_J_MA': cont_J_MA,
                                                              'cont_J_SB': cont_J_SB, 'cont_J_BB':cont_J_BB, 'cont_J_Total': cont_J_Total,'J_cont': J_cont, 
                                                              'J_cont1': J_cont1, 'J_cont2': J_cont2, 'J_cont3': J_cont3,'J_cont4': J_cont4,'J_cont5': J_cont5, 
                                                              'J_cont6': J_cont6, 'J_prom': J_prom, 'J_prom1': J_prom1, 'J_prom2': J_prom2,'J_prom3': J_prom3, 
                                                              'J_prom4': J_prom4, 'J_prom5': J_prom5, 'J_prom6': J_prom6,'nombre_s':nombre_s,'nombre_s1':nombre_s1,
                                                              'nombre_s2':nombre_s2,'nombre_s3':nombre_s3,'nombre_s4':nombre_s4,'nombre_s5':nombre_s5,'nombre_s6':nombre_s6,
                                                              'mejor_prom_ML':mejor_prom_ML,'mejor_prom_SP':mejor_prom_SP,'mejor_prom_T':mejor_prom_T,
                                                              'mejor_prom_Ud':mejor_prom_Ud,'mejor_prom_SB':mejor_prom_SB,'mejor_prom_MA':mejor_prom_MA,'mejor_prom_BB':mejor_prom_BB,  })
   

#NLF profecional

def Crear_NLF(request):
    if request.method == 'POST':
        formulario = NLF_Profecional_form(request.POST)
        if formulario.is_valid():
            formulario.clean()
            objeto_creado = formulario.save()
            
          
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NLF_Profecional.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NLF_Profecional.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NLF_Profecional.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NLF_Profecional.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NLF_Profecional/informes.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,  'formulario':formulario, 'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })
       
        else:
            return render(request, 'NLF_Profecional/crear_NLF_profecional.html', {'formulario': formulario})
    else:
        formulario = NLF_Profecional_form()
        return render(request, 'NLF_Profecional/crear_NLF_profecional.html', {'formulario': formulario})

def Listar_NLF(request):
    lista =NLF_Profecional.objects.all().order_by('fecha')
    return render(request, 'NLF_Profecional/listar_NLF_profecional.html', {'lista':lista} )

def Eliminar_NLF(request, id):
    f = get_object_or_404(NLF_Profecional, id=id)
    f.delete()
    return redirect('listar_NLF_profecional')

def Buscar_NLF(request):
    resultados = []
    if request.method == 'POST':
        termino_busqueda = request.POST.get('searchbar')
        
        if termino_busqueda:
            # Construye condiciones para buscar en el nombre del equipo local o visitante
            condiciones = (
                Q(equipo_local__nombre__icontains=termino_busqueda) |
                Q(equipo_visitante__nombre__icontains=termino_busqueda)
            )
            
            # Filtra los resultados basándose en las condiciones construidas
            resultados = NLF_Profecional.objects.filter(condiciones)
        

        return render(request, 'NLF_Profecional/resultados.html', {'resultados': resultados})
    return render(request, 'NLF_Profecional/listar_NLF_profecional.html')

def Resultado_NLF(request, id):
    f = NLF_Profecional.objects.get(id=id)
    
    equipo_local = f.equipo_local.nombre
    equipo_visitante = f.equipo_visitante.nombre
    opciones_ganador = [ equipo_local,equipo_visitante,'Empate' ]
    
    if request.method == 'POST':
        form = resultado_NLF_Profecional_form(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return redirect('listar_NLF_profecional')
    else:
        form = resultado_NLF_Profecional_form( instance=f)

    return render(request, 'NLF_Profecional/resultado_NLF_profecional.html', {'form': form,'opciones_ganador': opciones_ganador})

def Informe_Resultado_NLF(request, id):
            objeto_creado = NLF_Profecional.objects.get(id=id)
    
    
   
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NLF_Profecional.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NLF_Profecional.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NLF_Profecional.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NLF_Profecional.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NLF_Profecional/informe_lista.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })

def Resultados_Sistemas_NLF(request): 
    
    partidos_filtrados = NLF_Profecional.objects.exclude(ganador__isnull=True).exclude(resultado__isnull=True)
    partidos = partidos_filtrados.order_by('-fecha')[:20]
    
    
    #Sistema A
    
    ganador=''
    cont_A_ML=0
    cont_A_SP=0
    cont_A_Ud=0
    cont_A_SB=0
    cont_A_MA=0
    cont_A_BB=0
    cont_A_Total=0
    A_cont=0
    A_cont1=0
    A_cont2=0
    A_cont3=0
    A_cont4=0
    A_cont5=0
    A_cont6=0
    sum=0
    res=0
    valor_izquierdo=0
    valor_derecho=0
    A_prom=0
    A_prom1=0
    A_prom2=0
    A_prom3=0
    A_prom4=0 
    A_prom5=0
    A_prom6=0
    
    for valor in partidos: 
        
        ganador=valor.ganador
        
        valor_izquierdo, valor_derecho = extraer_valores_de_resultado(valor)
        sum= valor_izquierdo+valor_derecho
        
        if valor.A_ML_equip is not None:
           A_cont+=1
           if ganador==valor.A_ML_equip.nombre:
              cont_A_ML+=1 
              
              
        if valor.A_Ud_equip is not None:
           A_cont1+=1      
           if ganador==valor.A_Ud_equip.nombre:
              cont_A_Ud+=1
              
              
        if valor.A_SB_equip is not None: 
           A_cont2+=1      
           if ganador==valor.A_SB_equip.nombre:
              cont_A_SB+=1
              
              
        if valor.A_MA is not None:
           A_cont3+=1 
           if ganador==valor.A_MA.nombre:
              cont_A_MA+=1
              
              
        if valor.A_BB is not None:  
           A_cont4+=1 
           if ganador==valor.A_BB.nombre:
              cont_A_BB+=1
         
         
        if valor.A_total_punto is not None: 
           A_cont5+=1 
           if sum>valor.A_total_punto and valor.A_Total_OU=='OVER':
              cont_A_Total+=1
           if sum<=valor.A_total_punto and valor.A_Total_OU=='UNDER':
              cont_A_Total+=1
         
         
       
        if valor_izquierdo>valor_derecho:
            res=valor_izquierdo-valor_derecho
           
        elif valor_izquierdo<valor_derecho:
            res=valor_derecho-valor_izquierdo 
        
        else: 
            res=0
        
        if valor.A_SP_dif is not None:
           A_cont6+=1
           if ganador==valor.A_SP_equip.nombre and res>valor.A_SP_dif :
              cont_A_SP+=1
           
           
           
    if cont_A_ML !=0 and A_cont !=0:
           A_prom=cont_A_ML*100/A_cont
        
    if cont_A_SP !=0 and A_cont6 !=0:
           A_prom6=cont_A_SP*100/A_cont6
           
    if cont_A_Ud !=0 and A_cont1 !=0:
           A_prom1=cont_A_Ud*100/A_cont1
           
    if cont_A_SB !=0 and A_cont2 !=0:
           A_prom2=cont_A_SB*100/A_cont2
           
    if cont_A_MA !=0 and A_cont3 !=0:
           A_prom3=cont_A_MA*100/A_cont3
           
    if cont_A_BB !=0 and A_cont4 !=0:
           A_prom4=cont_A_BB*100/A_cont5
           
    if cont_A_Total !=0 and A_cont5 !=0:
           A_prom5=cont_A_Total*100/A_cont5      
           
           
           
    #Sistema B     
    
    B_ganador=''
    cont_B_ML=0
    cont_B_SP=0
    cont_B_Ud=0
    cont_B_SB=0
    cont_B_MA=0
    cont_B_BB=0
    cont_B_Total=0
    B_cont=0
    B_cont1=0
    B_cont2=0
    B_cont3=0
    B_cont4=0
    B_cont5=0
    B_cont6=0
    B_sum=0
    B_res=0
    B_valor_izquierdo=0
    B_valor_derecho=0
    B_prom=0
    B_prom1=0
    B_prom2=0
    B_prom3=0
    B_prom4=0 
    B_prom5=0
    B_prom6=0
    
    for valor in partidos: 
        
        B_ganador=valor.ganador
        
        B_valor_izquierdo, B_valor_derecho = extraer_valores_de_resultado(valor)
        B_sum= B_valor_izquierdo+B_valor_derecho
        
        if valor.B_ML_equip is not None:
           B_cont+=1
           if B_ganador==valor.B_ML_equip.nombre:
              cont_B_ML+=1 
              
              
        if valor.B_Ud_equip is not None:
           B_cont1+=1      
           if B_ganador==valor.B_Ud_equip.nombre:
              cont_B_Ud+=1
              
              
        if valor.B_SB_equip is not None: 
           B_cont2+=1      
           if B_ganador==valor.B_SB_equip.nombre:
              cont_B_SB+=1
              
              
        if valor.B_MA is not None:
           B_cont3+=1 
           if B_ganador==valor.B_MA.nombre:
              cont_B_MA+=1
              
              
        if valor.B_BB is not None:  
           B_cont4+=1 
           if B_ganador==valor.B_BB.nombre:
              cont_B_BB+=1
         
         
        if valor.B_total_punto is not None: 
           B_cont5+=1 
           if B_sum>valor.B_total_punto and valor.B_Total_OU=='OVER':
              cont_B_Total+=1
           if B_sum<=valor.B_total_punto and valor.B_Total_OU=='UNDER':
              cont_B_Total+=1
         
         
       
        if B_valor_izquierdo>B_valor_derecho:
            B_res=B_valor_izquierdo-B_valor_derecho
           
        elif B_valor_izquierdo<B_valor_derecho:
            B_res=B_valor_derecho-B_valor_izquierdo 
        
        else: 
            B_res=0
        
        if valor.B_SP_dif is not None:
           B_cont6+=1
           if B_ganador==valor.B_SP_equip.nombre and B_res>valor.B_SP_dif :
              cont_B_SP+=1
           
           
           
    if cont_B_ML !=0 and B_cont !=0:
           B_prom=cont_B_ML*100/B_cont
        
    if cont_B_SP !=0 and B_cont6 !=0:
           B_prom6=cont_B_SP*100/B_cont6
           
    if cont_B_Ud !=0 and B_cont1 !=0:
           B_prom1=cont_B_Ud*100/B_cont1
           
    if cont_B_SB !=0 and B_cont2 !=0:
           B_prom2=cont_B_SB*100/B_cont2
           
    if cont_B_MA !=0 and B_cont3 !=0:
           B_prom3=cont_B_MA*100/B_cont3
           
    if cont_B_BB !=0 and B_cont4 !=0:
           B_prom4=cont_B_BB*100/B_cont5
           
    if cont_B_Total !=0 and B_cont5 !=0:
           B_prom5=cont_B_Total*100/B_cont5             
           
           
    C_ganador=''
    cont_C_ML=0
    cont_C_SP=0
    cont_C_Ud=0
    cont_C_SB=0
    cont_C_MA=0
    cont_C_BB=0
    cont_C_Total=0
    C_cont=0
    C_cont1=0
    C_cont2=0
    C_cont3=0
    C_cont4=0
    C_cont5=0
    C_cont6=0
    C_sum=0
    C_res=0
    C_valor_izquierdo=0
    C_valor_derecho=0
    C_prom=0
    C_prom1=0
    C_prom2=0
    C_prom3=0
    C_prom4=0 
    C_prom5=0        
    C_prom6=0
       
    for valor in partidos: 
        
        C_ganador=valor.ganador
            
        C_valor_izquierdo, C_valor_derecho = extraer_valores_de_resultado(valor)
        C_sum= C_valor_izquierdo+C_valor_derecho
            
        if valor.C_ML_equip is not None:
            C_cont+=1
            if C_ganador==valor.C_ML_equip.nombre:
                cont_C_ML+=1 
                
        if valor.C_Ud_equip is not None:
            C_cont1+=1      
            if C_ganador==valor.C_Ud_equip.nombre:
                cont_C_Ud+=1
                
        if valor.C_SB_equip is not None: 
            C_cont2+=1      
            if C_ganador==valor.C_SB_equip.nombre:
                cont_C_SB+=1
                
        if valor.C_MA is not None:
            C_cont3+=1 
            if C_ganador==valor.C_MA.nombre:
                cont_C_MA+=1
                
        if valor.C_BB is not None:  
            C_cont4+=1 
            if C_ganador==valor.C_BB.nombre:
                cont_C_BB+=1
            
            
        if valor.C_total_punto is not None: 
            C_cont5+=1 
            if C_sum>valor.C_total_punto and valor.C_Total_OU=='OVER':
                cont_C_Total+=1
            if C_sum<=valor.C_total_punto and valor.C_Total_OU=='UNDER':
                cont_C_Total+=1
            
            

        if C_valor_izquierdo>C_valor_derecho:
            C_res=C_valor_izquierdo-C_valor_derecho
            
        elif C_valor_izquierdo<C_valor_derecho:
            C_res=C_valor_derecho-C_valor_izquierdo 

        else: 
            C_res=0
            
        if valor.C_SP_dif is not None:
            C_cont6+=1
            if C_ganador==valor.C_SP_equip.nombre and C_res>valor.C_SP_dif :
                cont_C_SP+=1
           
           
    if cont_C_ML !=0 and C_cont !=0:
       C_prom=cont_C_ML*100/C_cont
            
    if cont_C_SP !=0 and C_cont6 !=0:
       C_prom6=cont_C_SP*100/C_cont6
            
    if cont_C_Ud !=0 and C_cont1 !=0:
       C_prom1=cont_C_Ud*100/C_cont1
            
    if cont_C_SB !=0 and C_cont2 !=0:
       C_prom2=cont_C_SB*100/C_cont2
            
    if cont_C_MA !=0 and C_cont3 !=0:
       C_prom3=cont_C_MA*100/C_cont3
            
    if cont_C_BB !=0 and C_cont4 !=0:
       C_prom4=cont_C_BB*100/C_cont5
            
    if cont_C_Total !=0 and C_cont5 !=0:
       C_prom5=cont_C_Total*100/C_cont5       
           
    
    
    D_ganador=''
    cont_D_ML=0
    cont_D_SP=0
    cont_D_Ud=0
    cont_D_SB=0
    cont_D_MA=0
    cont_D_BB=0
    cont_D_Total=0
    D_cont=0
    D_cont1=0
    D_cont2=0
    D_cont3=0
    D_cont4=0
    D_cont5=0
    D_cont6=0
    D_sum=0
    D_res=0
    D_valor_izquierdo=0
    D_valor_derecho=0
    D_prom=0
    D_prom1=0
    D_prom2=0
    D_prom3=0
    D_prom4=0 
    D_prom5=0        
    D_prom6=0

    
    
    
    for valor in partidos: 
        
        D_ganador=valor.ganador
            
        D_valor_izquierdo, D_valor_derecho = extraer_valores_de_resultado(valor)
        D_sum= D_valor_izquierdo+D_valor_derecho
            
        if valor.D_ML_equip is not None:
           D_cont+=1
           if D_ganador==valor.D_ML_equip.nombre:
              cont_D_ML+=1 
            
        if valor.D_Ud_equip is not None:
           D_cont1+=1      
           if D_ganador==valor.D_Ud_equip.nombre:
              cont_D_Ud+=1
            
        if valor.D_SB_equip is not None: 
           D_cont2+=1      
           if D_ganador==valor.D_SB_equip.nombre:
              cont_D_SB+=1
            
        if valor.D_MA is not None:
           D_cont3+=1 
           if D_ganador==valor.D_MA.nombre:
              cont_D_MA+=1
            
        if valor.D_BB is not None:  
           D_cont4+=1 
           if D_ganador==valor.D_BB.nombre:
              cont_D_BB+=1
        
        
        if valor.D_total_punto is not None: 
           D_cont5+=1 
           if D_sum>valor.D_total_punto and valor.D_Total_OU=='OVER':
              cont_D_Total+=1
           if D_sum<=valor.D_total_punto and valor.D_Total_OU=='UNDER':
              cont_D_Total+=1
        
        
    
        if D_valor_izquierdo>D_valor_derecho:
            D_res=D_valor_izquierdo-D_valor_derecho
        
        elif D_valor_izquierdo<D_valor_derecho:
            D_res=D_valor_derecho-D_valor_izquierdo 
        
        else: 
            D_res=0
            
        if valor.D_SP_dif is not None:
           D_cont6+=1
           if D_ganador==valor.D_SP_equip.nombre and D_res>valor.D_SP_dif :
              cont_D_SP+=1
             
           
    if cont_D_ML !=0 and D_cont !=0:
       D_prom=cont_D_ML*100/D_cont
            
    if cont_D_SP !=0 and D_cont6 !=0:
       D_prom6=cont_D_SP*100/D_cont6
            
    if cont_D_Ud !=0 and D_cont1 !=0:
       D_prom1=cont_D_Ud*100/D_cont1
            
    if cont_D_SB !=0 and D_cont2 !=0:
       D_prom2=cont_D_SB*100/D_cont2
            
    if cont_D_MA !=0 and D_cont3 !=0:
       D_prom3=cont_D_MA*100/D_cont3
            
    if cont_D_BB !=0 and D_cont4 !=0:
       D_prom4=cont_D_BB*100/D_cont5
            
    if cont_D_Total !=0 and D_cont5 !=0:
       D_prom5=cont_D_Total*100/D_cont5
        
    
    E_ganador=''
    cont_E_ML=0
    cont_E_SP=0
    cont_E_Ud=0
    cont_E_SB=0
    cont_E_MA=0
    cont_E_BB=0
    cont_E_Total=0
    E_cont=0
    E_cont1=0
    E_cont2=0
    E_cont3=0
    E_cont4=0
    E_cont5=0
    E_cont6=0
    E_sum=0
    E_res=0
    E_valor_izquierdo=0
    E_valor_derecho=0
    E_prom=0
    E_prom1=0
    E_prom2=0
    E_prom3=0
    E_prom4=0 
    E_prom5=0        
    E_prom6=0
       
    for valor in partidos: 
        
        E_ganador=valor.ganador
            
        E_valor_izquierdo, E_valor_derecho = extraer_valores_de_resultado(valor)
        E_sum= E_valor_izquierdo+E_valor_derecho
            
        if valor.E_ML_equip is not None:
           E_cont+=1
           if E_ganador==valor.E_ML_equip.nombre:
              cont_E_ML+=1 
            
        if valor.E_Ud_equip is not None:
           E_cont1+=1      
           if E_ganador==valor.E_Ud_equip.nombre:
              cont_E_Ud+=1
            
        if valor.E_SB_equip is not None: 
           E_cont2+=1      
           if E_ganador==valor.E_SB_equip.nombre:
              cont_E_SB+=1
            
        if valor.E_MA is not None:
           E_cont3+=1 
           if E_ganador==valor.E_MA.nombre:
              cont_E_MA+=1
            
        if valor.E_BB is not None:  
           E_cont4+=1 
           if E_ganador==valor.E_BB.nombre:
              cont_E_BB+=1
        
        
        if valor.E_total_punto is not None: 
           E_cont5+=1 
           if E_sum>valor.E_total_punto and valor.E_Total_OU=='OVER':
              cont_E_Total+=1
           if E_sum<=valor.E_total_punto and valor.E_Total_OU=='UNDER':
              cont_E_Total+=1
        
        
    
        if E_valor_izquierdo>E_valor_derecho:
            E_res=E_valor_izquierdo-E_valor_derecho
        
        elif E_valor_izquierdo<E_valor_derecho:
            E_res=E_valor_derecho-E_valor_izquierdo 
        
        else: 
            E_res=0
            
        if valor.E_SP_dif is not None:
           E_cont6+=1
           if E_ganador==valor.E_SP_equip.nombre and E_res>valor.E_SP_dif :
              cont_E_SP+=1
            
           
    if cont_E_ML !=0 and E_cont !=0:
       E_prom=cont_E_ML*100/E_cont
            
    if cont_E_SP !=0 and E_cont6 !=0:
       E_prom6=cont_E_SP*100/E_cont6
            
    if cont_E_Ud !=0 and E_cont1 !=0:
       E_prom1=cont_E_Ud*100/E_cont1   
        
    if cont_E_SB !=0 and E_cont2 !=0:
       E_prom2=cont_E_SB*100/E_cont2
            
    if cont_E_MA !=0 and E_cont3 !=0:
       E_prom3=cont_E_MA*100/E_cont3
            
    if cont_E_BB !=0 and E_cont4 !=0:
       E_prom4=cont_E_BB*100/E_cont5
            
    if cont_E_Total !=0 and E_cont5 !=0:
       E_prom5=cont_E_Total*100/E_cont5     
    
    
    
    
    F_ganador=''
    cont_F_ML=0
    cont_F_SP=0
    cont_F_Ud=0
    cont_F_SB=0
    cont_F_MA=0
    cont_F_BB=0
    cont_F_Total=0
    F_cont=0
    F_cont1=0
    F_cont2=0
    F_cont3=0
    F_cont4=0
    F_cont5=0
    F_cont6=0
    F_sum=0
    F_res=0
    F_valor_izquierdo=0
    F_valor_derecho=0
    F_prom=0
    F_prom1=0
    F_prom2=0
    F_prom3=0
    F_prom4=0 
    F_prom5=0        
    F_prom6=0
       
    
    for valor in partidos: 
        
 
        F_valor_izquierdo, F_valor_derecho = extraer_valores_de_resultado(valor)
        F_sum = F_valor_izquierdo + F_valor_derecho
                
        if valor.F_ML_equip is not None:
           F_cont+=1
           if F_ganador==valor.F_ML_equip.nombre:
              F_cont_ML+=1 
                
        if valor.F_Ud_equip is not None:
           F_cont1+=1      
           if F_ganador==valor.F_Ud_equip.nombre:
              F_cont_Ud+=1
                
        if valor.F_SB_equip is not None: 
           F_cont2+=1      
           if F_ganador==valor.F_SB_equip.nombre:
              F_cont_SB+=1
                
        if valor.F_MA is not None:
           F_cont3+=1 
           if F_ganador==valor.F_MA.nombre:
              F_cont_MA+=1
                
        if valor.F_BB is not None:  
           F_cont4+=1 
           if F_ganador==valor.F_BB.nombre:
              F_cont_BB+=1
            
            
        if valor.F_total_punto is not None: 
           F_cont5+=1 
           if F_sum>F_valor_izquierdo and valor.F_Total_OU=='OVER':
              F_cont_Total+=1
           if F_sum<=valor.F_total_punto and valor.F_Total_OU=='UNDER':
              F_cont_Total+=1
            
            
        if F_valor_izquierdo>F_valor_derecho:
            F_res=F_valor_izquierdo-F_valor_derecho
            
        elif F_valor_izquierdo<F_valor_derecho:
            F_res=F_valor_derecho-F_valor_izquierdo 
        
        else: 
            F_res=0
                
        if valor.F_SP_dif is not None:
           F_cont6+=1
           if F_ganador==valor.F_SP_equip.nombre and F_res>valor.F_SP_dif :
              F_cont_SP+=1
            
           
    if cont_F_ML !=0 and F_cont !=0:
       F_prom=F_cont_ML*100/F_cont
                
    if cont_F_SP !=0 and F_cont6 !=0:
       F_prom6=F_cont_SP*100/F_cont6
                
    if cont_F_Ud !=0 and F_cont1 !=0:
       F_prom1=F_cont_Ud*100/F_cont1   
            
    if cont_F_SB !=0 and F_cont2 !=0:
       F_prom2=F_cont_SB*100/F_cont2
                
    if cont_F_MA !=0 and F_cont3 !=0:
       F_prom3=F_cont_MA*100/F_cont3
                
    if cont_F_BB !=0 and F_cont4 !=0:
       F_prom4=F_cont_BB*100/F_cont5
                
    if cont_F_Total !=0 and F_cont5 !=0:
       F_prom5=F_cont_Total*100/F_cont5
        
    
    G_ganador=''
    cont_G_ML=0
    cont_G_SP=0
    cont_G_Ud=0
    cont_G_SB=0
    cont_G_MA=0
    cont_G_BB=0
    cont_G_Total=0
    G_cont=0
    G_cont1=0
    G_cont2=0
    G_cont3=0
    G_cont4=0
    G_cont5=0
    G_cont6=0
    G_sum=0
    G_res=0
    G_valor_izquierdo=0
    G_valor_derecho=0
    G_prom=0
    G_prom1=0
    G_prom2=0
    G_prom3=0
    G_prom4=0 
    G_prom5=0        
    G_prom6=0

    for valor in partidos: 
        
        G_valor_izquierdo, G_valor_derecho = extraer_valores_de_resultado(valor)
        G_sum = G_valor_izquierdo + G_valor_derecho
                    
        if valor.G_ML_equip is not None:
           G_cont+=1
           if G_ganador==valor.G_ML_equip.nombre:
              G_cont_ML+=1 
                    
        if valor.G_Ud_equip is not None:
           G_cont1+=1      
           if G_ganador==valor.G_Ud_equip.nombre:
              G_cont_Ud+=1
                    
        if valor.G_SB_equip is not None: 
           G_cont2+=1      
           if G_ganador==valor.G_SB_equip.nombre:
              G_cont_SB+=1
                    
        if valor.G_MA is not None:
           G_cont3+=1 
           if G_ganador==valor.G_MA.nombre:
              G_cont_MA+=1
                    
        if valor.G_BB is not None:  
           G_cont4+=1 
           if G_ganador==valor.G_BB.nombre:
              G_cont_BB+=1
                
                
        if valor.G_total_punto is not None: 
           G_cont5+=1 
           if G_sum>G_valor_izquierdo and valor.G_Total_OU=='OVER':
              G_cont_Total+=1
           if G_sum<=valor.G_total_punto and valor.G_Total_OU=='UNDER':
              G_cont_Total+=1
                
                
        if G_valor_izquierdo>G_valor_derecho:
            G_res=G_valor_izquierdo-G_valor_derecho
                
        elif G_valor_izquierdo<G_valor_derecho:
            G_res=G_valor_derecho-G_valor_izquierdo 
            
        else: 
            G_res=0
                    
        if valor.G_SP_dif is not None:
           G_cont6+=1
           if G_ganador==valor.G_SP_equip.nombre and G_res>valor.G_SP_dif :
              G_cont_SP+=1
            
           
    if cont_G_ML !=0 and G_cont !=0:
       G_prom=G_cont_ML*100/G_cont
                    
    if cont_G_SP !=0 and G_cont6 !=0:
       G_prom6=G_cont_SP*100/G_cont6
                    
    if cont_G_Ud !=0 and G_cont1 !=0:
       G_prom1=G_cont_Ud*100/G_cont1   
                
    if cont_G_SB !=0 and G_cont2 !=0:
       G_prom2=G_cont_SB*100/G_cont2
                    
    if cont_G_MA !=0 and G_cont3 !=0:
       G_prom3=G_cont_MA*100/G_cont3
                    
    if cont_G_BB !=0 and G_cont4 !=0:
       G_prom4=G_cont_BB*100/G_cont5
                    
    if cont_G_Total !=0 and G_cont5 !=0:
       G_prom5=G_cont_Total*100/G_cont5
            
            
            
    H_ganador=''
    cont_H_ML=0
    cont_H_SP=0
    cont_H_Ud=0
    cont_H_SB=0
    cont_H_MA=0
    cont_H_BB=0
    cont_H_Total=0
    H_cont=0
    H_cont1=0
    H_cont2=0
    H_cont3=0
    H_cont4=0
    H_cont5=0
    H_cont6=0
    H_sum=0
    H_res=0
    H_valor_izquierdo=0
    H_valor_derecho=0
    H_prom=0
    H_prom1=0
    H_prom2=0
    H_prom3=0
    H_prom4=0 
    H_prom5=0        
    H_prom6=0
        
            
    for valor in partidos: 
        
        H_valor_izquierdo, H_valor_derecho = extraer_valores_de_resultado(valor)
        H_sum = H_valor_izquierdo + H_valor_derecho
                        
        if valor.H_ML_equip is not None:
           H_cont+=1
           if H_ganador==valor.H_ML_equip.nombre:
              H_cont_ML+=1 
                        
        if valor.H_Ud_equip is not None:
           H_cont1+=1      
           if H_ganador==valor.H_Ud_equip.nombre:
              H_cont_Ud+=1
                        
        if valor.H_SB_equip is not None: 
           H_cont2+=1      
           if H_ganador==valor.H_SB_equip.nombre:
              H_cont_SB+=1
                        
        if valor.H_MA is not None:
           H_cont3+=1 
           if H_ganador==valor.H_MA.nombre:
              H_cont_MA+=1
                        
        if valor.H_BB is not None:  
           H_cont4+=1 
           if H_ganador==valor.H_BB.nombre:
              H_cont_BB+=1
                    
                    
        if valor.H_total_punto is not None: 
           H_cont5+=1 
           if H_sum>H_valor_izquierdo and valor.H_Total_OU=='OVER':
              H_cont_Total+=1
           if H_sum<=valor.H_total_punto and valor.H_Total_OU=='UNDER':
              H_cont_Total+=1
                    
                    
        if H_valor_izquierdo>H_valor_derecho:
                H_res=H_valor_izquierdo-H_valor_derecho
                    
        elif H_valor_izquierdo<H_valor_derecho:
                H_res=H_valor_derecho-H_valor_izquierdo 
                
        else: 
                H_res=0
                        
        if valor.H_SP_dif is not None:
           H_cont6+=1
           if H_ganador==valor.H_SP_equip.nombre and H_res>valor.H_SP_dif :
              H_cont_SP+=1
            
           
    if cont_H_ML !=0 and H_cont !=0:
       H_prom=H_cont_ML*100/H_cont
                    
    if cont_H_SP !=0 and H_cont6 !=0:
       H_prom6=H_cont_SP*100/H_cont6
                    
    if cont_H_Ud !=0 and H_cont1 !=0:
       H_prom1=H_cont_Ud*100/H_cont1   
                
    if cont_H_SB !=0 and H_cont2 !=0:
       H_prom2=H_cont_SB*100/H_cont2
                    
    if cont_H_MA !=0 and H_cont3 !=0:
       H_prom3=H_cont_MA*100/H_cont3
                    
    if cont_H_BB !=0 and H_cont4 !=0:
       H_prom4=H_cont_BB*100/H_cont5
                    
    if cont_H_Total !=0 and H_cont5 !=0:
       H_prom5=H_cont_Total*100/H_cont5        
            
    
    
    I_ganador=''
    cont_I_ML=0
    cont_I_SP=0
    cont_I_Ud=0
    cont_I_SB=0
    cont_I_MA=0
    cont_I_BB=0
    cont_I_Total=0
    I_cont=0
    I_cont1=0
    I_cont2=0
    I_cont3=0
    I_cont4=0
    I_cont5=0
    I_cont6=0
    I_sum=0
    I_res=0
    I_valor_izquierdo=0
    I_valor_derecho=0
    I_prom=0
    I_prom1=0
    I_prom2=0
    I_prom3=0
    I_prom4=0 
    I_prom5=0        
    I_prom6=0
        
            
    for valor in partidos: 
        
        I_valor_izquierdo, I_valor_derecho = extraer_valores_de_resultado(valor)
        I_sum = I_valor_izquierdo + I_valor_derecho
                        
        if valor.I_ML_equip is not None:
           I_cont+=1
           if I_ganador==valor.I_ML_equip.nombre:
              I_cont_ML+=1 
                        
        if valor.I_Ud_equip is not None:
           I_cont1+=1      
           if I_ganador==valor.I_Ud_equip.nombre:
              I_cont_Ud+=1
                        
        if valor.I_SB_equip is not None: 
           I_cont2+=1      
           if I_ganador==valor.I_SB_equip.nombre:
              I_cont_SB+=1
                        
        if valor.I_MA is not None:
           I_cont3+=1 
           if I_ganador==valor.I_MA.nombre:
              I_cont_MA+=1
                        
        if valor.I_BB is not None:  
           I_cont4+=1 
           if I_ganador==valor.I_BB.nombre:
              I_cont_BB+=1
                    
                    
        if valor.I_total_punto is not None: 
           I_cont5+=1 
           if I_sum>I_valor_izquierdo and valor.I_Total_OU=='OVER':
              I_cont_Total+=1
           if I_sum<=valor.I_total_punto and valor.I_Total_OU=='UNDER':
              I_cont_Total+=1
                    
                    
        if I_valor_izquierdo>I_valor_derecho:
                I_res=I_valor_izquierdo-I_valor_derecho
                    
        elif I_valor_izquierdo<I_valor_derecho:
                I_res=I_valor_derecho-I_valor_izquierdo 
                
        else: 
                I_res=0
                        
        if valor.I_SP_dif is not None:
           I_cont6+=1
           if I_ganador==valor.I_SP_equip.nombre and I_res>valor.I_SP_dif :
              I_cont_SP+=1
            
           
    if cont_I_ML !=0 and I_cont !=0:
       I_prom=I_cont_ML*100/I_cont
                        
    if cont_I_SP !=0 and I_cont6 !=0:
       I_prom6=I_cont_SP*100/I_cont6
                        
    if cont_I_Ud !=0 and I_cont1 !=0:
       I_prom1=I_cont_Ud*100/I_cont1   
                    
    if cont_I_SB !=0 and I_cont2 !=0:
       I_prom2=I_cont_SB*100/I_cont2
                        
    if cont_I_MA !=0 and I_cont3 !=0:
       I_prom3=I_cont_MA*100/I_cont3
                        
    if cont_I_BB !=0 and I_cont4 !=0:
       I_prom4=I_cont_BB*100/I_cont5
                        
    if cont_I_Total !=0 and I_cont5 !=0:
       I_prom5=I_cont_Total*100/I_cont5        
            
            
    J_ganador=''
    cont_J_ML=0
    cont_J_SP=0
    cont_J_Ud=0
    cont_J_SB=0
    cont_J_MA=0
    cont_J_BB=0
    cont_J_Total=0
    J_cont=0
    J_cont1=0
    J_cont2=0
    J_cont3=0
    J_cont4=0
    J_cont5=0
    J_cont6=0
    J_sum=0
    J_res=0
    J_valor_izquierdo=0
    J_valor_derecho=0
    J_prom=0
    J_prom1=0
    J_prom2=0
    J_prom3=0
    J_prom4=0 
    J_prom5=0        
    J_prom6=0
        
    for valor in partidos: 
        
        J_valor_izquierdo, J_valor_derecho = extraer_valores_de_resultado(valor)
        J_sum = J_valor_izquierdo + J_valor_derecho
                            
        if valor.J_ML_equip is not None:
           J_cont+=1
           if J_ganador==valor.J_ML_equip.nombre:
              J_cont_ML+=1 
                            
        if valor.J_Ud_equip is not None:
           J_cont1+=1      
           if J_ganador==valor.J_Ud_equip.nombre:
              J_cont_Ud+=1
                            
        if valor.J_SB_equip is not None: 
           J_cont2+=1      
           if J_ganador==valor.J_SB_equip.nombre:
              J_cont_SB+=1
                            
        if valor.J_MA is not None:
           J_cont3+=1 
           if J_ganador==valor.J_MA.nombre:
              J_cont_MA+=1
                            
        if valor.J_BB is not None:  
           J_cont4+=1 
           if J_ganador==valor.J_BB.nombre:
              J_cont_BB+=1
                        
                        
        if valor.J_total_punto is not None: 
           J_cont5+=1 
           if J_sum>J_valor_izquierdo and valor.J_Total_OU=='OVER':
              J_cont_Total+=1
           if J_sum<=valor.J_total_punto and valor.J_Total_OU=='UNDER':
              J_cont_Total+=1
                        
                        
        if J_valor_izquierdo>J_valor_derecho:
                J_res=J_valor_izquierdo-J_valor_derecho
                        
        elif J_valor_izquierdo<J_valor_derecho:
                J_res=J_valor_derecho-J_valor_izquierdo 
                    
        else: 
                J_res=0
                            
        if valor.J_SP_dif is not None:
           J_cont6+=1
           if J_ganador==valor.J_SP_equip.nombre and J_res>valor.J_SP_dif :
              J_cont_SP+=1
            
           
    if cont_J_ML !=0 and J_cont !=0:
       J_prom=J_cont_ML*100/J_cont
                            
    if cont_J_SP !=0 and J_cont6 !=0:
       J_prom6=J_cont_SP*100/J_cont6
                            
    if cont_J_Ud !=0 and J_cont1 !=0:
       J_prom1=J_cont_Ud*100/J_cont1   
                        
    if cont_J_SB !=0 and J_cont2 !=0:
       J_prom2=J_cont_SB*100/J_cont2
                            
    if cont_J_MA !=0 and J_cont3 !=0:
       J_prom3=J_cont_MA*100/J_cont3
                            
    if cont_J_BB !=0 and J_cont4 !=0:
       J_prom4=J_cont_BB*100/J_cont5
                            
    if cont_J_Total !=0 and J_cont5 !=0:
       J_prom5=J_cont_Total*100/J_cont5      
       
       
    mejor_prom_ML=0
    mejor_prom_SP=0
    mejor_prom_T=0
    mejor_prom_Ud=0
    mejor_prom_SB=0
    mejor_prom_MA=0     
    mejor_prom_BB=0
    nombre_s=0
    nombre_s1=0
    nombre_s2=0
    nombre_s3=0
    nombre_s4=0
    nombre_s5=0
    nombre_s6=0
    
    
    list_ML=[A_prom,B_prom,C_prom,D_prom,E_prom,F_prom,G_prom,H_prom,I_prom,J_prom]
    list_SP=[A_prom6,B_prom6,C_prom6,D_prom6,E_prom6,F_prom6,G_prom6,H_prom6,I_prom6,J_prom6]
    list_T=[A_prom5,B_prom5,C_prom5,D_prom5,E_prom5,F_prom5,G_prom5,H_prom5,I_prom5,J_prom5]
    list_Ud=[A_prom1,B_prom1,C_prom1,D_prom1,E_prom1,F_prom1,G_prom1,H_prom1,I_prom1,J_prom1]     
    list_SB=[A_prom2,B_prom2,C_prom2,D_prom2,E_prom2,F_prom2,G_prom2,H_prom2,I_prom2,J_prom2]
    list_MA=[A_prom3,B_prom3,C_prom3,D_prom3,E_prom3,F_prom3,G_prom3,H_prom3,I_prom3,J_prom3]
    list_BB=[A_prom4,B_prom4,C_prom4,D_prom4,E_prom4,F_prom4,G_prom4,H_prom4,I_prom4,J_prom4]
    
    lista_sistemas=['VeriBet','Action Network','Sports Insights','PFF','Covers','Team Rankings','BetQL','Odds Jams','Scores and Odds','Betting on Cash']
       
    for indice,i in enumerate(list_ML):
        if i>mejor_prom_ML:
           mejor_prom_ML=i   
           nombre_s=indice
           
        
    for indice,i in enumerate(list_SP):
        if i>mejor_prom_SP:
           mejor_prom_SP=i        
           nombre_s1=indice
            
    for indice,i in enumerate( list_T):
        if i>mejor_prom_T:
           mejor_prom_T=i         
           nombre_s2=indice
           
    for indice,i in enumerate(list_Ud):
        if i>mejor_prom_Ud:
           mejor_prom_Ud=i 
           nombre_s3=indice
           
    for indice,i in enumerate(list_SB):
        if i>mejor_prom_SB:
           mejor_prom_SB=i 
           nombre_s4=indice
           
    for indice,i in enumerate(list_MA):
        if i>mejor_prom_MA:
           mejor_prom_MA=i 
           nombre_s5=indice
           
    for indice,i in enumerate(list_BB):
        if i>mejor_prom_BB:
           mejor_prom_BB=i 
           nombre_s6=indice
           
           
           
           
           
    for indice,i in enumerate(lista_sistemas):
        if nombre_s==indice:
           nombre_s=i       
           break
              
    for indice,i in enumerate(lista_sistemas):
        if nombre_s1==indice:
           nombre_s1=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s2==indice:
           nombre_s2=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s3==indice:
           nombre_s3=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s4==indice:
           nombre_s4=i       
           break
    
    for indice,i in enumerate(lista_sistemas):
        if nombre_s5==indice:
           nombre_s5=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s6==indice:
           nombre_s6=i       
           break          
              
              
              
              
    return render(request,'NLF_Profecional/resultados_sistemas.html', {'cont_A_ML':cont_A_ML, 'cont_A_SP':cont_A_SP, 'cont_A_Ud':cont_A_Ud, 
                                                              'cont_A_MA':cont_A_MA,'cont_A_SB':cont_A_SB,'cont_A_BB':cont_A_BB,
                                                              'cont_A_Total':cont_A_Total,'A_cont':A_cont,'A_cont1':A_cont1,'A_cont2':A_cont2,
                                                              'A_cont3':A_cont3,'A_cont4':A_cont4,'A_cont5':A_cont5,'A_cont6':A_cont6, 
                                                              'A_prom':A_prom,'A_prom1':A_prom1,'A_prom2':A_prom2,'A_prom3':A_prom3,'A_prom4':A_prom4,
                                                              'A_prom5':A_prom5,'A_prom6':A_prom6,'cont_B_ML': cont_B_ML, 'cont_B_SP': cont_B_SP, 
                                                              'cont_B_Ud': cont_B_Ud, 'cont_B_MA': cont_B_MA, 'cont_B_SB': cont_B_SB, 'cont_B_BB': cont_B_BB,
                                                              'cont_B_Total': cont_B_Total, 'B_cont': B_cont, 'B_cont1': B_cont1, 'B_cont2': B_cont2,
                                                              'B_cont3': B_cont3, 'B_cont4': B_cont4, 'B_cont5': B_cont5, 'B_cont6': B_cont6, 'B_prom': B_prom,
                                                              'B_prom1': B_prom1, 'B_prom2': B_prom2, 'B_prom3': B_prom3, 'B_prom4': B_prom4, 'B_prom5': B_prom5, 
                                                              'B_prom6': B_prom6,'cont_C_ML': cont_C_ML, 'cont_C_SP': cont_C_SP, 'cont_C_Ud': cont_C_Ud, 
                                                              'cont_C_MA': cont_C_MA, 'cont_C_SB': cont_C_SB, 'cont_C_BB': cont_C_BB, 'cont_C_Total': cont_C_Total,
                                                              'C_cont': C_cont, 'C_cont1': C_cont1, 'C_cont2': C_cont2, 'C_cont3': C_cont3, 'C_cont4': C_cont4,
                                                              'C_cont5': C_cont5, 'C_cont6': C_cont6, 'C_prom': C_prom, 'C_prom1': C_prom1, 'C_prom2': C_prom2,
                                                              'C_prom3': C_prom3, 'C_prom4': C_prom4, 'C_prom5': C_prom5, 'C_prom6': C_prom6, 'cont_D_ML': cont_D_ML,
                                                              'cont_D_SP': cont_D_SP, 'cont_D_Ud': cont_D_Ud, 'cont_D_MA': cont_D_MA, 'cont_D_SB': cont_D_SB,
                                                              'cont_D_BB': cont_D_BB, 'cont_D_Total':cont_D_Total, 'D_cont': D_cont, 'D_cont1': D_cont1,
                                                              'D_cont2': D_cont2, 'D_cont3': D_cont3, 'D_cont4': D_cont4,'D_cont5': D_cont5, 'D_cont6': D_cont6,
                                                              'D_prom': D_prom, 'D_prom1': D_prom1, 'D_prom2': D_prom2,'D_prom3': D_prom3, 'D_prom4': D_prom4, 
                                                              'D_prom5': D_prom5, 'D_prom6': D_prom6, 'cont_E_ML': cont_E_ML, 'cont_E_SP': cont_E_SP, 
                                                              'cont_E_Ud': cont_E_Ud, 'cont_E_MA': cont_E_MA, 'cont_E_SB': cont_E_SB, 'cont_E_BB': cont_E_BB, 
                                                              'cont_E_Total': cont_E_Total,'E_cont': E_cont, 'E_cont1': E_cont1, 'E_cont2': E_cont2, 'E_cont3': E_cont3,
                                                              'E_cont4': E_cont4,'E_cont5': E_cont5, 'E_cont6': E_cont6, 'E_prom': E_prom, 'E_prom1': E_prom1, 
                                                              'E_prom2': E_prom2,'E_prom3': E_prom3, 'E_prom4': E_prom4, 'E_prom5': E_prom5, 'E_prom6': E_prom6,
                                                              'cont_F_ML': cont_F_ML, 'cont_F_SP': cont_F_SP, 'cont_F_Ud': cont_F_Ud, 'cont_F_MA': cont_F_MA, 
                                                              'cont_F_SB': cont_F_SB, 'cont_F_BB': cont_F_BB, 'cont_F_Total': cont_F_Total,'F_cont': F_cont, 
                                                              'F_cont1': F_cont1, 'F_cont2': F_cont2, 'F_cont3': F_cont3,'F_cont4': F_cont4,'F_cont5': F_cont5, 
                                                              'F_cont6': F_cont6, 'F_prom': F_prom, 'F_prom1': F_prom1, 'F_prom2': F_prom2,'F_prom3': F_prom3, 
                                                              'F_prom4': F_prom4, 'F_prom5': F_prom5, 'F_prom6': F_prom6,'cont_G_ML': cont_G_ML, 'cont_G_SP': cont_G_SP,
                                                              'cont_G_Ud': cont_G_Ud, 'cont_G_MA':cont_G_MA, 'cont_G_SB':cont_G_SB, 'cont_G_BB': cont_G_BB,
                                                              'cont_G_Total':cont_G_Total,'G_cont': G_cont, 'G_cont1': G_cont1, 'G_cont2': G_cont2, 'G_cont3': G_cont3,
                                                              'G_cont4': G_cont4,'G_cont5': G_cont5, 'G_cont6': G_cont6, 'G_prom': G_prom, 'G_prom1': G_prom1, 
                                                              'G_prom2': G_prom2,'G_prom3': G_prom3, 'G_prom4': G_prom4, 'G_prom5': G_prom5, 'G_prom6': G_prom6,
                                                              'cont_H_ML': cont_H_ML, 'cont_H_SP': cont_H_SP, 'cont_H_Ud': cont_H_Ud, 'cont_H_MA':cont_H_MA,
                                                              'cont_H_SB': cont_H_SB, 'cont_H_BB': cont_H_BB, 'cont_H_Total':cont_H_Total,'H_cont': H_cont,
                                                              'H_cont1': H_cont1, 'H_cont2': H_cont2, 'H_cont3': H_cont3,'H_cont4': H_cont4,'H_cont5': H_cont5,
                                                              'H_cont6': H_cont6, 'H_prom': H_prom, 'H_prom1': H_prom1, 'H_prom2': H_prom2,'H_prom3': H_prom3, 
                                                              'H_prom4': H_prom4, 'H_prom5': H_prom5, 'H_prom6': H_prom6,'cont_I_ML': cont_I_ML, 'cont_I_SP': cont_I_SP,
                                                              'cont_I_Ud': cont_I_Ud, 'cont_I_MA': cont_I_MA, 'cont_I_SB': cont_I_SB, 'cont_I_BB': cont_I_BB, 
                                                              'cont_I_Total': cont_I_Total,'I_cont': I_cont, 'I_cont1': I_cont1, 'I_cont2': I_cont2, 'I_cont3': I_cont3,
                                                              'I_cont4': I_cont4,'I_cont5': I_cont5, 'I_cont6': I_cont6, 'I_prom': I_prom, 'I_prom1': I_prom1,
                                                              'I_prom2': I_prom2,'I_prom3': I_prom3, 'I_prom4': I_prom4, 'I_prom5': I_prom5, 'I_prom6': I_prom6,
                                                              'cont_J_ML': cont_J_ML, 'cont_J_SP': cont_J_SP, 'cont_J_Ud': cont_J_Ud, 'cont_J_MA': cont_J_MA,
                                                              'cont_J_SB': cont_J_SB, 'cont_J_BB':cont_J_BB, 'cont_J_Total': cont_J_Total,'J_cont': J_cont, 
                                                              'J_cont1': J_cont1, 'J_cont2': J_cont2, 'J_cont3': J_cont3,'J_cont4': J_cont4,'J_cont5': J_cont5, 
                                                              'J_cont6': J_cont6, 'J_prom': J_prom, 'J_prom1': J_prom1, 'J_prom2': J_prom2,'J_prom3': J_prom3, 
                                                              'J_prom4': J_prom4, 'J_prom5': J_prom5, 'J_prom6': J_prom6,'nombre_s':nombre_s,'nombre_s1':nombre_s1,
                                                              'nombre_s2':nombre_s2,'nombre_s3':nombre_s3,'nombre_s4':nombre_s4,'nombre_s5':nombre_s5,'nombre_s6':nombre_s6,
                                                              'mejor_prom_ML':mejor_prom_ML,'mejor_prom_SP':mejor_prom_SP,'mejor_prom_T':mejor_prom_T,
                                                              'mejor_prom_Ud':mejor_prom_Ud,'mejor_prom_SB':mejor_prom_SB,'mejor_prom_MA':mejor_prom_MA,'mejor_prom_BB':mejor_prom_BB,  })
   

#NLF colegial

def Crear_NLFC(request):
    if request.method == 'POST':
        formulario = NLF_Colegial_form(request.POST)
        if formulario.is_valid():
            formulario.clean()
            objeto_creado = formulario.save()
            
          
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NLF_Colegial.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NLF_Colegial.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NLF_Colegial.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NLF_Colegial.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NLF_Colegial/informes.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,  'formulario':formulario, 'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })
       
        else:
            return render(request, 'NLF_Colegial/crear_NLF_colegial.html', {'formulario': formulario})
    else:
        formulario = NLF_Colegial_form()
        return render(request, 'NLF_Colegial/crear_NLF_colegial.html', {'formulario': formulario})

def Listar_NLFC(request):
    lista =NLF_Colegial.objects.all().order_by('fecha')
    return render(request, 'NLF_Colegial/listar_NLF_colegial.html', {'lista':lista} )

def Eliminar_NLFC(request, id):
    f = get_object_or_404(NLF_Colegial, id=id)
    f.delete()
    return redirect('listar_NLF_colegial')

def Buscar_NLFC(request):
    resultados = []
    if request.method == 'POST':
        termino_busqueda = request.POST.get('searchbar')
        
        if termino_busqueda:
            # Construye condiciones para buscar en el nombre del equipo local o visitante
            condiciones = (
                Q(equipo_local__nombre__icontains=termino_busqueda) |
                Q(equipo_visitante__nombre__icontains=termino_busqueda)
            )
            
            # Filtra los resultados basándose en las condiciones construidas
            resultados = NLF_Colegial.objects.filter(condiciones)
        

        return render(request, 'NLF_Colegial/resultados.html', {'resultados': resultados})
    return render(request, 'NLF_Colegial/listar_colegial.html')

def Resultado_NLFC(request, id):
    f = NLF_Colegial.objects.get(id=id)
    
    equipo_local = f.equipo_local.nombre
    equipo_visitante = f.equipo_visitante.nombre
    opciones_ganador = [ equipo_local,equipo_visitante,'Empate' ]
    
    if request.method == 'POST':
        form = resultado_NLF_Colegial_form(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return redirect('listar_NLF_colegial')
    else:
        form = resultado_NLF_Colegial_form( instance=f)

    return render(request, 'NLF_Colegial/resultado_NLF_colegial.html', {'form': form,'opciones_ganador': opciones_ganador})

def Informe_Resultado_NLFC(request, id):
            objeto_creado = NLF_Colegial.objects.get(id=id)
    
    
   
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NLF_Colegial.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NLF_Colegial.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NLF_Colegial.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NLF_Colegial.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NLF_Colegial/informe_lista.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })

def Resultados_Sistemas_NLFC(request): 
    
    partidos_filtrados = NLF_Colegial.objects.exclude(ganador__isnull=True).exclude(resultado__isnull=True)
    partidos = partidos_filtrados.order_by('-fecha')[:20]
    
    
    #Sistema A
    
    ganador=''
    cont_A_ML=0
    cont_A_SP=0
    cont_A_Ud=0
    cont_A_SB=0
    cont_A_MA=0
    cont_A_BB=0
    cont_A_Total=0
    A_cont=0
    A_cont1=0
    A_cont2=0
    A_cont3=0
    A_cont4=0
    A_cont5=0
    A_cont6=0
    sum=0
    res=0
    valor_izquierdo=0
    valor_derecho=0
    A_prom=0
    A_prom1=0
    A_prom2=0
    A_prom3=0
    A_prom4=0 
    A_prom5=0
    A_prom6=0
    
    for valor in partidos: 
        
        ganador=valor.ganador
        
        valor_izquierdo, valor_derecho = extraer_valores_de_resultado(valor)
        sum= valor_izquierdo+valor_derecho
        
        if valor.A_ML_equip is not None:
           A_cont+=1
           if ganador==valor.A_ML_equip.nombre:
              cont_A_ML+=1 
              
              
        if valor.A_Ud_equip is not None:
           A_cont1+=1      
           if ganador==valor.A_Ud_equip.nombre:
              cont_A_Ud+=1
              
              
        if valor.A_SB_equip is not None: 
           A_cont2+=1      
           if ganador==valor.A_SB_equip.nombre:
              cont_A_SB+=1
              
              
        if valor.A_MA is not None:
           A_cont3+=1 
           if ganador==valor.A_MA.nombre:
              cont_A_MA+=1
              
              
        if valor.A_BB is not None:  
           A_cont4+=1 
           if ganador==valor.A_BB.nombre:
              cont_A_BB+=1
         
         
        if valor.A_total_punto is not None: 
           A_cont5+=1 
           if sum>valor.A_total_punto and valor.A_Total_OU=='OVER':
              cont_A_Total+=1
           if sum<=valor.A_total_punto and valor.A_Total_OU=='UNDER':
              cont_A_Total+=1
         
         
       
        if valor_izquierdo>valor_derecho:
            res=valor_izquierdo-valor_derecho
           
        elif valor_izquierdo<valor_derecho:
            res=valor_derecho-valor_izquierdo 
        
        else: 
            res=0
        
        if valor.A_SP_dif is not None:
           A_cont6+=1
           if ganador==valor.A_SP_equip.nombre and res>valor.A_SP_dif :
              cont_A_SP+=1
           
           
           
    if cont_A_ML !=0 and A_cont !=0:
           A_prom=cont_A_ML*100/A_cont
        
    if cont_A_SP !=0 and A_cont6 !=0:
           A_prom6=cont_A_SP*100/A_cont6
           
    if cont_A_Ud !=0 and A_cont1 !=0:
           A_prom1=cont_A_Ud*100/A_cont1
           
    if cont_A_SB !=0 and A_cont2 !=0:
           A_prom2=cont_A_SB*100/A_cont2
           
    if cont_A_MA !=0 and A_cont3 !=0:
           A_prom3=cont_A_MA*100/A_cont3
           
    if cont_A_BB !=0 and A_cont4 !=0:
           A_prom4=cont_A_BB*100/A_cont5
           
    if cont_A_Total !=0 and A_cont5 !=0:
           A_prom5=cont_A_Total*100/A_cont5      
           
           
           
    #Sistema B     
    
    B_ganador=''
    cont_B_ML=0
    cont_B_SP=0
    cont_B_Ud=0
    cont_B_SB=0
    cont_B_MA=0
    cont_B_BB=0
    cont_B_Total=0
    B_cont=0
    B_cont1=0
    B_cont2=0
    B_cont3=0
    B_cont4=0
    B_cont5=0
    B_cont6=0
    B_sum=0
    B_res=0
    B_valor_izquierdo=0
    B_valor_derecho=0
    B_prom=0
    B_prom1=0
    B_prom2=0
    B_prom3=0
    B_prom4=0 
    B_prom5=0
    B_prom6=0
    
    for valor in partidos: 
        
        B_ganador=valor.ganador
        
        B_valor_izquierdo, B_valor_derecho = extraer_valores_de_resultado(valor)
        B_sum= B_valor_izquierdo+B_valor_derecho
        
        if valor.B_ML_equip is not None:
           B_cont+=1
           if B_ganador==valor.B_ML_equip.nombre:
              cont_B_ML+=1 
              
              
        if valor.B_Ud_equip is not None:
           B_cont1+=1      
           if B_ganador==valor.B_Ud_equip.nombre:
              cont_B_Ud+=1
              
              
        if valor.B_SB_equip is not None: 
           B_cont2+=1      
           if B_ganador==valor.B_SB_equip.nombre:
              cont_B_SB+=1
              
              
        if valor.B_MA is not None:
           B_cont3+=1 
           if B_ganador==valor.B_MA.nombre:
              cont_B_MA+=1
              
              
        if valor.B_BB is not None:  
           B_cont4+=1 
           if B_ganador==valor.B_BB.nombre:
              cont_B_BB+=1
         
         
        if valor.B_total_punto is not None: 
           B_cont5+=1 
           if B_sum>valor.B_total_punto and valor.B_Total_OU=='OVER':
              cont_B_Total+=1
           if B_sum<=valor.B_total_punto and valor.B_Total_OU=='UNDER':
              cont_B_Total+=1
         
         
       
        if B_valor_izquierdo>B_valor_derecho:
            B_res=B_valor_izquierdo-B_valor_derecho
           
        elif B_valor_izquierdo<B_valor_derecho:
            B_res=B_valor_derecho-B_valor_izquierdo 
        
        else: 
            B_res=0
        
        if valor.B_SP_dif is not None:
           B_cont6+=1
           if B_ganador==valor.B_SP_equip.nombre and B_res>valor.B_SP_dif :
              cont_B_SP+=1
           
           
           
    if cont_B_ML !=0 and B_cont !=0:
           B_prom=cont_B_ML*100/B_cont
        
    if cont_B_SP !=0 and B_cont6 !=0:
           B_prom6=cont_B_SP*100/B_cont6
           
    if cont_B_Ud !=0 and B_cont1 !=0:
           B_prom1=cont_B_Ud*100/B_cont1
           
    if cont_B_SB !=0 and B_cont2 !=0:
           B_prom2=cont_B_SB*100/B_cont2
           
    if cont_B_MA !=0 and B_cont3 !=0:
           B_prom3=cont_B_MA*100/B_cont3
           
    if cont_B_BB !=0 and B_cont4 !=0:
           B_prom4=cont_B_BB*100/B_cont5
           
    if cont_B_Total !=0 and B_cont5 !=0:
           B_prom5=cont_B_Total*100/B_cont5             
           
           
    C_ganador=''
    cont_C_ML=0
    cont_C_SP=0
    cont_C_Ud=0
    cont_C_SB=0
    cont_C_MA=0
    cont_C_BB=0
    cont_C_Total=0
    C_cont=0
    C_cont1=0
    C_cont2=0
    C_cont3=0
    C_cont4=0
    C_cont5=0
    C_cont6=0
    C_sum=0
    C_res=0
    C_valor_izquierdo=0
    C_valor_derecho=0
    C_prom=0
    C_prom1=0
    C_prom2=0
    C_prom3=0
    C_prom4=0 
    C_prom5=0        
    C_prom6=0
       
    for valor in partidos: 
        
        C_ganador=valor.ganador
            
        C_valor_izquierdo, C_valor_derecho = extraer_valores_de_resultado(valor)
        C_sum= C_valor_izquierdo+C_valor_derecho
            
        if valor.C_ML_equip is not None:
            C_cont+=1
            if C_ganador==valor.C_ML_equip.nombre:
                cont_C_ML+=1 
                
        if valor.C_Ud_equip is not None:
            C_cont1+=1      
            if C_ganador==valor.C_Ud_equip.nombre:
                cont_C_Ud+=1
                
        if valor.C_SB_equip is not None: 
            C_cont2+=1      
            if C_ganador==valor.C_SB_equip.nombre:
                cont_C_SB+=1
                
        if valor.C_MA is not None:
            C_cont3+=1 
            if C_ganador==valor.C_MA.nombre:
                cont_C_MA+=1
                
        if valor.C_BB is not None:  
            C_cont4+=1 
            if C_ganador==valor.C_BB.nombre:
                cont_C_BB+=1
            
            
        if valor.C_total_punto is not None: 
            C_cont5+=1 
            if C_sum>valor.C_total_punto and valor.C_Total_OU=='OVER':
                cont_C_Total+=1
            if C_sum<=valor.C_total_punto and valor.C_Total_OU=='UNDER':
                cont_C_Total+=1
            
            

        if C_valor_izquierdo>C_valor_derecho:
            C_res=C_valor_izquierdo-C_valor_derecho
            
        elif C_valor_izquierdo<C_valor_derecho:
            C_res=C_valor_derecho-C_valor_izquierdo 

        else: 
            C_res=0
            
        if valor.C_SP_dif is not None:
            C_cont6+=1
            if C_ganador==valor.C_SP_equip.nombre and C_res>valor.C_SP_dif :
                cont_C_SP+=1
           
           
    if cont_C_ML !=0 and C_cont !=0:
       C_prom=cont_C_ML*100/C_cont
            
    if cont_C_SP !=0 and C_cont6 !=0:
       C_prom6=cont_C_SP*100/C_cont6
            
    if cont_C_Ud !=0 and C_cont1 !=0:
       C_prom1=cont_C_Ud*100/C_cont1
            
    if cont_C_SB !=0 and C_cont2 !=0:
       C_prom2=cont_C_SB*100/C_cont2
            
    if cont_C_MA !=0 and C_cont3 !=0:
       C_prom3=cont_C_MA*100/C_cont3
            
    if cont_C_BB !=0 and C_cont4 !=0:
       C_prom4=cont_C_BB*100/C_cont5
            
    if cont_C_Total !=0 and C_cont5 !=0:
       C_prom5=cont_C_Total*100/C_cont5       
           
    
    
    D_ganador=''
    cont_D_ML=0
    cont_D_SP=0
    cont_D_Ud=0
    cont_D_SB=0
    cont_D_MA=0
    cont_D_BB=0
    cont_D_Total=0
    D_cont=0
    D_cont1=0
    D_cont2=0
    D_cont3=0
    D_cont4=0
    D_cont5=0
    D_cont6=0
    D_sum=0
    D_res=0
    D_valor_izquierdo=0
    D_valor_derecho=0
    D_prom=0
    D_prom1=0
    D_prom2=0
    D_prom3=0
    D_prom4=0 
    D_prom5=0        
    D_prom6=0

    
    
    
    for valor in partidos: 
        
        D_ganador=valor.ganador
            
        D_valor_izquierdo, D_valor_derecho = extraer_valores_de_resultado(valor)
        D_sum= D_valor_izquierdo+D_valor_derecho
            
        if valor.D_ML_equip is not None:
           D_cont+=1
           if D_ganador==valor.D_ML_equip.nombre:
              cont_D_ML+=1 
            
        if valor.D_Ud_equip is not None:
           D_cont1+=1      
           if D_ganador==valor.D_Ud_equip.nombre:
              cont_D_Ud+=1
            
        if valor.D_SB_equip is not None: 
           D_cont2+=1      
           if D_ganador==valor.D_SB_equip.nombre:
              cont_D_SB+=1
            
        if valor.D_MA is not None:
           D_cont3+=1 
           if D_ganador==valor.D_MA.nombre:
              cont_D_MA+=1
            
        if valor.D_BB is not None:  
           D_cont4+=1 
           if D_ganador==valor.D_BB.nombre:
              cont_D_BB+=1
        
        
        if valor.D_total_punto is not None: 
           D_cont5+=1 
           if D_sum>valor.D_total_punto and valor.D_Total_OU=='OVER':
              cont_D_Total+=1
           if D_sum<=valor.D_total_punto and valor.D_Total_OU=='UNDER':
              cont_D_Total+=1
        
        
    
        if D_valor_izquierdo>D_valor_derecho:
            D_res=D_valor_izquierdo-D_valor_derecho
        
        elif D_valor_izquierdo<D_valor_derecho:
            D_res=D_valor_derecho-D_valor_izquierdo 
        
        else: 
            D_res=0
            
        if valor.D_SP_dif is not None:
           D_cont6+=1
           if D_ganador==valor.D_SP_equip.nombre and D_res>valor.D_SP_dif :
              cont_D_SP+=1
             
           
    if cont_D_ML !=0 and D_cont !=0:
       D_prom=cont_D_ML*100/D_cont
            
    if cont_D_SP !=0 and D_cont6 !=0:
       D_prom6=cont_D_SP*100/D_cont6
            
    if cont_D_Ud !=0 and D_cont1 !=0:
       D_prom1=cont_D_Ud*100/D_cont1
            
    if cont_D_SB !=0 and D_cont2 !=0:
       D_prom2=cont_D_SB*100/D_cont2
            
    if cont_D_MA !=0 and D_cont3 !=0:
       D_prom3=cont_D_MA*100/D_cont3
            
    if cont_D_BB !=0 and D_cont4 !=0:
       D_prom4=cont_D_BB*100/D_cont5
            
    if cont_D_Total !=0 and D_cont5 !=0:
       D_prom5=cont_D_Total*100/D_cont5
        
    
    E_ganador=''
    cont_E_ML=0
    cont_E_SP=0
    cont_E_Ud=0
    cont_E_SB=0
    cont_E_MA=0
    cont_E_BB=0
    cont_E_Total=0
    E_cont=0
    E_cont1=0
    E_cont2=0
    E_cont3=0
    E_cont4=0
    E_cont5=0
    E_cont6=0
    E_sum=0
    E_res=0
    E_valor_izquierdo=0
    E_valor_derecho=0
    E_prom=0
    E_prom1=0
    E_prom2=0
    E_prom3=0
    E_prom4=0 
    E_prom5=0        
    E_prom6=0
       
    for valor in partidos: 
        
        E_ganador=valor.ganador
            
        E_valor_izquierdo, E_valor_derecho = extraer_valores_de_resultado(valor)
        E_sum= E_valor_izquierdo+E_valor_derecho
            
        if valor.E_ML_equip is not None:
           E_cont+=1
           if E_ganador==valor.E_ML_equip.nombre:
              cont_E_ML+=1 
            
        if valor.E_Ud_equip is not None:
           E_cont1+=1      
           if E_ganador==valor.E_Ud_equip.nombre:
              cont_E_Ud+=1
            
        if valor.E_SB_equip is not None: 
           E_cont2+=1      
           if E_ganador==valor.E_SB_equip.nombre:
              cont_E_SB+=1
            
        if valor.E_MA is not None:
           E_cont3+=1 
           if E_ganador==valor.E_MA.nombre:
              cont_E_MA+=1
            
        if valor.E_BB is not None:  
           E_cont4+=1 
           if E_ganador==valor.E_BB.nombre:
              cont_E_BB+=1
        
        
        if valor.E_total_punto is not None: 
           E_cont5+=1 
           if E_sum>valor.E_total_punto and valor.E_Total_OU=='OVER':
              cont_E_Total+=1
           if E_sum<=valor.E_total_punto and valor.E_Total_OU=='UNDER':
              cont_E_Total+=1
        
        
    
        if E_valor_izquierdo>E_valor_derecho:
            E_res=E_valor_izquierdo-E_valor_derecho
        
        elif E_valor_izquierdo<E_valor_derecho:
            E_res=E_valor_derecho-E_valor_izquierdo 
        
        else: 
            E_res=0
            
        if valor.E_SP_dif is not None:
           E_cont6+=1
           if E_ganador==valor.E_SP_equip.nombre and E_res>valor.E_SP_dif :
              cont_E_SP+=1
            
           
    if cont_E_ML !=0 and E_cont !=0:
       E_prom=cont_E_ML*100/E_cont
            
    if cont_E_SP !=0 and E_cont6 !=0:
       E_prom6=cont_E_SP*100/E_cont6
            
    if cont_E_Ud !=0 and E_cont1 !=0:
       E_prom1=cont_E_Ud*100/E_cont1   
        
    if cont_E_SB !=0 and E_cont2 !=0:
       E_prom2=cont_E_SB*100/E_cont2
            
    if cont_E_MA !=0 and E_cont3 !=0:
       E_prom3=cont_E_MA*100/E_cont3
            
    if cont_E_BB !=0 and E_cont4 !=0:
       E_prom4=cont_E_BB*100/E_cont5
            
    if cont_E_Total !=0 and E_cont5 !=0:
       E_prom5=cont_E_Total*100/E_cont5     
    
    
    
    
    F_ganador=''
    cont_F_ML=0
    cont_F_SP=0
    cont_F_Ud=0
    cont_F_SB=0
    cont_F_MA=0
    cont_F_BB=0
    cont_F_Total=0
    F_cont=0
    F_cont1=0
    F_cont2=0
    F_cont3=0
    F_cont4=0
    F_cont5=0
    F_cont6=0
    F_sum=0
    F_res=0
    F_valor_izquierdo=0
    F_valor_derecho=0
    F_prom=0
    F_prom1=0
    F_prom2=0
    F_prom3=0
    F_prom4=0 
    F_prom5=0        
    F_prom6=0
       
    
    for valor in partidos: 
        
 
        F_valor_izquierdo, F_valor_derecho = extraer_valores_de_resultado(valor)
        F_sum = F_valor_izquierdo + F_valor_derecho
                
        if valor.F_ML_equip is not None:
           F_cont+=1
           if F_ganador==valor.F_ML_equip.nombre:
              F_cont_ML+=1 
                
        if valor.F_Ud_equip is not None:
           F_cont1+=1      
           if F_ganador==valor.F_Ud_equip.nombre:
              F_cont_Ud+=1
                
        if valor.F_SB_equip is not None: 
           F_cont2+=1      
           if F_ganador==valor.F_SB_equip.nombre:
              F_cont_SB+=1
                
        if valor.F_MA is not None:
           F_cont3+=1 
           if F_ganador==valor.F_MA.nombre:
              F_cont_MA+=1
                
        if valor.F_BB is not None:  
           F_cont4+=1 
           if F_ganador==valor.F_BB.nombre:
              F_cont_BB+=1
            
            
        if valor.F_total_punto is not None: 
           F_cont5+=1 
           if F_sum>F_valor_izquierdo and valor.F_Total_OU=='OVER':
              F_cont_Total+=1
           if F_sum<=valor.F_total_punto and valor.F_Total_OU=='UNDER':
              F_cont_Total+=1
            
            
        if F_valor_izquierdo>F_valor_derecho:
            F_res=F_valor_izquierdo-F_valor_derecho
            
        elif F_valor_izquierdo<F_valor_derecho:
            F_res=F_valor_derecho-F_valor_izquierdo 
        
        else: 
            F_res=0
                
        if valor.F_SP_dif is not None:
           F_cont6+=1
           if F_ganador==valor.F_SP_equip.nombre and F_res>valor.F_SP_dif :
              F_cont_SP+=1
            
           
    if cont_F_ML !=0 and F_cont !=0:
       F_prom=F_cont_ML*100/F_cont
                
    if cont_F_SP !=0 and F_cont6 !=0:
       F_prom6=F_cont_SP*100/F_cont6
                
    if cont_F_Ud !=0 and F_cont1 !=0:
       F_prom1=F_cont_Ud*100/F_cont1   
            
    if cont_F_SB !=0 and F_cont2 !=0:
       F_prom2=F_cont_SB*100/F_cont2
                
    if cont_F_MA !=0 and F_cont3 !=0:
       F_prom3=F_cont_MA*100/F_cont3
                
    if cont_F_BB !=0 and F_cont4 !=0:
       F_prom4=F_cont_BB*100/F_cont5
                
    if cont_F_Total !=0 and F_cont5 !=0:
       F_prom5=F_cont_Total*100/F_cont5
        
    
    G_ganador=''
    cont_G_ML=0
    cont_G_SP=0
    cont_G_Ud=0
    cont_G_SB=0
    cont_G_MA=0
    cont_G_BB=0
    cont_G_Total=0
    G_cont=0
    G_cont1=0
    G_cont2=0
    G_cont3=0
    G_cont4=0
    G_cont5=0
    G_cont6=0
    G_sum=0
    G_res=0
    G_valor_izquierdo=0
    G_valor_derecho=0
    G_prom=0
    G_prom1=0
    G_prom2=0
    G_prom3=0
    G_prom4=0 
    G_prom5=0        
    G_prom6=0

    for valor in partidos: 
        
        G_valor_izquierdo, G_valor_derecho = extraer_valores_de_resultado(valor)
        G_sum = G_valor_izquierdo + G_valor_derecho
                    
        if valor.G_ML_equip is not None:
           G_cont+=1
           if G_ganador==valor.G_ML_equip.nombre:
              G_cont_ML+=1 
                    
        if valor.G_Ud_equip is not None:
           G_cont1+=1      
           if G_ganador==valor.G_Ud_equip.nombre:
              G_cont_Ud+=1
                    
        if valor.G_SB_equip is not None: 
           G_cont2+=1      
           if G_ganador==valor.G_SB_equip.nombre:
              G_cont_SB+=1
                    
        if valor.G_MA is not None:
           G_cont3+=1 
           if G_ganador==valor.G_MA.nombre:
              G_cont_MA+=1
                    
        if valor.G_BB is not None:  
           G_cont4+=1 
           if G_ganador==valor.G_BB.nombre:
              G_cont_BB+=1
                
                
        if valor.G_total_punto is not None: 
           G_cont5+=1 
           if G_sum>G_valor_izquierdo and valor.G_Total_OU=='OVER':
              G_cont_Total+=1
           if G_sum<=valor.G_total_punto and valor.G_Total_OU=='UNDER':
              G_cont_Total+=1
                
                
        if G_valor_izquierdo>G_valor_derecho:
            G_res=G_valor_izquierdo-G_valor_derecho
                
        elif G_valor_izquierdo<G_valor_derecho:
            G_res=G_valor_derecho-G_valor_izquierdo 
            
        else: 
            G_res=0
                    
        if valor.G_SP_dif is not None:
           G_cont6+=1
           if G_ganador==valor.G_SP_equip.nombre and G_res>valor.G_SP_dif :
              G_cont_SP+=1
            
           
    if cont_G_ML !=0 and G_cont !=0:
       G_prom=G_cont_ML*100/G_cont
                    
    if cont_G_SP !=0 and G_cont6 !=0:
       G_prom6=G_cont_SP*100/G_cont6
                    
    if cont_G_Ud !=0 and G_cont1 !=0:
       G_prom1=G_cont_Ud*100/G_cont1   
                
    if cont_G_SB !=0 and G_cont2 !=0:
       G_prom2=G_cont_SB*100/G_cont2
                    
    if cont_G_MA !=0 and G_cont3 !=0:
       G_prom3=G_cont_MA*100/G_cont3
                    
    if cont_G_BB !=0 and G_cont4 !=0:
       G_prom4=G_cont_BB*100/G_cont5
                    
    if cont_G_Total !=0 and G_cont5 !=0:
       G_prom5=G_cont_Total*100/G_cont5
            
            
            
    H_ganador=''
    cont_H_ML=0
    cont_H_SP=0
    cont_H_Ud=0
    cont_H_SB=0
    cont_H_MA=0
    cont_H_BB=0
    cont_H_Total=0
    H_cont=0
    H_cont1=0
    H_cont2=0
    H_cont3=0
    H_cont4=0
    H_cont5=0
    H_cont6=0
    H_sum=0
    H_res=0
    H_valor_izquierdo=0
    H_valor_derecho=0
    H_prom=0
    H_prom1=0
    H_prom2=0
    H_prom3=0
    H_prom4=0 
    H_prom5=0        
    H_prom6=0
        
            
    for valor in partidos: 
        
        H_valor_izquierdo, H_valor_derecho = extraer_valores_de_resultado(valor)
        H_sum = H_valor_izquierdo + H_valor_derecho
                        
        if valor.H_ML_equip is not None:
           H_cont+=1
           if H_ganador==valor.H_ML_equip.nombre:
              H_cont_ML+=1 
                        
        if valor.H_Ud_equip is not None:
           H_cont1+=1      
           if H_ganador==valor.H_Ud_equip.nombre:
              H_cont_Ud+=1
                        
        if valor.H_SB_equip is not None: 
           H_cont2+=1      
           if H_ganador==valor.H_SB_equip.nombre:
              H_cont_SB+=1
                        
        if valor.H_MA is not None:
           H_cont3+=1 
           if H_ganador==valor.H_MA.nombre:
              H_cont_MA+=1
                        
        if valor.H_BB is not None:  
           H_cont4+=1 
           if H_ganador==valor.H_BB.nombre:
              H_cont_BB+=1
                    
                    
        if valor.H_total_punto is not None: 
           H_cont5+=1 
           if H_sum>H_valor_izquierdo and valor.H_Total_OU=='OVER':
              H_cont_Total+=1
           if H_sum<=valor.H_total_punto and valor.H_Total_OU=='UNDER':
              H_cont_Total+=1
                    
                    
        if H_valor_izquierdo>H_valor_derecho:
                H_res=H_valor_izquierdo-H_valor_derecho
                    
        elif H_valor_izquierdo<H_valor_derecho:
                H_res=H_valor_derecho-H_valor_izquierdo 
                
        else: 
                H_res=0
                        
        if valor.H_SP_dif is not None:
           H_cont6+=1
           if H_ganador==valor.H_SP_equip.nombre and H_res>valor.H_SP_dif :
              H_cont_SP+=1
            
           
    if cont_H_ML !=0 and H_cont !=0:
       H_prom=H_cont_ML*100/H_cont
                    
    if cont_H_SP !=0 and H_cont6 !=0:
       H_prom6=H_cont_SP*100/H_cont6
                    
    if cont_H_Ud !=0 and H_cont1 !=0:
       H_prom1=H_cont_Ud*100/H_cont1   
                
    if cont_H_SB !=0 and H_cont2 !=0:
       H_prom2=H_cont_SB*100/H_cont2
                    
    if cont_H_MA !=0 and H_cont3 !=0:
       H_prom3=H_cont_MA*100/H_cont3
                    
    if cont_H_BB !=0 and H_cont4 !=0:
       H_prom4=H_cont_BB*100/H_cont5
                    
    if cont_H_Total !=0 and H_cont5 !=0:
       H_prom5=H_cont_Total*100/H_cont5        
            
    
    
    I_ganador=''
    cont_I_ML=0
    cont_I_SP=0
    cont_I_Ud=0
    cont_I_SB=0
    cont_I_MA=0
    cont_I_BB=0
    cont_I_Total=0
    I_cont=0
    I_cont1=0
    I_cont2=0
    I_cont3=0
    I_cont4=0
    I_cont5=0
    I_cont6=0
    I_sum=0
    I_res=0
    I_valor_izquierdo=0
    I_valor_derecho=0
    I_prom=0
    I_prom1=0
    I_prom2=0
    I_prom3=0
    I_prom4=0 
    I_prom5=0        
    I_prom6=0
        
            
    for valor in partidos: 
        
        I_valor_izquierdo, I_valor_derecho = extraer_valores_de_resultado(valor)
        I_sum = I_valor_izquierdo + I_valor_derecho
                        
        if valor.I_ML_equip is not None:
           I_cont+=1
           if I_ganador==valor.I_ML_equip.nombre:
              I_cont_ML+=1 
                        
        if valor.I_Ud_equip is not None:
           I_cont1+=1      
           if I_ganador==valor.I_Ud_equip.nombre:
              I_cont_Ud+=1
                        
        if valor.I_SB_equip is not None: 
           I_cont2+=1      
           if I_ganador==valor.I_SB_equip.nombre:
              I_cont_SB+=1
                        
        if valor.I_MA is not None:
           I_cont3+=1 
           if I_ganador==valor.I_MA.nombre:
              I_cont_MA+=1
                        
        if valor.I_BB is not None:  
           I_cont4+=1 
           if I_ganador==valor.I_BB.nombre:
              I_cont_BB+=1
                    
                    
        if valor.I_total_punto is not None: 
           I_cont5+=1 
           if I_sum>I_valor_izquierdo and valor.I_Total_OU=='OVER':
              I_cont_Total+=1
           if I_sum<=valor.I_total_punto and valor.I_Total_OU=='UNDER':
              I_cont_Total+=1
                    
                    
        if I_valor_izquierdo>I_valor_derecho:
                I_res=I_valor_izquierdo-I_valor_derecho
                    
        elif I_valor_izquierdo<I_valor_derecho:
                I_res=I_valor_derecho-I_valor_izquierdo 
                
        else: 
                I_res=0
                        
        if valor.I_SP_dif is not None:
           I_cont6+=1
           if I_ganador==valor.I_SP_equip.nombre and I_res>valor.I_SP_dif :
              I_cont_SP+=1
            
           
    if cont_I_ML !=0 and I_cont !=0:
       I_prom=I_cont_ML*100/I_cont
                        
    if cont_I_SP !=0 and I_cont6 !=0:
       I_prom6=I_cont_SP*100/I_cont6
                        
    if cont_I_Ud !=0 and I_cont1 !=0:
       I_prom1=I_cont_Ud*100/I_cont1   
                    
    if cont_I_SB !=0 and I_cont2 !=0:
       I_prom2=I_cont_SB*100/I_cont2
                        
    if cont_I_MA !=0 and I_cont3 !=0:
       I_prom3=I_cont_MA*100/I_cont3
                        
    if cont_I_BB !=0 and I_cont4 !=0:
       I_prom4=I_cont_BB*100/I_cont5
                        
    if cont_I_Total !=0 and I_cont5 !=0:
       I_prom5=I_cont_Total*100/I_cont5        
            
            
    J_ganador=''
    cont_J_ML=0
    cont_J_SP=0
    cont_J_Ud=0
    cont_J_SB=0
    cont_J_MA=0
    cont_J_BB=0
    cont_J_Total=0
    J_cont=0
    J_cont1=0
    J_cont2=0
    J_cont3=0
    J_cont4=0
    J_cont5=0
    J_cont6=0
    J_sum=0
    J_res=0
    J_valor_izquierdo=0
    J_valor_derecho=0
    J_prom=0
    J_prom1=0
    J_prom2=0
    J_prom3=0
    J_prom4=0 
    J_prom5=0        
    J_prom6=0
        
    for valor in partidos: 
        
        J_valor_izquierdo, J_valor_derecho = extraer_valores_de_resultado(valor)
        J_sum = J_valor_izquierdo + J_valor_derecho
                            
        if valor.J_ML_equip is not None:
           J_cont+=1
           if J_ganador==valor.J_ML_equip.nombre:
              J_cont_ML+=1 
                            
        if valor.J_Ud_equip is not None:
           J_cont1+=1      
           if J_ganador==valor.J_Ud_equip.nombre:
              J_cont_Ud+=1
                            
        if valor.J_SB_equip is not None: 
           J_cont2+=1      
           if J_ganador==valor.J_SB_equip.nombre:
              J_cont_SB+=1
                            
        if valor.J_MA is not None:
           J_cont3+=1 
           if J_ganador==valor.J_MA.nombre:
              J_cont_MA+=1
                            
        if valor.J_BB is not None:  
           J_cont4+=1 
           if J_ganador==valor.J_BB.nombre:
              J_cont_BB+=1
                        
                        
        if valor.J_total_punto is not None: 
           J_cont5+=1 
           if J_sum>J_valor_izquierdo and valor.J_Total_OU=='OVER':
              J_cont_Total+=1
           if J_sum<=valor.J_total_punto and valor.J_Total_OU=='UNDER':
              J_cont_Total+=1
                        
                        
        if J_valor_izquierdo>J_valor_derecho:
                J_res=J_valor_izquierdo-J_valor_derecho
                        
        elif J_valor_izquierdo<J_valor_derecho:
                J_res=J_valor_derecho-J_valor_izquierdo 
                    
        else: 
                J_res=0
                            
        if valor.J_SP_dif is not None:
           J_cont6+=1
           if J_ganador==valor.J_SP_equip.nombre and J_res>valor.J_SP_dif :
              J_cont_SP+=1
            
           
    if cont_J_ML !=0 and J_cont !=0:
       J_prom=J_cont_ML*100/J_cont
                            
    if cont_J_SP !=0 and J_cont6 !=0:
       J_prom6=J_cont_SP*100/J_cont6
                            
    if cont_J_Ud !=0 and J_cont1 !=0:
       J_prom1=J_cont_Ud*100/J_cont1   
                        
    if cont_J_SB !=0 and J_cont2 !=0:
       J_prom2=J_cont_SB*100/J_cont2
                            
    if cont_J_MA !=0 and J_cont3 !=0:
       J_prom3=J_cont_MA*100/J_cont3
                            
    if cont_J_BB !=0 and J_cont4 !=0:
       J_prom4=J_cont_BB*100/J_cont5
                            
    if cont_J_Total !=0 and J_cont5 !=0:
       J_prom5=J_cont_Total*100/J_cont5      
       
       
    mejor_prom_ML=0
    mejor_prom_SP=0
    mejor_prom_T=0
    mejor_prom_Ud=0
    mejor_prom_SB=0
    mejor_prom_MA=0     
    mejor_prom_BB=0
    nombre_s=0
    nombre_s1=0
    nombre_s2=0
    nombre_s3=0
    nombre_s4=0
    nombre_s5=0
    nombre_s6=0
    
    
    list_ML=[A_prom,B_prom,C_prom,D_prom,E_prom,F_prom,G_prom,H_prom,I_prom,J_prom]
    list_SP=[A_prom6,B_prom6,C_prom6,D_prom6,E_prom6,F_prom6,G_prom6,H_prom6,I_prom6,J_prom6]
    list_T=[A_prom5,B_prom5,C_prom5,D_prom5,E_prom5,F_prom5,G_prom5,H_prom5,I_prom5,J_prom5]
    list_Ud=[A_prom1,B_prom1,C_prom1,D_prom1,E_prom1,F_prom1,G_prom1,H_prom1,I_prom1,J_prom1]     
    list_SB=[A_prom2,B_prom2,C_prom2,D_prom2,E_prom2,F_prom2,G_prom2,H_prom2,I_prom2,J_prom2]
    list_MA=[A_prom3,B_prom3,C_prom3,D_prom3,E_prom3,F_prom3,G_prom3,H_prom3,I_prom3,J_prom3]
    list_BB=[A_prom4,B_prom4,C_prom4,D_prom4,E_prom4,F_prom4,G_prom4,H_prom4,I_prom4,J_prom4]
    
    lista_sistemas=['VeriBet','Action Network','Sports Insights','PFF','Covers','Team Rankings','BetQL','Odds Jams','Scores and Odds','Betting on Cash']
       
    for indice,i in enumerate(list_ML):
        if i>mejor_prom_ML:
           mejor_prom_ML=i   
           nombre_s=indice
           
        
    for indice,i in enumerate(list_SP):
        if i>mejor_prom_SP:
           mejor_prom_SP=i        
           nombre_s1=indice
            
    for indice,i in enumerate( list_T):
        if i>mejor_prom_T:
           mejor_prom_T=i         
           nombre_s2=indice
           
    for indice,i in enumerate(list_Ud):
        if i>mejor_prom_Ud:
           mejor_prom_Ud=i 
           nombre_s3=indice
           
    for indice,i in enumerate(list_SB):
        if i>mejor_prom_SB:
           mejor_prom_SB=i 
           nombre_s4=indice
           
    for indice,i in enumerate(list_MA):
        if i>mejor_prom_MA:
           mejor_prom_MA=i 
           nombre_s5=indice
           
    for indice,i in enumerate(list_BB):
        if i>mejor_prom_BB:
           mejor_prom_BB=i 
           nombre_s6=indice
           
           
           
           
           
    for indice,i in enumerate(lista_sistemas):
        if nombre_s==indice:
           nombre_s=i       
           break
              
    for indice,i in enumerate(lista_sistemas):
        if nombre_s1==indice:
           nombre_s1=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s2==indice:
           nombre_s2=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s3==indice:
           nombre_s3=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s4==indice:
           nombre_s4=i       
           break
    
    for indice,i in enumerate(lista_sistemas):
        if nombre_s5==indice:
           nombre_s5=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s6==indice:
           nombre_s6=i       
           break          
              
              
              
              
    return render(request,'NLF_Colegial/resultados_sistemas.html', {'cont_A_ML':cont_A_ML, 'cont_A_SP':cont_A_SP, 'cont_A_Ud':cont_A_Ud, 
                                                              'cont_A_MA':cont_A_MA,'cont_A_SB':cont_A_SB,'cont_A_BB':cont_A_BB,
                                                              'cont_A_Total':cont_A_Total,'A_cont':A_cont,'A_cont1':A_cont1,'A_cont2':A_cont2,
                                                              'A_cont3':A_cont3,'A_cont4':A_cont4,'A_cont5':A_cont5,'A_cont6':A_cont6, 
                                                              'A_prom':A_prom,'A_prom1':A_prom1,'A_prom2':A_prom2,'A_prom3':A_prom3,'A_prom4':A_prom4,
                                                              'A_prom5':A_prom5,'A_prom6':A_prom6,'cont_B_ML': cont_B_ML, 'cont_B_SP': cont_B_SP, 
                                                              'cont_B_Ud': cont_B_Ud, 'cont_B_MA': cont_B_MA, 'cont_B_SB': cont_B_SB, 'cont_B_BB': cont_B_BB,
                                                              'cont_B_Total': cont_B_Total, 'B_cont': B_cont, 'B_cont1': B_cont1, 'B_cont2': B_cont2,
                                                              'B_cont3': B_cont3, 'B_cont4': B_cont4, 'B_cont5': B_cont5, 'B_cont6': B_cont6, 'B_prom': B_prom,
                                                              'B_prom1': B_prom1, 'B_prom2': B_prom2, 'B_prom3': B_prom3, 'B_prom4': B_prom4, 'B_prom5': B_prom5, 
                                                              'B_prom6': B_prom6,'cont_C_ML': cont_C_ML, 'cont_C_SP': cont_C_SP, 'cont_C_Ud': cont_C_Ud, 
                                                              'cont_C_MA': cont_C_MA, 'cont_C_SB': cont_C_SB, 'cont_C_BB': cont_C_BB, 'cont_C_Total': cont_C_Total,
                                                              'C_cont': C_cont, 'C_cont1': C_cont1, 'C_cont2': C_cont2, 'C_cont3': C_cont3, 'C_cont4': C_cont4,
                                                              'C_cont5': C_cont5, 'C_cont6': C_cont6, 'C_prom': C_prom, 'C_prom1': C_prom1, 'C_prom2': C_prom2,
                                                              'C_prom3': C_prom3, 'C_prom4': C_prom4, 'C_prom5': C_prom5, 'C_prom6': C_prom6, 'cont_D_ML': cont_D_ML,
                                                              'cont_D_SP': cont_D_SP, 'cont_D_Ud': cont_D_Ud, 'cont_D_MA': cont_D_MA, 'cont_D_SB': cont_D_SB,
                                                              'cont_D_BB': cont_D_BB, 'cont_D_Total':cont_D_Total, 'D_cont': D_cont, 'D_cont1': D_cont1,
                                                              'D_cont2': D_cont2, 'D_cont3': D_cont3, 'D_cont4': D_cont4,'D_cont5': D_cont5, 'D_cont6': D_cont6,
                                                              'D_prom': D_prom, 'D_prom1': D_prom1, 'D_prom2': D_prom2,'D_prom3': D_prom3, 'D_prom4': D_prom4, 
                                                              'D_prom5': D_prom5, 'D_prom6': D_prom6, 'cont_E_ML': cont_E_ML, 'cont_E_SP': cont_E_SP, 
                                                              'cont_E_Ud': cont_E_Ud, 'cont_E_MA': cont_E_MA, 'cont_E_SB': cont_E_SB, 'cont_E_BB': cont_E_BB, 
                                                              'cont_E_Total': cont_E_Total,'E_cont': E_cont, 'E_cont1': E_cont1, 'E_cont2': E_cont2, 'E_cont3': E_cont3,
                                                              'E_cont4': E_cont4,'E_cont5': E_cont5, 'E_cont6': E_cont6, 'E_prom': E_prom, 'E_prom1': E_prom1, 
                                                              'E_prom2': E_prom2,'E_prom3': E_prom3, 'E_prom4': E_prom4, 'E_prom5': E_prom5, 'E_prom6': E_prom6,
                                                              'cont_F_ML': cont_F_ML, 'cont_F_SP': cont_F_SP, 'cont_F_Ud': cont_F_Ud, 'cont_F_MA': cont_F_MA, 
                                                              'cont_F_SB': cont_F_SB, 'cont_F_BB': cont_F_BB, 'cont_F_Total': cont_F_Total,'F_cont': F_cont, 
                                                              'F_cont1': F_cont1, 'F_cont2': F_cont2, 'F_cont3': F_cont3,'F_cont4': F_cont4,'F_cont5': F_cont5, 
                                                              'F_cont6': F_cont6, 'F_prom': F_prom, 'F_prom1': F_prom1, 'F_prom2': F_prom2,'F_prom3': F_prom3, 
                                                              'F_prom4': F_prom4, 'F_prom5': F_prom5, 'F_prom6': F_prom6,'cont_G_ML': cont_G_ML, 'cont_G_SP': cont_G_SP,
                                                              'cont_G_Ud': cont_G_Ud, 'cont_G_MA':cont_G_MA, 'cont_G_SB':cont_G_SB, 'cont_G_BB': cont_G_BB,
                                                              'cont_G_Total':cont_G_Total,'G_cont': G_cont, 'G_cont1': G_cont1, 'G_cont2': G_cont2, 'G_cont3': G_cont3,
                                                              'G_cont4': G_cont4,'G_cont5': G_cont5, 'G_cont6': G_cont6, 'G_prom': G_prom, 'G_prom1': G_prom1, 
                                                              'G_prom2': G_prom2,'G_prom3': G_prom3, 'G_prom4': G_prom4, 'G_prom5': G_prom5, 'G_prom6': G_prom6,
                                                              'cont_H_ML': cont_H_ML, 'cont_H_SP': cont_H_SP, 'cont_H_Ud': cont_H_Ud, 'cont_H_MA':cont_H_MA,
                                                              'cont_H_SB': cont_H_SB, 'cont_H_BB': cont_H_BB, 'cont_H_Total':cont_H_Total,'H_cont': H_cont,
                                                              'H_cont1': H_cont1, 'H_cont2': H_cont2, 'H_cont3': H_cont3,'H_cont4': H_cont4,'H_cont5': H_cont5,
                                                              'H_cont6': H_cont6, 'H_prom': H_prom, 'H_prom1': H_prom1, 'H_prom2': H_prom2,'H_prom3': H_prom3, 
                                                              'H_prom4': H_prom4, 'H_prom5': H_prom5, 'H_prom6': H_prom6,'cont_I_ML': cont_I_ML, 'cont_I_SP': cont_I_SP,
                                                              'cont_I_Ud': cont_I_Ud, 'cont_I_MA': cont_I_MA, 'cont_I_SB': cont_I_SB, 'cont_I_BB': cont_I_BB, 
                                                              'cont_I_Total': cont_I_Total,'I_cont': I_cont, 'I_cont1': I_cont1, 'I_cont2': I_cont2, 'I_cont3': I_cont3,
                                                              'I_cont4': I_cont4,'I_cont5': I_cont5, 'I_cont6': I_cont6, 'I_prom': I_prom, 'I_prom1': I_prom1,
                                                              'I_prom2': I_prom2,'I_prom3': I_prom3, 'I_prom4': I_prom4, 'I_prom5': I_prom5, 'I_prom6': I_prom6,
                                                              'cont_J_ML': cont_J_ML, 'cont_J_SP': cont_J_SP, 'cont_J_Ud': cont_J_Ud, 'cont_J_MA': cont_J_MA,
                                                              'cont_J_SB': cont_J_SB, 'cont_J_BB':cont_J_BB, 'cont_J_Total': cont_J_Total,'J_cont': J_cont, 
                                                              'J_cont1': J_cont1, 'J_cont2': J_cont2, 'J_cont3': J_cont3,'J_cont4': J_cont4,'J_cont5': J_cont5, 
                                                              'J_cont6': J_cont6, 'J_prom': J_prom, 'J_prom1': J_prom1, 'J_prom2': J_prom2,'J_prom3': J_prom3, 
                                                              'J_prom4': J_prom4, 'J_prom5': J_prom5, 'J_prom6': J_prom6,'nombre_s':nombre_s,'nombre_s1':nombre_s1,
                                                              'nombre_s2':nombre_s2,'nombre_s3':nombre_s3,'nombre_s4':nombre_s4,'nombre_s5':nombre_s5,'nombre_s6':nombre_s6,
                                                              'mejor_prom_ML':mejor_prom_ML,'mejor_prom_SP':mejor_prom_SP,'mejor_prom_T':mejor_prom_T,
                                                              'mejor_prom_Ud':mejor_prom_Ud,'mejor_prom_SB':mejor_prom_SB,'mejor_prom_MA':mejor_prom_MA,'mejor_prom_BB':mejor_prom_BB,  })
   


#NBA colegial

def Crear_NBAC(request):
    if request.method == 'POST':
        formulario = NBA_Colegial_form(request.POST)
        if formulario.is_valid():
            formulario.clean()
            objeto_creado = formulario.save()
            
          
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NBA_Colegial.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NBA_Colegial.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NBA_Colegial.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NBA_Colegial.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NBA_Colegial/informes.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,  'formulario':formulario, 'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })
       
        else:
            return render(request, 'NBA_Colegial/crear_NBA_colegial.html', {'formulario': formulario})
    else:
        formulario = NBA_Colegial_form()
        return render(request, 'NBA_Colegial/crear_NBA_colegial.html', {'formulario': formulario})

def Listar_NBAC(request):
    lista =NBA_Colegial.objects.all().order_by('fecha')
    return render(request, 'NBA_Colegial/listar_NBA_colegial.html', {'lista':lista} )

def Eliminar_NBAC(request, id):
    f = get_object_or_404(NBA_Colegial, id=id)
    f.delete()
    return redirect('listar_NBA_colegial')

def Buscar_NBAC(request):
    resultados = []
    if request.method == 'POST':
        termino_busqueda = request.POST.get('searchbar')
        
        if termino_busqueda:
            # Construye condiciones para buscar en el nombre del equipo local o visitante
            condiciones = (
                Q(equipo_local__nombre__icontains=termino_busqueda) |
                Q(equipo_visitante__nombre__icontains=termino_busqueda)
            )
            
            # Filtra los resultados basándose en las condiciones construidas
            resultados = NBA_Colegial.objects.filter(condiciones)
        

        return render(request, 'NBA_Colegial/resultados.html', {'resultados': resultados})
    return render(request, 'NBA_Colegial/listar_NBA_colegial.html')

def Resultado_NBAC(request, id):
    f = NBA_Colegial.objects.get(id=id)
    
    equipo_local = f.equipo_local.nombre
    equipo_visitante = f.equipo_visitante.nombre
    opciones_ganador = [ equipo_local,equipo_visitante,'Empate' ]
    
    if request.method == 'POST':
        form = resultado_NBA_Colegial_form(request.POST, instance=f)
        if form.is_valid():
            form.save()
            return redirect('listar_NBA_colegial')
    else:
        form = resultado_NBA_Colegial_form( instance=f)

    return render(request, 'NBA_Colegial/resultado_NBA_colegial.html', {'form': form,'opciones_ganador': opciones_ganador})

def Informe_Resultado_NBAC(request, id):
            objeto_creado = NBA_Colegial.objects.get(id=id)
    
    
   
            #nombre de equipos
            equipo_l=objeto_creado.equipo_local  
            equipo_v=objeto_creado.equipo_visitante 
            
            #logo de equipos
            equipo_ll=equipo_l.logo
            equipo_vl=equipo_v.logo
            
            
            #partidos jugados temporada
            partidos = NBA_Colegial.objects.all()
            c_j_l=0
            c_j_v=0
            
            
            for i in partidos:
                if i.equipo_local.nombre==equipo_l.nombre or i.equipo_visitante.nombre==equipo_l:
                   c_j_l=c_j_l+1 
                if i.equipo_visitante.nombre==equipo_v.nombre or i.equipo_local.nombre==equipo_v:
                   c_j_v=c_j_v+1 
            
            
            #partidos ganados temporada
            partidos = NBA_Colegial.objects.all()
            cont_l=0
            cont_v=0
            lista1 = []
            
            for o in partidos:
                if o.ganador is not None:
                  lista1.append(o.ganador) 
                
            for p in lista1:
                    
                if equipo_l.nombre==p:
                    cont_l=cont_l+1
                if equipo_v.nombre==p:
                    cont_v=cont_v+1
               
            #partidos ganados local
            cont_g_ll=0        
            cont_g_lv=0 
            cont_g_vl=0
            cont_g_vv=0
            
            for x in partidos:
                if x.ganador==equipo_l.nombre and x.equipo_local.nombre==equipo_l.nombre:
                    cont_g_ll+=1   
                if x.ganador==equipo_l.nombre and x.equipo_visitante.nombre==equipo_l.nombre:
                    cont_g_lv+=1 
                if x.ganador==equipo_v.nombre and x.equipo_local.nombre==equipo_v.nombre:
                    cont_g_vl+=1 
                if x.ganador==equipo_v.nombre and x.equipo_visitante.nombre==equipo_v.nombre:
                    cont_g_vv+=1    
                
            #ultimos 10 partidos equipo local  
            g_l=0
            p_l=0
            w=0
            objetos_con_ganador = NBA_Colegial.objects.exclude(ganador__isnull=True) 
            filtros_por_equipo = Q(equipo_local__nombre=equipo_l.nombre) | Q(equipo_visitante__nombre=equipo_l.nombre)
            objetos_filtrados = objetos_con_ganador.filter(filtros_por_equipo)
            objetos_ordenados= objetos_filtrados.order_by('-fecha')    
            ultimos_local = objetos_ordenados[:10]   
            for a in ultimos_local:
                w+=1
                if a.ganador==equipo_l.nombre:
                   g_l+=1           
            p_l=w-g_l    
                
            #ultimos 10 partidos equipo visitante    
            g_v=0
            p_v=0
            q=0    
            objetos_con_ganador_v = NBA_Profecional.objects.exclude(ganador__isnull=True)   
            filtros_por_equipo_v = Q(equipo_local__nombre=equipo_v.nombre) | Q(equipo_visitante__nombre=equipo_v.nombre)
            objetos_filtrados_v = objetos_con_ganador_v.filter(filtros_por_equipo_v)   
            objetos_ordenados_v= objetos_filtrados_v.order_by('-fecha')    
            ultimos_local_v = objetos_ordenados_v[:10]    
            for a in ultimos_local_v:
                q+=1
                if a.ganador==equipo_v.nombre:
                   g_v+=1           
            p_v=q-g_v
            
            
                
            #variables 
            
            #total probabilidad
            A_U = objeto_creado.A_Total_prob
            B_U = objeto_creado.B_Total_prob
            C_U = objeto_creado.C_Total_prob
            D_U = objeto_creado.D_Total_prob
            E_U = objeto_creado.E_Total_prob
            F_U = objeto_creado.F_Total_prob
            G_U = objeto_creado.G_Total_prob
            H_U = objeto_creado.H_Total_prob
            I_U = objeto_creado.I_Total_prob
            J_U = objeto_creado.J_Total_prob
            A_U1 = objeto_creado.A_Total_OU
            B_U1 = objeto_creado.B_Total_OU
            C_U1 = objeto_creado.C_Total_OU
            D_U1 = objeto_creado.D_Total_OU
            E_U1 = objeto_creado.E_Total_OU
            F_U1 = objeto_creado.F_Total_OU
            G_U1 = objeto_creado.G_Total_OU
            H_U1 = objeto_creado.H_Total_OU
            I_U1 = objeto_creado.I_Total_OU
            J_U1 = objeto_creado.J_Total_OU
            cont=0
            con=0
            N=0
            sum=0
            su=0
            prom_prob_total=0
            prom_prob_total1=0
            lis= []
            li=[]
            total=0
            total1=0
            total2=0
            under_over=''
            under_over1=''
            under_over2=''
            p_total=0
            p_total1=0
            p_total2=0
            d_total=0
            d_total1=0
            d_total2=0
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    lis.append(A_U)
                else:
                    li.append(A_U)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    lis.append(B_U)
                else:
                    li.append(B_U)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    lis.append(C_U)
                else:
                    li.append(C_U)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    lis.append(D_U)
                else:
                    li.append(D_U)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    lis.append(E_U)
                else:
                    li.append(E_U)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    lis.append(F_U)
                else:
                    li.append(F_U) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    lis.append(G_U)
                else:
                    li.append(G_U) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    lis.append(H_U)
                else:
                    li.append(H_U)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    lis.append(I_U)
                else:
                    li.append(I_U) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    lis.append(J_U)
                else:
                    li.append(J_U)   
                    
                          
                    
            for valor in lis:
                if valor is not None:
                    sum +=valor
                    cont+=1  
                else:
                    sum+=0
            if  cont>0:
                prom_prob_total=sum/cont          
            else:
                prom_prob_total='Insufficient data'        
                    
                    
            for valo in li:
                if valo is not None:
                    su +=valo
                    con+=1  
                else:
                    su+=0
            if  con>0:
                prom_prob_total1=su/con          
            else:
                prom_prob_total1='Insufficient data'       
            N=con+cont        
                   
                    
                    
            if con > cont:
               total= con
               under_over='OVER'
               p_total=prom_prob_total1
               
            elif cont > con:
                total= cont
                under_over='UNDER'
                p_total=prom_prob_total
                
            else:
                total1=cont
                total2=con       
                under_over1='OVER'    
                under_over2='UNDER'
                p_total1= prom_prob_total1 
                p_total2=prom_prob_total
            
            
            
                   
            #total referencia 
            A_U_p = objeto_creado.A_total_punto
            B_U_p = objeto_creado.B_total_punto
            C_U_p = objeto_creado.C_total_punto
            D_U_p = objeto_creado.D_total_punto
            E_U_p = objeto_creado.E_total_punto
            F_U_p = objeto_creado.F_total_punto
            G_U_p = objeto_creado.G_total_punto
            H_U_p = objeto_creado.H_total_punto
            I_U_p = objeto_creado.I_total_punto
            J_U_p = objeto_creado.J_total_punto   
            cont8=0
            sum8=0
            con8=0
            su8=0
            qw=0
            prom_punto_total1=0
            prom_punto_total=0
            p_lis=[]
            p_li=[]
            
            if A_U1 is not None:
                if A_U1.nombre=='UNDER':
                    p_lis.append(A_U_p)
                else:
                    p_li.append(A_U_p)
                    
            if B_U1 is not None:
                if B_U1.nombre=='UNDER':
                    p_lis.append(B_U_p)
                else:
                    p_li.append(B_U_p)
            
            if C_U1 is not None:
                if C_U1.nombre=='UNDER':
                    p_lis.append(C_U_p)
                else:
                    p_li.append(C_U_p)
                    
            if D_U1 is not None:
                if D_U1.nombre=='UNDER':
                    p_lis.append(D_U_p)
                else:
                    p_li.append(D_U_p)
                    
                    
            if E_U1 is not None:
                if E_U1.nombre=='UNDER':
                    p_lis.append(E_U_p)
                else:
                    p_li.append(E_U_p)        
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if F_U1 is not None:
                if F_U1.nombre=='UNDER':
                    p_lis.append(F_U_p)
                else:
                    p_li.append(F_U_p) 
            
            if G_U1 is not None:
                if G_U1.nombre=='UNDER':
                    p_lis.append(G_U_p)
                else:
                    p_li.append(G_U_p) 
                    
            if H_U1 is not None:
                if H_U1.nombre=='UNDER':
                    p_lis.append(H_U_p)
                else:
                    p_li.append(H_U_p)         
                    
            if I_U1 is not None:
                if I_U1.nombre=='UNDER':
                    p_lis.append(I_U_p)
                else:
                    p_li.append(I_U_p) 
                    
            if J_U1 is not None:
                if J_U1.nombre=='UNDER':
                    p_lis.append(J_U_p)
                else:
                    p_li.append(J_U_p)   
            
            
            for vaor in p_lis:
                if vaor is not None:
                    sum8 +=vaor
                    cont8+=1  
                else:
                    sum8+=0
            if  cont8>0:
                prom_punto_total=sum8/cont8         
            else:
                prom_punto_total='Insufficient data'    
            
             
            for vao in p_li:
                if vao is not None:
                    su8 +=vao
                    con8+=1  
                else:
                    su8+=0
            if  con8>0:
                prom_punto_total1=su8/con8         
            else:
                prom_punto_total1='Insufficient data' 
             
             
            if cont8>con8:
                d_total=prom_punto_total
            elif cont8<con8:
                d_total=prom_punto_total1
            else:
                d_total1=prom_punto_total 
                d_total2=prom_punto_total1 
             
            
            if prom_punto_total=='Insufficient data' and prom_punto_total1=='Insufficient data' :
                es_numero1=0
            else:   
                es_numero1=1
            
             
            #moneline probabilidad    
            A_ML = objeto_creado.A_ML_prob
            B_ML = objeto_creado.B_ML_prob
            C_ML = objeto_creado.C_ML_prob
            D_ML = objeto_creado.D_ML_prob
            E_ML = objeto_creado.E_ML_prob
            F_ML = objeto_creado.F_ML_prob
            G_ML = objeto_creado.G_ML_prob
            H_ML = objeto_creado.H_ML_prob
            I_ML = objeto_creado.I_ML_prob
            J_ML = objeto_creado.J_ML_prob
            A_ML1 = objeto_creado.A_ML_equip
            B_ML1 = objeto_creado.B_ML_equip
            C_ML1 = objeto_creado.C_ML_equip
            D_ML1 = objeto_creado.D_ML_equip
            E_ML1 = objeto_creado.E_ML_equip
            F_ML1 = objeto_creado.F_ML_equip
            G_ML1 = objeto_creado.G_ML_equip
            H_ML1 = objeto_creado.H_ML_equip
            I_ML1 = objeto_creado.I_ML_equip
            J_ML1 = objeto_creado.J_ML_equip
            
            cont1=0
            cont2=0
            cont_t=0
            sum1=0
            sum2=0
            prom1=0
            prom2=0
            l1=[]
            l2=[]
            moneline=0
            moneline1=0
            moneline2=0
            p_moneline=0
            p_moneline1=0
            p_moneline2=0
            m_logo1 = None
            m_logo = None
            m_logo2 = None
           
            if A_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(A_ML)
               else:
                   l2.append(A_ML)    
               
            if B_ML1 is not None:   
               if B_ML1.nombre == equipo_l.nombre:
                   l1.append(B_ML)
               else:
                   l2.append(B_ML)      
                  
            if C_ML1 is not None:   
               if C_ML1.nombre == equipo_l.nombre:
                   l1.append(C_ML)
               else:
                   l2.append(C_ML)      
                  
            if D_ML1 is not None:   
               if D_ML1.nombre == equipo_l.nombre:
                   l1.append(D_ML)
               else:
                   l2.append(D_ML)
            
            if E_ML1 is not None:   
               if E_ML1.nombre == equipo_l.nombre:
                   l1.append(E_ML)
               else:
                   l2.append(E_ML)
            
            if F_ML1 is not None:   
               if F_ML1.nombre == equipo_l.nombre:
                   l1.append(F_ML)
               else:
                   l2.append(F_ML)
            
            if G_ML1 is not None:   
               if G_ML1.nombre == equipo_l.nombre:
                   l1.append(G_ML)
               else:
                   l2.append(G_ML)
            
            if H_ML1 is not None:   
               if H_ML1.nombre == equipo_l.nombre:
                   l1.append(H_ML)
               else:
                   l2.append(H_ML)
            
            if I_ML1 is not None:   
               if A_ML1.nombre == equipo_l.nombre:
                   l1.append(I_ML)
               else:
                   l2.append(I_ML)
            
            if J_ML1 is not None:   
               if J_ML1.nombre == equipo_l.nombre:
                   l1.append(J_ML)
               else:
                   l2.append(J_ML)
            
            
            
            for valor1 in l1:
                if valor1 is not None:
                    sum1 +=valor1
                    cont1+=1  
                else:
                    sum1+=0
                    
            if  cont1>0:
                prom1=sum1/cont1          
            else:
                prom1='Insufficient data'                
                
                
            for valor2 in l2:
                if valor2 is not None:
                    sum2 +=valor2
                    cont2+=1  
                else:
                    sum2+=0
                    
            if  cont2>0:
                prom2=sum2/cont2          
            else:
                prom2='Insufficient data'    
                
               
            cont_t=cont1+cont2    
            
            
            #mayor cantidad sistemas
            if cont1>cont2:
                moneline=cont1
                m_logo=equipo_ll
                p_moneline=prom1
                
            elif cont1<cont2:
                moneline=cont2
                m_logo=equipo_vl
                p_moneline=prom2
            else:
                moneline=0
                moneline1=cont1 
                moneline2=cont2
                m_logo1=equipo_ll
                m_logo2=equipo_vl
                p_moneline1=prom1
                p_moneline2=prom2
                
           
            if prom1=='Insufficient data' and prom2=='Insufficient data' :
                es_numero=0
            else:   
                es_numero=1
                
                
                
            #Sperad probabilidad 
        
            A_SP = objeto_creado.A_SP_equip
            B_SP = objeto_creado.B_SP_equip
            C_SP = objeto_creado.C_SP_equip
            D_SP = objeto_creado.D_SP_equip
            E_SP = objeto_creado.E_SP_equip
            F_SP = objeto_creado.F_SP_equip
            G_SP = objeto_creado.G_SP_equip
            H_SP = objeto_creado.H_SP_equip
            I_SP = objeto_creado.I_SP_equip
            J_SP = objeto_creado.J_SP_equip
            p_A_SP = objeto_creado.A_SP_dif
            p_B_SP = objeto_creado.B_SP_dif
            p_C_SP = objeto_creado.C_SP_dif
            p_D_SP = objeto_creado.D_SP_dif
            p_E_SP = objeto_creado.E_SP_dif
            p_F_SP = objeto_creado.F_SP_dif
            p_G_SP = objeto_creado.G_SP_dif
            p_H_SP = objeto_creado.H_SP_dif
            p_I_SP = objeto_creado.I_SP_dif
            p_J_SP = objeto_creado.J_SP_dif
            p_A_SP1 = objeto_creado.A_SP_prob
            p_B_SP1 = objeto_creado.B_SP_prob
            p_C_SP1 = objeto_creado.C_SP_prob
            p_D_SP1 = objeto_creado.D_SP_prob
            p_E_SP1 = objeto_creado.E_SP_prob
            p_F_SP1 = objeto_creado.F_SP_prob
            p_G_SP1 = objeto_creado.G_SP_prob
            p_H_SP1 = objeto_creado.H_SP_prob
            p_I_SP1 = objeto_creado.I_SP_prob
            p_J_SP1 = objeto_creado.J_SP_prob
            co22=0
            co2=0
            con2=0
            cont22=0
            sum22=0
            su2=0
            s2=0
            s22=0
            pro_SP_p=0
            pro_SP_P1=0
            pro_SP=0
            pro_SP1=0
            lis2=[]
            li2=[]            
            lp=[]
            l=[]
            wq=0
            pq=0
            p_spread=0
            p_spread1=0
            p_spread2=0
            spread=0
            spread1=0
            spread2=0
            p_logo = None
            p_logo1 = None
            p_logo2 = None
           
            d_spread=0
            d_spread1=0
            d_spread2=0
            
            
            
            if A_SP is not None:   
               if A_SP.nombre == equipo_l.nombre:
                   lp.append(p_A_SP)
                   lis2.append(p_A_SP1)
               else:
                   l.append(p_A_SP)
                   li2.append(p_A_SP1)
            
            if B_SP is not None:   
               if B_SP.nombre == equipo_l.nombre:
                   lp.append(p_B_SP)
                   lis2.append(p_B_SP1)
               else:
                   l.append(p_B_SP)
                   li2.append(p_B_SP1)
                   
            if C_SP is not None:   
               if C_SP.nombre == equipo_l.nombre:
                   lp.append(p_C_SP)
                   lis2.append(p_C_SP1)
               else:
                   l.append(p_C_SP)
                   li2.append(p_C_SP1)
            
            if D_SP is not None:   
               if D_SP.nombre == equipo_l.nombre:
                   lp.append(p_D_SP)
                   lis2.append(p_D_SP1)
               else:
                   l.append(p_D_SP)
                   li2.append(p_D_SP1)
            
            if E_SP is not None:   
               if E_SP.nombre == equipo_l.nombre:
                   lp.append(p_E_SP)
                   lis2.append(p_E_SP1)
               else:
                   l.append(p_E_SP)
                   li2.append(p_E_SP1)
                   
           
            if F_SP is not None:   
               if F_SP.nombre == equipo_l.nombre:
                   lp.append(p_F_SP)
                   lis2.append(p_F_SP1)
               else:
                   l.append(p_F_SP)
                   li2.append(p_F_SP1)        
                   
            if G_SP is not None:   
               if G_SP.nombre == equipo_l.nombre:
                   lp.append(p_G_SP)
                   lis2.append(p_G_SP1)
               else:
                   l.append(p_G_SP)
                   li2.append(p_G_SP1)       
                   
            if H_SP is not None:   
               if H_SP.nombre == equipo_l.nombre:
                   lp.append(p_H_SP)
                   lis2.append(p_H_SP1)
               else:
                   l.append(p_H_SP)
                   li2.append(p_H_SP1)       
                   
            if I_SP is not None:   
               if I_SP.nombre == equipo_l.nombre:
                   lp.append(p_I_SP)
                   lis2.append(p_I_SP1)
               else:
                   l.append(p_I_SP)
                   li2.append(p_I_SP1)       
                   
            if J_SP is not None:   
               if J_SP.nombre == equipo_l.nombre:
                   lp.append(p_J_SP)
                   lis2.append(p_J_SP1)
               else:
                   l.append(p_J_SP)
                   li2.append(p_J_SP1)       
                   
                   
            
            for valor2 in lis2:
                if valor2 is not None:
                    sum22 +=valor2
                    cont22+=1  
                else:
                    sum22+=0   
            if  cont22>0:
                pro_SP_p=sum22/cont22          
            else:
                pro_SP_p='Insufficient data' 
            
            
            
            for valo2 in li2:
                if valo2 is not None:
                    su2 +=valo2
                    con2+=1  
                else:
                    su2+=0   
            if  con2>0:
                pro_SP_p1=su2/con2          
            else:
                pro_SP_p1='Insufficient data' 
            
            
            
            
            for val2 in lp:
                if val2 is not None:
                    s2 +=val2
                    co2+=1  
                else:
                    s2+=0   
            if  co2>0:
                pro_SP=s2/co2          
            else:
                pro_SP='Insufficient data'  
            
            
            
            for va2 in l:
                if va2 is not None:
                    s22 +=va2
                    co22+=1  
                else:
                    s22+=0   
            if  co22>0:
                pro_SP1=s22/co22          
            else:
                pro_SP1='Insufficient data'
            
            pq=con2+cont22
            wq=co22+co2
            
            
            if cont22>con2:
               spread=cont22 
               p_logo=equipo_ll
               p_spread=pro_SP_p
               
            elif cont22<con2:
               spread=con2
               p_logo=equipo_vl
               p_spread=pro_SP_p1
                
            else:
               spread=0
               spread1=cont22
               spread2=con2  
               p_logo1=equipo_ll 
               p_logo2=equipo_vl 
               p_spread1=pro_SP_p
               p_spread2=pro_SP_p1
                
                
            if co2>co22:
                d_spread=pro_SP
            elif co2<co22:
                d_spread=pro_SP1
            else:    
                d_spread1=pro_SP
                d_spread2=pro_SP1
                 
            if pro_SP=='Insufficient data' and pro_SP1=='Insufficient data' :
                es_numero2=0
            else:   
                es_numero2=1
                
                      
            #underdogs probabilidad
            A_Ud = objeto_creado.A_Ud_equip
            B_Ud = objeto_creado.B_Ud_equip
            C_Ud = objeto_creado.C_Ud_equip
            D_Ud = objeto_creado.D_Ud_equip
            E_Ud = objeto_creado.E_Ud_equip
            F_Ud = objeto_creado.F_Ud_equip
            G_Ud = objeto_creado.G_Ud_equip
            H_Ud = objeto_creado.H_Ud_equip
            I_Ud = objeto_creado.I_Ud_equip
            J_Ud = objeto_creado.J_Ud_equip
            A_Ud1 = objeto_creado.A_Ud_prob
            B_Ud1 = objeto_creado.B_Ud_prob
            C_Ud1 = objeto_creado.C_Ud_prob
            D_Ud1 = objeto_creado.D_Ud_prob
            E_Ud1 = objeto_creado.E_Ud_prob
            F_Ud1 = objeto_creado.F_Ud_prob
            G_Ud1 = objeto_creado.G_Ud_prob
            H_Ud1 = objeto_creado.H_Ud_prob
            I_Ud1 = objeto_creado.I_Ud_prob
            J_Ud1 = objeto_creado.J_Ud_prob
            su3=0
            con3=0
            cont3=0
            sum3=0
            lis3=[]
            list3 = []
            prom_Ud=0
            prom_Ud1=0
            var_Ud=0
            underdogs=0
            underdogs1=0
            underdogs2=0
            u_logo=None
            u_logo1=None
            u_logo2=None
            p_underdogs=0
            p_underdogs1=0
            p_underdogs2=0
            
            if A_Ud is not None:   
               if A_Ud.nombre == equipo_l.nombre:
                   list3.append(A_Ud1)
               else:
                   lis3.append(A_Ud1)
            
            if B_Ud is not None:   
               if B_Ud.nombre == equipo_l.nombre:
                   list3.append(B_Ud1)
               else:
                   lis3.append(B_Ud1)
            
            if C_Ud is not None:   
               if C_Ud.nombre == equipo_l.nombre:
                   list3.append(C_Ud1)
               else:
                   lis3.append(C_Ud1)
                   
        
            if D_Ud is not None:   
               if D_Ud.nombre == equipo_l.nombre:
                   list3.append(D_Ud1)
               else:
                   lis3.append(D_Ud1)
        
        
            if E_Ud is not None:   
               if E_Ud.nombre == equipo_l.nombre:
                   list3.append(E_Ud1)
               else:
                   lis3.append(E_Ud1)
        
        
        
            if F_Ud is not None:   
               if F_Ud.nombre == equipo_l.nombre:
                   list3.append(F_Ud1)
               else:
                   lis3.append(F_Ud1)
        
        
            if G_Ud is not None:   
               if G_Ud.nombre == equipo_l.nombre:
                   list3.append(G_Ud1)
               else:
                   lis3.append(G_Ud1)
                   
                   
            if H_Ud is not None:   
               if H_Ud.nombre == equipo_l.nombre:
                   list3.append(H_Ud1)
               else:
                   lis3.append(H_Ud1)        
                   
                   
            if I_Ud is not None:   
               if I_Ud.nombre == equipo_l.nombre:
                   list3.append(I_Ud1)
               else:
                   lis3.append(I_Ud1)       
        
        
            if J_Ud is not None:   
               if J_Ud.nombre == equipo_l.nombre:
                   list3.append(J_Ud1)
               else:
                   lis3.append(J_Ud1)
                   
                   
        
            for valor3 in list3:
                if valor3 is not None:
                    sum3+=valor3
                    cont3+=1  
                else:
                    sum3+=0
            if  cont3>0:
                prom_Ud=sum3/cont3          
            else:
                prom_Ud='Insufficient data' 
            
            
            for valo3 in lis3:
                if valo3 is not None:
                    su3+=valo3
                    con3+=1  
                else:
                    su3+=0
            if  con3>0:
                prom_Ud1=su3/con3          
            else:
                prom_Ud1='Insufficient data'
            
            var_Ud=cont3+con3
            
            if cont3>con3:
                underdogs=cont3
                u_logo=equipo_ll
                p_underdogs=prom_Ud
                
            elif cont3<con3:
                underdogs=con3
                u_logo=equipo_vl
                p_underdogs=prom_Ud1
                
            else:
                underdogs1=cont3
                underdogs2=con3
                u_logo1=equipo_ll
                u_logo2=equipo_vl
                p_underdogs1=prom_Ud
                p_underdogs2=prom_Ud1
    
            if prom_Ud=='Insufficient data' and prom_Ud1=='Insufficient data' :
                es_numero3=0
            else:   
                es_numero3=1
    
    
            #probabilidad Sharp Beter
            A_SB = objeto_creado.A_SB_equip
            B_SB = objeto_creado.B_SB_equip
            C_SB = objeto_creado.C_SB_equip
            D_SB = objeto_creado.D_SB_equip
            E_SB = objeto_creado.E_SB_equip
            F_SB = objeto_creado.F_SB_equip
            G_SB = objeto_creado.G_SB_equip
            H_SB = objeto_creado.H_SB_equip
            I_SB = objeto_creado.I_SB_equip
            J_SB = objeto_creado.J_SB_equip
            A_SB1 = objeto_creado.A_SB_prob
            B_SB1 = objeto_creado.B_SB_prob
            C_SB1 = objeto_creado.C_SB_prob
            D_SB1 = objeto_creado.D_SB_prob
            E_SB1 = objeto_creado.E_SB_prob
            F_SB1 = objeto_creado.F_SB_prob
            G_SB1 = objeto_creado.G_SB_prob
            H_SB1 = objeto_creado.H_SB_prob
            I_SB1 = objeto_creado.I_SB_prob
            J_SB1 = objeto_creado.J_SB_prob
           
            con5=0
            su5=0
            cont5=0
            sum5=0
            lis5=[]
            list5 = []
            prom_SB=0
            prom_SB1=0
            var_SB=0
            sharp=0
            sharp1=0
            sharp2=0
            p_sharp=0
            p_sharp1=0
            p_sharp2=0
            s_logo=None
            s_logo1=None
            s_logo2=None
            
            
            if A_SB is not None:   
               if A_SB.nombre == equipo_l.nombre:
                   list5.append(A_SB1)
               else:
                   lis5.append(A_SB1)
                   
            if B_SB is not None:   
               if B_SB.nombre == equipo_l.nombre:
                   list5.append(B_SB1)
               else:
                   lis5.append(B_SB1)
            
            if C_SB is not None:   
               if C_SB.nombre == equipo_l.nombre:
                   list5.append(C_SB1)
               else:
                   lis5.append(C_SB1)
            
            if D_SB is not None:   
               if D_SB.nombre == equipo_l.nombre:
                   list5.append(D_SB1)
               else:
                   lis5.append(D_SB1)
                   
                   
            if E_SB is not None:   
               if E_SB.nombre == equipo_l.nombre:
                   list5.append(E_SB1)
               else:
                   lis5.append(E_SB1)       
                   
                   
            if F_SB is not None:   
               if F_SB.nombre == equipo_l.nombre:
                   list5.append(F_SB1)
               else:
                   lis5.append(F_SB1)       
                   
            if G_SB is not None:   
               if G_SB.nombre == equipo_l.nombre:
                   list5.append(G_SB1)
               else:
                   lis5.append(G_SB1)
                   
                   
            if H_SB is not None:   
               if H_SB.nombre == equipo_l.nombre:
                   list5.append(H_SB1)
               else:
                   lis5.append(H_SB1)       
                   
                   
            if I_SB is not None:   
               if I_SB.nombre == equipo_l.nombre:
                   list5.append(I_SB1)
               else:
                   lis5.append(I_SB1)       
                   
                   
            if J_SB is not None:   
               if J_SB.nombre == equipo_l.nombre:
                   list5.append(J_SB1)
               else:
                   lis5.append(J_SB1)
                   
                   
                   
                                 
                   
            for valor5 in list5:
                if valor5 is not None:
                    sum5 +=valor5
                    cont5+=1  
                else:
                    sum5+=0
            if  cont5>0:
                prom_SB=sum5/cont5          
            else:
                prom_SB='Insufficient data' 
            
            for valo5 in lis5:
                if valo5 is not None:
                    su5 +=valo5
                    con5+=1  
                else:
                    su5+=0
            if  con5>0:
                prom_SB1=su5/con5          
            else:
                prom_SB1='Insufficient data'
            
            
            var_SB=cont5+con5
            
            
            if cont5>con5:
                sharp=cont5
                s_logo=equipo_ll
                p_sharp=prom_SB
            elif cont5<con5:
                sharp=con5
                s_logo=equipo_vl
                p_sharp=prom_SB1
                
            else:
                sharp1=cont5
                sharp2=con5
                s_logo1=equipo_ll
                s_logo2=equipo_vl
                p_sharp1=prom_SB
                p_sharp2=prom_SB1
            
            if prom_SB=='Insufficient data' and prom_SB1=='Insufficient data' :
                es_numero4=0
            else:   
                es_numero4=1
            
            # Money Adventage
            
            A_MA = objeto_creado.A_MA
            B_MA = objeto_creado.B_MA
            C_MA = objeto_creado.C_MA
            D_MA = objeto_creado.D_MA
            E_MA = objeto_creado.E_MA
            F_MA = objeto_creado.F_MA
            G_MA = objeto_creado.G_MA
            H_MA = objeto_creado.H_MA
            I_MA = objeto_creado.I_MA
            J_MA = objeto_creado.J_MA
            A_MA1 = objeto_creado.A_MA_prob
            B_MA1 = objeto_creado.B_MA_prob
            C_MA1 = objeto_creado.C_MA_prob
            D_MA1 = objeto_creado.D_MA_prob
            E_MA1 = objeto_creado.E_MA_prob
            F_MA1 = objeto_creado.F_MA_prob
            G_MA1 = objeto_creado.G_MA_prob
            H_MA1 = objeto_creado.H_MA_prob
            I_MA1 = objeto_creado.I_MA_prob
            J_MA1 = objeto_creado.J_MA_prob
            
            s9=0
            con9=0
            cont9=0
            sum9=0
            lis9=[]
            list9 = []
            prom_MA=0
            prom_MA1=0
            var_MA=0
            money=0
            money1=0
            money2=0
            ma_logo=None
            ma_logo1=None
            ma_logo2=None
            p_money=0
            p_money1=0
            p_money2=0
                    
                   
            if A_MA is not None:   
               if A_MA.nombre == equipo_l.nombre:
                   list9.append(A_MA1)
               else:
                   lis9.append(A_MA1)        
                   
            if B_MA is not None:   
               if B_MA.nombre == equipo_l.nombre:
                   list9.append(B_MA1)
               else:
                   lis9.append(B_MA1)
                   
            if C_MA is not None:   
               if C_MA.nombre == equipo_l.nombre:
                   list9.append(C_MA1)
               else:
                   lis9.append(C_MA1)       
                   
            if D_MA is not None:   
               if D_MA.nombre == equipo_l.nombre:
                   list9.append(D_MA1)
               else:
                   lis9.append(D_MA1)
                   
                   
            if E_MA is not None:   
               if E_MA.nombre == equipo_l.nombre:
                   list9.append(E_MA1)
               else:
                   lis9.append(E_MA1)       
                   
                   
            if F_MA is not None:   
               if F_MA.nombre == equipo_l.nombre:
                   list9.append(F_MA1)
               else:
                   lis9.append(F_MA1)
                   
                   
            if G_MA is not None:   
               if G_MA.nombre == equipo_l.nombre:
                   list9.append(G_MA1)
               else:
                   lis9.append(G_MA1)       
                          
            if H_MA is not None:   
               if H_MA.nombre == equipo_l.nombre:
                   list9.append(H_MA1)
               else:
                   lis9.append(H_MA1)
                   
                   
            if I_MA is not None:   
               if I_MA.nombre == equipo_l.nombre:
                   list9.append(I_MA1)
               else:
                   lis9.append(I_MA1)       
                                   
            if J_MA is not None:   
               if J_MA.nombre == equipo_l.nombre:
                   list9.append(J_MA1)
               else:
                   lis9.append(J_MA1)
                   
                   
            for valor9 in list9:
                if valor9 is not None:
                    sum9 +=valor9
                    cont9+=1  
                else:
                    sum9+=0
            if  cont9>0:
                prom_MA=sum9/cont9          
            else:
                prom_MA='Insufficient data'        
                   
            for valo9 in lis9:
                if valo9 is not None:
                    s9 +=valo9
                    con9+=1  
                else:
                    s9+=0
            if  con9>0:
                prom_MA1=s9/con9          
            else:
                prom_MA1='Insufficient data' 
                
            var_MA=cont9+con9
                
            if cont9>con9:
                money=cont9
                ma_logo=equipo_ll
                p_money=prom_MA
                
            elif cont9<con9:
                money=con9
                ma_logo=equipo_vl
                p_money=prom_MA1
                
            else:
                money1=cont9
                money2=con9
                ma_logo1=equipo_ll
                ma_logo2=equipo_vl
                p_money1=prom_MA
                p_money2=prom_MA1   
                
            if prom_MA=='Insufficient data' and prom_MA1=='Insufficient data' :
                es_numero5=0
            else:   
                es_numero5=1
                       
            #Best Bets
            
            A_BB = objeto_creado.A_BB
            B_BB = objeto_creado.B_BB
            C_BB = objeto_creado.C_BB
            D_BB = objeto_creado.D_BB
            E_BB = objeto_creado.E_BB
            F_BB = objeto_creado.F_BB
            G_BB = objeto_creado.G_BB
            H_BB = objeto_creado.H_BB
            I_BB = objeto_creado.I_BB
            J_BB = objeto_creado.J_BB
            A_BB1 = objeto_creado.A_BB_prob
            B_BB1 = objeto_creado.B_BB_prob
            C_BB1 = objeto_creado.C_BB_prob
            D_BB1 = objeto_creado.D_BB_prob
            E_BB1 = objeto_creado.E_BB_prob
            F_BB1 = objeto_creado.F_BB_prob
            G_BB1 = objeto_creado.G_BB_prob
            H_BB1 = objeto_creado.H_BB_prob
            I_BB1 = objeto_creado.I_BB_prob
            J_BB1 = objeto_creado.J_BB_prob
            s7=0
            con7=0
            cont7=0
            sum7=0
            lis7=[]
            list7 = []
            prom_BB=0
            prom_BB1=0
            var_BB=0
            best=0
            best1=0
            best2=0
            b_logo=None
            b_logo1=None
            b_logo2=None
            p_best=0
            p_best1=0
            p_best2=0
            
            if A_BB is not None:   
               if A_BB.nombre == equipo_l.nombre:
                   list7.append(A_BB1)
               else:
                   lis7.append(A_BB1)
                   
            if B_BB is not None:   
               if B_BB.nombre == equipo_l.nombre:
                   list7.append(B_BB1)
               else:
                   lis7.append(B_BB1)
                   
                   
            if C_BB is not None:   
               if C_BB.nombre == equipo_l.nombre:
                   list7.append(C_BB1)
               else:
                   lis7.append(C_BB1)       
                   
            if D_BB is not None:   
               if D_BB.nombre == equipo_l.nombre:
                   list7.append(D_BB1)
               else:
                   lis7.append(D_BB1)       
                   
            if E_BB is not None:   
               if E_BB.nombre == equipo_l.nombre:
                   list7.append(E_BB1)
               else:
                   lis7.append(E_BB1)       
                          
                          
            if F_BB is not None:   
               if F_BB.nombre == equipo_l.nombre:
                   list7.append(F_BB1)
               else:
                   lis7.append(F_BB1)              
                          
                          
            if G_BB is not None:   
               if G_BB.nombre == equipo_l.nombre:
                   list7.append(G_BB1)
               else:
                   lis7.append(G_BB1)             
                          
                          
            if H_BB is not None:   
               if H_BB.nombre == equipo_l.nombre:
                   list7.append(H_BB1)
               else:
                   lis7.append(H_BB1)              
                          
            if I_BB is not None:   
               if I_BB.nombre == equipo_l.nombre:
                   list7.append(I_BB1)
               else:
                   lis7.append(I_BB1)              
                          
            if J_BB is not None:   
               if J_BB.nombre == equipo_l.nombre:
                   list7.append(J_BB1)
               else:
                   lis7.append(J_BB1)    
                   
                   
            for valor7 in list7:
                if valor7 is not None:
                    sum7 +=valor7
                    cont7+=1  
                else:
                    sum7+=0
            if  cont7>0:
                prom_BB=sum7/cont7          
            else:
                prom_BB='Insufficient data'        
                   
            for valo7 in lis7:
                if valo7 is not None:
                    s7 +=valo7
                    con7+=1  
                else:
                    s7+=0
            if  con7>0:
                prom_BB1=s7/con7          
            else:
                prom_BB1='Insufficient data' 
                
            var_BB=cont7+con7
                
            if cont7>con7:
                best=cont7
                b_logo=equipo_ll
                p_best=prom_BB
                
            elif cont7<con7:
                best=con7
                b_logo=equipo_vl
                p_best=prom_BB1
                
            else:
                best1=cont7
                best2=con7
                b_logo1=equipo_ll
                b_logo2=equipo_vl
                p_best1=prom_BB
                p_best2=prom_BB1         
                   
                   
            if prom_BB=='Insufficient data' and prom_BB1=='Insufficient data' :
                es_numero6=0
            else:   
                es_numero6=1       
                   
                   
                             
                   
            
            return render(request, 'NBA_Colegial/informe_lista.html', { 'objeto': objeto_creado, 'prom_prob_total':prom_prob_total, 'prom1':prom1, 'prom2':prom2, 'prom_Ud':prom_Ud, 'prom_Ud1':prom_Ud1,'prom_punto_total':prom_punto_total,'pro_SP1':pro_SP1,'pro_SP':pro_SP,'pro_SP_p':pro_SP_p,'pro_SP_P1':pro_SP_P1,'p_sharp':p_sharp,'p_sharp1':p_sharp1,'p_sharp2':p_sharp2,
                                                            'prom_SB':prom_SB,'prom_SB1':prom_SB1, 'equipo_v':equipo_v,'equipo_l':equipo_l,'equipo_vl':equipo_vl, 'prom_punto_total': prom_punto_total,'prom_punto_total1':prom_punto_total1,'under_over':under_over,'under_over1':under_over1,'under_over2':under_over2,'best':best,'best1':best1,'best2':best2,
                                                            'equipo_ll':equipo_ll,'cont_l':cont_l,'cont_v':cont_v,'c_j_l':c_j_l,'c_j_v':c_j_v,'cont_g_ll':cont_g_ll,'prom_prob_total1':prom_prob_total1,'prom_punto_total':prom_punto_total,'N':N, 'total':total,'total1':total1,'total':total,'total1':total1,'total2':total2,
                                                            'cont_g_lv':cont_g_lv,'cont_g_vl':cont_g_vl,'cont_g_vv':cont_g_vv,'g_l':g_l,'p_l':p_l,'p_v':p_v,'g_v':g_v, 'moneline':moneline, 'moneline1':moneline1,'moneline2':moneline2,'m_logo':m_logo,'m_logo1':m_logo1,'m_logo2':m_logo2,'cont_t':cont_t,'p_total':p_total,'p_total1':p_total1,'p_total2':p_total2, 
                                                            'p_moneline':p_moneline,'p_moneline1':p_moneline1,'p_moneline2':p_moneline2,'spread':spread,'spread':spread,'spread1':spread1,'spread2':spread2,'p_spread':p_spread,'p_spread1':p_spread1,'p_spread2':p_spread2, 'p_logo':p_logo, 'p_logo1':p_logo1,'p_logo2':p_logo2,'sharp':sharp,'sharp1':sharp1,'sharp2':sharp2,
                                                            'wq':wq,'pq':pq,'d_spread':d_spread, 'd_spread1':d_spread1,'d_spread2':d_spread2,'var_Ud':var_Ud,'underdogs':underdogs,'underdogs1':underdogs1,'underdogs2':underdogs2,'u_logo':u_logo,'u_logo1':u_logo1,'u_logo2':u_logo2,'p_underdogs': p_underdogs,'p_underdogs1': p_underdogs1,'p_underdogs2': p_underdogs2, 
                                                            's_logo':s_logo,'s_logo1':s_logo1,'s_logo2':s_logo2,'var_SB':var_SB,'money':money, 'money1':money1,'money2':money2, 'p_money':p_money,'p_money1':p_money1,'p_money2':p_money2,'ma_logo':ma_logo,'ma_logo1':ma_logo1,'ma_logo2':ma_logo2, 'var_MA':var_MA,'b_logo':b_logo,'b_logo1':b_logo1,'b_logo2':b_logo2, 
                                                            'p_best':p_best,'p_best1':p_best1,'p_best2':p_best2,'var_BB':var_BB,'d_total':d_total,'d_total1':d_total1, 'd_total2':d_total2, 'es_numero':es_numero,'es_numero1':es_numero1,'es_numero2':es_numero2,'es_numero3':es_numero3,'es_numero4':es_numero4,'es_numero5':es_numero5,'es_numero6':es_numero6,  })

def Resultados_Sistemas_NBAC(request): 
    
    partidos_filtrados = NBA_Colegial.objects.exclude(ganador__isnull=True).exclude(resultado__isnull=True)
    partidos = partidos_filtrados.order_by('-fecha')[:20]
    
    
    #Sistema A
    
    ganador=''
    cont_A_ML=0
    cont_A_SP=0
    cont_A_Ud=0
    cont_A_SB=0
    cont_A_MA=0
    cont_A_BB=0
    cont_A_Total=0
    A_cont=0
    A_cont1=0
    A_cont2=0
    A_cont3=0
    A_cont4=0
    A_cont5=0
    A_cont6=0
    sum=0
    res=0
    valor_izquierdo=0
    valor_derecho=0
    A_prom=0
    A_prom1=0
    A_prom2=0
    A_prom3=0
    A_prom4=0 
    A_prom5=0
    A_prom6=0
    
    for valor in partidos: 
        
        ganador=valor.ganador
        
        valor_izquierdo, valor_derecho = extraer_valores_de_resultado(valor)
        sum= valor_izquierdo+valor_derecho
        
        if valor.A_ML_equip is not None:
           A_cont+=1
           if ganador==valor.A_ML_equip.nombre:
              cont_A_ML+=1 
              
              
        if valor.A_Ud_equip is not None:
           A_cont1+=1      
           if ganador==valor.A_Ud_equip.nombre:
              cont_A_Ud+=1
              
              
        if valor.A_SB_equip is not None: 
           A_cont2+=1      
           if ganador==valor.A_SB_equip.nombre:
              cont_A_SB+=1
              
              
        if valor.A_MA is not None:
           A_cont3+=1 
           if ganador==valor.A_MA.nombre:
              cont_A_MA+=1
              
              
        if valor.A_BB is not None:  
           A_cont4+=1 
           if ganador==valor.A_BB.nombre:
              cont_A_BB+=1
         
         
        if valor.A_total_punto is not None: 
           A_cont5+=1 
           if sum>valor.A_total_punto and valor.A_Total_OU=='OVER':
              cont_A_Total+=1
           if sum<=valor.A_total_punto and valor.A_Total_OU=='UNDER':
              cont_A_Total+=1
         
         
       
        if valor_izquierdo>valor_derecho:
            res=valor_izquierdo-valor_derecho
           
        elif valor_izquierdo<valor_derecho:
            res=valor_derecho-valor_izquierdo 
        
        else: 
            res=0
        
        if valor.A_SP_dif is not None:
           A_cont6+=1
           if ganador==valor.A_SP_equip.nombre and res>valor.A_SP_dif :
              cont_A_SP+=1
           
           
           
    if cont_A_ML !=0 and A_cont !=0:
           A_prom=cont_A_ML*100/A_cont
        
    if cont_A_SP !=0 and A_cont6 !=0:
           A_prom6=cont_A_SP*100/A_cont6
           
    if cont_A_Ud !=0 and A_cont1 !=0:
           A_prom1=cont_A_Ud*100/A_cont1
           
    if cont_A_SB !=0 and A_cont2 !=0:
           A_prom2=cont_A_SB*100/A_cont2
           
    if cont_A_MA !=0 and A_cont3 !=0:
           A_prom3=cont_A_MA*100/A_cont3
           
    if cont_A_BB !=0 and A_cont4 !=0:
           A_prom4=cont_A_BB*100/A_cont5
           
    if cont_A_Total !=0 and A_cont5 !=0:
           A_prom5=cont_A_Total*100/A_cont5      
           
           
           
    #Sistema B     
    
    B_ganador=''
    cont_B_ML=0
    cont_B_SP=0
    cont_B_Ud=0
    cont_B_SB=0
    cont_B_MA=0
    cont_B_BB=0
    cont_B_Total=0
    B_cont=0
    B_cont1=0
    B_cont2=0
    B_cont3=0
    B_cont4=0
    B_cont5=0
    B_cont6=0
    B_sum=0
    B_res=0
    B_valor_izquierdo=0
    B_valor_derecho=0
    B_prom=0
    B_prom1=0
    B_prom2=0
    B_prom3=0
    B_prom4=0 
    B_prom5=0
    B_prom6=0
    
    for valor in partidos: 
        
        B_ganador=valor.ganador
        
        B_valor_izquierdo, B_valor_derecho = extraer_valores_de_resultado(valor)
        B_sum= B_valor_izquierdo+B_valor_derecho
        
        if valor.B_ML_equip is not None:
           B_cont+=1
           if B_ganador==valor.B_ML_equip.nombre:
              cont_B_ML+=1 
              
              
        if valor.B_Ud_equip is not None:
           B_cont1+=1      
           if B_ganador==valor.B_Ud_equip.nombre:
              cont_B_Ud+=1
              
              
        if valor.B_SB_equip is not None: 
           B_cont2+=1      
           if B_ganador==valor.B_SB_equip.nombre:
              cont_B_SB+=1
              
              
        if valor.B_MA is not None:
           B_cont3+=1 
           if B_ganador==valor.B_MA.nombre:
              cont_B_MA+=1
              
              
        if valor.B_BB is not None:  
           B_cont4+=1 
           if B_ganador==valor.B_BB.nombre:
              cont_B_BB+=1
         
         
        if valor.B_total_punto is not None: 
           B_cont5+=1 
           if B_sum>valor.B_total_punto and valor.B_Total_OU=='OVER':
              cont_B_Total+=1
           if B_sum<=valor.B_total_punto and valor.B_Total_OU=='UNDER':
              cont_B_Total+=1
         
         
       
        if B_valor_izquierdo>B_valor_derecho:
            B_res=B_valor_izquierdo-B_valor_derecho
           
        elif B_valor_izquierdo<B_valor_derecho:
            B_res=B_valor_derecho-B_valor_izquierdo 
        
        else: 
            B_res=0
        
        if valor.B_SP_dif is not None:
           B_cont6+=1
           if B_ganador==valor.B_SP_equip.nombre and B_res>valor.B_SP_dif :
              cont_B_SP+=1
           
           
           
    if cont_B_ML !=0 and B_cont !=0:
           B_prom=cont_B_ML*100/B_cont
        
    if cont_B_SP !=0 and B_cont6 !=0:
           B_prom6=cont_B_SP*100/B_cont6
           
    if cont_B_Ud !=0 and B_cont1 !=0:
           B_prom1=cont_B_Ud*100/B_cont1
           
    if cont_B_SB !=0 and B_cont2 !=0:
           B_prom2=cont_B_SB*100/B_cont2
           
    if cont_B_MA !=0 and B_cont3 !=0:
           B_prom3=cont_B_MA*100/B_cont3
           
    if cont_B_BB !=0 and B_cont4 !=0:
           B_prom4=cont_B_BB*100/B_cont5
           
    if cont_B_Total !=0 and B_cont5 !=0:
           B_prom5=cont_B_Total*100/B_cont5             
           
           
    C_ganador=''
    cont_C_ML=0
    cont_C_SP=0
    cont_C_Ud=0
    cont_C_SB=0
    cont_C_MA=0
    cont_C_BB=0
    cont_C_Total=0
    C_cont=0
    C_cont1=0
    C_cont2=0
    C_cont3=0
    C_cont4=0
    C_cont5=0
    C_cont6=0
    C_sum=0
    C_res=0
    C_valor_izquierdo=0
    C_valor_derecho=0
    C_prom=0
    C_prom1=0
    C_prom2=0
    C_prom3=0
    C_prom4=0 
    C_prom5=0        
    C_prom6=0
       
    for valor in partidos: 
        
        C_ganador=valor.ganador
            
        C_valor_izquierdo, C_valor_derecho = extraer_valores_de_resultado(valor)
        C_sum= C_valor_izquierdo+C_valor_derecho
            
        if valor.C_ML_equip is not None:
            C_cont+=1
            if C_ganador==valor.C_ML_equip.nombre:
                cont_C_ML+=1 
                
        if valor.C_Ud_equip is not None:
            C_cont1+=1      
            if C_ganador==valor.C_Ud_equip.nombre:
                cont_C_Ud+=1
                
        if valor.C_SB_equip is not None: 
            C_cont2+=1      
            if C_ganador==valor.C_SB_equip.nombre:
                cont_C_SB+=1
                
        if valor.C_MA is not None:
            C_cont3+=1 
            if C_ganador==valor.C_MA.nombre:
                cont_C_MA+=1
                
        if valor.C_BB is not None:  
            C_cont4+=1 
            if C_ganador==valor.C_BB.nombre:
                cont_C_BB+=1
            
            
        if valor.C_total_punto is not None: 
            C_cont5+=1 
            if C_sum>valor.C_total_punto and valor.C_Total_OU=='OVER':
                cont_C_Total+=1
            if C_sum<=valor.C_total_punto and valor.C_Total_OU=='UNDER':
                cont_C_Total+=1
            
            

        if C_valor_izquierdo>C_valor_derecho:
            C_res=C_valor_izquierdo-C_valor_derecho
            
        elif C_valor_izquierdo<C_valor_derecho:
            C_res=C_valor_derecho-C_valor_izquierdo 

        else: 
            C_res=0
            
        if valor.C_SP_dif is not None:
            C_cont6+=1
            if C_ganador==valor.C_SP_equip.nombre and C_res>valor.C_SP_dif :
                cont_C_SP+=1
           
           
    if cont_C_ML !=0 and C_cont !=0:
       C_prom=cont_C_ML*100/C_cont
            
    if cont_C_SP !=0 and C_cont6 !=0:
       C_prom6=cont_C_SP*100/C_cont6
            
    if cont_C_Ud !=0 and C_cont1 !=0:
       C_prom1=cont_C_Ud*100/C_cont1
            
    if cont_C_SB !=0 and C_cont2 !=0:
       C_prom2=cont_C_SB*100/C_cont2
            
    if cont_C_MA !=0 and C_cont3 !=0:
       C_prom3=cont_C_MA*100/C_cont3
            
    if cont_C_BB !=0 and C_cont4 !=0:
       C_prom4=cont_C_BB*100/C_cont5
            
    if cont_C_Total !=0 and C_cont5 !=0:
       C_prom5=cont_C_Total*100/C_cont5       
           
    
    
    D_ganador=''
    cont_D_ML=0
    cont_D_SP=0
    cont_D_Ud=0
    cont_D_SB=0
    cont_D_MA=0
    cont_D_BB=0
    cont_D_Total=0
    D_cont=0
    D_cont1=0
    D_cont2=0
    D_cont3=0
    D_cont4=0
    D_cont5=0
    D_cont6=0
    D_sum=0
    D_res=0
    D_valor_izquierdo=0
    D_valor_derecho=0
    D_prom=0
    D_prom1=0
    D_prom2=0
    D_prom3=0
    D_prom4=0 
    D_prom5=0        
    D_prom6=0

    
    
    
    for valor in partidos: 
        
        D_ganador=valor.ganador
            
        D_valor_izquierdo, D_valor_derecho = extraer_valores_de_resultado(valor)
        D_sum= D_valor_izquierdo+D_valor_derecho
            
        if valor.D_ML_equip is not None:
           D_cont+=1
           if D_ganador==valor.D_ML_equip.nombre:
              cont_D_ML+=1 
            
        if valor.D_Ud_equip is not None:
           D_cont1+=1      
           if D_ganador==valor.D_Ud_equip.nombre:
              cont_D_Ud+=1
            
        if valor.D_SB_equip is not None: 
           D_cont2+=1      
           if D_ganador==valor.D_SB_equip.nombre:
              cont_D_SB+=1
            
        if valor.D_MA is not None:
           D_cont3+=1 
           if D_ganador==valor.D_MA.nombre:
              cont_D_MA+=1
            
        if valor.D_BB is not None:  
           D_cont4+=1 
           if D_ganador==valor.D_BB.nombre:
              cont_D_BB+=1
        
        
        if valor.D_total_punto is not None: 
           D_cont5+=1 
           if D_sum>valor.D_total_punto and valor.D_Total_OU=='OVER':
              cont_D_Total+=1
           if D_sum<=valor.D_total_punto and valor.D_Total_OU=='UNDER':
              cont_D_Total+=1
        
        
    
        if D_valor_izquierdo>D_valor_derecho:
            D_res=D_valor_izquierdo-D_valor_derecho
        
        elif D_valor_izquierdo<D_valor_derecho:
            D_res=D_valor_derecho-D_valor_izquierdo 
        
        else: 
            D_res=0
            
        if valor.D_SP_dif is not None:
           D_cont6+=1
           if D_ganador==valor.D_SP_equip.nombre and D_res>valor.D_SP_dif :
              cont_D_SP+=1
             
           
    if cont_D_ML !=0 and D_cont !=0:
       D_prom=cont_D_ML*100/D_cont
            
    if cont_D_SP !=0 and D_cont6 !=0:
       D_prom6=cont_D_SP*100/D_cont6
            
    if cont_D_Ud !=0 and D_cont1 !=0:
       D_prom1=cont_D_Ud*100/D_cont1
            
    if cont_D_SB !=0 and D_cont2 !=0:
       D_prom2=cont_D_SB*100/D_cont2
            
    if cont_D_MA !=0 and D_cont3 !=0:
       D_prom3=cont_D_MA*100/D_cont3
            
    if cont_D_BB !=0 and D_cont4 !=0:
       D_prom4=cont_D_BB*100/D_cont5
            
    if cont_D_Total !=0 and D_cont5 !=0:
       D_prom5=cont_D_Total*100/D_cont5
        
    
    E_ganador=''
    cont_E_ML=0
    cont_E_SP=0
    cont_E_Ud=0
    cont_E_SB=0
    cont_E_MA=0
    cont_E_BB=0
    cont_E_Total=0
    E_cont=0
    E_cont1=0
    E_cont2=0
    E_cont3=0
    E_cont4=0
    E_cont5=0
    E_cont6=0
    E_sum=0
    E_res=0
    E_valor_izquierdo=0
    E_valor_derecho=0
    E_prom=0
    E_prom1=0
    E_prom2=0
    E_prom3=0
    E_prom4=0 
    E_prom5=0        
    E_prom6=0
       
    for valor in partidos: 
        
        E_ganador=valor.ganador
            
        E_valor_izquierdo, E_valor_derecho = extraer_valores_de_resultado(valor)
        E_sum= E_valor_izquierdo+E_valor_derecho
            
        if valor.E_ML_equip is not None:
           E_cont+=1
           if E_ganador==valor.E_ML_equip.nombre:
              cont_E_ML+=1 
            
        if valor.E_Ud_equip is not None:
           E_cont1+=1      
           if E_ganador==valor.E_Ud_equip.nombre:
              cont_E_Ud+=1
            
        if valor.E_SB_equip is not None: 
           E_cont2+=1      
           if E_ganador==valor.E_SB_equip.nombre:
              cont_E_SB+=1
            
        if valor.E_MA is not None:
           E_cont3+=1 
           if E_ganador==valor.E_MA.nombre:
              cont_E_MA+=1
            
        if valor.E_BB is not None:  
           E_cont4+=1 
           if E_ganador==valor.E_BB.nombre:
              cont_E_BB+=1
        
        
        if valor.E_total_punto is not None: 
           E_cont5+=1 
           if E_sum>valor.E_total_punto and valor.E_Total_OU=='OVER':
              cont_E_Total+=1
           if E_sum<=valor.E_total_punto and valor.E_Total_OU=='UNDER':
              cont_E_Total+=1
        
        
    
        if E_valor_izquierdo>E_valor_derecho:
            E_res=E_valor_izquierdo-E_valor_derecho
        
        elif E_valor_izquierdo<E_valor_derecho:
            E_res=E_valor_derecho-E_valor_izquierdo 
        
        else: 
            E_res=0
            
        if valor.E_SP_dif is not None:
           E_cont6+=1
           if E_ganador==valor.E_SP_equip.nombre and E_res>valor.E_SP_dif :
              cont_E_SP+=1
            
           
    if cont_E_ML !=0 and E_cont !=0:
       E_prom=cont_E_ML*100/E_cont
            
    if cont_E_SP !=0 and E_cont6 !=0:
       E_prom6=cont_E_SP*100/E_cont6
            
    if cont_E_Ud !=0 and E_cont1 !=0:
       E_prom1=cont_E_Ud*100/E_cont1   
        
    if cont_E_SB !=0 and E_cont2 !=0:
       E_prom2=cont_E_SB*100/E_cont2
            
    if cont_E_MA !=0 and E_cont3 !=0:
       E_prom3=cont_E_MA*100/E_cont3
            
    if cont_E_BB !=0 and E_cont4 !=0:
       E_prom4=cont_E_BB*100/E_cont5
            
    if cont_E_Total !=0 and E_cont5 !=0:
       E_prom5=cont_E_Total*100/E_cont5     
    
    
    
    
    F_ganador=''
    cont_F_ML=0
    cont_F_SP=0
    cont_F_Ud=0
    cont_F_SB=0
    cont_F_MA=0
    cont_F_BB=0
    cont_F_Total=0
    F_cont=0
    F_cont1=0
    F_cont2=0
    F_cont3=0
    F_cont4=0
    F_cont5=0
    F_cont6=0
    F_sum=0
    F_res=0
    F_valor_izquierdo=0
    F_valor_derecho=0
    F_prom=0
    F_prom1=0
    F_prom2=0
    F_prom3=0
    F_prom4=0 
    F_prom5=0        
    F_prom6=0
       
    
    for valor in partidos: 
        
 
        F_valor_izquierdo, F_valor_derecho = extraer_valores_de_resultado(valor)
        F_sum = F_valor_izquierdo + F_valor_derecho
                
        if valor.F_ML_equip is not None:
           F_cont+=1
           if F_ganador==valor.F_ML_equip.nombre:
              F_cont_ML+=1 
                
        if valor.F_Ud_equip is not None:
           F_cont1+=1      
           if F_ganador==valor.F_Ud_equip.nombre:
              F_cont_Ud+=1
                
        if valor.F_SB_equip is not None: 
           F_cont2+=1      
           if F_ganador==valor.F_SB_equip.nombre:
              F_cont_SB+=1
                
        if valor.F_MA is not None:
           F_cont3+=1 
           if F_ganador==valor.F_MA.nombre:
              F_cont_MA+=1
                
        if valor.F_BB is not None:  
           F_cont4+=1 
           if F_ganador==valor.F_BB.nombre:
              F_cont_BB+=1
            
            
        if valor.F_total_punto is not None: 
           F_cont5+=1 
           if F_sum>F_valor_izquierdo and valor.F_Total_OU=='OVER':
              F_cont_Total+=1
           if F_sum<=valor.F_total_punto and valor.F_Total_OU=='UNDER':
              F_cont_Total+=1
            
            
        if F_valor_izquierdo>F_valor_derecho:
            F_res=F_valor_izquierdo-F_valor_derecho
            
        elif F_valor_izquierdo<F_valor_derecho:
            F_res=F_valor_derecho-F_valor_izquierdo 
        
        else: 
            F_res=0
                
        if valor.F_SP_dif is not None:
           F_cont6+=1
           if F_ganador==valor.F_SP_equip.nombre and F_res>valor.F_SP_dif :
              F_cont_SP+=1
            
           
    if cont_F_ML !=0 and F_cont !=0:
       F_prom=F_cont_ML*100/F_cont
                
    if cont_F_SP !=0 and F_cont6 !=0:
       F_prom6=F_cont_SP*100/F_cont6
                
    if cont_F_Ud !=0 and F_cont1 !=0:
       F_prom1=F_cont_Ud*100/F_cont1   
            
    if cont_F_SB !=0 and F_cont2 !=0:
       F_prom2=F_cont_SB*100/F_cont2
                
    if cont_F_MA !=0 and F_cont3 !=0:
       F_prom3=F_cont_MA*100/F_cont3
                
    if cont_F_BB !=0 and F_cont4 !=0:
       F_prom4=F_cont_BB*100/F_cont5
                
    if cont_F_Total !=0 and F_cont5 !=0:
       F_prom5=F_cont_Total*100/F_cont5
        
    
    G_ganador=''
    cont_G_ML=0
    cont_G_SP=0
    cont_G_Ud=0
    cont_G_SB=0
    cont_G_MA=0
    cont_G_BB=0
    cont_G_Total=0
    G_cont=0
    G_cont1=0
    G_cont2=0
    G_cont3=0
    G_cont4=0
    G_cont5=0
    G_cont6=0
    G_sum=0
    G_res=0
    G_valor_izquierdo=0
    G_valor_derecho=0
    G_prom=0
    G_prom1=0
    G_prom2=0
    G_prom3=0
    G_prom4=0 
    G_prom5=0        
    G_prom6=0

    for valor in partidos: 
        
        G_valor_izquierdo, G_valor_derecho = extraer_valores_de_resultado(valor)
        G_sum = G_valor_izquierdo + G_valor_derecho
                    
        if valor.G_ML_equip is not None:
           G_cont+=1
           if G_ganador==valor.G_ML_equip.nombre:
              G_cont_ML+=1 
                    
        if valor.G_Ud_equip is not None:
           G_cont1+=1      
           if G_ganador==valor.G_Ud_equip.nombre:
              G_cont_Ud+=1
                    
        if valor.G_SB_equip is not None: 
           G_cont2+=1      
           if G_ganador==valor.G_SB_equip.nombre:
              G_cont_SB+=1
                    
        if valor.G_MA is not None:
           G_cont3+=1 
           if G_ganador==valor.G_MA.nombre:
              G_cont_MA+=1
                    
        if valor.G_BB is not None:  
           G_cont4+=1 
           if G_ganador==valor.G_BB.nombre:
              G_cont_BB+=1
                
                
        if valor.G_total_punto is not None: 
           G_cont5+=1 
           if G_sum>G_valor_izquierdo and valor.G_Total_OU=='OVER':
              G_cont_Total+=1
           if G_sum<=valor.G_total_punto and valor.G_Total_OU=='UNDER':
              G_cont_Total+=1
                
                
        if G_valor_izquierdo>G_valor_derecho:
            G_res=G_valor_izquierdo-G_valor_derecho
                
        elif G_valor_izquierdo<G_valor_derecho:
            G_res=G_valor_derecho-G_valor_izquierdo 
            
        else: 
            G_res=0
                    
        if valor.G_SP_dif is not None:
           G_cont6+=1
           if G_ganador==valor.G_SP_equip.nombre and G_res>valor.G_SP_dif :
              G_cont_SP+=1
            
           
    if cont_G_ML !=0 and G_cont !=0:
       G_prom=G_cont_ML*100/G_cont
                    
    if cont_G_SP !=0 and G_cont6 !=0:
       G_prom6=G_cont_SP*100/G_cont6
                    
    if cont_G_Ud !=0 and G_cont1 !=0:
       G_prom1=G_cont_Ud*100/G_cont1   
                
    if cont_G_SB !=0 and G_cont2 !=0:
       G_prom2=G_cont_SB*100/G_cont2
                    
    if cont_G_MA !=0 and G_cont3 !=0:
       G_prom3=G_cont_MA*100/G_cont3
                    
    if cont_G_BB !=0 and G_cont4 !=0:
       G_prom4=G_cont_BB*100/G_cont5
                    
    if cont_G_Total !=0 and G_cont5 !=0:
       G_prom5=G_cont_Total*100/G_cont5
            
            
            
    H_ganador=''
    cont_H_ML=0
    cont_H_SP=0
    cont_H_Ud=0
    cont_H_SB=0
    cont_H_MA=0
    cont_H_BB=0
    cont_H_Total=0
    H_cont=0
    H_cont1=0
    H_cont2=0
    H_cont3=0
    H_cont4=0
    H_cont5=0
    H_cont6=0
    H_sum=0
    H_res=0
    H_valor_izquierdo=0
    H_valor_derecho=0
    H_prom=0
    H_prom1=0
    H_prom2=0
    H_prom3=0
    H_prom4=0 
    H_prom5=0        
    H_prom6=0
        
            
    for valor in partidos: 
        
        H_valor_izquierdo, H_valor_derecho = extraer_valores_de_resultado(valor)
        H_sum = H_valor_izquierdo + H_valor_derecho
                        
        if valor.H_ML_equip is not None:
           H_cont+=1
           if H_ganador==valor.H_ML_equip.nombre:
              H_cont_ML+=1 
                        
        if valor.H_Ud_equip is not None:
           H_cont1+=1      
           if H_ganador==valor.H_Ud_equip.nombre:
              H_cont_Ud+=1
                        
        if valor.H_SB_equip is not None: 
           H_cont2+=1      
           if H_ganador==valor.H_SB_equip.nombre:
              H_cont_SB+=1
                        
        if valor.H_MA is not None:
           H_cont3+=1 
           if H_ganador==valor.H_MA.nombre:
              H_cont_MA+=1
                        
        if valor.H_BB is not None:  
           H_cont4+=1 
           if H_ganador==valor.H_BB.nombre:
              H_cont_BB+=1
                    
                    
        if valor.H_total_punto is not None: 
           H_cont5+=1 
           if H_sum>H_valor_izquierdo and valor.H_Total_OU=='OVER':
              H_cont_Total+=1
           if H_sum<=valor.H_total_punto and valor.H_Total_OU=='UNDER':
              H_cont_Total+=1
                    
                    
        if H_valor_izquierdo>H_valor_derecho:
                H_res=H_valor_izquierdo-H_valor_derecho
                    
        elif H_valor_izquierdo<H_valor_derecho:
                H_res=H_valor_derecho-H_valor_izquierdo 
                
        else: 
                H_res=0
                        
        if valor.H_SP_dif is not None:
           H_cont6+=1
           if H_ganador==valor.H_SP_equip.nombre and H_res>valor.H_SP_dif :
              H_cont_SP+=1
            
           
    if cont_H_ML !=0 and H_cont !=0:
       H_prom=H_cont_ML*100/H_cont
                    
    if cont_H_SP !=0 and H_cont6 !=0:
       H_prom6=H_cont_SP*100/H_cont6
                    
    if cont_H_Ud !=0 and H_cont1 !=0:
       H_prom1=H_cont_Ud*100/H_cont1   
                
    if cont_H_SB !=0 and H_cont2 !=0:
       H_prom2=H_cont_SB*100/H_cont2
                    
    if cont_H_MA !=0 and H_cont3 !=0:
       H_prom3=H_cont_MA*100/H_cont3
                    
    if cont_H_BB !=0 and H_cont4 !=0:
       H_prom4=H_cont_BB*100/H_cont5
                    
    if cont_H_Total !=0 and H_cont5 !=0:
       H_prom5=H_cont_Total*100/H_cont5        
            
    
    
    I_ganador=''
    cont_I_ML=0
    cont_I_SP=0
    cont_I_Ud=0
    cont_I_SB=0
    cont_I_MA=0
    cont_I_BB=0
    cont_I_Total=0
    I_cont=0
    I_cont1=0
    I_cont2=0
    I_cont3=0
    I_cont4=0
    I_cont5=0
    I_cont6=0
    I_sum=0
    I_res=0
    I_valor_izquierdo=0
    I_valor_derecho=0
    I_prom=0
    I_prom1=0
    I_prom2=0
    I_prom3=0
    I_prom4=0 
    I_prom5=0        
    I_prom6=0
        
            
    for valor in partidos: 
        
        I_valor_izquierdo, I_valor_derecho = extraer_valores_de_resultado(valor)
        I_sum = I_valor_izquierdo + I_valor_derecho
                        
        if valor.I_ML_equip is not None:
           I_cont+=1
           if I_ganador==valor.I_ML_equip.nombre:
              I_cont_ML+=1 
                        
        if valor.I_Ud_equip is not None:
           I_cont1+=1      
           if I_ganador==valor.I_Ud_equip.nombre:
              I_cont_Ud+=1
                        
        if valor.I_SB_equip is not None: 
           I_cont2+=1      
           if I_ganador==valor.I_SB_equip.nombre:
              I_cont_SB+=1
                        
        if valor.I_MA is not None:
           I_cont3+=1 
           if I_ganador==valor.I_MA.nombre:
              I_cont_MA+=1
                        
        if valor.I_BB is not None:  
           I_cont4+=1 
           if I_ganador==valor.I_BB.nombre:
              I_cont_BB+=1
                    
                    
        if valor.I_total_punto is not None: 
           I_cont5+=1 
           if I_sum>I_valor_izquierdo and valor.I_Total_OU=='OVER':
              I_cont_Total+=1
           if I_sum<=valor.I_total_punto and valor.I_Total_OU=='UNDER':
              I_cont_Total+=1
                    
                    
        if I_valor_izquierdo>I_valor_derecho:
                I_res=I_valor_izquierdo-I_valor_derecho
                    
        elif I_valor_izquierdo<I_valor_derecho:
                I_res=I_valor_derecho-I_valor_izquierdo 
                
        else: 
                I_res=0
                        
        if valor.I_SP_dif is not None:
           I_cont6+=1
           if I_ganador==valor.I_SP_equip.nombre and I_res>valor.I_SP_dif :
              I_cont_SP+=1
            
           
    if cont_I_ML !=0 and I_cont !=0:
       I_prom=I_cont_ML*100/I_cont
                        
    if cont_I_SP !=0 and I_cont6 !=0:
       I_prom6=I_cont_SP*100/I_cont6
                        
    if cont_I_Ud !=0 and I_cont1 !=0:
       I_prom1=I_cont_Ud*100/I_cont1   
                    
    if cont_I_SB !=0 and I_cont2 !=0:
       I_prom2=I_cont_SB*100/I_cont2
                        
    if cont_I_MA !=0 and I_cont3 !=0:
       I_prom3=I_cont_MA*100/I_cont3
                        
    if cont_I_BB !=0 and I_cont4 !=0:
       I_prom4=I_cont_BB*100/I_cont5
                        
    if cont_I_Total !=0 and I_cont5 !=0:
       I_prom5=I_cont_Total*100/I_cont5        
            
            
    J_ganador=''
    cont_J_ML=0
    cont_J_SP=0
    cont_J_Ud=0
    cont_J_SB=0
    cont_J_MA=0
    cont_J_BB=0
    cont_J_Total=0
    J_cont=0
    J_cont1=0
    J_cont2=0
    J_cont3=0
    J_cont4=0
    J_cont5=0
    J_cont6=0
    J_sum=0
    J_res=0
    J_valor_izquierdo=0
    J_valor_derecho=0
    J_prom=0
    J_prom1=0
    J_prom2=0
    J_prom3=0
    J_prom4=0 
    J_prom5=0        
    J_prom6=0
        
    for valor in partidos: 
        
        J_valor_izquierdo, J_valor_derecho = extraer_valores_de_resultado(valor)
        J_sum = J_valor_izquierdo + J_valor_derecho
                            
        if valor.J_ML_equip is not None:
           J_cont+=1
           if J_ganador==valor.J_ML_equip.nombre:
              J_cont_ML+=1 
                            
        if valor.J_Ud_equip is not None:
           J_cont1+=1      
           if J_ganador==valor.J_Ud_equip.nombre:
              J_cont_Ud+=1
                            
        if valor.J_SB_equip is not None: 
           J_cont2+=1      
           if J_ganador==valor.J_SB_equip.nombre:
              J_cont_SB+=1
                            
        if valor.J_MA is not None:
           J_cont3+=1 
           if J_ganador==valor.J_MA.nombre:
              J_cont_MA+=1
                            
        if valor.J_BB is not None:  
           J_cont4+=1 
           if J_ganador==valor.J_BB.nombre:
              J_cont_BB+=1
                        
                        
        if valor.J_total_punto is not None: 
           J_cont5+=1 
           if J_sum>J_valor_izquierdo and valor.J_Total_OU=='OVER':
              J_cont_Total+=1
           if J_sum<=valor.J_total_punto and valor.J_Total_OU=='UNDER':
              J_cont_Total+=1
                        
                        
        if J_valor_izquierdo>J_valor_derecho:
                J_res=J_valor_izquierdo-J_valor_derecho
                        
        elif J_valor_izquierdo<J_valor_derecho:
                J_res=J_valor_derecho-J_valor_izquierdo 
                    
        else: 
                J_res=0
                            
        if valor.J_SP_dif is not None:
           J_cont6+=1
           if J_ganador==valor.J_SP_equip.nombre and J_res>valor.J_SP_dif :
              J_cont_SP+=1
            
           
    if cont_J_ML !=0 and J_cont !=0:
       J_prom=J_cont_ML*100/J_cont
                            
    if cont_J_SP !=0 and J_cont6 !=0:
       J_prom6=J_cont_SP*100/J_cont6
                            
    if cont_J_Ud !=0 and J_cont1 !=0:
       J_prom1=J_cont_Ud*100/J_cont1   
                        
    if cont_J_SB !=0 and J_cont2 !=0:
       J_prom2=J_cont_SB*100/J_cont2
                            
    if cont_J_MA !=0 and J_cont3 !=0:
       J_prom3=J_cont_MA*100/J_cont3
                            
    if cont_J_BB !=0 and J_cont4 !=0:
       J_prom4=J_cont_BB*100/J_cont5
                            
    if cont_J_Total !=0 and J_cont5 !=0:
       J_prom5=J_cont_Total*100/J_cont5      
       
       
    mejor_prom_ML=0
    mejor_prom_SP=0
    mejor_prom_T=0
    mejor_prom_Ud=0
    mejor_prom_SB=0
    mejor_prom_MA=0     
    mejor_prom_BB=0
    nombre_s=0
    nombre_s1=0
    nombre_s2=0
    nombre_s3=0
    nombre_s4=0
    nombre_s5=0
    nombre_s6=0
    
    
    list_ML=[A_prom,B_prom,C_prom,D_prom,E_prom,F_prom,G_prom,H_prom,I_prom,J_prom]
    list_SP=[A_prom6,B_prom6,C_prom6,D_prom6,E_prom6,F_prom6,G_prom6,H_prom6,I_prom6,J_prom6]
    list_T=[A_prom5,B_prom5,C_prom5,D_prom5,E_prom5,F_prom5,G_prom5,H_prom5,I_prom5,J_prom5]
    list_Ud=[A_prom1,B_prom1,C_prom1,D_prom1,E_prom1,F_prom1,G_prom1,H_prom1,I_prom1,J_prom1]     
    list_SB=[A_prom2,B_prom2,C_prom2,D_prom2,E_prom2,F_prom2,G_prom2,H_prom2,I_prom2,J_prom2]
    list_MA=[A_prom3,B_prom3,C_prom3,D_prom3,E_prom3,F_prom3,G_prom3,H_prom3,I_prom3,J_prom3]
    list_BB=[A_prom4,B_prom4,C_prom4,D_prom4,E_prom4,F_prom4,G_prom4,H_prom4,I_prom4,J_prom4]
    
    lista_sistemas=['VeriBet','Action Network','Sports Insights','PFF','Covers','Team Rankings','BetQL','Odds Jams','Scores and Odds','Betting on Cash']
       
    for indice,i in enumerate(list_ML):
        if i>mejor_prom_ML:
           mejor_prom_ML=i   
           nombre_s=indice
           
        
    for indice,i in enumerate(list_SP):
        if i>mejor_prom_SP:
           mejor_prom_SP=i        
           nombre_s1=indice
            
    for indice,i in enumerate( list_T):
        if i>mejor_prom_T:
           mejor_prom_T=i         
           nombre_s2=indice
           
    for indice,i in enumerate(list_Ud):
        if i>mejor_prom_Ud:
           mejor_prom_Ud=i 
           nombre_s3=indice
           
    for indice,i in enumerate(list_SB):
        if i>mejor_prom_SB:
           mejor_prom_SB=i 
           nombre_s4=indice
           
    for indice,i in enumerate(list_MA):
        if i>mejor_prom_MA:
           mejor_prom_MA=i 
           nombre_s5=indice
           
    for indice,i in enumerate(list_BB):
        if i>mejor_prom_BB:
           mejor_prom_BB=i 
           nombre_s6=indice
           
           
           
           
           
    for indice,i in enumerate(lista_sistemas):
        if nombre_s==indice:
           nombre_s=i       
           break
              
    for indice,i in enumerate(lista_sistemas):
        if nombre_s1==indice:
           nombre_s1=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s2==indice:
           nombre_s2=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s3==indice:
           nombre_s3=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s4==indice:
           nombre_s4=i       
           break
    
    for indice,i in enumerate(lista_sistemas):
        if nombre_s5==indice:
           nombre_s5=i       
           break
       
    for indice,i in enumerate(lista_sistemas):
        if nombre_s6==indice:
           nombre_s6=i       
           break          
              
              
              
              
    return render(request,'NBA_Colegial/resultados_sistemas.html', {'cont_A_ML':cont_A_ML, 'cont_A_SP':cont_A_SP, 'cont_A_Ud':cont_A_Ud, 
                                                              'cont_A_MA':cont_A_MA,'cont_A_SB':cont_A_SB,'cont_A_BB':cont_A_BB,
                                                              'cont_A_Total':cont_A_Total,'A_cont':A_cont,'A_cont1':A_cont1,'A_cont2':A_cont2,
                                                              'A_cont3':A_cont3,'A_cont4':A_cont4,'A_cont5':A_cont5,'A_cont6':A_cont6, 
                                                              'A_prom':A_prom,'A_prom1':A_prom1,'A_prom2':A_prom2,'A_prom3':A_prom3,'A_prom4':A_prom4,
                                                              'A_prom5':A_prom5,'A_prom6':A_prom6,'cont_B_ML': cont_B_ML, 'cont_B_SP': cont_B_SP, 
                                                              'cont_B_Ud': cont_B_Ud, 'cont_B_MA': cont_B_MA, 'cont_B_SB': cont_B_SB, 'cont_B_BB': cont_B_BB,
                                                              'cont_B_Total': cont_B_Total, 'B_cont': B_cont, 'B_cont1': B_cont1, 'B_cont2': B_cont2,
                                                              'B_cont3': B_cont3, 'B_cont4': B_cont4, 'B_cont5': B_cont5, 'B_cont6': B_cont6, 'B_prom': B_prom,
                                                              'B_prom1': B_prom1, 'B_prom2': B_prom2, 'B_prom3': B_prom3, 'B_prom4': B_prom4, 'B_prom5': B_prom5, 
                                                              'B_prom6': B_prom6,'cont_C_ML': cont_C_ML, 'cont_C_SP': cont_C_SP, 'cont_C_Ud': cont_C_Ud, 
                                                              'cont_C_MA': cont_C_MA, 'cont_C_SB': cont_C_SB, 'cont_C_BB': cont_C_BB, 'cont_C_Total': cont_C_Total,
                                                              'C_cont': C_cont, 'C_cont1': C_cont1, 'C_cont2': C_cont2, 'C_cont3': C_cont3, 'C_cont4': C_cont4,
                                                              'C_cont5': C_cont5, 'C_cont6': C_cont6, 'C_prom': C_prom, 'C_prom1': C_prom1, 'C_prom2': C_prom2,
                                                              'C_prom3': C_prom3, 'C_prom4': C_prom4, 'C_prom5': C_prom5, 'C_prom6': C_prom6, 'cont_D_ML': cont_D_ML,
                                                              'cont_D_SP': cont_D_SP, 'cont_D_Ud': cont_D_Ud, 'cont_D_MA': cont_D_MA, 'cont_D_SB': cont_D_SB,
                                                              'cont_D_BB': cont_D_BB, 'cont_D_Total':cont_D_Total, 'D_cont': D_cont, 'D_cont1': D_cont1,
                                                              'D_cont2': D_cont2, 'D_cont3': D_cont3, 'D_cont4': D_cont4,'D_cont5': D_cont5, 'D_cont6': D_cont6,
                                                              'D_prom': D_prom, 'D_prom1': D_prom1, 'D_prom2': D_prom2,'D_prom3': D_prom3, 'D_prom4': D_prom4, 
                                                              'D_prom5': D_prom5, 'D_prom6': D_prom6, 'cont_E_ML': cont_E_ML, 'cont_E_SP': cont_E_SP, 
                                                              'cont_E_Ud': cont_E_Ud, 'cont_E_MA': cont_E_MA, 'cont_E_SB': cont_E_SB, 'cont_E_BB': cont_E_BB, 
                                                              'cont_E_Total': cont_E_Total,'E_cont': E_cont, 'E_cont1': E_cont1, 'E_cont2': E_cont2, 'E_cont3': E_cont3,
                                                              'E_cont4': E_cont4,'E_cont5': E_cont5, 'E_cont6': E_cont6, 'E_prom': E_prom, 'E_prom1': E_prom1, 
                                                              'E_prom2': E_prom2,'E_prom3': E_prom3, 'E_prom4': E_prom4, 'E_prom5': E_prom5, 'E_prom6': E_prom6,
                                                              'cont_F_ML': cont_F_ML, 'cont_F_SP': cont_F_SP, 'cont_F_Ud': cont_F_Ud, 'cont_F_MA': cont_F_MA, 
                                                              'cont_F_SB': cont_F_SB, 'cont_F_BB': cont_F_BB, 'cont_F_Total': cont_F_Total,'F_cont': F_cont, 
                                                              'F_cont1': F_cont1, 'F_cont2': F_cont2, 'F_cont3': F_cont3,'F_cont4': F_cont4,'F_cont5': F_cont5, 
                                                              'F_cont6': F_cont6, 'F_prom': F_prom, 'F_prom1': F_prom1, 'F_prom2': F_prom2,'F_prom3': F_prom3, 
                                                              'F_prom4': F_prom4, 'F_prom5': F_prom5, 'F_prom6': F_prom6,'cont_G_ML': cont_G_ML, 'cont_G_SP': cont_G_SP,
                                                              'cont_G_Ud': cont_G_Ud, 'cont_G_MA':cont_G_MA, 'cont_G_SB':cont_G_SB, 'cont_G_BB': cont_G_BB,
                                                              'cont_G_Total':cont_G_Total,'G_cont': G_cont, 'G_cont1': G_cont1, 'G_cont2': G_cont2, 'G_cont3': G_cont3,
                                                              'G_cont4': G_cont4,'G_cont5': G_cont5, 'G_cont6': G_cont6, 'G_prom': G_prom, 'G_prom1': G_prom1, 
                                                              'G_prom2': G_prom2,'G_prom3': G_prom3, 'G_prom4': G_prom4, 'G_prom5': G_prom5, 'G_prom6': G_prom6,
                                                              'cont_H_ML': cont_H_ML, 'cont_H_SP': cont_H_SP, 'cont_H_Ud': cont_H_Ud, 'cont_H_MA':cont_H_MA,
                                                              'cont_H_SB': cont_H_SB, 'cont_H_BB': cont_H_BB, 'cont_H_Total':cont_H_Total,'H_cont': H_cont,
                                                              'H_cont1': H_cont1, 'H_cont2': H_cont2, 'H_cont3': H_cont3,'H_cont4': H_cont4,'H_cont5': H_cont5,
                                                              'H_cont6': H_cont6, 'H_prom': H_prom, 'H_prom1': H_prom1, 'H_prom2': H_prom2,'H_prom3': H_prom3, 
                                                              'H_prom4': H_prom4, 'H_prom5': H_prom5, 'H_prom6': H_prom6,'cont_I_ML': cont_I_ML, 'cont_I_SP': cont_I_SP,
                                                              'cont_I_Ud': cont_I_Ud, 'cont_I_MA': cont_I_MA, 'cont_I_SB': cont_I_SB, 'cont_I_BB': cont_I_BB, 
                                                              'cont_I_Total': cont_I_Total,'I_cont': I_cont, 'I_cont1': I_cont1, 'I_cont2': I_cont2, 'I_cont3': I_cont3,
                                                              'I_cont4': I_cont4,'I_cont5': I_cont5, 'I_cont6': I_cont6, 'I_prom': I_prom, 'I_prom1': I_prom1,
                                                              'I_prom2': I_prom2,'I_prom3': I_prom3, 'I_prom4': I_prom4, 'I_prom5': I_prom5, 'I_prom6': I_prom6,
                                                              'cont_J_ML': cont_J_ML, 'cont_J_SP': cont_J_SP, 'cont_J_Ud': cont_J_Ud, 'cont_J_MA': cont_J_MA,
                                                              'cont_J_SB': cont_J_SB, 'cont_J_BB':cont_J_BB, 'cont_J_Total': cont_J_Total,'J_cont': J_cont, 
                                                              'J_cont1': J_cont1, 'J_cont2': J_cont2, 'J_cont3': J_cont3,'J_cont4': J_cont4,'J_cont5': J_cont5, 
                                                              'J_cont6': J_cont6, 'J_prom': J_prom, 'J_prom1': J_prom1, 'J_prom2': J_prom2,'J_prom3': J_prom3, 
                                                              'J_prom4': J_prom4, 'J_prom5': J_prom5, 'J_prom6': J_prom6,'nombre_s':nombre_s,'nombre_s1':nombre_s1,
                                                              'nombre_s2':nombre_s2,'nombre_s3':nombre_s3,'nombre_s4':nombre_s4,'nombre_s5':nombre_s5,'nombre_s6':nombre_s6,
                                                              'mejor_prom_ML':mejor_prom_ML,'mejor_prom_SP':mejor_prom_SP,'mejor_prom_T':mejor_prom_T,
                                                              'mejor_prom_Ud':mejor_prom_Ud,'mejor_prom_SB':mejor_prom_SB,'mejor_prom_MA':mejor_prom_MA,'mejor_prom_BB':mejor_prom_BB,  })
   








