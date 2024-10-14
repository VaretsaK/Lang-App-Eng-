from django.shortcuts import render, redirect
from comments.models import Comment
from comments.forms import CommentForm
from django.views.generic import ListView


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comments.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All comments'
        return context


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comment')
    else:
        form = CommentForm()
    return render(request, 'comments/create_comment.html', {'form': form})

