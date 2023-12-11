from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la Categoria")
    description = models.TextField(verbose_name="Descripcion de la Categoria")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria' 
        verbose_name_plural = 'Categorias'
        db_table = 'categorias' 
        ordering = ['id'] 

class Services(models.Model):
    name = models.CharField(max_length=50, verbose_name= "Nombre del Servicio")
    description = models.TextField(verbose_name= "Descripcion del Servicio")
    price = models.FloatField(verbose_name= "Coste Unitario")
    difficulty = models.CharField(max_length=20, verbose_name= "Dificultad")
    fk_idcategory = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Categoria")
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Servicio' 
        verbose_name_plural = 'Servicios'
        db_table = 'servicios' 
        ordering = ['id'] 
    
class Sales(models.Model):
    name = models.CharField(max_length=50, verbose_name="Solicitud")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    amount = models.IntegerField(verbose_name="Cantidad")
    date = models.DateField(verbose_name="Fecha")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Servicio")
    pay = models.FloatField(verbose_name="Pago")
    completed = models.BooleanField(default=False, verbose_name="Completada")

    def save(self, *args, **kwargs):
        self.pay = self.amount * self.service.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'ventas'
        ordering = ['id']
