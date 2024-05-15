from django.contrib import admin
from django.urls import path, include
from web import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.views import  LoginView, LogoutView



urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='bienvenido'),
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]

