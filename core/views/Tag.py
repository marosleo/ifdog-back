from rest_framework.viewsets import ModelViewSet
from core.models import Tag
from core.serializers import TagSerializer, DetailTagSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailTagSerializer
        return TagSerializer