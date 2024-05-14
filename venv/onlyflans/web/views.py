from django.shortcuts import render, redirect
from .models import Flan
from .models import ContactForm

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about (request):
    return render (request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario en la base de datos
            return redirect('exito')  # Redirige a la página de éxito
    else:
        form = ContactForm()  # Crea una instancia del formulario

    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

