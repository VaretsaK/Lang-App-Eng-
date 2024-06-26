from django.shortcuts import render, redirect
from comments.models import Comment
from comments.forms import CommentForm


def comment(request):
    all_comments = Comment.objects.all()
    context = {
        'comments': all_comments,
        'title': 'All comments'
    }
    return render(request, 'comments/comments.html', context)


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comment')
    else:
        form = CommentForm()
    return render(request, 'comments/create_comment.html', {'form': form})

