from django import forms

from course.models import Comment


class CommentCourseForm(forms.ModelForm):
    class Meta:
        model = Comment
    fields = ['name', 'email', 'comment', 'is_published', 'rating', 'course_id', 'author_id']

    exclude = ()
