from .models import Empresa


def empresa_actual(request):
    try:
        empresa = Empresa.objects.order_by('-id').first()
    except Exception:
        empresa = None
    return {'empresa_actual': empresa}
