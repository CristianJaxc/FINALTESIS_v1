from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages
from django.views import generic
from .models import Client
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

def login(request):
    if request.session.get('id') != None:  # Puede iniciar sesión solo cuando no haya iniciado sesión
        messages.success(request, "Bienvenido")
        return redirect('product_list')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()            # Eliminar espacios y líneas nuevas
            password = password.strip()
            try:
                user = Client.objects.get(username=username)
            except:
                messages.success(request, "Nombre de Usuario no Existe ")
                return render(request, 'cliente/login.html')
            if user.password == password:
                request.session['id'] = user.id    # Registrar que el usuario ha iniciado sesión
                messages.success(request, "Bienvenido"+user.username)
                return redirect('product_list')
            else:
                messages.success(request, "contraseña Incorecta" )
                return render(request, 'cliente/login.html')
    return render(request, 'cliente/login.html')


def register(request):

    messages.success(request, "Cierra tu Cuenta primero ")
    if request.session.get('id') != None:  # Regístrese solo cuando no haya iniciado sesión
        return redirect('product_list')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        username = username.strip()  # Eliminar espacios y líneas nuevas
        password = password.strip()
        if Client.objects.filter(username=username).exists():
            messages.success(request, "Cliente Registrado")
            return render(request, 'cliente/login.html')
        user = Client()
        user.username = username
        user.password = password
        user.email = email
        user.telefono = telefono
        user.save()
        request.session['id'] = user.id   # Registrar que el usuario ha iniciado sesión
        messages.success(request, "Cliente Registrado")
        return redirect('register_cliente')


    return render(request, 'cliente/register.html')


def logouts(request):
    request.session.flush()
    messages.success(request, "ssss")
    return redirect('product_list')