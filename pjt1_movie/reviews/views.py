from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    reviews=Review.objects.order_by('-id').all()
    context= {
        'reviews':reviews,
    }
    return render(request,'reviews/index.html',context)

@login_required
def create(request):
    if request.method=="POST":
        form=ReviewForm(request.POST)
        if form.is_valid:
            review = form.save()
            return redirect('reviews:index')
    else:
        form=ReviewForm()
    context = {
        'form':form
    }
    return render(request,'reviews/create.html',context)

def detail(request,pk):
    review=get_object_or_404(Review,pk=pk)
    context = {
        'review':review,
    }
    return render(request,'reviews/detail.html',context)

def update(request,pk):
    review=get_object_or_404(Review,pk=pk)
    if request.method=="POST":
        form=ReviewForm(request.POST, instance=review)
        if form.is_valid:
            form.save()
            return redirect('reviews:index')
    else:
        form=ReviewForm(instance=review)
    context={
        'form':form
    }
    return render(request,'reviews/create.html',context)

@require_POST
def delete(request,pk):
    review=get_object_or_404(Review,pk=pk)
    review.delete()
    return redirect("reviews:index")