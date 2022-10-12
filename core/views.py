from django.contrib.auth.models import User
from .models import Cachorro, Publicacoes, Comedouro, Tag, Comentarios
from rest_framework.viewsets import ModelViewSet
from .serializers import RegistrationSerializer, PublicacoesSerializer, TagSerializer, ComedouroSerializer, CachorroSerializer, ComentariosSerializer, DetailComentariosSerializer, DetailTagSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class RegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        data['email'] = self.user.email
        

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CachorroViewSet(ModelViewSet):
    queryset = Cachorro.objects.all()
    serializer_class = CachorroSerializer


class ComedouroViewSet(ModelViewSet):
    queryset = Comedouro.objects.all()
    serializer_class = ComedouroSerializer
    

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailTagSerializer
        return TagSerializer

class PublicacoesViewSet(ModelViewSet):
    queryset = Publicacoes.objects.all()
    serializer_class = PublicacoesSerializer

class ComentariosViewSet(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailComentariosSerializer
        return ComentariosSerializer
   

