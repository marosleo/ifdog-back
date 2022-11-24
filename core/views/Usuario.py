from rest_framework.viewsets import ModelViewSet

from core.models import Usuario
from core.serializers import UsuarioSerializer, UsuarioCreateSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_serializer_class(self):
        if self.action in ["create"]:
            return UsuarioCreateSerializer
        return UsuarioSerializer
