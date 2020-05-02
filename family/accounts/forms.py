from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    child = forms.CharField(
                max_length=30,
                help_text="자식이 없을 경우 반드시 이와 같이 입력해주세요: 없음",
            )
    class Meta:
        model = get_user_model()
        fields = ['username','father','mather']


class MyUserChangeForm(UserChangeForm):
    child = forms.CharField(
                max_length=30,
                help_text="자식이 없을 경우 반드시 이와 같이 입력해주세요: 없음",
            )
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email','father','mather']