from django.db import models
from sales.models import Sales
from inventory.models import Material

class Profit(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad")
    date = models.DateField(verbose_name="Fecha")
    fk_sale = models.ForeignKey(Sales, on_delete=models.CASCADE, verbose_name="Venta")

    def save(self, *args, **kwargs):
        # Asigna la cantidad y la fecha de la venta a los campos correspondientes en Profit
        self.quantity = self.fk_sale.amount * self.fk_sale.service.price
        self.date = self.fk_sale.date
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ganancia de {self.fk_sale.user.username} el {self.date}"

    class Meta:
        verbose_name = 'Ganancia' 
        verbose_name_plural = 'Ganancias'
        db_table = 'ganancias' 
        ordering = ['id']

class Expenditure(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad")
    description = models.TextField(max_length=500, verbose_name="Descripcion")
    fecha = models.DateField(verbose_name="Date")
    fk_product = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material")
    
    def __str__(self):
        return f"Gasto: {self.descripcion} el {self.fecha}"
    
    class Meta:
        verbose_name = 'Gasto' 
        verbose_name_plural = 'Gastos'
        db_table = 'gastos' 
        ordering = ['id'] 