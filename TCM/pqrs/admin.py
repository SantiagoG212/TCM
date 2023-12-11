from django.contrib import admin
from .models import PQRS, AnswerPQRS
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(AnswerPQRS)
class AnswerPQRSAdmin(ImportExportModelAdmin):
    list_display = ('answer', 'response_date')
    search_fields = ('answer', 'response_date')
    ordering = ['-response_date']

@admin.register(PQRS)
class PQRSAdmin(ImportExportModelAdmin):
    list_display = ('case', 'description', 'creation_date', 'user')
    search_fields = ('case', 'description', 'creation_date', 'user')
    ordering = ['-creation_date']

class AnswerPQRSResource(resources.ModelResource):
    class Meta:
        model = AnswerPQRS
        fields = ('answer', 'response_date', 'pqrs__case')

class PQRSResource(resources.ModelResource):
    class Meta:
        model = PQRS
        fields = ('case', 'description', 'creation_date')
