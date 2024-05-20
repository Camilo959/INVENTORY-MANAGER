from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# FUNCIONES DEL SISTEMA

def home(request):
    return render(request, 'home.html')

@login_required
def adminpage(request):
    return render(request, "adminpage.html")

def exit(request):
    logout(request)
    return redirect('home')

#Falta todo el direccionamiento de las rutas aqui y en el archivo de urls
#Lo que hay dentro de .POST['persona_apellido'] corresponde al name que le debes colocar a los campos del formulario
