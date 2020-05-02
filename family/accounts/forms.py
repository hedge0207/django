from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','father','mather','child']


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email','father','mather','child']