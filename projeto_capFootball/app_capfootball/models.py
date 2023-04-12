from django.db import models

# Create your models here.
class jogos(models.Model):  
    
    times = models.CharField(max_length=100, default=None)  
    dia = models.CharField(max_length=50,default=None) 
    horario = models.CharField(max_length=10, default=None) 
    data = models.DateField(max_length=15, default=None)  
    class Meta:  
        db_table = "jogos"  

class administradores(models.Model):
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=30)
    class Meta:
        db_table = "administradores"