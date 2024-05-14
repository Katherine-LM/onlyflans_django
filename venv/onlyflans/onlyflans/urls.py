from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contacto'),
    path('exito/', views.exito, name='exito'),
]

