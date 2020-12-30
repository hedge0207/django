from django.shortcuts import get_object_or_404
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def article_update(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    serializer = ArticleSerializer(data=request.data,instance=article)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def article_delete(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    article.delete()
    return Response("OK")