from rest_framework.viewsets import ModelViewSet
from core.models import Publicacoes
from core.serializers import PublicacoesSerializer
 

class PublicacoesViewSet(ModelViewSet):
    queryset = Publicacoes.objects.all()
    serializer_class = PublicacoesSerializer