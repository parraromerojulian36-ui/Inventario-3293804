from django.shortcuts import render, redirect

from .models import Sede


# Página principal de Usuarios
def home(request):
    return render(request, 'usuarios/home.html')


# Datos de la empresa
def datos_empresa(request):
    if request.method == 'POST':
        pass

    return render(request, 'usuarios/empresa_forms.html')


# Lista de sedes
def lista_sedes(request):
    sedes = Sede.objects.all()

    return render(request, 'Usuarios/sedes.html', {'sedes': sedes})


# Crear una nueva sede
def crear_sede(request):
    if request.method == 'POST':
        nombreSede = request.POST.get('nombreSede')
        municipio = request.POST.get('municipio')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        if Sede.objects.filter(nombreSede=nombreSede, municipio=municipio).exists():
            return render(request, 'Usuarios/crear_sede.html', {
                'error': 'Esta sede ya está registrada.'
            })

        Sede.objects.create(
            nombreSede=nombreSede,
            municipio=municipio,
            direccion=direccion,
            telefono=telefono
        )

        return redirect('Usuarios:lista_sedes')

    return render(request, 'Usuarios/crear_sede.html')

# Editar una sede existente
def editar_sede(request, id):
    sede = Sede.objects.get(id=id)

    if request.method == 'POST':
        sede.nombreSede = request.POST.get('nombreSede')
        sede.municipio = request.POST.get('municipio')
        sede.direccion = request.POST.get('direccion')
        sede.telefono = request.POST.get('telefono')

                # Validación 1: solo una Sede Principal por municipio
        if (
            sede.nombreSede.strip().lower() == 'sede principal'
            and Sede.objects.filter(
                nombreSede__iexact='sede principal',
                municipio__iexact=sede.municipio.strip()
            ).exclude(id=id).exists()
        ):
            return render(request, 'Usuarios/editar_sede.html', {
                'sede': sede,
                'error': 'Ya existe una Sede Principal registrada en este municipio.'
            })

        # Validación 2: no permitir una sede completamente repetida
        if Sede.objects.filter(
            nombreSede__iexact=sede.nombreSede.strip(),
            municipio__iexact=sede.municipio.strip(),
            direccion__iexact=sede.direccion.strip(),
            telefono=sede.telefono.strip()
        ).exclude(id=id).exists():
            return render(request, 'Usuarios/editar_sede.html', {
                'sede': sede,
                'error': 'Esta sede ya está registrada con los mismos datos.'
            })

        sede.save()
        return redirect('Usuarios:lista_sedes')

    return render(request, 'Usuarios/editar_sede.html', {'sede': sede})

# Eliminar una sede
def eliminar_sede(request, id):
    sede = Sede.objects.get(id=id)
    sede.delete()

    return redirect('Usuarios:lista_sedes')

