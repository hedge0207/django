from django.shortcuts import render,redirect,get_object_or_404
from .forms import VoteForm, CommentForm
from .models import Vote, Comment

# Create your views here.
def index(request):
    votes = Vote.objects.all()
    context = {
        'votes':votes
    }
    return render(request,'index.html',context)

def create(request):
    if request.method=="POST":
        form=VoteForm(request.POST)
        if form.is_valid():
            vote = form.save()
            return redirect('vote:detail', vote.pk)
    else:
        form=VoteForm()
    context = {
        'form':form
    }
    return render(request, 'create.html',context)

def detail(request,vote_pk):
    vote = get_object_or_404(Vote,pk=vote_pk)
    comments = Comment.objects.all()
    form = CommentForm()
    cnt = comments.count()
    if cnt:
        red = comments.filter(pick=2).count()
        blue = cnt-red
        rred = 100-int(blue/cnt*100)
        rblue = 100-rred
    else:
        rred=0
        rblue=0
    context = {
        'vote':vote,
        'comments':comments,
        'form':form,
        'red':red,
        'blue':blue,
        'rred':rred,
        'rblue':rblue,
    }
    return render(request,'detail.html',context)

def create_comment(request,vote_pk):
    vote = get_object_or_404(Vote,pk=vote_pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.vote=vote
            form.save()
    return redirect('vote:detail', vote.pk)