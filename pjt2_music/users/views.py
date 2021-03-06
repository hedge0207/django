from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect("community:review_list")
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews:review_list")
    else:
        form=UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'users/signup.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect("community:review_list")
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'reviews:review_list')
    else:
        form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'users/login.html',context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('reviews:review_list')