from django.db import models


# Create your models here.


class equipos_futbol (models.Model):
    nombre=models.CharField(max_length=100,verbose_name='Nombre')
    logo=models.ImageField(upload_to='logo')
   
    def __str__(self):
      return str(self.nombre)
   
class equipos_NLF_profecional (models.Model):
    nombre= models.CharField(max_length=100,verbose_name='Nombre')
    logo=models.ImageField(upload_to='logo')
    
    def __str__(self):
      return str(self.nombre)
    
class equipos_NLF_colegial (models.Model):
    nombre= models.CharField(max_length=100,verbose_name='Nombre')
    logo=models.ImageField(upload_to='logo')
   
    def __str__(self):
      return str(self.nombre)
     
class equipos_NBA_profecional (models.Model):
    nombre= models.CharField(max_length=100,verbose_name='Nombre')
    logo=models.ImageField(upload_to='logo/')
    
    def __str__(self):
      return str(self.nombre)
    
class equipos_NBA_colegial (models.Model):
    nombre= models.CharField(max_length=100,verbose_name='Nombre')
    logo=models.ImageField(upload_to='logo')
   
    def __str__(self):
      return str(self.nombre)
   
class equipos_hockey (models.Model):
    nombre= models.CharField(max_length=100,verbose_name='Nombre')
    logo=models.ImageField(upload_to='logo')
    
    def __str__(self):
      return str(self.nombre)
    
class equipos_baseball (models.Model):
    nombre= models.CharField(max_length=100,verbose_name='Nombre')
    logo=models.ImageField(upload_to='logo')
    
    def __str__(self):
      return str(self.nombre)
    
class total (models.Model):
    nombre= models.CharField(max_length=100,verbose_name='Nombre')
    
    def __str__(self):
      return str(self.nombre)