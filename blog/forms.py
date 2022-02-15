
from django import forms

from blog.models import Comment, Like, Post, PostView


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'category', 'status')


class PostComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class LikePost(forms.ModelForm):
    class Meta:
        model = Like
        fields = ()
