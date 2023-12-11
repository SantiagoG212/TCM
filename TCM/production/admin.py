from django.contrib import admin
from .models import Process, Activities, Salary
from .models import PerfilUsuario
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Process)
class ProcessAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')  
    ordering = ['name']
    
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_production_daily', 'total_production_weekly', 'total_production_monthly')

@admin.register(Activities)
class ActivitiesAdmin(ImportExportModelAdmin):
    list_display = ('date', 'pay', 'description', 'repetitions', 'estimated_time', 'user')
    list_editable = ('description', 'repetitions', 'estimated_time')
    search_fields = ('date', 'pay', 'description', 'repetitions', 'estimated_time', 'user__username', 'activities_process__name')
    ordering = ['date']
    
    def save_model(self, request, obj, form, change):
        # Guarda el objeto primero
        super().save_model(request, obj, form, change)

        # Establece la relación después de que el objeto se ha guardado
        obj.activities_process.set(form.cleaned_data['activities_process'])

@admin.register(Salary)
class SalaryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'last_name', 'subtotal', 'total')
    list_editable = ('last_name', 'subtotal', 'total')
    search_fields = ('name', 'last_name', 'subtotal', 'total')
    ordering = ['name']
    list_display_links = ['name']

class ProcessResource(resources.ModelResource):
    class Meta:
        model = Process
        fields = ('name', 'description')

class ActivitiesResource(resources.ModelResource):
    class Meta:
        model = Activities
        fields = ('date', 'pay', 'description', 'repetitions', 'estimated_time', 'user__username', 'activities_process__name')

class SalaryResource(resources.ModelResource):
    class Meta:
        model = Salary
        fields = ('name', 'last_name', 'subtotal', 'total')