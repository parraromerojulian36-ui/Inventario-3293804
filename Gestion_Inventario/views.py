from django.shortcuts import render

def home_inventario(request):
    return render(request, 'Inventario/home.html')
