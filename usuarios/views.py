from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')
from django.shortcuts import render

def datos_empresa(request):
    if request.method == 'POST':
        pass
    return render(request, 'usuarios/empresa_forms.html')