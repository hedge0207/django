from django.shortcuts import render,redirect, get_object_or_404
from .models import MyUser
from .forms import MyUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as my_login
from django.contrib.auth import logout as my_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = MyUserCreationForm(reqeust.POST)
        if form.is_valid():
            form.save()
            return redirect('memories:index')
    form = MyUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html',context)