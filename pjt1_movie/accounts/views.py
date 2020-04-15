from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 게시글 목록 페이지
            return redirect('reviews:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method=="POST":
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reviews:index')
    else:
        form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'accounts/signin.html',context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect(request.GET.get('next') or 'reviews:index')

def detail(request):
    user=request.user
    context = {
        'user':user,
    }
    return render(request,'accounts/detail.html',context)

@login_required
def delete(request):
    request.user.delete()
    return redirect(request.GET.get('next') or 'reviews:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(request.GET.get('next') or 'reviews:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)
