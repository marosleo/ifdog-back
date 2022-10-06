from asyncore import write
import email
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Cachorro, Comedouro, Tag, Publicacoes, User, Comentarios
from rest_framework.serializers import ModelSerializer,                  SlugRelatedField
from media.models import Image
from media.serializers import ImageSerializer


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)
    password_confirmation = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password_confirmation')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        password = args.get('password')
        password_confirmation = args.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({'password': ('passwords does not match')})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(**validated_data)
    
    

class ComedouroSerializer(ModelSerializer):
    class Meta:
        model = Comedouro
        fields = "__all__"


class CachorroSerializer(ModelSerializer):
    class Meta:
        model = Cachorro
        fields = "__all__"
    foto_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

class CachorroDetailSerializer(ModelSerializer):
    foto = ImageSerializer(required=False)



class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class PublicacoesSerializer(ModelSerializer):
    class Meta:
        model = Publicacoes
        fields = "__all__"


class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = "__all__"
        
        
class DetailComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = "__all__"
        depth = 1