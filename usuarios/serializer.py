from rest_framework import serializers
from django.contrib.auth.models import User

from usuarios.models import Empresa

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields="__all__"
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'