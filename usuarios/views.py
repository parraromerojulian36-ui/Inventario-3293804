from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Empresa  

def home(request):
    empresas = Empresa.objects.all()
    return render(request, 'usuarios/home.html', {'empresas': empresas})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Empresa  

def home(request):
    # Consultamos las empresas registradas
    empresas = Empresa.objects.all()
    return render(request, 'usuarios/home.html', {'empresas': empresas})

def crear_empresa(request):
    if request.method == 'POST':
       
        tipo_razon_social = request.POST.get('tipo_razon_social')
        razon_social = request.POST.get('razon_social')
        serial = request.POST.get('serial')
        tipo_identificacion = request.POST.get('tipo_identificacion')
        identificacion = request.POST.get('identificacion')
        tipo_comercio = request.POST.get('tipo_comercio')
        digito_verificacion = request.POST.get('digito_verificacion') 
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        contacto = request.POST.get('contacto')

        Empresa.objects.create(
            tipo_razon_social=tipo_razon_social,
            razon_social=razon_social,
            serial=serial,
            tipo_identificacion=tipo_identificacion,
            identificacion=identificacion,
            tipo_comercio=tipo_comercio,
            digito_verificacion=digito_verificacion,
            correo=correo,
            direccion=direccion,
            contacto=contacto
        )

       
        messages.success(request, '¡Empresa/Persona creada con éxito!')
        return redirect('home')
    return render(request, 'usuarios/empresa_forms.html')


def editar_empresa(request, id_empresa):
  
    empresa_obj = Empresa.objects.filter(id=id_empresa).first()

   
    if not empresa_obj:
        empresa_obj = Empresa()

    if request.method == 'POST':
       
        empresa_obj.tipo_razon_social = request.POST.get('tipo_razon_social')
        empresa_obj.razon_social = request.POST.get('razon_social')
        empresa_obj.serial = request.POST.get('serial')
        empresa_obj.tipo_identificacion = request.POST.get('tipo_identificacion')
        empresa_obj.identificacion = request.POST.get('identificacion')
        empresa_obj.tipo_comercio = request.POST.get('tipo_comercio')
        empresa_obj.digito_verificacion = request.POST.get('digito_verificacion') 
        empresa_obj.correo = request.POST.get('correo')
        empresa_obj.direccion = request.POST.get('direccion')
        empresa_obj.contacto = request.POST.get('contacto')

       
        empresa_obj.save()

        messages.success(request, '¡Los datos de la empresa han sido actualizados con éxito!')
        return redirect('home')

    return render(request, 'usuarios/empresa_forms.html', {'empresa': empresa_obj})