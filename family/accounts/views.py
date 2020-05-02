from django.shortcuts import render,redirect, get_object_or_404
from .forms import MyUserCreationForm,MyUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as my_login
from django.contrib.auth import logout as my_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('memories:index')
    else:
        form = MyUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html',context)

def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request,request.POST)
        print(request.POST)
        if form.is_valid():
            my_login(request, form.get_user())
            return redirect('memories:index')
    else:
        form=AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/form.html',context)

def logout(request):
    my_logout(request)
    return redirect('memories:index')

def profile(request,user_pk):
    User = get_user_model()
    user = get_object_or_404(User,pk=user_pk)
    context = {
        'user':user
    }
    return render(request,'accounts/profile.html',context)

@require_POST
def user_delete(request,user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    user.delete()
    return redirect('memories:index')


def user_update(request):
    if request.method=="POST":
        form = MyUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile', user.pk)
    else:
        form =MyUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/user_update.html',context)