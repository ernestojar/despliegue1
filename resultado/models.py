from django.db import models
from aplication.models import futbol, Baseball, NBA_Profecional,NBA_Colegial,NLF_Profecional,NLF_Colegial,Hockey


# Create your models here.


class resultado_futbol (models.Model):
   partido=models.OneToOneField(futbol,verbose_name='Partido',on_delete=models.CASCADE) 
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')
   
class resultado_baseball (models.Model):
   partido=models.OneToOneField(Baseball,verbose_name='Partido',on_delete=models.CASCADE) 
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')
   
class resultado_NBA_profecional (models.Model):
   partido=models.OneToOneField(NBA_Profecional,verbose_name='Partido',on_delete=models.CASCADE) 
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')
   
   
class resultado_NBA_colegial (models.Model):
   partido=models.OneToOneField(NBA_Colegial,verbose_name='Partido',on_delete=models.CASCADE) 
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')
   
   
class resultado_NLF_profecional (models.Model):
   partido=models.OneToOneField(NLF_Profecional,verbose_name='Partido',on_delete=models.CASCADE) 
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')
   
   
class resultado_NLF_colegial (models.Model):
   partido=models.OneToOneField(NLF_Colegial,verbose_name='Partido',on_delete=models.CASCADE) 
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')
   
   
class resultado_Hockey (models.Model):
   partido=models.OneToOneField(Hockey,verbose_name='Partido',on_delete=models.CASCADE) 
   resultado=models.CharField(max_length=100,verbose_name='Resultado',default='0-0')
   ganador=models.CharField(max_length=100,verbose_name='Ganador',default='Empate')