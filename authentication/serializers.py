from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework import serializers 
from .models import CustomUser 
from posts.models import Post

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod 
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user) 

        token['fav_color'] = user.fav_color
        return token


class CustomUserSerializer(serializers.ModelSerializer): 
    """ Currently unused in preference of the below. """ 
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    email = serializers.EmailField( required=True ) 
    username = serializers.CharField() 
    password = serializers.CharField(min_length=8, write_only=True) 
    
    class Meta: 
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data) # as long as the fields are the same, we can just use this 
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance