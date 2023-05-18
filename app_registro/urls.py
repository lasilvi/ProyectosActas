"""Importe de las libreraís necesarias."""
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('RegistroActa/', views.Register, name='Registro'),
    path('RegistroUsuarios/', views.RegisterUser, name='RegistroUser'),
    path('RegistroDesarrollo/', views.RegisterDevelopment, name='RegistroDevelop'),
    path('RegistroCompromiso/', views.RegisterCommintment, name='RegistroCommintment'),
    ]