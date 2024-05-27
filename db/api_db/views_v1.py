from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *

class UsuariosViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Adiciona a relação com o nível de acesso à consulta
        queryset = queryset.select_related('nivel_acesso')
        return queryset

class RotinasViewSet(ModelViewSet):
    queryset = Rotinas.objects.all()
    serializer_class = RotinasSerializer

class DepartamentosViewSet(ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer

class UsuariosRotinaViewSet(ModelViewSet):
    queryset = UsuariosRotina.objects.all()
    serializer_class = UsuariosRotinaSerializer

class EtapasAprovacoesViewSet(ModelViewSet):
    queryset = EtapasAprovacoes.objects.all()
    serializer_class = EtapasAprovacoesSerializer

class TabelasViewSet(ModelViewSet):
    queryset = Tabelas.objects.all()
    serializer_class = TabelasSerializer
