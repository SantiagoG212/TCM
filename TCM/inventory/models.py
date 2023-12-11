from django.db import models

    
class Inventory(models.Model):
    material_type = models.CharField(max_length=50, verbose_name="Tipo Material")
    amount = models.IntegerField(verbose_name="Cantidad")
    entrance = models.DateField(max_length=50, verbose_name="Fecha de Entrada")
    stock = models.IntegerField(verbose_name="Existencias")

    class Meta:
        verbose_name_plural = "Inventarios"
        ordering = ['material_type']

    def __str__(self):
        return f'{self.material_type} - {self.amount}'    

class Material(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name="Material")
    name = models.CharField(max_length=50, verbose_name="Nombre material")
    type = models.CharField(max_length=50, verbose_name="Tipo material")
    description = models.CharField(max_length=50, verbose_name="Descripcion del material")
    
    class Meta:
        verbose_name_plural = "Materiales"
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.type}'