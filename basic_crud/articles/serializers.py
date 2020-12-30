from rest_framework import serializers
from .models import Article
from accounts.serializers import UserSerializer

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'