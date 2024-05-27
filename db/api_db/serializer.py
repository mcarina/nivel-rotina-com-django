from rest_framework import serializers
from .models import *

class NiveisAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NiveisAcesso
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    nivel_acesso = NiveisAcessoSerializer()
    rotinas = serializers.SerializerMethodField()

    class Meta:
        model = Usuarios
        fields = '__all__'

    def get_rotinas(self, obj):
        rotinas = UsuariosRotina.objects.filter(usuario=obj).values_list('rotina__descricao_rotina', flat=True)
        return rotinas

class RotinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rotinas
        fields = '__all__'

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'

class UsuariosRotinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosRotina
        fields = '__all__'

class EtapasAprovacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapasAprovacoes
        fields = '__all__'

class TabelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabelas
        fields = '__all__'
