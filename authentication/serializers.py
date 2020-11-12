from rest_framework import serializers 
from .models import CustomUser 
from posts.models import Post


class CustomUserSerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField( required=True ) 
    username = serializers.CharField() 
    password = serializers.CharField(min_length=8, write_only=True)
    avatar = serializers.CharField()
    cover = serializers.CharField()
    
    class Meta: 
        model = CustomUser
        fields = ['id', 'email', 'username', 'avatar', 'cover', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance