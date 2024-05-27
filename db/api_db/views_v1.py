from rest_framework.generics import ListAPIView
from .models import *
from .serializer import *

class UsuariosListView(ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Adiciona a relação com o nível de acesso à consulta
        queryset = queryset.select_related('nivel_acesso')
        return queryset

class RotinasListView(ListAPIView):
    queryset = Rotinas.objects.all()
    serializer_class = RotinasSerializer

class DepartamentosListView(ListAPIView):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer

class UsuariosRotinaListView(ListAPIView):
    queryset = UsuariosRotina.objects.all()
    serializer_class = UsuariosRotinaSerializer

class EtapasAprovacoesListView(ListAPIView):
    queryset = EtapasAprovacoes.objects.all()
    serializer_class = EtapasAprovacoesSerializer

class TabelasListView(ListAPIView):
    queryset = Tabelas.objects.all()
    serializer_class = TabelasSerializer
