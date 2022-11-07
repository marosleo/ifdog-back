from rest_framework.serializers import ModelSerializer
from core.models import Comedouro

class ComedouroSerializer(ModelSerializer):
    class Meta:
        model = Comedouro
        fields = "__all__"