from django import forms

from blog.models import Comment


class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ['name', 'email', 'comment', 'is_published', 'rating', 'blog_id', 'author_id']
        exclude = []
