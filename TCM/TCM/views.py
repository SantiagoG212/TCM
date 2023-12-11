from decimal import Decimal, DecimalException
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import login as auth_login, logout, authenticate
from sales.forms import RegistroUsuarioForm
from django.contrib.auth.models import Group
from production.models import Activities, PerfilUsuario
from django.shortcuts import get_object_or_404
from sales.forms import RegistroUsuarioForm, SalesForm
from sales.models import Services, Sales
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from production.forms import CompletarActividadForm
from django.utils import timezone
from datetime import datetime, timedelta
from django.db import transaction
from django_tables2 import RequestConfig
from production.tables import ActivitiesTable
from pqrs.forms import PQRSForm
from pqrs.models import PQRS

def index(request):
    return render(request,'index/index.html',{
    })
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))

            # Verificar si el usuario pertenece al grupo "Empleados"
            if user.groups.filter(name='Empleados').exists():
                return redirect('empleado')  # Redirigir a la vista de empleados
            else:
                return redirect('home')  # Redirigir a la vista de gerencia
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'dashboard/login.html', {

    })

def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha sido creado')
        else:
            messages.success(request, f'Error durante la creacion del usuario')
    else:
        form = RegistroUsuarioForm()
    context = { 'form' : form}
    return render(request, 'register/registro.html', context)

@login_required(login_url='login')
def home(request):
    user = request.user
    group_name = None
    if user.is_authenticated:
        group = Group.objects.filter(user=user).first()
        if group:
            group_name = group.name
    grupo = group_name        
    return render(request,'index/admin.html', {"grupo":grupo
        })

@login_required(login_url='login')
def solicitudes(request):
    sales_list = Sales.objects.filter(user=request.user)
    return render(request, 'actividades/actividades.html', {'sales': sales_list})
def nueva_actividad(request):
    return render(request,'actividades/actividad_nueva.html',{
    })
def editar_actividad(request):
    return render(request,'actividades/editar_actividad.html',{
    })
def servicios(request):
    serivices = Services.objects.all()
    return render(request,'ganancias/ganancias.html', {"servicios": serivices})

@login_required(login_url='login')
def solicitud_compra(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Su solicitud de compra ha sido enviada')
            return redirect('servicios')
        else:
            messages.success(request, f'Error durante el envio de la solicitud')
    else:
        form = SalesForm()
    context = { 'form' : form}
    return render(request, 'ganancias/nueva_ganancia.html', context)


@transaction.atomic
@login_required(login_url='login')
def veractividades(request):
    user = request.user
    group_name = None
    if user.is_authenticated:
        group = Group.objects.filter(user=user).first()
        if group:
            group_name = group.name
    grupo = group_name

    # Obtener o crear el perfil de usuario
    perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=request.user)

    # Obtener la fecha actual
    today = datetime.now().date()

    # Obtener el total de producción diario
    total_production_daily = Activities.objects.filter(user=request.user, date=today, completed=True).aggregate(Sum('pay'))['pay__sum'] or 0
    
    # Restablecer el total de producción diario en el perfil del usuario
    perfil_usuario.total_production_daily = float(total_production_daily)
    perfil_usuario.save()

    # Obtener el número de semana actual
    current_week = today.isocalendar()[1]

    # Obtener el total de producción semanal
    total_production_weekly = Activities.objects.filter(user=request.user, date__week=current_week, completed=True).aggregate(Sum('pay'))['pay__sum'] or 0

    # Obtener el total de producción mensual
    total_production_monthly = Activities.objects.filter(user=request.user, date__month=today.month, completed=True).aggregate(Sum('pay'))['pay__sum'] or 0

    # Obtener el total de producción anual
    total_production_yearly = Activities.objects.filter(user=request.user, date__year=today.year, completed=True).aggregate(Sum('pay'))['pay__sum'] or 0

    # Lista de actividades por defecto
    activities = Activities.objects.filter(user__username=request.user.username, completed=False)

    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        try:
            activity = Activities.objects.get(id=activity_id, user=request.user, completed=False)
        except Activities.DoesNotExist:
            activity = None

        if activity:
            activity.completed = True
            activity.save()

            # Asegúrate de que 'pay' es un número válido
            pay_value = activity.pay
            try:
                pay_decimal = float(pay_value)
            except ValueError:
                pay_decimal = 0

            # Actualizar los totales de producción
            total_production_daily += pay_decimal
            total_production_weekly += pay_decimal
            total_production_monthly += pay_decimal
            total_production_yearly += pay_decimal

            # Actualizar los totales en el perfil del usuario
            perfil_usuario.total_production_daily = float(total_production_daily)
            perfil_usuario.total_production_weekly = float(total_production_weekly)
            perfil_usuario.total_production_monthly = float(total_production_monthly)
            perfil_usuario.total_production_yearly = float(total_production_yearly)
            
            perfil_usuario.save()

    return render(request, 'produccion/veractividades.html', {
        'activities': activities,
        'total_production_daily': total_production_daily,
        'total_production_weekly': total_production_weekly,
        'total_production_monthly': total_production_monthly,
        'total_production_yearly': total_production_yearly,
        'grupo': grupo
    })


def editar_ganancia(request):
    return render(request,'ganancias/editar_ganancia.html',{
    })
def procesos(request):
    return render(request,'procesos/procesos.html',{
    })
def proceso_nuevo(request):
    return render(request,'procesos/proceso_nuevo.html',{
    })
def editar_proceso(request):
    return render(request,'procesos/editar_proceso.html',{
    })
@login_required(login_url='login')  # Asegura que solo usuarios autenticados pueden acceder a la vista
def empleado(request):
    user = request.user
    group_name = None
    if user.is_authenticated:
        group = Group.objects.filter(user=user).first()
        if group:
            group_name = group.name
    grupo = group_name
    return render(request, 'index/empleado.html', {'grupo': grupo
})
@login_required(login_url='login')
def pqrs(request):
    user = request.user
    group_name = None
    if user.is_authenticated:
        group = Group.objects.filter(user=user).first()
        if group:
            group_name = group.name
    grupo = group_name
    comentarios = PQRS.objects.filter(user=request.user).order_by('-id')
    if request.method == 'POST':
        form = PQRSForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Su comentario fue enviado')
            return redirect('pqrs')
        else:
            messages.success(request, f'Error durante el envio del comentario')
    else:
        form = SalesForm()
    return render(request,'pqrs/pqrstcm.html',{'form':form, 'pqrs':comentarios, 'grupo': grupo})
@transaction.atomic
def produccion(request):
    user = request.user
    group_name = None
    if user.is_authenticated:
        group = Group.objects.filter(user=user).first()
        if group:
            group_name = group.name
    grupo = group_name
    # Obtener o crear el perfil de usuario
    perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=request.user)

    # Obtener el total de producción actual
    total_production = perfil_usuario.total_production

    # Obtener el total de producción diario
    today = datetime.now().date()
    total_production_daily = Activities.objects.filter(user=request.user, date=today, completed=True).aggregate(Sum('pay'))['pay__sum'] or 0

    # Obtener el total de producción semanal
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    total_production_weekly = Activities.objects.filter(user=request.user, date__range=[start_of_week, end_of_week], completed=True).aggregate(Sum('pay'))['pay__sum'] or 0

    # Obtener el total de producción mensual
    start_of_month = today.replace(day=1)
    end_of_month = (start_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    total_production_monthly = Activities.objects.filter(user=request.user, date__range=[start_of_month, end_of_month], completed=True).aggregate(Sum('pay'))['pay__sum'] or 0

    # Obtener el total de producción anual
    start_of_year = today.replace(month=1, day=1)
    end_of_year = today.replace(month=12, day=31)
    total_production_yearly = Activities.objects.filter(user=request.user, date__range=[start_of_year, end_of_year], completed=True).aggregate(Sum('pay'))['pay__sum'] or 0

    return render(request, 'produccion/produccion.html', {
        'total_production': total_production,
        'total_production_daily': total_production_daily,
        'total_production_weekly': total_production_weekly,
        'total_production_monthly': total_production_monthly,
        'total_production_yearly': total_production_yearly,
        'grupo': grupo
    })

@login_required
def salario(request):
    user = request.user
    group_name = None
    if user.is_authenticated:
        group = Group.objects.filter(user=user).first()
        if group:
            group_name = group.name
    grupo = group_name
    user = request.user  # Obtiene el usuario actual
    current_month = 12  # Cambia esto al mes actual (puedes usar datetime para obtener el mes actual)

    # Filtra las actividades del usuario actual y del mes actual
    queryset = Activities.objects.filter(user=user, date__month=current_month)

    # Crea la tabla con el queryset filtrado
    table = ActivitiesTable(queryset)

    # Calcula el total de producción mensual del usuario actual
    total_production_monthly = queryset.aggregate(Sum('pay'))['pay__sum'] or 0

    # Pasa la tabla y otros contextos a la plantilla
    return render(request, 'produccion/salario.html', {'table': table, 'total_production_monthly': total_production_monthly, 'grupo': grupo})
