from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from core.models import Tag
from media.models import Image
from media.serializers import ImageSerializer

class TagSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
        
    )
    foto = ImageSerializer(required=False, read_only=True, default=None)
    id = serializers.IntegerField(read_only=True, required=False)
    
    class Meta:
        model = Tag
        fields = "__all__"

class DetailTagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        depth = 1