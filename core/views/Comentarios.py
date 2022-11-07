from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from core.models import Comentarios
from core.serializers import  ComentariosSerializer,DetailComentariosSerializer


class ComentariosViewSet(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailComentariosSerializer
        return ComentariosSerializer