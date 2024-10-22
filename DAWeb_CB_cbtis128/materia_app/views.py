from django.shortcuts import render

# Create your views here.

def inicio_Vista(request):
    return render(request, 'gestionarMateria.html')
