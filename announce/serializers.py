from rest_framework import serializers
from .models import Post  
from records.serializers import CustomUserSerializer
from records.models import CustomUser
from rest_framework import serializers
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser  
    fields = ['id', 'username']
    
class PostSerializer(serializers.ModelSerializer):

  author = AuthorSerializer(read_only=True)

  class Meta:
    model = Post
    fields = ['id', 'title', 'body', 'author', 'image']
    extra_kwargs = {
    'author': {'read_only': True},
    'image': {'required': False}
    }