# Generated by Django 4.2.7 on 2023-12-10 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('fk_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.sales', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'Ganancia',
                'verbose_name_plural': 'Ganancias',
                'db_table': 'ganancias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad')),
                ('description', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('fecha', models.DateField(verbose_name='Date')),
                ('fk_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.material', verbose_name='Material')),
            ],
            options={
                'verbose_name': 'Gasto',
                'verbose_name_plural': 'Gastos',
                'db_table': 'gastos',
                'ordering': ['id'],
            },
        ),
    ]
