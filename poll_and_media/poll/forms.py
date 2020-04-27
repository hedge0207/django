from django import forms
from .models import Vote,Comment


class VoteForm(forms.ModelForm):
    class Meta:
        model=Vote
        fields = '__all__'

class CommentForm(forms.ModelForm):
    CHOICES = (
        (1,'Blue'),
        (2,'Red'),
    )
    pick = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model=Comment
        fields = '__all__'
        exclude = ['vote']