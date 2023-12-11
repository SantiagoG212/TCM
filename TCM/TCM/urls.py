"""
URL configuration for TCM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import logout_then_login
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/solicitar', views.solicitud_compra, name='solicitud_compra'),
    path('pqrstcm/', views.pqrs, name='pqrs'),
    path('empleado/', views.empleado, name='empleado'),
    path('produccion/', views.produccion, name='produccion'),
    path('veractividades/', views.veractividades, name='veractividades'),
    path('salario/', views.salario, name='salario'),
    path('logout/', logout_then_login, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
