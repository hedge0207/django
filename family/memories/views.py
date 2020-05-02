from django.shortcuts import render,redirect,get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm,CommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
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
            return redirect('memories:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'memories/article_form.html',context)

def detail(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article':article,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request,'memories/detail.html',context)

@require_POST
def delete(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    article.delete()
    return redirect("memories:index")


def update(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('memories:detail', article.pk)
    else:
        form=ArticleForm(instance=article)
    context = {
        'form':form
    }
    return render(request,'memories/article_form.html', context)

def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user=request.user
        comment.article=article
        comment.save()
    return redirect('memories:detail', article_pk)

def comment_delete(request,article_pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return redirect('memories:detail', article_pk)

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(id=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('memories:detail', article.pk)


