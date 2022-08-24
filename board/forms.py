from django import forms
from .models import Comment

class SearchForm(forms.Form):
    keyword=forms.CharField(max_length=50, required=False)
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    