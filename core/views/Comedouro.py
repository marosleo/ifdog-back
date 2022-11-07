from rest_framework.viewsets import ModelViewSet
from core.models import Comedouro
from core.serializers import ComedouroSerializer

class ComedouroViewSet(ModelViewSet):
    queryset = Comedouro.objects.all()
    serializer_class = ComedouroSerializer