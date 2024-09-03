from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'owner']
        read_only_fields = ["owner",]