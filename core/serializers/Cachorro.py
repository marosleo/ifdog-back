from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Cachorro
from media.models import Image
from media.serializers import ImageSerializer

class CachorroSerializer(ModelSerializer):
    class Meta:
        model = Cachorro
        fields = "__all__"
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

class CachorroDetailSerializer(ModelSerializer):
    foto = ImageSerializer(required=False)