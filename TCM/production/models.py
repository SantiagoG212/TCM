from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Process(models.Model): 
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=50, verbose_name="Descripcion")
  
    class Meta:
        verbose_name_plural = "Procesos"
        ordering = ['name']

    def __str__(self):
        return self.name
    
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_production = models.FloatField(default=0)
    total_production_daily = models.FloatField(default=0)
    total_production_weekly = models.FloatField(default=0)
    total_production_monthly = models.FloatField(default=0)
    total_production_yearly = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
    
class Activities(models.Model):
    date = models.DateField(verbose_name="Fecha", default=timezone.now)
    description = models.CharField(max_length=50, verbose_name="Descripcion")
    repetitions = models.FloatField(verbose_name="Repeticiones")
    estimated_time = models.CharField(max_length=50, verbose_name="Tiempo estimado")
    activities_process = models.ManyToManyField('Process')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Empleado", default=None)
    pay = models.FloatField(verbose_name="Pago")
    completed = models.BooleanField(default=False, verbose_name="Completada")
    
        
    class Meta:
        verbose_name_plural = "Actividades"
        ordering = ['date']

    def __str__(self):
        return f'{self.date} - {self.description}'
    
class Salary(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    subtotal = models.CharField(max_length=50, verbose_name="Subtotal")
    total = models.CharField(max_length=50, verbose_name="Total")
    
    class Meta:
        verbose_name_plural = "Salarios"
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.last_name} - {self.total}'
