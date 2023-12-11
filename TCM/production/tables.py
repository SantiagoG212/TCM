import django_tables2 as tables
from .models import Activities

class ActivitiesTable(tables.Table):
    class Meta:
        model = Activities
        template_name = 'produccion/salario.html'