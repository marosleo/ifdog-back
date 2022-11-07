from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Usuario
from media.models import Image
from rest_framework import serializers
from media.serializers import ImageSerializer


class UsuarioSerializer(ModelSerializer):
    
    password_confirmation = serializers.CharField(max_length=150, write_only=True)
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    

    class Meta:
        model = Usuario
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password_confirmation','foto','foto_attachment_key','typeuser')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        password = args.get('password')
        password_confirmation = args.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({'password': ('passwords does not match')})
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return Usuario.objects.create_user(**validated_data)