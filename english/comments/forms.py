from django import forms
from lessons.models import Lesson, Exercise


class CommentForm(forms.Form):
    title = forms.CharField(max_length=128)
    content = forms.CharField()
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all())
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
