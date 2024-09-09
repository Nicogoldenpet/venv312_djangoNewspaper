from django import forms
from .models import Comment

class CommentForm(forms.ModelForm): #Formato del comentario
    class Meta:
        model = Comment
        fields = ("comment", "author")