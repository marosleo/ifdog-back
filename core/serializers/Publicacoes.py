from rest_framework.serializers import ModelSerializer
from core.models import Publicacoes

class PublicacoesSerializer(ModelSerializer):
    class Meta:
        model = Publicacoes
        fields = "__all__"