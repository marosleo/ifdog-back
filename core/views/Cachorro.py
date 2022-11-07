from rest_framework.viewsets import ModelViewSet
from core.models import Cachorro
from core.serializers import CachorroSerializer


class CachorroViewSet(ModelViewSet):
    queryset = Cachorro.objects.all()
    serializer_class = CachorroSerializer