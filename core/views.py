from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Cachorro, Publicacoes, Comedouro, Tag, Comentarios
from rest_framework.viewsets import ModelViewSet
from .serializers import RegistrationSerializer, PublicacoesSerializer, TagSerializer, ComedouroSerializer, CachorroSerializer, ComentariosSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework import permissions
from rest_framework import serializers
import uuid
from rest_framework.permissions import AllowAny

class RegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class RegistrationAPIView(generics.GenericAPIView):

#     serializer_class = RegistrationSerializer
#     permission_classes = ()
#     queryset = User.objects.all()
#     def post(self, request):
#         serializer = self.get_serializer(data = request.data)
#         # serializer.is_valid(raise_exception = True)
#         # serializer.save()
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response({
#                 "RequestId": str(uuid.uuid4()),
#                 "Message": "User created successfully",
                
#                 "User": serializer.data}, status=status.HTTP_201_CREATED
#                 )
        
#         return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class CachorroViewSet(ModelViewSet):
    queryset = Cachorro.objects.all()
    serializer_class = CachorroSerializer


class ComedouroViewSet(ModelViewSet):
    queryset = Comedouro.objects.all()
    serializer_class = ComedouroSerializer
    

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PublicacoesViewSet(ModelViewSet):
    queryset = Publicacoes.objects.all()
    serializer_class = PublicacoesSerializer

class ComentariosViewSet(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer 

