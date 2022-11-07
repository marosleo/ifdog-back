from rest_framework.serializers import ModelSerializer
from core.models import Comentarios

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = "__all__"
        
        
class DetailComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = "__all__"
        depth = 1