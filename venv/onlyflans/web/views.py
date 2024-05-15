from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Flan
from .models import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from .forms import ContactForm
from django.shortcuts import render, redirect
from .forms import ContactFormForm

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige a la página de inicio después de cerrar sesión

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bienvenido')  # Redirige a la página de bienvenida
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})


def about (request):
    return render (request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})


def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormForm()
    
    return render(request, 'contact.html', {'form': form})


    
def exito(request):
    return render(request, 'exito.html')

