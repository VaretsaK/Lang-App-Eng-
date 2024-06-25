from django.shortcuts import render
from comments.models import Comment


def comment(request):
    all_comments = Comment.objects.all()
    context = {
        'comments': all_comments,
        'title': 'All comments'
    }
    return render(request, 'comments/comments.html', context)


def add_comment(request):
    ...
