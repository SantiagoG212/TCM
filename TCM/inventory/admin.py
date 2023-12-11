from django.contrib import admin
from .models import Inventory, Material
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class MaterialResource(resources.ModelResource):
    class Meta:
        model = Material
        fields = ('inventory__material_type', 'name', 'type', 'description')

class InventoryResource(resources.ModelResource):
    class Meta:
        model = Inventory
        fields = ('material_type', 'amount', 'entrance', 'stock')

@admin.register(Material)
class MaterialAdmin(ImportExportModelAdmin):
    resource_class = MaterialResource  # Asociar el recurso con el modelo
    list_display = ('inventory', 'name', 'type', 'description')
    list_editable = ('name', 'type', 'description')
    search_fields = ('inventory__material_type', 'name', 'type', 'description')
    list_filter = ('inventory__material_type',)
    ordering = ['name']

@admin.register(Inventory)
class InventoryAdmin(ImportExportModelAdmin):
    resource_class = InventoryResource  # Asociar el recurso con el modelo
    list_display = ('material_type', 'amount', 'entrance', 'stock')
    list_editable = ('amount', 'entrance', 'stock')
    search_fields = ('material_type', 'amount', 'entrance', 'stock')
    ordering = ['material_type']


# Register your models here.
