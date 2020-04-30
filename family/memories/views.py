from django.shortcuts import render,redirect,get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm,CommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'memories/index.html',context)

def create(request):
    if request.method=="POST":
        form=ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('memiries:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'memories/create.html',context)

def detail(request, aritcle_pk):
    article = get_object_or_404(Article,pk=article_pk)
    context = {
        'article':article
    }
    return render(request,'memories/detail.html',context)