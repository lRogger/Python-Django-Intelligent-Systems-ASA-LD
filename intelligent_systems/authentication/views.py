from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    return render(request,'sign-up.html')
  
  

# Vista para crear una cuenta de usuario
def signup(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'sign-up.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'sign-up.html', {
            'error': 'Contraseña no coincide'
        })


# Vista para iniciar sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'sign-in.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sign-in.html', {
                'form': AuthenticationForm(),
                'error': 'Correo o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')
          
          
def home(request):
    return render(request,'home.html')