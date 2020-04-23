from django.shortcuts import render,redirect,get_object_or_404
from .forms import ReviewForm,CommentForm
from .models import Review,Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def review_list(request):
    reviews=Review.objects.all()
    context = {
        'reviews':reviews
    }
    return render(request, 'reviews/review_list.html',context)

@login_required
def create(request):
    if request.method=="POST":
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.user=request.user
            review.save()
            return redirect('reviews:review_list')
    else:
        form=ReviewForm()
    context={
        'form':form
    }
    return render(request,'reviews/create.html',context)


def detail(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    comments=review.comment_set.all()
    form=CommentForm()
    context={
        'review':review,
        'comments':comments,
        'form':form
    }
    return render(request,'reviews/detail.html',context)


@login_required
def update(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method=="POST":
        form=ReviewForm(request.POST,instance=review)
        if form.is_valid():
            review=form.save(commit=False)
            review.user=request.user
            review.save()
            return redirect('reviews:detail', review_pk)
    else:
        form=ReviewForm(instance=review)
    context = {
        'form':form
    }
    return render(request,'reviews/create.html',context)


@require_POST
def delete(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    review.delete()
    return redirect('reviews:review_list')


@login_required
def comment_create(request,review_pk):
    form=CommentForm(request.POST)
    review=get_object_or_404(Review,pk=review_pk)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.review=review
        comment.user=request.user
        comment.save()
        return redirect('reviews:detail', review_pk)


@login_required
def comment_delete(request,review_pk,comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)

def comment_update(request,review_pk,comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    if request.method=="POST":
        form=CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', review_pk)
    else:
        form=CommentForm(instance=comment)
    context = {
        'form':form
    }
    return redirect('reviews:detail', review_pk)
