from django import forms
from .models import Review
from django.contrib.auth import get_user_model


class ReviewForm(forms.ModelForm):
    nickname=forms.CharField(max_length=40)
    class Meta:
        model=Review
        fields="__all__"