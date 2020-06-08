from django.shortcuts import render
from .models import Article
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer

# Create your views here.

#원래 사용하던 코드, django에서 template까지 제공하는 코드
# def index(request):
#     articles = Article.objects.all()
#     context = {
#         'articles':articles
#     }
#     return render(request,'articles/index.html',context)

# json으로 data를 보내는 코드, template을 render하지 않는다.
# def index(request):
#     articles = Article.objects.all()
#     data = []
#     for article in articles:
#         data.append({
#             'article_id':article.id,
#             'title':article.title,
#             'content':article.content,
#         })
#     return JsonResponse(data, safe=False)


#serializer를 사용하는 방법
# @require_GET
# def index(request):
#     articles = Article.objects.all()
#     data = serializers.serialize('json',articles)
#     # return JsonResponse(data, safe=False)
#     return HttpResponse(data,content_type='application/json')
    

#최종적으로 사용할 방법, rest framework
@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializers = ArticleSerializer(articles,many=True)

    return Response(serializers.data)