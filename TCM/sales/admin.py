from django.contrib import admin
from .models import Categories, Services, Sales
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Categories)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ['id']

@admin.register(Services)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'price', 'difficulty', 'fk_idcategory')
    list_editable = ('price', 'difficulty', 'fk_idcategory')
    search_fields = ('name',)
    list_filter = ('fk_idcategory',)
    ordering = ['id']

@admin.register(Sales)
class SalesAdmin(ImportExportModelAdmin):
    list_display = ('name', 'pay', 'amount', 'date', 'user', 'service', 'completed')
    search_fields = ('pay', 'amount', 'date')
    list_display_links = ('date',)  # Eliminé 'amount' de list_display_links
    ordering = ['id']
    
class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories
        fields = ('name', 'description')

class ServicesResource(resources.ModelResource):
    class Meta:
        model = Services
        fields = ('name', 'description', 'price', 'difficulty', 'fk_idcategory')

class SalesResource(resources.ModelResource):
    class Meta:
        model = Sales
        fields = ('pay', 'amount', 'date', 'services_sales')

    
 